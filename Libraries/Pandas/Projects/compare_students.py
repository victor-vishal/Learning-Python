"""
compare_students.py
-------------------
Compare one column (e.g. Name or RollNo) between two Excel files and export
the differences to  difference_of_2_files.csv

How to use
    1. Put this script and your .xlsx files in the same folder.
    2. Run:  python compare_students.py            (uses the script's folder)
       or:   python compare_students.py "C:\\path\\to\\folder"
    3. Answer the prompts (pick file, sheet, column by number).

Needs:  pip install pandas openpyxl
"""

import sys
import re
import difflib
from collections import Counter
from pathlib import Path

import pandas as pd

OUTPUT_NAME = "difference_of_2_files.csv"

# Cell values that tell us "this row is the header row"
HEADER_HINTS = {"name", "rollno", "roll no", "roll number", "student name", "enrollment no"}


# --------------------------------------------------------------------------
# Small helpers for asking the user questions
# --------------------------------------------------------------------------
def ask_choice(title, options, default=None):
    """Show a numbered list and return the index chosen (0-based)."""
    print(f"\n{title}")
    for i, opt in enumerate(options, start=1):
        marker = "  (default)" if default is not None and i - 1 == default else ""
        print(f"  {i}. {opt}{marker}")
    while True:
        raw = input("Enter number: ").strip()
        if raw == "" and default is not None:
            return default
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print(f"  Please type a number between 1 and {len(options)}.")


def clean(value):
    """Normalise a value so 'Rahil  AHMAD ' and 'rahil ahmad' match."""
    return re.sub(r"\s+", " ", str(value)).strip().lower()


# --------------------------------------------------------------------------
# Loading an Excel sheet (handles the 2-row header in your files)
# --------------------------------------------------------------------------
def find_header_row(raw, max_scan=15):
    """Return index of the row that holds labels like 'Name' / 'RollNo'."""
    for i in range(min(max_scan, len(raw))):
        cells = {clean(v) for v in raw.iloc[i] if pd.notna(v)}
        if cells & HEADER_HINTS:
            return i
    return None


def build_labels(raw, header_row):
    """
    Build readable column labels. If the header cell is blank or just a number
    (like the max-marks 27, 35...), use the text from the row above instead
    (like 'CS 503[T]').
    """
    labels, seen = [], Counter()
    for col in range(raw.shape[1]):
        label = raw.iat[header_row, col]
        if (pd.isna(label) or isinstance(label, (int, float))) and header_row > 0:
            label = raw.iat[header_row - 1, col]
        label = f"Column {col + 1}" if pd.isna(label) else str(label).strip()
        seen[label] += 1
        if seen[label] > 1:                      # keep labels unique
            label = f"{label} ({seen[label]})"
        labels.append(label)
    return labels


def load_sheet(path):
    """Ask which sheet to use, load it, return (DataFrame, sheet_name)."""
    sheets = pd.ExcelFile(path).sheet_names
    if len(sheets) == 1:
        sheet = sheets[0]
        print(f"\n'{path.name}' has one sheet: {sheet}")
    else:
        sheet = sheets[ask_choice(f"Sheets in '{path.name}':", sheets)]

    raw = pd.read_excel(path, sheet_name=sheet, header=None)
    header_row = find_header_row(raw)
    if header_row is None:
        print("  Couldn't auto-detect the header row.")
        header_row = int(input("  Which Excel row number holds the column names? ")) - 1

    df = raw.iloc[header_row + 1:].reset_index(drop=True)
    df.columns = build_labels(raw, header_row)
    return df, sheet


def pick_column(df, file_label):
    """List all column names and ask which one to compare."""
    cols = list(df.columns)
    default = next((i for i, c in enumerate(cols) if clean(c) == "name"), None)
    return cols[ask_choice(f"Columns in {file_label} - which one to compare?", cols, default)]


# --------------------------------------------------------------------------
# Comparison
# --------------------------------------------------------------------------
def to_counter(series):
    """Return (Counter of cleaned values, {cleaned value: original text})."""
    series = series.dropna()
    series = series[series.astype(str).str.strip() != ""]
    display, counts = {}, Counter()
    for original in series:
        key = clean(original)
        counts[key] += 1
        display.setdefault(key, str(original).strip())
    return counts, display


