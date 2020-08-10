import requests
import json
import time
import datetime
 
def start():
    #缓存文件的userId
    userId = "26398280"
    #缓存文件的token
    token = "D2A6AFB93531605DBE56DC2EEE74C4C9987A712B8B88B961B1FD1D77EA7638E98C11876C11E5DCE7CC0565963F917D29EDC68B689ADA81A6EF7681EE1C8EEF94D836F63E41B8CD2AFCAC5AFAA3121027241053A4B0C3744852ED144E8313F576.E28C556BA4E681092E106D23BF2DD192DE227AB6A6B3E562C260AF127B5EA468"
    #缓存文件的ck
    ck = "session=%7B%22accessToken%22%3A%22d6327d5a06a942618a571438e688b3f6%22%2C%22appType%22%3A6%2C%22expireAt%22%3A1599622152338%2C%22loginId%22%3A%2226398280%22%2C%22userType%22%3A99%2C%22gray%22%3Afalse%7D; accessToken2=d6327d5a06a942618a571438e688b3f6; appType2=6; expireAt2=1599622152338; loginId2=26398280; userType2=99; gray2=false; accessToken=D2A6AFB93531605DBE56DC2EEE74C4C9987A712B8B88B961B1FD1D77EA7638E98C11876C11E5DCE7CC0565963F917D29EDC68B689ADA81A6EF7681EE1C8EEF94D836F63E41B8CD2AFCAC5AFAA3121027241053A4B0C3744852ED144E8313F576.E28C556BA4E681092E106D23BF2DD192DE227AB6A6B3E562C260AF127B5EA468"
    step = 9999
    url = "https://sports.lifesense.com/sport_service/sport/sport/uploadMobileStepV2?accesstoken=" + token + "&userId=" + userId + "&appType=6&longitude=360&latitude=360&network_type=wifi&systemType=1&version=4.6.1&osversion=12.3.1&platform=ios&screenwidth=320&screenheight=568&requestId=0ee82a94c139470686968a3f9b4a8089&area=CN&language=zh&openudid=933BFE46-60C7-4869-86EF-93FBF14F5EAD&devicemodel=iPhone%20SE&os_country=CN&os_langs=zh&promotion_channel=app_store&timezone=Asia/Shanghai"
 
    pyload = {'timestamp': int(round(time.time())), 'list': [{'calories': '0', 'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'dataSource': '3',
                                            'deviceId': 'M_FE37336EBAD9788C46D99ACBA06A33CD923189CA', 'distance': '0',
                                            'id': '4610b81308c05444f93b8ce5ccd1ca026fd',
                                            'measurementTime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'priority': '0', 'step': step,
                                            'type': '0', 'userId': userId}]}
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Cookie": ck
    }
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text
    print(response)
    result = json.loads(response)
    print(result["msg"])
    return result["msg"];
 
 
def main_handler(event, context):
    return start()
 
 
if __name__ == '__main__':
    start();