
#технические шололадки technic moments
import time
import os
import pickle
import datetime

current_time = datetime.datetime.now()

# Создаем объект datetime для 1 числа текущего месяца и текущего года, без изменения времени 



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
try:
  with open('language.txt', 'r') as file:
      language = file.read()
except FileNotFoundError:
  language = 'en'  #language язык

answer1 = 0
answer2 = 0
answer3 = 6
adminmode = 0
antivirus = 1

if language == 'ru' :
  print('установлен русский язык')
  #работа со всем
  print('консоль запущена')
  time.sleep(2)
  print(f'система windows 1 приветствует вас {name}')
  time.sleep(2)

  while True:
      answer1 = int(input('нужен пароль, если не знаете введите 2, если знаете введите 1: '))
  #if answer1 == 1 2 планируется вариант 3
      if answer1 == 1:
          playerpassword = int(input("введите пароль: "))
          if playerpassword == password:
              print('доступ разрешен')
              time.sleep(3)
  #работа с консолью windows 1
              while answer2 != 4:
                  print('0 - время! может работать не корректно!')
                  print("1 - смена пароля")
                  print("2 - переключить режим администратора !надо включать каждый раз!")
                  print("3 - переключить антивирус !очень не рекомендуется!")
                  print("4 - перезапуск консоли")
                  print("5 - текстовый редактор")
                  print("6 - вывод последнего текста")
                  print("7 - выбрать язык")
                  if adminmode == 1:
                      print("8 - изменить имя пользователя")
                      print("9 - проверить имя")
                      
                    

          
                  answer2 = int(input("введите номер команды: "))
  #время
                  if answer2 ==0:
                    print("Текущее время:", current_time)
                    time.sleep(1.5)
                    #пароль
                  elif answer2 == 1:
                      print("введите новый пароль")
                      newpassword = int(input("введите новый пароль: "))
                      with open('password.txt', 'w') as file:
                          file.write(str(newpassword))
                      print('операция выполнена')
                      password = newpassword
                      time.sleep(1)
  #включение режима администратора
                  elif answer2 == 2:
                      adminmode = 1
                      print('успешно')
                      time.sleep(1)
  #на данный момент антивирус не работает, но в будущем будет наверно
                  elif answer2 == 3:
                      antivirus = 0
                      print("выключено, будьте осторожны")
                      time.sleep(1)
  #перезапуск консоли
                  elif answer2 == 4:
                      print("перезапуск консоли")
                      os.system('clear')  # for UNIX-based systems like MacOS or Linux
                      os.system('cls')  # for Windows
                      os.system('python main.py')
                      break
                    
  #сохранение текста в text.txt (в планах сделать несколько текстовых файлов) 

                  elif answer2 == 5:
                      # Текстовый редактор
                      text = input("Введите текст: ")
                      # Сохранение переменной text в файл text.txt 
                      with open('text.txt', 'wb') as file:
                          pickle.dump(text, file)
                      print('текст сохранен')
                      time.sleep(3)

                  elif answer2 == 6:
                      # Вывод последнего текстового файлы
                      with open('text.txt', 'rb') as file:
                          text = pickle.load(file)
                          print(text)
                      time.sleep(3)
                  elif answer2 == 7:
                      language = input("введите новый язык en/ru: ")
                      with open('language.txt', 'w') as file:
                          file.write(str(language))
                      print('операция выполнена')
                      language = language
                      time.sleep(3)
                #задать имя если есть режим администратора/
                  elif answer2 == 8 and adminmode == 1:
                    print("введите новое имя")
                    name = input("введите новое имя: ")
                    with open('name.txt', 'w') as file:
                        file.write(str(name))
                    print('операция выполнена')
                    name = name 
                    time.sleep(3)
  #проверка имени
                  elif answer2 == 9 and adminmode == 1:
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
  #рестарт
          os.system('clear')  # мак и линукс очищение консоли
          os.system('cls')  # windows очищение консоли
          os.system('python main.py') #рестарт
  #справка по работе с библеотекой time: time.sleep(число) - задержка времени на число
