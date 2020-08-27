#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from .apikey import * #if using on django , should using .apikey instead apikey 
import json

def regionFindAPI(inputKeyword):
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    queryParams = '?' + 'ServiceKey=' + ServiceKey + '&' + urlencode({
        quote_plus('numOfRows') : '2',
        quote_plus('pageNo') : '1',
        quote_plus('MobileOS') : 'ETC',
        quote_plus('MobileApp') : 'AppTest',
        quote_plus('listYN') : 'Y',
        quote_plus('arrange') : 'A',
        quote_plus('contentTypeId') : '15',
        quote_plus('areaCode') : '1',
        quote_plus('sigunguCode') : '1',
        quote_plus('cat1') : '',
        quote_plus('cat2') : '',
        quote_plus('cat3') : '',
        quote_plus('modifiedtime') : ''
    })
    request = Request(url + queryParams + "&_type=json")
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    getJson = json.loads(response_body)["response"]["body"]
    retItems = {}
    i = 0
    for item in getJson['items']['item'] :
        item = dict(item.items())
        retItems['item'+str(i)] = (json.dumps(item,ensure_ascii=False))
        i += 1
    return retItems

regionFindAPI('')