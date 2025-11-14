# fin_aiml

1. Pulling data from NSE using different broking accounts
2. Adding technical analysis after pulling the data
3. Adding financial data 
4. Look into building successful Trading Straties (Machine Learning and Deep Learning) and Back testing them
5. Trade to grow the capital by 66% CAGR


# Version of files
1. {no}_{script_name)_x.y.z.ipynb or .py
2. z version is updated for each development update
3. y version is updated for each testing update
4. x version is updated for each release either paper trading or real trading

5. {no} denotes the stage in the pipeline





# {no} and its significances
000 to 099 - Master data scripts, 
-   pulling hist or delta data. 
-   Downloading daily data, weekly data, min or 3 min or 15 min data from different sources NSE, Dhan, Fyers, yahoofinance etc. 
-   Also downloading financial data, 
-   downloading news, 
-   company events, 
-   results days etc.
-   downloading future expiry information
-   download relevant strike prices 
-   Also downloading Futures and Options data
100 to 199 - Transforming Data from individual Master files so that they are either in timeseries format or denormalized format or joining data between different formats to interpret better
200 to 499 - TA libraries to add more inferences to the data, either local min, max computations


Watching youtube Fessorpro 45 min