def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    d={}
    count=0
    for i in medical_speciality.keys():
        count=patient_medical_speciality_list.count(i)
        d[count]=i
        c=d[max(i for i in d)]
        speciality=medical_speciality[c]
        return speciality
    
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E',342,'E',563,'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)