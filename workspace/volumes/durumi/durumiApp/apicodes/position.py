#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from .apikey import * #if using on django , should using .apikey instead apikey 
import json

def positionFindAPI(inputKeyword):
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/locationBasedList'
    queryParams = '?' + 'ServiceKey=' + ServiceKey + '&' + urlencode({
        quote_plus('numOfRows') : '10',
        quote_plus('pageNo') : '1',
        quote_plus('MobileOS') : 'ETC',
        quote_plus('MobileApp') : 'AppTest',
        quote_plus('listYN') : 'Y',
        quote_plus('arrange') : 'A',
        quote_plus('contentTypeId') : '12',
        #quote_plus('mapX') : '126.981611',
        #quote_plus('mapY') : '37.568477',
        quote_plus('mapX') : '126.8022693',
        quote_plus('mapY') : '37.4859658',
        quote_plus('radius') : '1000',
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