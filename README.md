# Mining-Stats

### Works on Python 2.x and Python 3.x (1/28/2017)

Display miner stats individually and group stats for up to two miners on pool.bitcoin.com.
Also includes wallet stats, amount of BTC/BCH and USD value of wallet balance according to coinbase.com and the instant the request is made.

##### Sample output:
---
                    ----------------------MINER STATS-------------------------------------------
                                 TH/s Now  TH/s 10min Avg  TH/s 3hr Avg             Last Share
                  miner_01       15.55555       14.444444     12.222222  1776-13-13 05:55:55.0
                  miner_02       15.55555       13.333333     11.111111  1776-13-13 05:55:55.0




                  -----------------------USER STATS--------------------------------------------
                      Net HR 24h Avg  BTC Balance  BTC-USD  BCH Balance  BCH-USD
                  ->  30.003  19.920     0.000001  $123.45     0.000001  $123.45

---
When this program is run, https://api.coinbase.com/v2/prices/'PAIR'/spot is used to get current price of BCH and BTC. 
This data is placed in a Pandas DataFrame in KEY:VALUE format.



#### Limitations:

Can only track 2 miners.


###### Planned Upgrades:

1. ~~Allow the program to be refreshed, user set time between refresh.~~ Using watch for now
2. Get real fancy and add some colors; green=good, while red=bad.
3. May skip #2 if I decide to go down the GUI route and see what the options are for this program coupled with a GUI.
