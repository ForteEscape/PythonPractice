
class TextProcess:
    __textObjectCount = 0

    def __init__(self, path):
        TextProcess.__textObjectCount += 1

        self.__path = path
        self.__str_fileObject = None
        self.__processedData = None
        self.__filterList = []

    def __readFile(self):
        with open(self.__path, 'r') as fileObject:
            self.__str_fileObject = fileObject.read()

    def __processing(self):
        for index in self.__str_fileObject:
            __asciiCode = ord(index)

            if(__asciiCode < 65 or __asciiCode >90) and (__asciiCode < 97 or __asciiCode > 122):
                self.__str_fileObject = self.__str_fileObject.replace(index, ' ')

            self.__processedData = self.__str_fileObject.split()

    def __setFilterList(self):
        for index in self.__processedData:
            if index not in self.__filterList:
                self.__filterList.append(index)

    def writeFile(self, resultName):                      # writeFile, printResultData are output method -> public
        with open(resultName, 'w') as fileObject:
            openingString = "Word".ljust(18) + "Count\n"
            fileObject.write(openingString)

            for index in self.__filterList:
                cnt = self.__processedData.count(index)
                data = str(index).ljust(20) + str(cnt) + "\n"

                fileObject.write(data)

    def printResultData(self):
        for index in self.__filterList:
            wordCount = self.__processedData.count(index)
            data = str(index).ljust(20) + str(wordCount)

            print(data)

    def getObjectCount(self):
        return TextProcess.__textObjectCount

    def excuteAtOnce(self):                                 # processing manager method
        self.__readFile()
        self.__processing()
        self.__setFilterList()


myTextObject = TextProcess("MIT.txt")
print(myTextObject.getObjectCount())

yourTextObject = TextProcess("MIT.txt")
print(yourTextObject.getObjectCount())
