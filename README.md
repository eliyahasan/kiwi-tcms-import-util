# kiwi-tcms-import-util
utility to import test cases in Kiwi TCMS using a CSV

Your Test Case CSV should contain these columns,

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