def closest(name, candidates):
    """Best spelling match from the other side (helps spot typos)."""
    hit = difflib.get_close_matches(name, candidates, n=1, cutoff=0.75)
    return hit[0] if hit else ""


def compare(counts_a, disp_a, counts_b, disp_b, label_a, label_b):
    only_a = sorted(k for k in counts_a if k not in counts_b)
    only_b = sorted(k for k in counts_b if k not in counts_a)
    count_diff = sorted(k for k in counts_a if k in counts_b and counts_a[k] != counts_b[k])

    rows = []
    for k in only_a:
        rows.append({
            "Value": disp_a[k], "Status": f"Only in {label_a}",
            f"Count in {label_a}": counts_a[k], f"Count in {label_b}": 0,
            "Possible match in other file": disp_b.get(closest(k, only_b), ""),
        })
    for k in only_b:
        rows.append({
            "Value": disp_b[k], "Status": f"Only in {label_b}",
            f"Count in {label_a}": 0, f"Count in {label_b}": counts_b[k],
            "Possible match in other file": disp_a.get(closest(k, only_a), ""),
        })
    for k in count_diff:
        rows.append({
            "Value": disp_a[k], "Status": "Appears a different number of times",
            f"Count in {label_a}": counts_a[k], f"Count in {label_b}": counts_b[k],
            "Possible match in other file": "",
        })
    return rows, only_a, only_b, count_diff


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    files = sorted(p for p in folder.glob("*.xlsx") if not p.name.startswith("~$"))
    if len(files) < 2:
        sys.exit(f"Need at least two .xlsx files in {folder} (found {len(files)}).")

    names = [p.name for p in files]
    file_a = files[ask_choice("Select FILE 1 (e.g. the department file):", names)]
    file_b = files[ask_choice("Select FILE 2 (e.g. the section file):", names)]

    df_a, sheet_a = load_sheet(file_a)
    df_b, sheet_b = load_sheet(file_b)

    label_a, label_b = file_a.stem, file_b.stem
    if label_a == label_b:                       # same file picked twice -> keep labels distinct
        label_a, label_b = f"{label_a} [{sheet_a}]", f"{label_b} [{sheet_b}]"

    col_a = pick_column(df_a, f"'{file_a.name}'")
    col_b = pick_column(df_b, f"'{file_b.name}'")

    counts_a, disp_a = to_counter(df_a[col_a])
    counts_b, disp_b = to_counter(df_b[col_b])
    total_a, total_b = sum(counts_a.values()), sum(counts_b.values())

    rows, only_a, only_b, count_diff = compare(counts_a, disp_a, counts_b, disp_b, label_a, label_b)

    # ---- console report ----
    print("\n" + "=" * 60)
    print("RESULT")
    print("=" * 60)
    print(f"{label_a}: {total_a} entries   |   {label_b}: {total_b} entries")
    if total_a == total_b:
        print("Both files have the same number of entries.")
    else:
        bigger, smaller = (label_a, label_b) if total_a > total_b else (label_b, label_a)
        print(f"-> {bigger} has {abs(total_a - total_b)} MORE than {smaller}.")

    if not rows:
        print("\nNo differences - every value matches in both files.")
    else:
        for title, keys, disp in [
            (f"Only in {label_a} (missing from {label_b})", only_a, disp_a),
            (f"Only in {label_b} (missing from {label_a})", only_b, disp_b),
        ]:
            if keys:
                print(f"\n{title}:")
                for k in keys:
                    print(f"  - {disp[k]}")
        if count_diff:
            print("\nAppear a different number of times:")
            for k in count_diff:
                print(f"  - {disp_a[k]}: {counts_a[k]} in {label_a}, {counts_b[k]} in {label_b}")

    # ---- export CSV ----
    out_path = folder / OUTPUT_NAME
    columns = ["Value", "Status", f"Count in {label_a}", f"Count in {label_b}",
               "Possible match in other file"]
    pd.DataFrame(rows, columns=columns).to_csv(out_path, index=False, encoding="utf-8-sig")
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()