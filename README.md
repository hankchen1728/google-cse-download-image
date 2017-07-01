# google-cse-download-image

## 1.新增搜尋引擎
[https://cse.google.com/cse/](https://cse.google.com/cse/)<br />
1)**新增搜尋引擎** > 要搜尋的網站：**www.google.com** > 點擊 **建立** <br>
2)**編輯搜尋引擎** > 開啟 **圖片搜尋** > **要搜尋的網站** 選擇 **搜尋整個網路，但特別強調收錄的網站** > 點擊 **搜尋引擎ID** 並複製  <br>

## 2.取得API key
[https://console.developers.google.com/](https://console.developers.google.com/)<br />

## python設定
### 安裝Google APIs Client Library
	$ pip install --upgrade google-api-python-client

google_api_image_download.py 第10行 **DIR** 請改成自己儲存圖片資料夾的路徑

## 參考資料
[https://stackoverflow.com/questions/22866579/download-images-with-google-custom-search-api](https://stackoverflow.com/questions/22866579/download-images-with-google-custom-search-api)<br>
[https://stackoverflow.com/questions/6562125/getting-a-cx-id-for-custom-search-google-api-python]
(https://stackoverflow.com/questions/6562125/getting-a-cx-id-for-custom-search-google-api-python)<br>
[https://productforums.google.com/forum/#!topic/customsearch/2qilVDaCz0A]
(https://productforums.google.com/forum/#!topic/customsearch/2qilVDaCz0A)<br>
