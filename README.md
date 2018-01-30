# Mining-Stats

### Works on Python 2.x and Python 3.x (1/28/2017)

Get all miners on pool.bitcoin.com account; their hashrate individually. Also includes user stats, like how much is in the wallet and what the USD value of it is.


Sample output:

                    ----------------------MINER STATS-------------------------------------------
                                 TH/s Now  TH/s 10min Avg  TH/s 3hr Avg             Last Share
                  miner_01       15.55555       14.444444     12.222222  1776-13-13 05:55:55.0
                  miner_02       15.55555       13.333333     11.111111  1776-13-13 05:55:55.0




                  -----------------------USER STATS--------------------------------------------
                      Net HR 24h Avg  BTC Balance  BTC-USD  BCH Balance  BCH-USD
                  ->  30.003  19.920     0.000001  $123.45     0.000001  $123.45


When this program is run, https://api.coinbase.com/v2/prices/'PAIR'/spot is used to get current price of BCH and BTC. 
This data is placed in a Pandas DataFrame in KEY:VALUE format.



Limitations:

Can only run across 2 miners currently. I am still working out, in my head, how I will make it scalable to accommodate X number of miners. 



Planned Upgrades:

1. Allow the program to be refreshed, user set time between refresh.
2. Get real fancy and add some colors; green will be an increase, while red will be a decrease since last refresh.
3. May skip #2 if I decide to go down the GUI route and see what the options are for this program coupled with a GUI.
4. Continue learning Python (started in June of 2017).
