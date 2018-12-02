import sys, getopt, time
import imap.connection, imap.mail
import gmail.connection, gmail.mail
import csv_helper

def imapExtractor(hostname, username, password, verbose):
	# la session sera nettoyée à la fin
	with imap.connection.open(hostname, username, password, verbose) as c:
		full_mails = imap.mail.getMails(c, verbose=verbose)
		mails = imap.mail.standardizeMails(full_mails)
		csv_helper.saveMails(username, mails)
	
	return True


def gmailExtractor(username, verbose):
	service = gmail.connection.open(verbose)
	allMails = gmail.mail.getMails(service)

	labelisedMails = []
	unlabelisedMails = []

	for mail in allMails:
		if 'folder' in mail:
			labelisedMails.append(mail)
		else:
			unlabelisedMails.append(mail)

	csv_helper.saveMails('LABELISED_' + username, labelisedMails)
	csv_helper.saveMails('UNLABELISED_' + username, unlabelisedMails)

	return True


def main(argv):
	unixOptions = 'he'
	gnuOptions = ['help', 'extractor=']

	try:
		arguments, values = getopt.getopt(argv, unixOptions, gnuOptions)
	except getopt.error as err:
		print(str(err))
		sys.exit(1)
	
	print(arguments, values)
	"""
	if len(arguments) == 0:
		print('You must choose an extractor between imap and gmail')
		sys.exit(1)
	"""
	hostname = 'imap.gmail.com'
	username = 'm1.autolabel1@gmail.com'
	password = 'm1-luminy'

	for currentArg, currentValue in arguments:
		if currentArg in ('-e', '--extractor'):

			if currentValue == 'imap':
				start = time.time()
				imapExtractor(
					hostname=hostname,
					username=username,
					password=password,
					verbose=True)
				end = time.time()
				print('Execution time {}'.format(end - start))
				return True

			elif currentValue == 'gmail':
				start = time.time()
				gmailExtractor(
					username=username,
					verbose=True)
				end = time.time()
				print('Execution time {}'.format(end - start))
				return True
			else:
				print('Invalid extractor')
				sys.exit(1)
		elif currentArg in ('-h', '--help'):
			print('Display help here...')

	start = time.time()
	gmailExtractor(
		username=username,
		verbose=True)
	end = time.time()
	print('Execution time {}'.format(end - start))

if __name__ == '__main__':
	main(sys.argv[1:])