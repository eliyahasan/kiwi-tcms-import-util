import os
import glob
from tcms_api import TCMS
import datetime
from ReadCsv import ReadCsv


class Main:

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH = glob.glob(ROOT_DIR + "/*.csv")
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
            if j == i or j > i:
                break

        print(finalList)

    def createTestPlan(self):
        test_plan = self.rpc_client.exec.TestPlan.create(
            {
                "name": "Foree Mobile App From Script",
                "text": "Function Testing, Integration Testing, Regression Testing",
                "type": 11,  # Performance
                "product": 2,
                "product_version": 4,
                "is_active": True,
            }
        )

    def formatString(self, listOfString):
        formattedString = ""
        for s in listOfString:
            formattedString = formattedString + s + "\n"
        return formattedString

    def createTestCases(self):
        test_cases = self.csvToList()
        for idx, case in enumerate(test_cases):
            val = case[0]
            break_list = val.split(",")
            list_of_desc = break_list[0]
            desc = list_of_desc
            list_of_steps = break_list[1].split("\\n")
            steps = self.formatString(list_of_steps)
            list_of_data = break_list[2].split("\\n")
            data = self.formatString(list_of_data)
            list_of_expected = break_list[3].split("\\n")
            expected_results = self.formatString(list_of_expected)
            is_automated = break_list[4].strip().lower() in ["true"]
            text = f"**Test case data: ** \n {data} \n\n\n**Steps: ** \n {steps} \n\n\n **Expected :** \n {expected_results}"
            test_case = self.rpc_client.exec.TestCase.create(
                {
                    "summary": desc,
                    "text": text,
                    "product": 2,  # the ID of the product.
                    "category": 4,
                    "priority": 1,
                    "case_status": 2,  # CONFIRMED
                    "author": "2",
                    "is_automated": is_automated,
                    "managers_of_runs": "on",
                    "assignees_of_case_runs": "on",
                    "default_tester_of_case": "on",
                    "default_testers_of_runs": "on",
                    "notify_on_case_update": "on",
                    "notify_on_case_delete": "on",
                }
            )
            self.rpc_client.exec.TestPlan.add_case(
                7, test_case["id"]
            )  # 7 is the ID of the TestPlan where the testcase will be added


m = Main()
m.createTestCases()
