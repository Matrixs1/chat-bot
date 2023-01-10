import os
from random import randint
import time
x = {}


# اول مرحالة
try:
    file1 = open('data1.txt', 'r',1,"utf-8")
    file2 = open('data2.txt', 'r',1,"utf-8")
    while True:
        line1 = file1.readline()
        line2 = file2.readline()
        x[line1.replace("\n","")] = line2.replace("\n","")
        if not line1:
            break
            file1.close()
            file2.close()
    print(x)
    print("if you need tools print ->(tools)<- 😄")


    
    while True:
        z =  str(input("\nEnter your question 😄: "))
        try:
            #ثالث مرحاله
            
            t = None
            u = None
            count = 0
            soall = 0
            c = x.keys()
            m = x.values()
            for t in c:
                t = list(c)
                count += 1
                
                
                
            for  u in m:
                u = list(m)
                
            #رابع مرحاله    
            if z != x[z]:
                print("Your Answer 😀")
                time.sleep(1)
                print("\n" + x[z] + "\n")
                soall = randint(0,count - 1)
                ss = t[soall]
                jj = u[soall]
                if ss == "":
                    pass
                else:
                    time.sleep(1)
                    print("a question for you 😁\n")
                    time.sleep(1)
                    print(ss)
                    l = input("\nYour Answer 😁: ")
                    if l == jj :
                        time.sleep(1)
                        print("\nGood 😁")
                    else:
                        time.sleep(1)
                        print("\nThis Answer not True :(")
                        time.sleep(1)
                        print("\nThe True Answer is -> " + jj + " 😁")
                    
            #رابع مرحاله    
            if z == x[z]:
                print("Your Answer 😀")
                time.sleep(1)
                print("\n" + x[z] + "\n")
                ss = t[randint(0,count - 1)]
                if ss == "":
                    pass
                else:
                    time.sleep(1)
                    print("a question for you 😁\n")
                    time.sleep(1)
                    print(ss)
                    l = input("\nYour Answer 😁: ")
                    if l == jj :
                        time.sleep(1)
                        print("\nGood 😁")
                    else:
                        time.sleep(1)
                        print("\nThis Answer not True :(")
                        time.sleep(1)
                        print("\nThe True Answer is -> " + jj + " 😁")
                
        except:
                    
            
            if z == "tools":
                os.system("tools.py")

                
            if z != "tools":
                print("\nI don't know :D" )
            
                # تاني مرحالة
            
                file3 = open('data1.txt', 'a',1,"utf-8")
                file4 = open('data2.txt', 'a',1,"utf-8")
                a1 = str(input("Enter Title: "))
                a2 = str(input("Enter Discription: "))
                file3.write("\n" + a1)
                file4.write("\n" + a2)
                x[a1.replace("\n","")] = a2.replace("\n","")
                file3.close()
                file4.close()
 
except:
    file1 = open('data1.txt', 'w',1,"utf-8")
    file2 = open('data2.txt', 'w',1,"utf-8")
    file1.close()
    file2.close()
    os.system("active.py")
    









    







    









