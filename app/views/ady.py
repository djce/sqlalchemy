from flask import Blueprint
from flask import jsonify
from ..extensions import session
from ..models import Girl
from flask import request

from urllib import request as _request
import re
import time

BASE_URL = 'https://pc.0ady.me/topic/'

ROOT_PATTERN = ''

class Ady8:

    def __init__(self) -> None:
        
        self.Headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }

    def get_urls(self):
        
        urls = [f'{BASE_URL}']

        tmp = [ f'{BASE_URL}index_{i}.html' for i in range(2,14) ]

        urls.extend(tmp)

        return urls

    def _fetch_content(self, url):
        req=_request.Request(url=url,headers=self.Headers)
        # req = request.urlopen(BASE_URL)
        res = _request.urlopen(req)
        content = res.read()
        return str(content, encoding='utf-8')

    def _analysis(self,html):
        pattern = '<div class="stui-vodlist__box">([\s\S]*?)<div class="stui-vodlist__detail">'
        pattern2 = '<a class="stui-vodlist__thumb active lazyload" href="/topic/.*/" title="(.*)" data-original="(.*)" style=" padding-top: .*%;" >'
        data = re.findall(pattern2, html)
        
        return [ {'name': item[0], 'avatar': item[1]} for item in data ]


    def go(self):
        urls = self.get_urls()

        data = []
        for url in urls:
            html = self._fetch_content(url)
            girls = self._analysis(html)
            print(girls)
            data.extend(girls)
            
        return data
    
ady_bp = Blueprint('girl', __name__)

@ady_bp.route('/ady', methods=['GET','POST'])
def add_girl():

    # data = Ady8().go()

    # girls = [ Girl(**item) for item in data ]

    # session.add_all(girls)

    # session.commit()

    args = request.args
    params = args.to_dict()

    pageIndex = int(params.get('page',1))
    pageSize = int(params.get('size',10))

    # girls = session.query(Girl).all()

    girls = session.query(Girl).limit(pageSize).offset((pageIndex-1)*pageSize).all()

    data = [ girl.to_dict() for girl in girls ]

    return jsonify({'code': 200, 'data': data})

