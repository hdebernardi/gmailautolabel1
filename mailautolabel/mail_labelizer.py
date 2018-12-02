import sys
import csv_helper

def main(argv):
	try:
		username = 'm1.autolabel1@gmail.com'
		#username = 'chucknorrism1luminy@gmail.com'

		labelised = csv_helper.toDict('LABELISED_' + username)
		unlabelised = csv_helper.toDict('UNLABELISED_' + username)
		
		predictions = ml.supervised.predictLabel(labelised, unlabelised)
		
		# on ouvre une connexion afin d'appliquer les labels
		service = gmail.connection.open(verbose)
		for prediction in predictions :
			gmail.mail.ajoutLabel(service, prediction['id'], prediction['label'])
	except Exception as err:
		print(err)
		sys.exit(1)
	
if __name__ == '__main__':
    main(sys.argv)
