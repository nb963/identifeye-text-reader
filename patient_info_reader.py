# Patient Info Reader

# opening input file and reading all lines
f = open("patient_record.txt", "r")
all_lines = f.readlines()

# initializing variables to store patient and exam information
patient_records = {}
exams = []

for line in all_lines:
    # removing extra whitespaces
    line = line.strip()

    # splitting line by whitespace
    change_record = line.split(" ")

    if change_record[0] == 'ADD':
        if change_record[1] == 'PATIENT':
            # while adding new patient record, check if it already exists
            identifier = change_record[2]

            if identifier not in patient_records:
                # if not, insert patient information into patient_records
                patient_records[identifier] = [
                    (change_record[3]+" "+change_record[4]), []]

        elif change_record[1] == 'EXAM':
            # while adding new exam, check if it already exists
            if change_record[3] not in exams:
                identifier = change_record[2]

                if identifier in patient_records:
                    # if not, insert exam into patient_records and all exam records
                    patient_records[identifier][1].append(change_record[3])
                    exams.append(change_record[3])

    elif change_record[0] == 'DEL':
        # while deleting existing patient, check if patient exists exists
        if change_record[1] == 'PATIENT':
            identifier = change_record[2]

            if identifier in patient_records:
                # if patient exists, delete all of patient's exams
                exams = list(
                    filter(lambda i: i not in patient_records[identifier][1], exams))

                # then delete patient record
                patient_records.pop(identifier)

        elif change_record[1] == 'EXAM':
            if change_record[3] in exams:
                identifier = change_record[2]

                if identifier in patient_records:
                    # if exam exists and patient exists, delete exam record
                    patient_records[identifier][1].remove(change_record[3])
                    exams.remove(change_record[3])


for k in patient_records:
    # printing patient records
    print("Name: " + (patient_records[k][0]) + ", Id: " +
          k + ", Exam Count: " + str(len(patient_records[k][1])))
