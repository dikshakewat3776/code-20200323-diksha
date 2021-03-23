inputData = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]


bmiLowerLimit = 0
bmiUpperLimit = 100


bmiCategoryMapping = {
    "Underweight": (bmiLowerLimit, 18.4),
    "Normal weight": (18.5, 24.9),
    "Overweight": (25, 29.9),
    "Moderately obese": (30, 34.9),
    "Severely obese": (35, 39.9),
    "Very severely obese": (40, bmiUpperLimit)
}


healthRiskMapping = {
    "Malnutrition risk": (bmiLowerLimit, 18.4),
    "Low risk": (18.5, 24.9),
    "Enhanced risk": (25, 29.9),
    "Medium risk": (30, 34.9),
    "High risk": (35, 39.9),
    "Very high risk": (40, bmiUpperLimit)
}