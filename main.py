#технические шололадки technic moments
import time
import os
import pickle

try:
    with open('text.txt', 'rb') as file:
        text = pickle.load(file)
except FileNotFoundError:
    text = "null" #стандартный текст standart text

try:
    with open('password.txt', 'r') as file:
        password = int(file.read())
except FileNotFoundError:
    password = 12345  #стандартный пароль standart password
try:
  with open('name.txt', 'r') as file:
      name = file.read()
except FileNotFoundError:
  name = 'user'  # стандартное имя standart name

answer1 = 0
answer2 = 0
answer3 = 6
adminmode = 0
antivirus = 1
#language =  input('select language ')

#работа со всем work with everything
print('консоль запущена')
time.sleep(2)
print(f'система windows 1 приветствует вас {name}')
time.sleep(2)

while True:
    answer1 = int(input('нужен пароль, если не знаете введите 2, если знаете введите 1, если это первый запуск, пароль будет 12345: '))
#if answer1 == 1 2 планируется вариант 3 The plans include option 3
    if answer1 == 1:
        playerpassword = int(input("введите пароль: "))
        if playerpassword == password or playerpassword == 12345:
            print('доступ разрешен')
            time.sleep(3)
#работа с консолью windows 1 working with the windows 1 console
            while answer2 != 4:
                print("1 - смена пароля")
                print("2 - включить режим администратора !надо включать каждый раз!")
                print("3 - отключить антивирус !очень не рекомендуется!")
                print("4 - перезапуск консоли")
                print("5 - текстовый редактор")
                print("6 - вывод последнего текстового формата")
                if adminmode == 1:
                    print("7 - изменить имя пользователя")
                    print("8 - проверить имя!сбрасывается при перезапуске!")


                answer2 = int(input("введите номер команды: "))
#установка пороля set password
                if answer2 == 1:
                    print("введите новый пароль")
                    newpassword = int(input("введите новый пароль: "))
                    with open('password.txt', 'w') as file:
                        file.write(str(newpassword))
                    print('операция выполнена')
                    password = newpassword
                    time.sleep(1)
#включение режима администратора enabling administrator mode
                elif answer2 == 2:
                    adminmode = 1
                    print('успешно')
                    time.sleep(1)
#на данный момент антивирус не работает, но в будущем будет наверно the antivirus is not working at the moment, but it will probably be in the future
                elif answer2 == 3:
                    antivirus = 0
                    print("выключено, будьте осторожны")
                    time.sleep(1)
#перезапуск консоли restarting the console
                elif answer2 == 4:
                    print("перезапуск консоли")
                    os.system('clear')  # for UNIX-based systems like MacOS or Linux
                    os.system('cls')  # for Windows
                    os.system('python main.py')
                    break
#сохранение текста в text.txt (в планах сделать несколько текстовых файлов) 
#saving text in text.txt (there are plans to make several text files)
                elif answer2 == 5:
                    # Текстовый редактор text editor
                    text = input("Введите текст: ")
                    # Сохранение переменной text в файл text.txt 
                    #Saving the text variable to a file text.txt
                    with open('text.txt', 'wb') as file:
                        pickle.dump(text, file)
                    print('текст сохранен')
                    time.sleep(3)

                elif answer2 == 6:
                    # Вывод последнего текстового формата Output of the latest text format
                    with open('text.txt', 'rb') as file:
                        text = pickle.load(file)
                        print(text)
                    time.sleep(3)
#задать имя если есть режим администратора set the name if there is an administrator mode
                elif answer2 == 7 and adminmode == 1:
                  print("введите новое имя")
                  name = input("введите новое имя: ")
                  with open('name.txt', 'w') as file:
                      file.write(str(name))
                  print('операция выполнена')
                  name = name 
                  time.sleep(3)
#проверка имени name verification
                elif answer2 == 8 and adminmode == 1:
                    print(name)
                    time.sleep(1.5)
                else:
                    print("неверный номер команды")
                    time.sleep(1.5)
#сброс пороля reset password
    elif answer1 == 2:
        print("введите новый пароль")
        newpassword = int(input("введите новый пароль: "))
        with open('password.txt', 'w') as file:
            file.write(str(newpassword))
        print('операция выполнена')
        password = newpassword
        time.sleep(1)
        print(f'пароль установлен на {password} начинаю перезапуск')
        time.sleep(3)
#рестарт restart
        os.system('clear')  # мак и линукс очищение консоли mac and linux reset console
        os.system('cls')  # windows очищение консоли windows reset console
        os.system('python main.py') #рестарт restrt console
#справка по работе с библеотекой time: time.sleep(число) - задержка времени
#help for working with the Bible library time: time.sleep(number) - time delay