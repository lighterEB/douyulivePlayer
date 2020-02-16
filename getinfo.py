import requests
from settings import Player
def getLiveAddr(rid):
    headers = {
        "Host": "playweb.douyucdn.cn",
        "Referer": "https://www.douyu.com/directory/myFollow",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "rid": "96291",
        "time": "1580382106787",
        "auth": "11f8c3b14a7b55fade7ce5162855ce81",
    }

    ret = requests.post("http://playweb.douyucdn.cn/lapi/live/hlsH5Preview/{}?rid={}&did=2dfd02149496030e407b1e3900031501".format(rid, rid), headers=headers)
    arry = ret.json()['data']['rtmp_live'].split("_")[0]
    addr = "http://tx2play1.douyucdn.cn/"+arry+"_4000.flv"
    return addr

def getLiveInfo(page):
    ret = requests.get("http://capi.douyucdn.cn/api/v1/live?limit=20&offset=%s" % page)
    # ret = requests.get("http://open.douyucdn.cn/api/RoomApi/live")
    ret = ret.json()['data']
    infoBox = []
    for i in range(len(ret)):
        if ret[i]['show_status'] == "1":
            ret[i]['show_status'] = "正在直播"
        else:
            ret[i]['show_status'] = "未开播"
        infoBox.append("房间名：{} {} ====房间号：{} ==== 直播状态：{}".format(ret[i]['nickname'], ret[i]['room_name'], ret[i]['room_id'], ret[i]['show_status']))
        print("房间名：{} {} ====房间号：{} ==== 直播状态：{}\n".format(ret[i]['nickname'], ret[i]['room_name'], ret[i]['room_id'], ret[i]['show_status']))
    return infoBox
if __name__ == "__main__":
    pass