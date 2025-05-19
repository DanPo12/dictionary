country= {"France":"Paris","China":"Béijing","Thailand":"Bangkok","Japan":"Tokyo"}
print(country)
print(country["China"])
#add new key-v
country["Russia"]='moscow'
print(country)
#delete key v
del country["France"]
print(country)
key=country.keys()
print(key)
value=country.values()
print(value)
for key in country.keys():
    print(country[key],"is the capital of",key)