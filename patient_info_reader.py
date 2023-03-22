f = open(patient_records.txt)
all_lines = f.readlines()

for line in all_lines:
    patient_record = line.split(" ")