f = open(patient_records.txt)
all_lines = f.readlines()

patient_records = {}
exams = []

for line in all_lines:
    change_record = line.split(" ")
    if change_record[0] == 'ADD':
        if change_record[1] == 'PATIENT':
            identifier = change_record[2]
            if identifier not in patient_records.keys():
                patient_records[identifier] = [(change_record[3]+" "+change_record[4]), []]
                
        elif change_record[1] == 'EXAM': 
            if change_record[3] not in exams:
                identifier = change_record[2]
                if identifier in patient_records.keys():
                    patient_records[identifier][1].append(change_record[3])
                    exams.append(change_record[3])
                    
    elif change_record[0] == 'DELETE':
        if change_record[1] == 'PATIENT':
            identifier = change_record[2]
            if identifier in patient_records.keys():
                patient_records.pop(identifier)
                
        elif change_record[1] == 'EXAM': 
            if change_record[3] in exams:
                identifier = change_record[2]
                if identifier in patient_records.keys():
                    patient_records[identifier][1].pop(change_record[3])
                    exams.pop(change_record[3])
            
        
        
                    
                
            
            
        