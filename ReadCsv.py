class ReadCsv():

    def readCsv(self, pathOfCsv):
        output = []
        csvFile = open(pathOfCsv, newline='')
        for line in csvFile:
            row = [line]
            output.append(row)
        return output
