import gspread
from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'ReadyDraftOne.json', scope)

gc = gspread.authorize(credentials)

wks1 = gc.open("Attendance_Sheet")#new sheet make a new var if need to open older sheet for ID and name

worksheet1 = wks1.get_worksheet(0)

values_list = worksheet1.get_all_values()
last_row=len(values_list)+1#getting last row
#print(values_list)



lst=[]
"""for i in range(1):
    strn=str(input("Enter name "+str(i+1)+": "))
    lst.append(strn)#taking value from user"""

#name=str(input("Enter name: "))#take name
#i=str(input("Enter id: "))#take id
#lst=[name,i]
time=str(datetime.time(datetime.now()))#current time
date=str(datetime.date(datetime.now()))#current date
#lst=[i,name,time,date]#making a list of values to be stored and added in the file
#i+=1
worksheet1.delete_row(2)
#for i in range(1,5):#from cell 1 to 4
 #   worksheet1.update_cell(last_row,i,lst[i-1])#saving values from 0 to 3

final_list=worksheet1.get_all_values()#final list values
#print(final_list)
 
