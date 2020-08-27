#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from apikey import *

def keywordfind(inputKeyword):
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword'
    queryParams = '?' + 'ServiceKey='+ServiceKey+'&'+urlencode({ 
        quote_plus('MobileApp') : 'AppTest', 
        quote_plus('MobileOS') : 'ETC', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', 
        quote_plus('listYN') : 'Y', quote_plus('arrange') : 'A', quote_plus('contentTypeId') : '12', 
        quote_plus('areaCode') : '', quote_plus('sigunguCode') : '', quote_plus('cat1') : '', 
        quote_plus('cat2') : '', quote_plus('cat3') : '', quote_plus('keyword') : inputKeyword 
    })
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    return (response_body)