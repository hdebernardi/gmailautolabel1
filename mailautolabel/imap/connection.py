import imapclient

def open(hostname, username, password, verbose=False):
	# Connexion au serveur
	if verbose :
		print('Connexion à', hostname)
	connection = imapclient.IMAPClient(host=hostname)

	# Connexion à notre compte
	if verbose:
		print('Connexion en tant que', username)
	try:
		connection.login(username, password)
		print('Connecté avec succès')
		return connection
	except Exception as err:
		print('ERREUR:', err)
		sys.exit(2)
