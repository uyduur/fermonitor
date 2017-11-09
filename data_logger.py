from arduino_graphing import DataHandler


class Logger():

    def __init__(self, beer_logs, fridge_logs, time_logs):

        self.beer_logs=beer_logs
        self.fridge_logs=fridge_logs
        self.time_logs=time_logs

        beer_logs = []
        fridge_logs = []
        time_logs = [0]


        beer_logs.append(DataHandler.bt)
        fridge_logs.append(DataHandler.ft)
        time_logs.append(len(beer_logs))

    def input_data():
        if len(self.beer_logs)==0:
            csv=open()
