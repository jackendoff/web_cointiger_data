import requests
import json
import csv
import time

# 获取cointiger.pro的深度盘口数据，并保存到对应csv文件中
class GetCoin_tiger(object):

    def __init__(self,coin_name):
        self.coin_name = coin_name
        self.url = 'https://api.cointiger.pro/exchange/trading/api/market/depth?symbol='+coin_name+'&type=step0'

    @staticmethod
    def get_all_coin_name():
        # 获取所有的cointiger.pro coin_name
        url = 'https://api.cointiger.pro/exchange/trading/api/v2/currencys'

        data = requests.get(url)
        dict_data = json.loads(data.content.decode())
        print(data, type(data))
        coin_name = []
        for every_dict in dict_data['data']:
            for coin in dict_data['data'][every_dict]:
                coin_str = coin['baseCurrency'] + coin['quoteCurrency']
                coin_name.append(coin_str)
        return coin_name

    def get_data(self):
        r = requests.get(self.url)
        data = r.content.decode()
        return data

    def data_buy_to_csv(self,data_dict):
        headers = ['price','amount']
        rows = data_dict['data']['depth_data']['tick']['buys']
        with open(self.coin_name+'_buy.csv', 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)
        print(coin_name,'_buy:保存文件完成')

    def data_asks_to_csv(self,data_dict):
        headers = ['price','amount']
        rows = data_dict['data']['depth_data']['tick']['asks']
        with open(self.coin_name+'_asks.csv', 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)
        print(coin_name,'_asks:保存文件完成')


if __name__ == '__main__':
    coin_list =['xembitcny', 'ethbitcny', 'ocnbitcny', 'gtobitcny', 'trxbitcny', 'btabitcny', 'btcbitcny', 'tchbitcny', 'socbtc', 'binbtc', 'kkgbtc', 'eosbtc', 'dicebtc', 'finbtc', 'qosbtc', 'etcbtc', 'ethbtc', 'cvcoinbtc', 'weccbtc', 'ocnbtc', 'repbtc', 'elfbtc', 'icxbtc', 'tusdbtc', 'mtbtc', 'olebtc', 'sphbtc', 'sdabtc', 'rcbtc', 'ctxcbtc', 'ihtbtc', 'eletbtc', 'trxbtc', 'alzabtc', 'zrxbtc', 'aacbtc', 'fgcbtc', 'gusbtc', 'bcgbtc', 'omgbtc', 'psmbtc', 'avhbtc', 'tchbtc', 'yeebtc', 'enbbtc', 'ltcbtc', 'btmbtc', 'pxgbtc', 'incbtc', 'afcbtc', 'btsbtc', 'mexbtc', 'bchabcbtc', 'storjbtc', 'enubtc', 'csbtc', 'pttbtc', 'tfbtc', 'bkbtbtc', 'sntbtc', 'bchsvbtc', 'riskbtc', 'eosusdt', 'etcusdt', 'ethusdt', 'omgusdt', 'btcusdt', 'ltcusdt', 'tctusdt', 'bineth', 'kkgeth', 'eoseth', 'qoseth', 'cvcoineth', 'wecceth', 'mteth', 'oleeth', 'sdaeth', 'rceth', 'ctxceth', 'ihteth', 'baiceth', 'eleteth', 'trxeth', 'alzaeth', 'zrxeth', 'fgceth', 'guseth', 'bcgeth', 'omgeth', 'psmeth', 'voceth', 'btaeth', 'yeeeth', 'enbeth', 'btmeth', 'pxgeth', 'inceth', 'btseth', 'enueth', 'cseth', 'ptteth', 'tfeth', 'bkbteth', 'risketh', 'nasheth']
    print('总共的数据量',len(coin_list))
    n = 1
    for coin_name in coin_list:
        try:
            obj_data_deep = GetCoin_tiger(coin_name)
            data_str = obj_data_deep.get_data()
            if data_str == '':
                print(coin_name,'数据为空')
                continue
            data_dict = eval(data_str)
            obj_data_deep.data_buy_to_csv(data_dict)
            obj_data_deep.data_asks_to_csv(data_dict)
            time.sleep(1)
            print('已完成数据量',n)
            n += 1
        except:
            print(coin_name,'============数据错误，请查看')
            continue