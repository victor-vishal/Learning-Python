"""
compare_students.py
-------------------
Compare one column (e.g. RollNo or Name) between two Excel files, print a
report, and APPEND the same report to  difference_of_2_files.csv
(each run becomes its own bordered section).

How to use
    1. Put this script and your .xlsx files in the same folder.
    2. Run:  python compare_students.py            (uses the script's folder)
       or:   python compare_students.py "C:\\path\\to\\folder"
    3. Answer the prompts (pick file, sheet, column by number).

Needs:  pip install pandas openpyxl
"""

import sys
import re
import csv
import difflib
from collections import Counter
from datetime import datetime
from pathlib import Path

import pandas as pd

OUTPUT_NAME = "difference_of_2_files.csv"
BORDER = "═" * 70   # not "=" because Excel treats a CSV cell starting with "=" as a formula

# Cell values that tell us "this row is the header row"
HEADER_HINTS = {"name", "rollno", "roll no", "roll number", "student name", "enrollment no"}
ROLL_HINTS = {"rollno", "roll no", "roll number", "enrollment no"}
NAME_HINTS = {"name", "student name"}


# --------------------------------------------------------------------------
# Asking the user questions
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
    Readable column labels. If the header cell is blank or just a number
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
    default = next((i for i, c in enumerate(cols) if clean(c) in ROLL_HINTS), None)
    if default is None:
        default = next((i for i, c in enumerate(cols) if clean(c) in NAME_HINTS), None)
    return cols[ask_choice(f"Columns in {file_label} - which one to compare?", cols, default)]


# --------------------------------------------------------------------------
# Building the comparison
# --------------------------------------------------------------------------
def find_col(df, hints):
    return next((c for c in df.columns if clean(c) in hints), None)


def shown_columns(df, compared):
    """Which columns to display in the report: {report header: df column}."""
    roll, name = find_col(df, ROLL_HINTS), find_col(df, NAME_HINTS)
    cols = {}
    if compared not in (roll, name):
        cols[str(compared)] = compared
    if roll:
        cols["RollNo"] = roll
    if name:
        cols["Name"] = name
    return cols


def build_entries(df, compared, cols):
    """clean key -> {'count', 'value' (as written), 'info' {header: text}}"""
    entries = {}
    for _, row in df.iterrows():
        v = row[compared]
        if pd.isna(v) or str(v).strip() == "":
            continue
        key = clean(v)
        if key not in entries:
            entries[key] = {
                "count": 0,
                "value": str(v).strip(),
                "info": {h: ("" if pd.isna(row[c]) else str(row[c]).strip()) for h, c in cols.items()},
            }
        entries[key]["count"] += 1
    return entries


def similar_text(key, other_keys, other_entries):
    """Closest spelling in the other file (helps spot typos)."""
    hit = difflib.get_close_matches(key, other_keys, n=1, cutoff=0.75)
    if not hit:
        return ""
    info = other_entries[hit[0]]["info"]
    return " / ".join(v for v in info.values() if v)


