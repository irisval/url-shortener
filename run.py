import click
import math

ALPHABET = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
base = len(ALPHABET)

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


@click.command()
@click.option('--link', prompt='Link to Shorten')
def shorten(link):
	print(encode(10002))
	print(decode('Tgmc'))
	print(decode(''))

if __name__ == '__main__':
   shorten()
  
