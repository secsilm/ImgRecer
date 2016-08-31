# coding:utf8
import pandas as pd


def checkCSV(filename):
    data = pd.read_csv(filename)
    print "Checking ..."
    errorrow = []
    for rowidx in range(len(data)):
        if data.loc[rowidx, 'ID'] != int(data.loc[rowidx, 'FileName'].split('.')[0]):
            errorrow.append(data.loc[rowidx, 'ID'])
    if len(errorrow) == 0:
        print 'Congratulations! Everything looks fine!'
        return 1
    else:
        print 'Oh, NO! Something wrong happened ... '
        return 0

    return None