def build_report(ea, eb, cols_a, cols_b, label_a, label_b, compared_header, has_names):
    """Return a list of sections: {'title', 'header', 'rows'}."""
    only_a = sorted(k for k in ea if k not in eb)
    only_b = sorted(k for k in eb if k not in ea)
    both = sorted(k for k in ea if k in eb)
    sections = []

    if only_a:
        sections.append({
            "title": f"Only in {label_a} (missing from {label_b})",
            "header": list(cols_a) + ["Similar in other file"],
            "rows": [list(ea[k]["info"].values()) + [similar_text(k, only_b, eb)] for k in only_a],
        })
    if only_b:
        sections.append({
            "title": f"Only in {label_b} (missing from {label_a})",
            "header": list(cols_b) + ["Similar in other file"],
            "rows": [list(eb[k]["info"].values()) + [similar_text(k, only_a, ea)] for k in only_b],
        })

    count_diff = [k for k in both if ea[k]["count"] != eb[k]["count"]]
    if count_diff:
        sections.append({
            "title": "Appear a different number of times",
            "header": list(cols_a) + [f"Count in {label_a}", f"Count in {label_b}"],
            "rows": [list(ea[k]["info"].values()) + [ea[k]["count"], eb[k]["count"]] for k in count_diff],
        })

    if has_names:   # same key, but the name written differs
        name_diff = [k for k in both
                     if clean(ea[k]["info"].get("Name", "")) != clean(eb[k]["info"].get("Name", ""))]
        if name_diff:
            sections.append({
                "title": f"Same {compared_header} but the Name differs",
                "header": [compared_header, f"Name in {label_a}", f"Name in {label_b}"],
                "rows": [[ea[k]["value"], ea[k]["info"]["Name"], eb[k]["info"]["Name"]] for k in name_diff],
            })
    return sections


# --------------------------------------------------------------------------
# Output: console + CSV (same content)
# --------------------------------------------------------------------------
def print_report(summary_lines, sections):
    print("\n" + "=" * 60)
    print("RESULT")
    print("=" * 60)
    for line in summary_lines:
        print(line)
    if not sections:
        print("\nNo differences - every value matches in both files.")
    for s in sections:
        print(f"\n{s['title']}  [{len(s['rows'])}]:")
        for row in s["rows"]:
            shown = [str(c) for c in row[:len(s["header"])] if str(c) != ""]
            print("  - " + "  |  ".join(shown))


def append_csv(path, meta_rows, summary_lines, sections):
    rows = [[BORDER], ["COMPARISON RUN", datetime.now().strftime("%d %b %Y, %I:%M %p")]]
    rows += meta_rows
    rows += [["Result", line] for line in summary_lines]
    rows.append([])
    if not sections:
        rows += [["No differences - every value matches in both files."], []]
    for s in sections:
        rows.append([s["title"], f"{len(s['rows'])} found"])
        rows.append(s["header"])
        rows += s["rows"]
        rows.append([])
    rows += [[BORDER], [], []]

    encoding = "utf-8" if path.exists() else "utf-8-sig"   # BOM only at the very start of a new file
    try:
        with open(path, "a", newline="", encoding=encoding) as f:
            csv.writer(f).writerows(rows)
    except PermissionError:
        sys.exit(f"\nCouldn't write to {path}. Is it open in Excel? Close it and run again.")


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

    cols_a, cols_b = shown_columns(df_a, col_a), shown_columns(df_b, col_b)
    ea, eb = build_entries(df_a, col_a, cols_a), build_entries(df_b, col_b, cols_b)
    total_a = sum(e["count"] for e in ea.values())
    total_b = sum(e["count"] for e in eb.values())

    compared_header = next((h for h, c in cols_a.items() if c == col_a), str(col_a))
    has_names = "Name" in cols_a and "Name" in cols_b and compared_header != "Name"
    sections = build_report(ea, eb, cols_a, cols_b, label_a, label_b, compared_header, has_names)

    summary = [f"{label_a}: {total_a} entries   |   {label_b}: {total_b} entries"]
    if total_a == total_b:
        summary.append("Both files have the same number of entries.")
    else:
        bigger, smaller = (label_a, label_b) if total_a > total_b else (label_b, label_a)
        summary.append(f"{bigger} has {abs(total_a - total_b)} MORE than {smaller}.")

    print_report(summary, sections)

    meta = [
        ["File 1", file_a.name, "Sheet", sheet_a, "Column compared", str(col_a)],
        ["File 2", file_b.name, "Sheet", sheet_b, "Column compared", str(col_b)],
    ]
    out_path = folder / OUTPUT_NAME
    append_csv(out_path, meta, summary, sections)
    print(f"\nAppended to: {out_path}")


if __name__ == "__main__":
    main()