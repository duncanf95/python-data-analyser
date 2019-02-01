from collections import OrderedDict


class UserData():
    def __init__(self, inputCountry):
        self.userInfo = {}
        self.docInfo = {}
        self.jointReaders = {}
        self.c = inputCountry

    def addUserDocument(self, line):
        visitor = line["visitor_uuid"]
        doc = line["subject_doc_id"]
        country = line["visitor_country"]
        if country in self.c.Data:
            continent = self.c.Data[line["visitor_country"]]["Continent Code"]

            if visitor in self.userInfo:
                self.userInfo[visitor]['read'].append(doc)
            else:
                self.userInfo[visitor] = {'read': [doc], 'country': country, 'continent': continent}

            if doc in self.docInfo:
                self.docInfo[doc].append(visitor)
            else:
                self.docInfo[doc] = [visitor]

    def getJointReaders(self, docId, userId):
        readers = self.docInfo[docId]
        if(userId == ''):
            for i in range(len(readers)):
                for c in range(len(self.userInfo[readers[i]]['read'])):
                    readDocument = self.userInfo[readers[i]]['read'][c]

                    if self.userInfo[readers[i]]['read'][c] in self.jointReaders:
                        if readers[i] not in self.jointReaders[readDocument][0]:
                            self.jointReaders[readDocument][0].append(readers[i])
                            self.jointReaders[readDocument][1] += 1
                    else:
                        self.jointReaders[self.userInfo[readers[i]]['read'][c]] = [[readers[i]], 1]
        else:
            for i in range(len(readers)):
                for c in range(len(self.userInfo[readers[i]]['read'])):
                    readDocument = self.userInfo[readers[i]]['read'][c]
                    if readers[i] != userId or readDocument == docId:
                        if self.userInfo[readers[i]]['read'][c] in self.jointReaders:
                            if readers[i] not in self.jointReaders[readDocument][0]:
                                self.jointReaders[readDocument][0].append(readers[i])
                                self.jointReaders[readDocument][1] += 1
                        else:
                            self.jointReaders[self.userInfo[readers[i]]['read'][c]] = [[readers[i]], 1]
        return OrderedDict(sorted(self.jointReaders.items(), key=lambda e: e[1][1], reverse=True))

    def getUserJointReaders(self, docId, userId):
        return 0

    def getReaders(self, docId):
        return self.docInfo[docId]

    def getReadDocuments(self, userId):
        return self.userInfo[userId]
