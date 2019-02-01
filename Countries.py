import json


class Countries():
    def __init__(self, jsonPath):
        self.jsonFile = open(jsonPath, 'r')
        self.Data = {}
        self.CountryCount = {}
        self.ContinentCount = {'AF': 0, 'AN': 0, 'AS': 0, 'EU': 0, 'NA': 0, 'OC': 0, 'SA': 0}


        self.readFile()
        self.createCounters()
        #print(self.Data["AS"])
        #print(self.CountryCount)

    def readFile(self):
        self.Data = json.load(self.jsonFile)

    def createCounters(self):

        for key, val in self.Data.items():
            self.CountryCount[key] = 0


    def addCountry(self, line):
        if isinstance(line, str):
            country = line
        else:
            country = line["visitor_country"]
        if country in self.CountryCount:
            self.CountryCount[country] += 1
        else:
            self.CountryCount[country] = 1

    def addContinent(self, line):
        continent = ''
        if isinstance(line, str):
            inputVal = line
        else:
            inputVal = line["visitor_country"]
        if inputVal in self.CountryCount:
            if(inputVal in self.Data):
                continent = self.Data[inputVal]["Continent Code"]
                self.ContinentCount[continent] += 1
