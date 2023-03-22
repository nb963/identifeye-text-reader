f = open(patient_records.txt)
all_lines = f.readlines()

patient_records = {}

for line in all_lines:
    change_record = line.split(" ")
    if change_record[0] == 'ADD':
        if change_record[1] == 'PATIENT':
            identifier = change_record[2]
            if identifier not in patient_records.keys():
                patient_records[identifier] = [(change_record[3]+" "+change_record[3]), 0]
                
            
            
        