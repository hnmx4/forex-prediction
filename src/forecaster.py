import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR


class Forecaster:
    def __init__(self, ohlc):
        self.ohlc = ohlc

    def forecast(self):
        ts = self.ohlc.ix[:, 'close']
        Y = ts.values
        train, test = Y[1:len(Y) - 96], Y[len(Y) - 96:]

        model = AR(train)
        model_fit = model.fit()

        predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)

        plt.plot(test)
        plt.plot(predictions, 'b')
        plt.show()
