diction = {"name":"Mikhail", "country":"Kenya", "city":"Mombasa"}
new_dict = diction.copy()
print(diction)
print(new_dict)

dict1 = {"name","age","city"}
value1 = "digitech"
final = diction.fromkeys(dict1,value1)
print(final)

getting = diction.get("city")
print(getting)

all = diction.items()
print(all)

all_values = diction.values()
print(all_values)

poping = diction.pop("name")
print(poping)

update_dict = diction
key,values = update_dict.popitem()
print(key,values)

addition = update_dict.setdefault("name","digitech")
print(addition)

k1 = ["name", "age", "city"]
v1 = ["idris",30,"great lagos"]
final_p = dict(zip(k1,v1))
print(final_p)