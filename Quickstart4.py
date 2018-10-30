import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'ReadyDraftOne.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("ReadyDraftOne")

worksheet = wks.get_worksheet(0)

all = worksheet.get_all_values()
end_row = len(all)+1
entry = list(map(str, input('Enter values to be inserted:\n').split()))
for i in range(1, 3):
    worksheet.update_cell(end_row, i, entry[i-1])


list_of_lists = worksheet.get_all_values()
print(list_of_lists)
