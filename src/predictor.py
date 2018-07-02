import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans


class Predictor:
    def __init__(self, ohlc):
        self.ohlc = ohlc

    def kmeans(self):
        _step = 96
        train = np.empty((0, _step))
        ts = self.ohlc.ix[:, 'close']
        for i in range(_step, len(ts), _step):
            train = np.append(train, np.array(ts.iloc[i - _step:i].values.reshape(1, _step)), axis=0)

        kmeans = KMeans(n_clusters=3, random_state=0).fit(train)
        print(kmeans.labels_)

    def predict_ar(self):
        ts = self.ohlc.ix[:, 'close']
        Y = ts.values
        train, test = Y[1:len(Y) - 96], Y[len(Y) - 96:]

        model = AR(train)
        model_fit = model.fit()

        predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)

        plt.plot(test)
        plt.plot(predictions, 'b')
        plt.show()

    def predict_ar2(self):
        ts = self.ohlc.ix[:, 'close']
        Y = ts.values
        train, test = Y[1:len(Y) - 96], Y[len(Y) - 96:]

        model = AR(train)
        model_fit = model.fit()
        window = model_fit.k_ar
        coef = model_fit.params

        history = train[len(train) - window:]
        print(history)
        history = [history[i] for i in range(len(history))]
        print(history)

        predictions = list()
        for t in range(len(test)):
            length = len(history)
            lag = [history[i] for i in range(length - window, length)]
            yhat = coef[0]
            for d in range(window):
                yhat += coef[d + 1] * lag[window - d - 1]
            obs = test[t]
            predictions.append(yhat)
            history.append(obs)
            print('predicted=%f, expected=%f' % (yhat, obs))
        error = mean_squared_error(test, predictions)
        print('Test MSE: %.3f' % error)

        plt.plot(test)
        plt.plot(predictions, 'b')
        plt.show()
