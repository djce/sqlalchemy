from datetime import datetime, date
from flask.json import JSONEncoder as _JSONEncoder
from flask import Response as _Response
import decimal
import uuid

class Response(_Response):
    default_mimetype = "application/json"

class JSONEncoder(_JSONEncoder):
    
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, uuid.UUID):
            return str(o)
        elif isinstance(o, bytes):
            return o.decode('utf-8')
        else:
            _JSONEncoder.default(self, o)