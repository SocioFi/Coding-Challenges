import random
import pandas as pd

# Define some compliant and non-compliant text samples
compliant_samples = [
    "Workers are paid at least the national minimum wage.",
    "All employees receive annual leave as per labor law requirements.",
    "Protective equipment is provided in all hazardous areas.",
    "Employees are granted regular breaks during long shifts.",
    "Overtime is paid at the legal rate for all extra hours worked.",
    "Child labor is strictly prohibited in the factory.",
    "Workers have access to medical facilities and health insurance.",
    "The workplace is regularly inspected for safety compliance.",
    "Maternity leave is granted as per national labor laws.",
    "Employees are free to form trade unions and engage in collective bargaining.",
    "All workers are entitled to a minimum of 10 days of paid vacation annually.",
    "Child labor is strictly prohibited in all company operations.",
    "Health and safety regulations are strictly followed.",
    "All employees are provided with annual health check-ups.",
    "The workplace is free from harassment and discrimination."
]

non_compliant_samples = [
    "Employees are required to work more than 12 hours a day without additional pay.",
    "No safety equipment is provided in the workplace.",
    "Child labor is used in hazardous factory conditions.",
    "Workers are denied the minimum wage.",
    "Maternity leave is not provided to female employees.",
    "Employees are terminated without notice or severance pay.",
    "No health and safety training is provided to workers.",
    "Workers are subjected to verbal abuse by their supervisors.",
    "Employees are forced to sign unfair contracts.",
    "No paid annual leave is granted to workers despite long service.",
    "Overtime is not compensated as per the legal requirement.",
    "Workers are required to work 12-hour shifts without any overtime pay.",
    "Employees are not given any medical insurance.",
    "The company does not provide paid sick leave to employees.",
    "Wages are paid below the minimum legal requirement."
]

# Generate a large dataset
data = []

for _ in range(500):
    data.append([random.choice(compliant_samples), 1])
    data.append([random.choice(non_compliant_samples), 0])

# Create a DataFrame
df = pd.DataFrame(data, columns=["text", "label"])

# Save the dataset to a CSV file
dataset_path = "dummy_compliance_dataset.csv"
df.to_csv(dataset_path, index=False)

# Return the path of the saved file
dataset_path
