# -*- coding: <utf-8> -*-

import bs4

################################################################################
def decode_html(html):
	soup = bs4.BeautifulSoup(html, 'html.parser')
	
	# kill all script and style elements
	for script in soup(['script', 'style']):
		script.extract() # rip it out

	# get text
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())

	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split(' '))
	# drop blank lines
	#text = '\n'.join(chunk for chunk in chunks if chunk)
	text = ''.join(chunk for chunk in chunks if chunk)

	return text
