# словарь в python изменяемые данные {} ключ:значени

# практика 

dict = {
  "name":"Artur",
  "age":18
}
#dict.update({"year:2012"}) # кошот данные
#dict.popiten() # удаление
#dict["age"] = 20 # изменить
# dict.clar() # очистка
#dict.get("age")

print(dict.keys())
print(dict.values())

list = ["barsbek","aida","jibek"]
print("adyl"in list ) # True = 1 False = 0

a = "hello"
print(type(a))


facebok ={
"fist_name": "Samira",
"Surname": "Niazkulova",
"nuber": 996000222134,
"email": "samira@gmail.com",
"password": "OldPassword123",
"try passowrd": "OldPassword123"
}
print(facebok)
print("-" * 40)
facebok["password"] = "JennieStyle2026"
facebok["try passowrd"] = "JennieStyle2026"
facebok["region"] = "chui"
for key,value in facebok.items():
    print(f"{key}:{value}")
print("-" * 40 )
facebok.clear()
print("facebook")
