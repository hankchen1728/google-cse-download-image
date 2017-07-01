from apiclient.discovery import build
import requests
import os
import json

Search_engine = input('Enter the search engine to use in your request:')
api_key = input('Enter your API key:')
search = input('Enter what you want to search:')
#DIR請改成要儲存圖片資料夾的路徑
DIR = '/Users/hankchen/downloads/'
DIR = os.path.join(DIR,search)
if not os.path.exists(DIR):
    os.mkdir(DIR)

def build_request(startindex,low_range):
    service = build("customsearch", "v1",developerKey=api_key)
    res = service.cse().list(
        q = search,
        cx = Search_engine,
        num = 10,
        start = startindex,
        searchType='image',
        safe= 'off',
        lowRange=low_range,
        highRange=low_range+100
    ).execute()
    return res

for x in range(1,1000,10):
    print("這是第",x,"~",x+9,"結果")
    StartIndex = x%100
    LowRange = (x//100)*100
    res = build_request(StartIndex,LowRange)
    count = 0
    for item in res['items']:
        index = x + count
        #print(item['link'])
        link = item['link']
        reqimg = requests.get(link,stream=True,headers=header)
        imgdata = reqimg.content
        filename = search+str(index)+'.jpg'
        #以返回的二進位制數據創建圖片
        f = open(os.path.join(DIR , filename), 'wb')
        f.write(imgdata)
        f.close
        del reqimg
        print('第',index,'張',search,'圖片下載完成')
        count += 1
