marks = {
    "nitye": 100, 
    "devansh": 99,
    "anmol": 78,
    0: "harry"
}

print(marks.items()) ; 
print(marks.keys()) ; 
print(marks.values()) ; 

marks.update({"anmol": 99,"renuka": 34}) ; 

print(marks) ; 

print(marks.get("nitye")) ; 
print(marks["nitye"]) ; 
print(marks["anmol"]) ; 

