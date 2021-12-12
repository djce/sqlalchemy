
query_string = 'name=root&password=123456'

def to_dict(query_string):
	return { k:v for k,_,v in map(lambda x:x.partition('='),query_string.split('&'))}



params = to_dict(query_string)

