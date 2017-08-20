import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint # format the json that is displayed

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('drive_secret_key.json', scope)
client = gspread.authorize(creds)

sheet = client.open('New_refund_sheet').sheet1

# get the sheet without formatting
python_drive_sheet = sheet.get_all_records()
print (python_drive_sheet)

# get the sheet with formatting
pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
pp.pprint(result)

# get value for individual row
result = sheet.row_values(2)
pp.pprint(result)

# get value for individual coloumn
result = sheet.col_values(2)
pp.pprint(result)

# Get a shell value
result = sheet.cell(2, 3).value
pp.pprint(result)

# Update a shell value
sheet.update_cell(2, 3, 'nicenow@nice.com')
result = sheet.cell(2, 3).value
pp.pprint(result)

# create new row
row = ['kkkkkkkk', '123456', 'k@kkkk.com', 'IN']
index = 6
sheet.insert_row(row, index)

# Delete new row
index = 5
sheet.delete_row(index)

# Print Row Content
print(sheet.row_count)


