command = int(input())
days = command
doctors = 7
treated_patients = 0
untreated_patients = 0
for day in range(1, command + 1):
    patients = int(input())
    if day % 3 == 0 and treated_patients < untreated_patients:
        doctors += 1
    if patients > doctors:
        untreated_patients += patients - doctors
        treated_patients += doctors
    else:
        treated_patients += patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
