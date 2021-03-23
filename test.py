"""
Sample Test Runner for unit and integration tests
"""
import unittest
from task_functions import calculate_body_mass_index, get_bodyMassIndex_category, get_bodyMassIndex_health_risk
from main import compute_bmi_details, count_overweight_people


class test_calculate_body_mass_index(unittest.TestCase):
    def test_int_inputs(self):
        """
        Test that it can calculate bmi of integers
        """
        result = calculate_body_mass_index(heightCm=175, weightKg=75)
        self.assertEqual(result, 24.49)


if __name__ == '__main__':
    unittest.main()


"""
OUTPUT:
Testing started at 00:27 ...
"D:\Other Projects\CodeChallenge20210323\venv\Scripts\python.exe" "C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\helpers\pycharm\_jb_pytest_runner.py" --path "D:/Other Projects/CodeChallenge20210323/test.py"
Launching pytest with arguments D:/Other Projects/CodeChallenge20210323/test.py in D:\Other Projects\CodeChallenge20210323
============================= test session starts =============================
platform win32 -- Python 3.7.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: D:\Other Projects\CodeChallenge20210323collected 1 item

test.py .                                                                [100%]

============================== 1 passed in 1.82s ==============================
"""