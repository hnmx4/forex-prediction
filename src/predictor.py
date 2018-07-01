import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error


class Predictor:
    def __init__(self, ohlc):
        self.ohlc = ohlc

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
                yhat += coef[d + 1] * lag[window-d-1]
            obs = test[t]
            predictions.append(yhat)
            history.append(obs)
            print('predicted=%f, expected=%f' % (yhat, obs))
        error = mean_squared_error(test, predictions)
        print('Test MSE: %.3f' % error)

        plt.plot(test)
        plt.plot(predictions, 'b')
        plt.show()
