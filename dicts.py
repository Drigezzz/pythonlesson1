a = {
    "city": "Москва",
    "temperature": 20}
print(a)
print(type(a))
print(a["city"])
print(a.get("city"))
print(a["temperature"]-5)
a["temperature"] = a["temperature"] - 5
print(a["temperature"])
print(a.get("country"))
a["country"] = "Russia"
print(a)
a["date"] = "27.05.2019"
print(a)
print(len(a))