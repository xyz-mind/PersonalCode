import httpx
import logging
import json


with httpx.Client(http2 = True) as client:
    response = client.get('https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=1963c3ae0bcc8-0241b60ae4589a-26011c51-168000-1963c3ae0bdc8&timeStamp=1744892767678&User-Agent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2&index=98&channelId=40009&sVersion=2&signKey=8906318f6de9fd9af8ea518a033cc011&WuKongReady=h5')
    json_data = response.json()
    print(json_data)

with open('../data/maoyan_crawler.json', 'w',encoding='utf-8') as f:
    f.write(json.dumps(json_data, indent=4, ensure_ascii=False))