"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000

"""

import json

infile = open('school_data.json', 'r')

schools = json.load(infile)
conference_schools = [372, 108, 107, 130]

# How many schools are in this file?

# print(len(schools))

# Display report for all universities that have a graduation rate for Women over 50%

print('\nAll Universities that have a Graduation Rate for Women over 50%\n')

for row in schools:
    if row['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
        if row['Graduation rate  women (DRVGR2020)'] > 50:
            print(row["instnm"], ', ',
                  row['Graduation rate  women (DRVGR2020)'], '%', sep='')

# Display report for all universities that have a total price for in-state students living off campus over $50,000

print('\nAll Universities that have a Total Price for in-state Students living Off Campus Over 50,000$\n')

for row in schools:
    if row['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
        total = row['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']
        if type(total) == int:
            if total > 50000:
                print(total, '$ ', row["instnm"], sep='')
