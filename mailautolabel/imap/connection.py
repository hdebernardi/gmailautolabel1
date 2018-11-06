# -*- coding: <utf-8> -*-

import imapclient

################################################################################
def open(hostname, username, password, verbose=False):
	# Connect to the server
	if verbose :
		print('Connecting to', hostname)
	connection = imapclient.IMAPClient(host=hostname)

	# Login to our account
	if verbose:
		print('Logging in as', username)
	try:
		connection.login(username, password)
		print('Logged successfully')
	except Exception as err:
		print('ERROR:', err)

	return connection
