import os
import glob
from tcms_api import TCMS
import datetime
from ReadCsv import ReadCsv


class Main():

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH = glob.glob(os.path.join(ROOT_DIR, 'csv/')+"*.csv")
    rpc_client = TCMS()

    def csvToList(self):
        print(self.CSV_PATH)
        for files in self.CSV_PATH:
            readCsv1 = ReadCsv()
            outputOfCsv = readCsv1.readCsv(files)
            print(outputOfCsv)
            return outputOfCsv

    def __Main__(self):
        print(self.CSV_PATH)

    def formatList(self):
        csv = self.csvToList()
        finalList = []
        i = len(csv)
        j = 0
        k = 0

        while j < i:
            finalList.append([])
            while k < 7:
                finalList[j].append(csv[k])
                k = k + 1
            j = j + 1
            if  j == i or j > i:
                break

        print(finalList)



    def createTestPlan(self):
        test_plan = self.rpc_client.exec.TestPlan.create({
            'name': 'Mobile App From Script',
            'text': 'Function Testing, Integration Testing, Regression Testing',
            'type': 11,  # Performance
            'product': 2,
            'product_version': 4,
            'is_active': True,
        })

    def formatString(self,listOfString):
        formattedString = "";
        for s in listOfString:
            formattedString = formattedString + s + '\n'
        return formattedString




    def createTestCases(self):
        test_cases = self.csvToList()
        for idx,case in enumerate(test_cases):
            val = case[0]
            break_list = val.split(',')
            list_of_desc = break_list[1].split('\\n')
            desc = self.formatString(list_of_desc)
            list_of_steps = break_list[3].split('\\n')
            steps = self.formatString(list_of_steps)
            list_of_data = break_list[4].split('\\n')
            data = self.formatString(list_of_data)
            list_of_expected = break_list[6].split('\\n')
            expected_results = self.formatString(list_of_expected)
            is_automated = break_list[5]
            text = f'**Data: ** \n {data} \n\n\n**Steps: ** \n {steps} \n\n\n **Expected :** \n {expected_results}'
            test_case = self.rpc_client.exec.TestCase.create({
                'summary': desc,
                'text': text,
                'product': 2,
                'category': 4,
                'priority': 1,
                'case_status': 2,  # CONFIRMED
                'author': 'on',
                'is_automated': is_automated,
                'managers_of_runs': 'on',
                'assignees_of_case_runs': 'on',
                'default_tester_of_case': 'on',
                'default_testers_of_runs': 'on',
                'notify_on_case_update': 'on',
                'notify_on_case_delete': 'on'
            })
            self.rpc_client.exec.TestPlan.add_case(4, test_case['case_id'])


m = Main()
m.createTestCases()