elif language == 'en': 
  print('The English language is set')
#work with everything
print('the console is running')
time.sleep(2)
print(f'windows 1 system welcomes you {name}')
time.sleep(2)

while True:
    answer1 = int(input('you need a password, if you dont know, enter 2, if you know, enter 1: '))
#if answer1 == 1 2 The plans include option 3
    if answer1 == 1:
        playerpassword = int(input("enter the password: "))
        if playerpassword == password:
            print('access is allowed')
            time.sleep(3)
#working with the windows 1 console
            while answer2 != 4:
                print('0 - time!it doesnt work correctly!')
                print("1 - changing the password")
                print("2 - Enable or disable administrator mode!You have to turn it on every time!")
                print("3 - enable or disable antivirus !it is highly not recommended!")
                print("4 - restart the console")
                print("5 - text editor")
                print("6 - the output of the last text text")
                print("7 - choose the language")
                if adminmode == 1:
                    print("8 - change the user name")
                    print("9 - Check the name!resets on restart!")


                answer2 = int(input("enter the command number: "))
#time
                if answer2 ==0:
                  print("current time:", current_time)
                  time.sleep(1.5)
                  #password
                elif answer2 == 1:
                    print("enter a new password")
                    newpassword = int(input("enter a new password: "))
                    with open('password.txt', 'w') as file:
                        file.write(str(newpassword))
                    print('The operation is completed')
                    password = newpassword
                    time.sleep(1)
#enabling administrator mode
                elif answer2 == 2:
                    adminmode = 1
                    print('successfully')
                    time.sleep(1)
#the antivirus is not working at the moment, but it will probably be in the future
                elif answer2 == 3:
                    antivirus = 0
                    print("off, be careful")
                    time.sleep(1)
#restarting the console
                elif answer2 == 4:
                    print("restarting the console")
                    os.system('clear')  # for UNIX-based systems like MacOS or Linux
                    os.system('cls')  # for Windows
                    os.system('python main.py')
                    break
#saving text in text.txt (there are plans to make several text files)
                elif answer2 == 5:
                    #text editor
                    text = input("Enter the text: ")
                    #Saving the text variable to a file text.txt
                    with open('text.txt', 'wb') as file:
                        pickle.dump(text, file)
                    print('the text is saved')
                    time.sleep(3)
            #Output of the latest text format
                elif answer2 == 6:
                    with open('text.txt', 'rb') as file:
                        text = pickle.load(file)
                        print(text)
                    time.sleep(3)
                  #set the language
                elif answer2 == 7:
                  language = input("enter a new language ru/en: ")
                  with open('language.txt', 'w') as file:
                    file.write(str(language))
                  print('the operation is completed')
                  language = language
                  time.sleep(3)
                  os.system('clear')  #mac and linux reset console
                  os.system('cls')  #windows reset console
                  os.system('python main.py') #restart console
              #set the name if there is an administrator mode
                elif answer2 == 8 and adminmode == 1:
                  print("enter a new name")
                  name = input("enter a new name: ")
                  with open('name.txt', 'w') as file:
                      file.write(str(name))
                  print('The operation is completed')
                  name = name 
                  time.sleep(3)
#name verification
                elif answer2 == 9 and adminmode == 1:
                    print(name)
                    time.sleep(1.5)
                else:
                    print("invalid command number")
                    time.sleep(1.5)
#reset password
    elif answer1 == 2:
        print("enter a new password")
        newpassword = int(input("enter a new password: "))
        with open('password.txt', 'w') as file:
            file.write(str(newpassword))
        print('The operation is completed')
        password = newpassword
        time.sleep(1)
        print(f'the password is set to {password} starting the restart')
        time.sleep(3)
#restart
        os.system('clear')  #mac and linux reset console
        os.system('cls')  #windows reset console
        os.system('python main.py') #restart console

#help for working with the Bible library time: time.sleep(number) - time delay on the number