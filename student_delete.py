import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'Face_Recognition_json.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Face")

worksheet = wks.get_worksheet(0)

#creating and sharing a spreadsheet on each entry
"""sh = gc.create('sheet2')
sh.share('amanjai01@gmail.com',
         perm_type='user', role='writer')"""

#worksheet2 = wks.add_worksheet(title="Sheet2", rows="100", cols="20")


#getting cell value
# With label
"""val1 = worksheet.acell('A1').value
val2 = worksheet.acell('B1').value
print(val1)
print(val2)"""

# With coords
"""val = worksheet.cell(1, 2).value#here 1 is the row and 2 is the col, same as 1B element
print(val)"""

# To get a cell formula
#cell = worksheet.acell('B1')  # or .cell(1, 2)
#cell.input_value

#Vals from a row or a column
# Get all values from the first row
"""values_list = worksheet.row_values(1)
print(values_list)"""

# Get all values from the first column
"""values_list2 = worksheet.col_values(1)
print(values_list2)"""


#all values from all row/col as a list of lists
"""list_of_lists = worksheet.get_all_values()
print(list_of_lists)"""

#each cell properties to be used
"""value = cell.value
row_number = cell.row
column_number = cell.col"""

#finding a cell in the sheet
# Find a cell with exact string value
"""cell = worksheet.find("Dough")

print("Found something at R%sC%s" % (cell.row, cell.col))

# Find a cell matching a regular expression
amount_re = re.compile(r'(Big|Enormous) dough')
cell = worksheet.find(amount_re)"""

#updating a cell, finally
"""worksheet.update_acell('B1', 'AmanJIKYaHaalHai')"""

# Or
#worksheet.update_cell(1, 2, 'Bingo!')

# Select a range
"""cell_list = worksheet.range('A1:C7')

for cell in cell_list:
    cell.value = 'O_o'

list_of_lists = worksheet.get_all_values()
print(list_of_lists)"""

# Update in batch
"""worksheet.update_cells(cell_list)"""

#all = worksheet.get_all_values()
#end_row = len(all)+1
#print(all)

worksheet.delete_row(2)

#Id=input("Enter id : ")
#name=input("Enter name :")
entry=[]
#entry.append(Id)
#entry.append(name)
#for i in range(1,3):
 #   worksheet.update_cell(end_row, i, entry[i-1])

#entry=list(map(str,input('Enter values to be inserted seperated between spaces(Ex-Ashish Dubey):\n').split()))
#for i in range(1,3):
   # worksheet.update_cell(end_row, i, entry[i-1])

#to delete a row
all = worksheet.row_values(1)

"""worksheet.delete_row(len(all))"""

#nu=worksheet.row_values(1)
#print(nu)

list_of_lists = worksheet.get_all_values()
#print(list_of_lists)



"""all = worksheet.get_all_values()
end_row = len(all)+1
count=0
print(worksheet.col_values)
print(int(worksheet.col_count))
print(end_row)"""#hence for updating, end_row is the row and 1,2,3... is the column

