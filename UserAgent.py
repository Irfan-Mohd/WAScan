from urllib import FancyURLopener


class UserAgent(FancyURLopener):
	"""It Contains useragents for the request"""
	version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'

userAgent = UserAgent()
