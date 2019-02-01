import json
import time
from Browser import BrowserData
from Countries import Countries
from DotFileConverter import DOTFileConverter
from Graphs import Graphs
from UserDoc import UserData


class DataReader():
    def __init__(self, jsonPath):
        self.jsonFile = open(jsonPath, 'r')
        self.jsonData = []
        self.rData = []
        self.countries = []
        self.c = Countries('countries_out.json')
        self.b = BrowserData()
        self.u = UserData(self.c)
        self.g = Graphs(self.c)
        self.d = DOTFileConverter()

        start_time = time.time()

        self.readFile()
        elapsed_time = time.time() - start_time
        print("read file in: " + str(elapsed_time) + " seconds")
        start_time = time.time()
        #print(self.c.CountryCount["US"])
        print(self.c.ContinentCount)
        print(self.countries[0])
        #print(self.b.BrowserCount)
        #print(self.rData[33491]["visitor_uuid"])
        #print(self.u.docInfo['130601015527-c1e2993d8290975e7ef350f078134390'])
        docId = '140207031738-eb742a5444c9b73df2d1ec9bff15dae9'
        userId = ''
        #readers = self.u.getJointReaders(docId, userId)
        elapsed_time = start_time - time.time()
        print("found joint readers in: " + str(elapsed_time) + " seconds")
        #for key, val in readers.items():
        #    print("Doc: " + key + ", Read by:" + str(val))
        #self.g.ContinentHistogram(self.u, 'aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe')
        #self.g.ContinentHistogram(self.u, 'aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe')
        #self.g.GeneralBrowserHistogram(self.b)
        #self.d.createDOTFile(readers, docId, userId)
        #dump(self.b.testlines)

        #print(self.u.userInfo['892bfc5b9f6dfbfb'])
        print(self.b.OsKeys)
        print(len(self.b.BrowserOsCount))
        #print(self.b.BrowserCount)

    def readFile(self):
        all_counter = 0
        jsonLine = []


        for line in self.jsonFile:
            #print(all_counter)
            jsonLine = json.loads(line)
            self.rData.append(jsonLine)
            self.c.addCountry(jsonLine)
            self.c.addContinent(jsonLine)
            if(jsonLine["event_type"] == "read"):
                self.u.addUserDocument(jsonLine)
            if "visitor_useragent" in line:
                self.b.addBrowser(jsonLine["visitor_useragent"])
                self.countries.append(jsonLine['visitor_country'])
            #print(all_counter)

            all_counter += 1
            if(all_counter%100000 == 0):
                print(all_counter)
        print("out of loop")

        print("joined")

    def getCountryCount(self):
        return self.c.CountryCount

    def getContinents(self):
        return self.c.ContinentCount

    def OutputUserDoc(self,docId, userId):
        readers = self.u.getJointReaders(docId, userId)
        for key, val in readers.items():
            print("Doc: " + key + ", Read by:" + str(val))

    def CreateDotFile(self,docId,userId):
        readers = self.u.getJointReaders(docId, userId)
        self.d.createDOTFile(readers, docId, userId)
