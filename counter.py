from mongoengine import *
import datetime

class Counter(Document):
	meta = {
		"strict": False
	}
	seq = IntField(default=0,required=True)

class Urls(Document):
	meta = {
		"strict": False
	}
	_id = IntField(default=0, primary_key=True)
	full_url = StringField(required=True)
	timestamp = DateTimeField(default=datetime.datetime.now)