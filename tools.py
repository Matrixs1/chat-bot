from datetime import datetime
from random import randint
import os
import webbrowser
import hashlib


while True:
    print("1-Date  2-Open Browser 3-Create Hash Md5 \n4-Create Wordlist Password 5-Open Matrix Script\n6-Ping To Website")
    
    try:
        i = int(input("Select Number: "))

        if i == 1:
            now = datetime.now()
            print(now.strftime("%Y/%m/%d %H:%M:%S"))
            break



        if i == 2:
            url = input("Enter Url: ")
            webbrowser.open_new(url)
            break


        if i == 3:
            text = input("Enter The Text: ")
            print(hashlib.md5(text.encode('UTF-8')).hexdigest())
            break

        if i == 4:
            file1 = open('password.txt', 'w',1,"utf-8")
            for c in range(1000):
                num1 = randint(0,9)
                num2 = randint(0,9)
                num3 = randint(0,9)
                num4 = randint(0,9)
                num5 = randint(0,9)
                num6 = randint(0,9)
                num7 = randint(0,9)
                num8 = randint(0,9)
                x = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num8)
                print(x + "\n")
                file1.write(x + "\n")
            file1.close()
            print("Done")
            break

        if i == 5:
            os.system("bash Matrixs.sh")
            break

        if i == 6:
            url = input("Enter Url Website-> ")
            os.system("ping " + url)
            break
        
    except:
        print("\nPlease choose a number\n")
