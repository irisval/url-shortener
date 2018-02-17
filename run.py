import config as CONFIG
from counter import *
import click
import math
from mongoengine import *
# chekc valid url
ALPHABET = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
base = len(ALPHABET)
UrlExistsError = Exception("Duplicate URL not being processed")
register_connection (
    alias = "default", 
    name = CONFIG.DB_NAME,
    username = CONFIG.DB_USERNAME,
    password = CONFIG.DB_PASSWORD,
    host = CONFIG.DB_HOST,
    port = CONFIG.DB_PORT
)

def encode(num):
	encoding = ''
	while (num):
		mod = num % base;
		encoding = ALPHABET[mod] + encoding
		num = math.floor(num / base)

	return encoding

def decode(str):
	decoding = 0
	while (str):
		index = ALPHABET.find(str[0])
		power = len(str) - 1
		decoding += index * (math.pow(base, power))
		str = str[1:]
	return int(decoding)

def check_url(url):
	try:
		entries = Urls.objects(full_url = url)
		if entries.count() == 1:
			return entries[0]
		return None
	except Exception:
		raise UrlExistsError

@click.command()
@click.option('--link', prompt='Link to Shorten')
def shorten(link):
	# print(check_url(link))
	u = Urls(Counter.objects()[0]["seq"], link)
	u.save()
	Counter.objects().update_one(upsert=True, inc__seq=1)
	# print(encode(10002))
	# print(decode('Tgmc'))
	# print(decode(''))
	# shortened = "http://irisv.me/" + encode()

if __name__ == '__main__':
   shorten()

# c = Counter(seq=)
# c.save()
# print(Counter.objects()[0]["seq"])
# Counter.objects()[0].update()
# Counter.objects().update_one(upsert=True, inc__seq=1)
# p = Urls(full_url="https://www.google.com/")
# p.save()

# MongoLab
