#!/usr/bin/python

abc= {"Employee Name": "Chaithanya",
      "Date of Joinong":"22-feb-2009",
      "salary": 80000,
      "Department" :"Testing",
      "position" : "Senior_software"
      }

if 'salary' in abc:
    del abc['salary']

print(id(abc), type(abc), abc)
print(' ')
print(abc["position"])