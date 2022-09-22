# kiwi-tcms-import-util
utility to import test cases in Kiwi TCMS using a CSV

In order to simply import test cases into an existing Test plan one needs to fill the Test cases.csv
with the desired test cases. Then edit main.py by entering your Test plan id.
```python
            self.rpc_client.exec.TestPlan.add_case(
                7, test_case["id"]
            )  # 7 is the ID of the TestPlan where the testcase will be added
```

Run the program and the tests will be updated in the test plan.


If you face any SSL issues check [KIWI dock](https://kiwitcms.readthedocs.io/en/latest/installing_docker.html?highlight=ssl#enable-plain-text-http-access:~:text=environment%3A%0A%20%20%20%20KIWI_DONT_ENFORCE_HTTPS%3A%20%22true%22
)
