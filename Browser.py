class BrowserData():
    def __init__(self):
        self.BrowserCount = {}
        self.BrowserOsCount = {}
        self.browserKeys = ["Chrome", "Firefox", "Safari", "Opera", "MSIE", "Trident", "Nokia"]
        self.OsKeys = {'Windows NT':0, "Mac OS X": 0, 'Linux':0, "Android":0, "iPhone": 0, "unknown":0, "Windows Phone":0, "CrOS":0, "Nokia": 0, "UCBrowser": 0, "BB10":0, "BlackBerry":0}
        self.testlines = []


    def checkBrowser(self, browser, version):
        if browser not in self.BrowserCount:
            self.BrowserCount[browser] = {'total': 0, 'versions': {version: 0}}
        elif (version not in self.BrowserCount[browser]['versions']):
                self.BrowserCount[browser]['versions'][version] = 0

    def addBrowser(self, line):

        browserName = self.getBrowserString(line)
        version = ''
        if(browserName != None):
            sub = line.find(browserName)
            version = self.getVersion(line[sub:len(line)], browserName)
        self.checkBrowser(browserName, version)
        self.BrowserCount[browserName]['total'] += 1
        self.BrowserCount[browserName]['versions'][version] += 1

    def getBrowserString(self, line):
        #if line in self.BrowserOsCount:
        #    self.BrowserOsCount[line] += 1
        #else:
        #    self.BrowserOsCount[line] = 1
        found = False
        for key, val in self.OsKeys.items():
            if key in line:

                self.OsKeys[key]+=1
                OS = key

                found = True
                break
        if not found:
            OS = "unknown"
            self.OsKeys["unknown"]+=1

            print(line)


        for i in range(len(self.browserKeys)):
            if(self.browserKeys[i] in line):
                #print(self.browserKeys[i])
                browser = self.browserKeys[i]
                break
            else:
                browser = "unknown"
                version = ''
        if browser != 'unknown':
            sub = line.find(browser)
            version = self.getVersion(line[sub:len(line)], browser)
        fullText = OS + " " + browser + " " + version
        if fullText in self.BrowserOsCount:
            self.BrowserOsCount[fullText] += 1
        else:
            self.BrowserOsCount[fullText] = 1
        self.testlines.append(line)
        #print(browser)
        return browser

    def getVersion(self, line, browserKey):
        if(browserKey != 'unknown'):
            addition = len(browserKey)+1
        else:
            addition = 0
        counter = 0
        version = ''
        while (((counter + addition) < len(line)) and line[counter + addition] != ' '):
            version += line[counter + addition]
            counter += 1
            if((counter + addition) >= (len(line))):
                break

        return version
