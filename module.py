# Библиотека в python это модуль готовые функции кода
# import - импортировать

# random - генераци случайных чисел

#import random

#print(random.randint(1,100))

#import random

#list = ["Artur","Barsbek","Omurgul","Sanjar"]
#print(random.choice(list))

#import random
#print(random.uniform(1,100))

#import time
#print(time.ctime())

#import calendar 
#print(calendar.month(2026,7))

#while True:
    #import time
   # print(time.ctime())
   # time.sleep(1)

# cntrl + c stop

#import math

#number = 25
#print(math.sqrt(number))

#  корень квадратный
#print(math.pow(2,3))

# куб
#print(math.pow(2,3))

#import pyfiglet
#text = "hello python 47"

#print(pyfiglet.figlet_format(text))

#import random

#def guess_the_number():
   # secret_number = random.randint(1,10)
   # attempts = 0
   ## print("🤖Компютерь: Мен 1ден 10го чейин бир сан жашырдым.Тапканга аракет кыл!")

#while True:
   #  print("↘ Кичирек болуп калды, чон сан киргизиниз")
   # elif user_guess > secret_number:
    #    print("↖ Чон болуп калды, киччине санды киргиз")
  #  else:
   #     print(f"🎉 Кутуктайм! Сен санды{attempts} аракетте таптын! Жашыруун сан {secret_number} болчу.")
    #    break
   # except ValueError:
   # print("⚠ Сураныч сан гана киргизиниз!")

# Оюнду баштоо
#guess_the_number()


#import random

def guess_the_number():
    print("Добро пожаловать в игру <<Угадай число!>>")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
             
     guess = int(input("Введите число от 1 до 100: "))
   
    if guess < secret_number:
        print("Загадданное число БОЛЬШЕ.")
    elif user_guess >secret_number:
        print("Загадданное число МЕНЬШЕ.")

    else:
        print(f"Ура! Вы угадали число{secret_number}!")
       break

      
            
