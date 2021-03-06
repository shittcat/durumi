#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from apikey import * #if using on django , should using .apikey instead apikey 
import json 

def keywordFindAPI(inputKeyword):
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword'
    #find place by keyword API
    queryParams = '?' + 'ServiceKey='+ServiceKey+'&'+urlencode({ 
        quote_plus('MobileApp') : 'AppTest', 
        quote_plus('MobileOS') : 'ETC', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '100', 
        quote_plus('listYN') : 'Y', quote_plus('arrange') : 'A', quote_plus('contentTypeId') : '12', 
        quote_plus('areaCode') : '', quote_plus('sigunguCode') : '', quote_plus('cat1') : '', 
        quote_plus('cat2') : '', quote_plus('cat3') : '', quote_plus('keyword') : inputKeyword 
    })
    request = Request(url + queryParams + "&_type=json")
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    
    #make dict datas
    getJson = json.loads(response_body)["response"]["body"]
    retItems = {}
    i=0
    
    tcount = (getJson['totalCount'])
    tnum = (getJson['numOfRows'])
    
    if (tcount == 1) or (tnum == 1) : #if result count is 1
        item = getJson["items"]["item"]
        retItems['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
    else :
        for item in getJson["items"]["item"] :
            item = dict( item.items() )
            retItems['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
            i += 1
            #make dict_items type Objects to list type objects
    return retItems #return datas to json data


def positionFindAPI(gpsLoc):
    gpsLoc = gpsLoc.split(":")
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/locationBasedList'
    queryParams = '?' + 'ServiceKey=' + ServiceKey + '&' + urlencode({
        quote_plus('numOfRows') : '10',
        quote_plus('pageNo') : '1',
        quote_plus('MobileOS') : 'ETC',
        quote_plus('MobileApp') : 'AppTest',
        quote_plus('listYN') : 'Y',
        quote_plus('arrange') : 'A',
        quote_plus('contentTypeId') : '12',
        quote_plus('mapX') : gpsLoc[0],
        quote_plus('mapY') : gpsLoc[1],
        quote_plus('radius') : '3000',
        quote_plus('modifiedtime') : ''
    })
    request = Request(url + queryParams + "&_type=json")
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    #make dict datas
    getJson = json.loads(response_body)["response"]["body"]
    retItems = {}
    i=0
    
    tcount = (getJson['totalCount'])
    tnum = (getJson['numOfRows'])
    print (getJson["items"]["item"])
    if (tcount == 1) or (tnum == 1) : #if result count is 1
        item = getJson["items"]["item"]
        retItems['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
    else :
        for item in getJson["items"]["item"] :
            item = dict( item.items() )
            retItems['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
            i += 1
            #make dict_items type Objects to list type objects
    return retItems #return datas to json data

if __name__ == "__main__" : 
    gpsLoc = "126.804388:37.485773"
    print (positionFindAPI(gpsLoc))
    # print (keywordFindAPI("광화문"))