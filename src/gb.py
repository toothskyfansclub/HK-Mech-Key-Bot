from pymongo import MongoClient
from decouple import config

from utils import get_time, send_text


def get_keycap_GB(update, context):
    args =context.args
    val = 7 if len(args) == 0 else int(args[0])
    date_list = get_time(month=True, value=val)

    client = MongoClient(config('DB'))
    keycaps_db = client.mechkey.keycap

    res = '由今天計起，未來' + str(val) + '日內終結的鍵帽團購有：\n'

    for date in date_list:
        keycaps = keycaps_db.find_one({'date': date})
        if keycaps:
            res += '\n' + date + '\n'
            for keycap in keycaps['name']:
                res += ('- ' + keycap + '\n') 

    send_text(update, context, res + '\n完\n\n*基於資訊網可信性成疑，以及時區問題，Bot不確保100%準確，玩家請自行Double Check')