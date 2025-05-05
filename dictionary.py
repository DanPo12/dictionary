country= {"France":"Paris","China":"Béijing","Thailand":"Bangkok","Japan":"Tokyo"}
print(country)
print(country["China"])
#add new key-v
country["Russia"]='moscow'
print(country)
#delete key v
del country["France"]
print(country)