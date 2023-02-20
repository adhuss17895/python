import openpyxl as xl

wb = xl.load_workbook('transaction.xlsx')
sheet = wb['Sheet1']
cell = sheet['A1']
print(cell.value)