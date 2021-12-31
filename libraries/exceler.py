import os
from RPA.Excel.Files import Files
from RPA.Tables import Tables

# FILE_EXCEL_PATH = os.environ["<path to Excel file>"]

excel = Files()
tables = Tables()

# def get_filtered_excel(excel_path):
#     excel = read_excel_as_table(excel_path)
#     tables.filter_table_by_column(excel, "<column to filter>", "==", "<value to filter>")
#     return excel

def read_excel_as_table(excel_path):
    try:
        excel.open_workbook(excel_path)
        return excel.read_worksheet_as_table(header=True)
    finally:
        excel.close_workbook()