import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class Prediction(object):
    def __init__(self, ticker_symbol=None):
        self.ticker_symbol = ticker_symbol

    def prediction(self):
        # read_data
        data = pandas_datareader.data.DataReader(self.ticker_symbol, 'yahoo', '2020-01-01')
        # calculate SMA
        data['SMA'] = data['Close'].rolling(window=14).mean()
        # calculate change rate in a day
        data['change'] = ((data['Close'] - data['Open']) / data['Open']) * 100
        # put
        data['label'] = data['Close'].shift(-30)
        # set train data and test data
        X = np.array(data.drop(['label', 'SMA'], axis=1))
        X = sklearn.preprocessing.scale(X)
        predict_data = X[-30:]
        X = X[:-30]
        y = np.array(data['label'])
        y = y[:-30]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        # create linear regression instance
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        predicted_data = lr.predict(predict_data)

        data['Predict'] = np.nan
        last_date = data.iloc[-1].name

        one_day = 86400
        next_unix = last_date.timestamp() + one_day

        for p_data in predicted_data:
            next_date = datetime.datetime.fromtimestamp(next_unix)
            next_unix += one_day
            data.loc[next_date] = np.append([np.nan]* (len(data.columns) - 1), p_data)

        data['Close'].plot(figsize=(8,4), color='green')
        data['Predict'].plot(figsize=(8,4), color='orange')
        # plt.show()
        plt.savefig('graph/graph.jpeg')
        plt.close()