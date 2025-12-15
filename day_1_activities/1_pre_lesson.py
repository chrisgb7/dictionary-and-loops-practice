# this is what we will use for the video intro to dictionaries
#dictionary - a c ollection of {key:value} pairs orded and changeable no duplicates

capitals = {"Usa":"Washington Dc",
            "india": "new delhi", 
            "china": "beijing,"
            "russia": "Mascow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("japan"))

if capitals.get("japan")
    print("that capital exits")
else:
    print("that capital doestn exits")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.popitem()
# capitals.clear()
# print(capitals)

keys= capitals.keys()
for key in capitals.keys():
    print(key)

values =capital.values()
for value in capitals.values():
    print(value)

for key,value in capitals.items():
    print(f"{key}: {value}")