import requests

def is_url_alive(url):
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

urls = ['http://www.google.com', 'http://www.facebook.fr', 'https://www.youtube.fr',
	'http://urlfictive.eu', 'http://   coupé.com'
]

for url in urls:
	print(f'{url} is alive: {is_url_alive(url)}')