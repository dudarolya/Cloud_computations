from pprint import pprint
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

print("Enter the ID of the file...")
sheet_id = input()
CREDENTIALS_FILE = 'proj1.json'
spreadsheet_id = sheet_id
#17Pe1U2_86I2MGm802sloZtdN8DH0wez4Fs17BWCL2dI
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E15',
    majorDimension='COLUMNS'
).execute()
pprint(values)

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B3:C4",
             "majorDimension": "ROWS",
             "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
            {"range": "D5:E6",
             "majorDimension": "COLUMNS",
             "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
        ]
    }
).execute()
