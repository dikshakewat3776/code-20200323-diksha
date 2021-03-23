from constants import inputData
from task_functions import calculate_body_mass_index, get_bodyMassIndex_category, get_bodyMassIndex_health_risk
import pandas as pd


"""
TASK 1:
Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health risk from Table 1 of the person 
and add them as 3 new columns.
"""


def compute_bmi_details(data: list):
    """
    :param data: list of inputData
    :return: list of computed bmi details
    """
    bmiDetails = []
    try:
        for entry in data:
            entry['bmi'] = calculate_body_mass_index(heightCm=entry.get('HeightCm'), weightKg=entry.get('WeightKg'))
            entry['bmi_category'] = get_bodyMassIndex_category(bodyMassIndex=entry['bmi'])
            entry['bmi_health_risk'] = get_bodyMassIndex_health_risk(bodyMassIndex=entry['bmi'])
            bmiDetails.append(entry)
        print("Successfully Computed BMI details.")
    except Exception as e:
        print("Encountered exception while calculating the Body Mass Index details :::" + str(e))
    return bmiDetails


def save_bmi_details_to_csv(data: list, filename: str):
    """
    :param data: list of computed bmi details
    :param filename: filename to be given to the output csv file
    :return: <filename>.csv created in current working directory
    """
    try:
        dataFrame = pd.DataFrame(data)
        fname = filename + ".csv"
        dataFrame.to_csv(fname, header=True, index=True)
        print("Successfully created {} .".format(fname))
    except Exception as e:
        print("Encountered exception while saving bmi details as csv:::" + str(e))


"""
TASK 2:
Count the total number of overweight people using ranges in the column BMI Category of Table 1, 
check this is consistent programmatically and add any other observations in the documentation.
"""


def count_overweight_people(data: list):
    """
    :param data: list of inputData
    :return: count of overweight people
    """
    count = 0
    try:
        for entry in data:
            if entry.get('bmi_category') == "Overweight":
                count += 1
    except Exception as e:
        print("Encountered exception while calculating the Body Mass Index details :::" + str(e))
    return count


if __name__ == "__main__":
    result = compute_bmi_details(data=inputData)
    print(result)
    save_bmi_details_to_csv(data=result, filename="BmiDetails")
    overweightCount = count_overweight_people(data=result)
    print(overweightCount)
