#27/03/2023
from string import printable
from random import choice

status=False
while status==False:
    answer_two=int(input("Какая будет длина пароля?"))
    if answer_two<7:
        print("Слишком короткий пароль")
    elif answer_two>20:
        print("Слишком длиный пароль")
    else:
        print("Хорошо, создаю пароль")
        status=True
while status == True:
    password= ''.join([choice(list(printable)) for number in range(7)])
    password=password.replace(" ", choice(list(printable)))
    password=password.replace("\n", choice(list(printable)))
    print("Новый пароль", password)
    answer_one=input("Понравился полученный пароль?")
    if answer_one=="да" or answer_one=="Да" or answer_one=="ДА":
        print("Отлично, ваш новый пароль", password)
        status=False
    else:
        print("Подбераем новый пароль")
