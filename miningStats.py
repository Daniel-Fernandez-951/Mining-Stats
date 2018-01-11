import requests
import pandas as pd


# Mining data and Mining user data
# To speed up remove APIKEY variable and insert manually in both ({0} with your api string)
    # AND remove <.format(APIKEY)> from both worker_loc & user_loc
APIKEY = ''
worker_loc = ('https://console.pool.bitcoin.com/srv/api/workers?apikey={0}'.format(APIKEY))
user_loc = ('https://console.pool.bitcoin.com/srv/api/user?apikey={0}'.format(APIKEY))

# Transaction fee of all currencies
tx_fee = ('https://bittrex.com/api/v1.1/public/getcurrencies')


# Get price of currency in USD
market_coinbase_priceBTC = ('https://api.coinbase.com/v2/prices/BTC-USD/spot')
market_coinbase_priceBCH = ('https://api.coinbase.com/v2/prices/BCH-USD/spot')


def minerStats():
    worker_call = (requests.get(worker_loc)).json()
    miner_df = pd.DataFrame(
            {'Last Share': [(str(worker_call[0]['lastShareTime'])),
                (str(worker_call[1]['lastShareTime']))],
            'TH/s 3hr Avg': [(float(worker_call[0]['hashrate3hrAverageTerahashes'])),
                (float(worker_call[1]['hashrate3hrAverageTerahashes']))],
            'TH/s 10min Avg': [(float(worker_call[0]['hashrate10minAverageTerahashes'])),
                (float(worker_call[1]['hashrate10minAverageTerahashes']))],
            'TH/s Now': [(float(worker_call[0]['hashrateNowTerahashes'])),
                (float(worker_call[1]['hashrateNowTerahashes']))]},
            index=[(worker_call[0]['workername']), (worker_call[1]['workername'])],
            columns=['TH/s Now', 'TH/s 10min Avg', 'TH/s 3hr Avg', 'Last Share'])

    print miner_df


def userStats():
    user_call = (requests.get(user_loc)).json()
    bch_call = (requests.get(market_coinbase_priceBCH)).json()
    btc_call = (requests.get(market_coinbase_priceBTC)).json()

    btc_usd = (float(user_call['bitcoinBalance'])
                * float(btc_call['data']['amount']))
    bch_usd = (float(user_call['bitcoinCashBalance'])
                * float(bch_call['data']['amount']))

    user_df = pd.DataFrame(
            {'Net HR': (float(user_call['hashrateNowTerahashes'])),
            '24h Avg': (float(user_call['hashrateAverage24hrsTerahashes'])),
            'BTC Balance': (float(user_call['bitcoinBalance'])),
            'BTC-USD Balance': ('$' + str(btc_usd)),
            'BCH Balance': (float(user_call['bitcoinCashBalance'])),
            'BCH-USD Balance': ('$' + str(bch_usd))},
            index=['->'],
            columns=['Net HR', '24h Avg', 'BTC Balance', 'BTC-USD Balance', 'BCH Balance', 'BCH-USD Balance'])

    print user_df


print '\n', '----------------------MINER STATS-------------------------------------------', '\n'
minerStats()

print '\n', '\n', '-----------------------USER STATS--------------------------------------------', '\n'
userStats()
print '\n'
