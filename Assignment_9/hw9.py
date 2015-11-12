__author__ = 'Suman'


import Tkinter
import tkFileDialog
import pandas as pd
import numpy as np
import os

def load_data():
    root = Tkinter.Tk()
    root.withdraw()
    f = tkFileDialog.askopenfilename(defaultextension='.txt', title="Select the EPA-HTTP Data File")

    #read the file using read_csv, also escape the = , and put na values wherever reply bytes is '-' etc.
    data =  pd.read_csv(f, delimiter=" ", quoting=1, quotechar="\"", escapechar="=",
                        header = 0,
                        names=["host", "date", "request", "status", "replyBytes"],
                        index_col=["host", "date", "request", "status"],
                        na_values={"replyBytes" : "-"})

    #replace NaN for replyBytes with zeroes (mutate the data frame)
    data["replyBytes"].fillna(0, inplace=True)

    return data


def analyse_data(data):
    print '----------------------------------------------------------------------------------------------'
    #Which hostname or IP address made the most requests?
    reqs = data.groupby(level='host')
    print 'The host that made the max number of requests was: %s, with a total of %d requests.' \
         % (reqs.size().argmax(), reqs.size().max())
    print os.linesep

    #Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive?
    print 'The host that received the most total bytes from the server is: %s, with a total of %d bytes' \
        % (reqs.replyBytes.sum().argmax(), reqs.replyBytes.sum().max())
    print os.linesep

    #During what hour was the server the busiest in terms of requests?
    #let add hour to the df
    rawdata = data.reset_index()
    dateVals = rawdata.loc[:, "date"]
    dataWithHr = rawdata.join(pd.Series(data=dateVals.str.split(":").str.get(1), name="hour"))
    dataWithHr = dataWithHr.set_index(keys = ["host", "date", "request", "status", "hour"])
    hourGroup = dataWithHr.groupby(level="hour")
    print 'The maximum number of requests : %s, received during the hour %s:00 - %s:00.' \
          % (hourGroup.size().max(), hourGroup.size().argmax(), int(hourGroup.size().argmax()) + 1)
    print os.linesep

    #Which .gif image was downloaded the most during the day?
    gifdata = rawdata[rawdata['request'].str.contains(".gif")].groupby('request')
    print 'The .gif file that was most requested : %s, with a total number of %d requests.' \
          % (gifdata.size().argmax().split('/')[2].split(' ')[0], gifdata.size().max())
    print os.linesep

    #What HTTP reply codes were sent other than 200?
    statusdata = rawdata.loc[:, "status"]
    uniqueStatuses = statusdata.unique()
    print('HTTP reply code other than 200 : %s' % uniqueStatuses[np.where(uniqueStatuses <> 200)])
    print '----------------------------------------------------------------------------------------------'


if __name__ == '__main__':
    #Load the data & analyse
    analyse_data(load_data())

