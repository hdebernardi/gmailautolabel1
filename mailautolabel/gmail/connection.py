import sys

from oauth2client import file, client, tools
from googleapiclient.discovery import build
from httplib2 import Http

def open(verbose=False):
	"""
	Ouvre et renvoie la connexion à l'api Gmail
	"""
	try:
		store = file.Storage('mailautolabel/gmail/token.json')
		creds = store.get()

		if not creds or creds.invalid:
			# Si vous modifiez ces `SCOPES`, supprimez le fichier `token.json`.
			SCOPES = 'https://www.googleapis.com/auth/gmail.modify'

			flow = client.flow_from_clientsecrets('mailautolabel/gmail/credentials1.json', SCOPES)
			creds = tools.run_flow(flow, store)
		
		return build('gmail', 'v1', http=creds.authorize(Http()))
	
	except Exception as err:
		print(err)
		sys.exit(2)