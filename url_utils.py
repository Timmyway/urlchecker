import requests
import re

def is_url_alive(url):
	if not re.match(re.compile(r'http://|https://', re.I), url):
		url = f'http://{url}'
		print('New url value: ', url)
	try:
		r = requests.head(url, timeout=5)
		if r.status_code < 400:
			return True
		else:
			return False
	except requests.exceptions.ConnectionError as e:
		print(e)
		return False
	except requests.exceptions.InvalidURL as e:
		print(e)
		return False
	except requests.exceptions.MissingSchema as e:
		print(e)
		return False

urls = ['http://www.google.com', 'http://www.facebook.fr', 'https://www.youtube.fr',
	'http://urlfictive.eu', 'http://   coupé.com', 'www.google.com', 'www.foudamourdetoi.org',
	'HTTP://www.instagram.com', 'HT://www.instagram.com'
]

for url in urls:
	if is_url_alive(url):
		print(url, 'is alive')
	else:
		print(url, 'is down')