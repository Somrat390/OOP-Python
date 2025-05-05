import json

# Serialization
# l = [1,2,3,4]
# with open("demo.json", "w") as f:
#     json.dump(l,f)

# dic = {
#     "name" : "Somrat",
#     "age" : 21,
#     "gender" : "male"
# }
# with open("demo1.json", "w") as f:
#     json.dump(dic,f,indent=4)

# Deserialization
with open("demo1.json","r") as f:
    d = json.load(f)
    print(d)