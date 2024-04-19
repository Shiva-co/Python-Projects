# Project 5 : Typing Speed Calculator

from time import *
import random as r

def mistake(par,user):
       error = 0
       for i in range(len(par)):
              try:
                     if par[i] != user[i]:
                            error = error + 1
              except:
                     error = error + 1
       return error

def speed_time(time_s,time_e,userinput):
       time_delay = time_e - time_s
       time_r = round(time_delay,2)
       speed = len(userinput)/ time_r
       return round(speed)

if __name__ == '__main__':
       while True:
              ck = input(" ready to test : yes / no :")
              if ck == "yes":
                     test = ["India is very big Country and Delhi is a capital city of India.",
                            "Pune is cultural capital of india and also known as educational hub"]

                     test1 = r.choice(test)
                     print("     *****typing speed*****")
                     print(test1)
                     print()
                     print()

                     time_1 = time()
                     testinput = input(" Enter : ")
                     time_2 = time()

                     print("Speed : ",speed_time(time_1,time_2,testinput),"w/sec")
                     print("Error : ",mistake(test1,testinput))

              elif ck == "no":
                     print(" Thank you ")
                     break

              else:
                     print("wrong input")


