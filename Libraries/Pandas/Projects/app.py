import pandas as pd

# 1. Load the Excel files
# Replace file names, sheet names, and column names with your actual ones
df_csc = pd.read_excel(r"Libraries\Pandas\Projects\CS-C.xlsx")
df_dept = pd.read_excel(r"Libraries\Pandas\Projects\CSE-dept.xlsx", sheet_name='Core CSE - Sec C')

# # sheet_List = pd.ExcelFile(r"Libraries\Pandas\Projects\CSE-dept.xlsx").sheet_names
# # df = pd.DataFrame(sheet_List)
# # df.to_csv(r"Libraries\Pandas\Projects\CSE-dept_SheetNames.csv", index=False)  

# 2. Clean the data (remove extra spaces and standardize capitalization)
# Change 'Student Name' to your actual column name (or use Roll Number for better accuracy)
col_name = "Name"

csc_students = set(df_csc[col_name].dropna().astype(str).str.strip().str.lower())
dept_students = set(df_dept[col_name].dropna().astype(str).str.strip().str.lower())

# 3. Find the missing students
missing_in_csc = dept_students - csc_students
missing_in_dept = csc_students - dept_students

# 4. Print the results
print("In Dept file, but MISSING in CS-C file:")
for student in sorted(missing_in_csc):
    print(f" - {student.title()}")

print("\nIn CS-C file, but MISSING in Dept file:")
for student in sorted(missing_in_dept):
    print(f" - {student.title()}")
