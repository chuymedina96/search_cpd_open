import csv

html_output = ''
names = []
full_time = 0
part_time = 0
salary_total = 0.00
six_figs = 0

with open('./all_chicago_employees.csv', 'r') as csvfile:
    cop_data = csv.DictReader(csvfile) #DictReader makes a dictionary with the field names as keys
    
    #for item in cop_data: #prints everything out 
    #    print(item)
    #
    
    for line in cop_data:
        if line ['Department'] == "POLICE":
            pass #why does pass work if index =='POLICE' instead of index != 'POLICE
            names.append(f"{line['Name']} {line['Job Titles']} {line['Full or Part-Time']} {line['Salary or Hourly']} {line['Typical Hours']} {line['Annual Salary']} {line['Hourly Rate']}")
            if(line['Full or Part-Time'] == "F"):
                full_time += 1
                salary_total += float(line['Annual Salary'])
                if(float(line['Annual Salary']) >= 100000.00):
                    six_figs += 1
            if(line['Full or Part-Time'] == "P"):
                part_time += 1

#print(names)

for name in names:
    print(name)
    
print(len(names))
print(full_time)
print(part_time)
print("Average salary of full time cops: " + str(round(salary_total/len(names),2)))
print(f"Cops making six figures or more: {str(six_figs)} ({str(int(round(six_figs/len(names),2)*100))}% of all cops)")