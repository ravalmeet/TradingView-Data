
# TradingView Data For any Indexes and Stocks

A Simple TradingView Data Downloader. TradinViewData allows downloading upto 5000 Candles on any of the supported timeframe.

    
# Usage

```Python
from TradingviewData import TredingViewData,Interval

request = TradingViewData()
```


# Get Symbol


To find the exact symbols for an instrument you can use ``` request.search_symbol ``` method.

```Python

request.search('METAL','MCX')
```

Other method is check Manually via [Tradingview Search]("https://www.tradingview.com/markets/indices/").


# Getting Data


## Index

```Python
nifty_data = request.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.hour_1,n_bars=1000)
```
## Futures continuous contract

```Python
nifty_futures = request.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.hour_1,n_bars=1000,fut_contract=1)
```

## Stocks

```Python
relience_data = request.get_hist(symbol='RELIANCE',exchange='NSE',interval=Interval.min_5,n_bars=5000)
```

## MCX

```Python
crudeoil_data = request.get_hist(symbol='CRUDEOIL',exchange='MCX',interval=Interval.hour_1,n_bars=5000)
```

## Downloading data for extended market hours


```Python
extended_data = request.get_hist(symbol="EICHERMOT",exchange="NSE",interval=Interval.hour_1,n_bars=500, extended_session=False)
```


## Supported Time Frames


#####  1 Minute = min_1
#####  3 Minute = min_3
#####  5 Minute = min_5
#####  15 Minute = min_15
#####  30 Minute = min_30
#####  45 Minute = min_45
#####  1 Hour = hour_1
#####  2 Hour = hour_2
#####  3 Hour = hour_3
#####  4 Hour = hour_4
#####  1 Day = daily
#####  1 Week = weekly
#####  1 Month = monthy
