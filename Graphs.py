import matplotlib.pyplot as plotter
from Countries import Countries
from collections import OrderedDict
import operator

class Graphs():
    def __init__(self, countires):
        self.c = Countries('countries_out.json')

    def CountryHistorgram(self, u, docId):

        data = u.getReaders(docId)
        xData = []
        yData = []

        for i in range(len(data)):
            self.c.addCountry(u.userInfo[data[i]]['country'])
        print(self.c.CountryCount)

        for key, val in self.c.CountryCount.items():
            if val > 0:
                xData.append(key)
                yData.append(val)

        return {'xData': xData, 'yData': yData}


    def ContinentHistogram(self, u, docId):
        data = u.getReaders(docId)
        xData = []
        yData = []

        for i in range(len(data)):
            self.c.addContinent(u.userInfo[data[i]]['country'])
        print(self.c.ContinentCount)

        for key, val in self.c.ContinentCount.items():
            if val > 0:
                xData.append(key)
                yData.append(val)

        #for i in range(len(yData)):
        #    del self.c.ContinentCount[yData[i]]
        return {'xData': xData, 'yData': yData}

    def GeneralBrowserHistogram(self, b):
        xData = []
        yData = []
        for key, val in b.BrowserCount.items():
            xData.append(key)
            yData.append(val['total'])

        return {'xData': xData, 'yData': yData}

    def AllBrowserHistogram(self, b):
        xData = []
        yData = []

        orderedData = OrderedDict(sorted(b.BrowserOsCount.items(), key=operator.itemgetter(1), reverse=True))
        for key, val in orderedData.items():
            xData.append(key)
            yData.append(val)

        return {'xData': xData, 'yData': yData}
