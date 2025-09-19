myDictionary = {"s1":"Ethan", "s2":"Michael"}
print(myDictionary)

myDictionary.update({"s3":"Bob"})
myDictionary.update({"s4":"Carrol"})

print(myDictionary)

del myDictionary["s2"]
print(myDictionary)