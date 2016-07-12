from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

#Column Locations
DATE = 0
SOURCE = 1
LINK = 7
APTINFO = 8
COMMENTS = 14

def display_Sheets():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '18qeIFJ6IHN60zag4jnLAAK43ChyYFsWlwNyxNkVENC0'
    rangeName = 'A1:O'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    data = [];
    # s = '''<style> table {
    # font-family: arial, sans-serif;
    # border-collapse: collapse;
    # width: 100%;
    # }
    
    # td, th {
    # border: 1px solid #dddddd;
    # text-align: left;
    # padding: 8px;
    # }
    
    # tr:nth-child(even) {
    # background-color: #dddddd;
    # }
    #</style>'''
    if not values:
        s = 'No data found.'
    else:
        #s += '<table> <tr> <th>Date</th> <th>Source:</th> <th>LINK</th> <th>APARTMENT INFO</th> <th>COMMENTS</th>  <tr>'
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            data.append({'date': row[DATE], 'source': row[SOURCE], \
                         'link': row[LINK], 'aptinfo': row[APTINFO], \
                         'comments': row[COMMENTS] })
            #s += '<tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>' % (row[DATE], row[SOURCE], row[LINK], row[APTINFO], row[COMMENTS])
        #s += '</table>'
    return data

def main():
    print("Main")
