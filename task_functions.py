from constants import bmiCategoryMapping, healthRiskMapping


def calculate_body_mass_index(heightCm:int, weightKg:int):
    """
    :param heightCm: height in cms
    :param weightKg: weight in kgs
    :formula : The BMI in (kg/m2 ) is equal to the weight in kilograms divided by your height in meters squared.
    :return: bmi (Body Mass Index)
    """
    bodyMassIndex = None
    try:
        if heightCm <= 0 or weightKg <= 0:
            raise Exception("'heightCm' & 'weightKg' should be a positive integer.")
        else:
            heightM = heightCm / 100
            bodyMassIndex = round(weightKg / (heightM*heightM), 2)
    except Exception as e:
        print("Encountered exception while calculating the Body Mass Index:::" + str(e))
    return bodyMassIndex


def get_bodyMassIndex_category(bodyMassIndex:float):
    """
    :param bodyMassIndex: float
    :return: bmiCategory: string
    """
    bmiCategory = None
    try:
        if bodyMassIndex <= 0:
            raise Exception("'bodyMassIndex' should be a positive integer.")
        else:
            for category, ranges in bmiCategoryMapping.items():
                if ranges[0] <= bodyMassIndex <= ranges[1]:
                    bmiCategory = category
    except Exception as e:
        print("Encountered exception while fetching the Body Mass Index category:::" + str(e))
    return bmiCategory


def get_bodyMassIndex_health_risk(bodyMassIndex:float):
    """
    :param bodyMassIndex: float
    :return: healthRisk: string
    """
    healthRisk = None
    try:
        if bodyMassIndex <= 0:
            raise Exception("'bodyMassIndex' should be a positive integer.")
        else:
            for risk, ranges in healthRiskMapping.items():
                if ranges[0] <= bodyMassIndex <= ranges[1]:
                    healthRisk = risk
    except Exception as e:
        print("Encountered exception while fetching the Body Mass Index category:::" + str(e))
    return healthRisk


if __name__ == "__main__":
    bmi = calculate_body_mass_index(heightCm=175, weightKg=75)
    print(bmi)
    a = get_bodyMassIndex_category(25)
    print(a)
    b = get_bodyMassIndex_health_risk(25)
    print(b)


