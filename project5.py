# this program was built to help you process your scores, it other features includes, calculating your GP & CGPA


import random
import time

print("===========================WELCOME=================================")
time.sleep(1.5)
print("loading.............. pls wait............")
time.sleep(1)

print("CHECKOUT YOUR GP HERE")
time.sleep(1)
name = input("May I know your name please: ")
time.sleep(1)
print("Hello " + name, " You are welcome here!")
time.sleep(1)
print("I can help you process and compute your results")
time.sleep(1)
print("please enter your grades below")
time.sleep(1)

F = int(1.50)
EF = int(1.75)
E = int(2)
DE = int(2.25)
D = int(2.50)
CD = int(2.75)
C = int(3)
BC = int(3.25)
B = int(3.50)
AB = int(3.75)
A = int(4)

GP = [F, EF, E, DE, D, CD, C, BC, B, AB, A]



courseName1 = input("Enter the course name ")
score1 = int(input("Enter score "))
CU1 = int(input("Enter the Credit Unit: "))
if score1 <= 34:
    TP1 = int(1.50 * CU1)
elif score1 <= 39:
    TP1 = int(1.75 * CU1)
elif score1 <= 44:
    TP1 = int(2.00 * CU1)
elif score1 <= 49:
    TP1 = int(2.25 * CU1)
elif score1 <= 54:
    TP1 = int(2.50 * CU1)
elif score1 <= 59:
    TP1 = int(2.75 * CU1)
elif score1 <= 64:
    TP1 = int(3.00 * CU1)
elif score1 <= 69:
    TP1 = int(3.25 * CU1)
elif score1 <= 74:
    TP1 = int(3.50 * CU1)
elif score1 <= 79:
    TP1 = int(3.75 * CU1)
elif score1 <= 100:
    TP1 = int(4.00 * CU1)
else:
    print("Invalid input ")

courseName2 = input("Enter the course name ")
score2 = int(input("Enter score "))
CU2 = int(input("Enter the Credit Unit: "))
if score2 <= 34:
    TP2 = int(1.50 * CU2)
elif score2 <= 39:
    TP2 = int(1.75 * CU2)
elif score2 <= 44:
    TP2 = int(2.00 * CU2)
elif score2 <= 49:
    TP2 = int(2.25 * CU2)
elif score2 <= 54:
    TP2 = int(2.50 * CU2)
elif score2 <= 59:
    TP2 = int(2.75 * CU2)
elif score2 <= 64:
    TP2 = int(3.00 * CU2)
elif score2 <= 69:
    TP2 = int(3.25 * CU2)
elif score2 <= 74:
    TP2 = int(3.50 * CU2)
elif score2 <= 79:
    TP2 = int(3.75 * CU2)
elif score2 <= 100:
    TP2 = int(4.00 * CU2)
else:
    print("Invalid input ")

courseName3 = input("Enter the course name ")
score3 = int(input("Enter score "))
CU3 = int(input("Enter the Credit Unit: "))
if score3 <= 34:
    TP3 = int(1.50 * CU3)
elif score3 <= 39:
    TP3 = int(1.75 * CU3)
elif score3 <= 44:
    TP3 = int(2.00 * CU3)
elif score3 <= 49:
    TP3 = int(2.25 * CU3)
elif score3 <= 54:
    TP3 = int(2.50 * CU3)
elif score3 <= 59:
    TP3 = int(2.75 * CU3)
elif score3 <= 64:
    TP3 = int(3.00 * CU3)
elif score3 <= 69:
    TP3 = int(3.25 * CU3)
elif score3 <= 74:
    TP3 = int(3.50 * CU3)
elif score3 <= 79:
    TP3 = int(3.75 * CU3)
elif score3 <= 100:
    TP3 = int(4.00 * CU3)
else:
    print("Invalid input ")

courseName4 = input("Enter the course name ")
score4 = int(input("Enter score "))
CU4 = int(input("Enter the Credit Unit: "))
if score4 <= 34:
    TP4 = int(1.50 * CU4)
elif score4 <= 39:
    TP4 = int(1.75 * CU4)
elif score4 <= 44:
    TP4 = int(2.00 * CU4)
elif score4 <= 49:
    TP4 = int(2.25 * CU4)
elif score4 <= 54:
    TP4 = int(2.50 * CU4)
elif score4 <= 59:
    TP4 = int(2.75 * CU4)
elif score4 <= 64:
    TP4 = int(3.00 * CU4)
elif score4 <= 69:
    TP4 = int(3.25 * CU4)
elif score4 <= 74:
    TP4 = int(3.50 * CU4)
elif score4 <= 79:
    TP4 = int(3.75 * CU4)
elif score4 <= 100:
    TP4 = int(4.00 * CU4)
else:
    print("Invalid input ")

courseName5 = input("Enter the course name ")
score5 = int(input("Enter score "))
CU5 = int(input("Enter the Credit Unit: "))
if score5 <= 34:
    TP5 = int(1.50 * CU5)
elif score5 <= 39:
    TP5 = int(1.75 * CU5)
elif score5 <= 44:
    TP5 = int(2.00 * CU5)
elif score5 <= 49:
    TP5 = int(2.25 * CU5)
elif score5 <= 54:
    TP5 = int(2.50 * CU5)
elif score5 <= 59:
    TP5 = int(2.75 * CU5)
elif score5 <= 64:
    TP5 = int(3.00 * CU5)
elif score5 <= 69:
    TP5 = int(3.25 * CU5)
elif score5 <= 74:
    TP5 = int(3.50 * CU5)
elif score5 <= 79:
    TP5 = int(3.75 * CU5)
elif score5 <= 100:
    TP5 = int(4.00 * CU5)
else:
    print("Invalid input ")

courseName6 = input("Enter the course name ")
score6 = int(input("Enter score "))
CU6 = int(input("Enter the Credit Unit: "))
if score6 <= 34:
    TP6 = int(1.50 * CU6)
elif score6 <= 39:
    TP6 = int(1.75 * CU6)
elif score6 <= 44:
    TP6 = int(2.00 * CU6)
elif score6 <= 49:
    TP6 = int(2.25 * CU6)
elif score6 <= 54:
    TP6 = int(2.50 * CU6)
elif score6 <= 59:
    TP6 = int(2.75 * CU6)
elif score6 <= 64:
    TP6 = int(3.00 * CU6)
elif score6 <= 69:
    TP6 = int(3.25 * CU6)
elif score6 <= 74:
    TP6 = int(3.50 * CU6)
elif score6 <= 79:
    TP6 = int(3.75 * CU6)
elif score6 <= 100:
    TP6 = int(4.00 * CU6)
else:
    print("Invalid input ")

courseName7 = input("Enter the course name ")
score7 = int(input("Enter score "))
CU7 = int(input("Enter the Credit Unit: "))
if score7 <= 34:
    TP7 = int(1.50 * CU7)
elif score7 <= 39:
    TP7 = int(1.75 * CU7)
elif score7 <= 44:
    TP7 = int(2.00 * CU7)
elif score7 <= 49:
    TP7 = int(2.25 * CU7)
elif score7 <= 54:
    TP7 = int(2.50 * CU7)
elif score7 <= 59:
    TP7 = int(2.75 * CU7)
elif score7 <= 64:
    TP7 = int(3.00 * CU7)
elif score7 <= 69:
    TP7 = int(3.25 * CU7)
elif score7 <= 74:
    TP7 = int(3.50 * CU7)
elif score7 <= 79:
    TP7 = int(3.75 * CU7)
elif score7 <= 100:
    TP7 = int(4.00 * CU7)
else:
    print("Invalid input ")

courseName8 = input("Enter the course name ")
score8 = int(input("Enter score "))
CU8 = int(input("Enter the Credit Unit: "))
if score8 <= 34:
    TP8 = int(1.50 * CU8)
elif score8 <= 39:
    TP8 = int(1.75 * CU8)
elif score8 <= 44:
    TP8 = int(2.00 * CU8)
elif score8 <= 49:
    TP8 = int(2.25 * CU8)
elif score8 <= 54:
    TP8 = int(2.50 * CU8)
elif score8 <= 59:
    TP8 = int(2.75 * CU8)
elif score8 <= 64:
    TP8 = int(3.00 * CU8)
elif score8 <= 69:
    TP8 = int(3.25 * CU8)
elif score8 <= 74:
    TP8 = int(3.50 * CU8)
elif score8 <= 79:
    TP8 = int(3.75 * CU8)
elif score8 <= 100:
    TP8: int = int(4.00 * CU8)
else:
    print("Invalid input ")

courseName9 = input("Enter the course name ")
score9 = int(input("Enter score "))
CU9 = int(input("Enter the Credit Unit: "))
if score9 <= 34:
    TP9 = int(1.50 * CU9)
elif score9 <= 39:
    TP9 = int(1.75 * CU9)
elif score9 <= 44:
    TP9 = int(2.00 * CU9)
elif score9 <= 49:
    TP9 = int(2.25 * CU9)
elif score9 <= 54:
    TP9 = int(2.50 * CU9)
elif score9 <= 59:
    TP9 = int(2.75 * CU9)
elif score9 <= 64:
    TP9 = int(3.00 * CU9)
elif score9 <= 69:
    TP9 = int(3.25 * CU9)
elif score9 <= 74:
    TP9 = int(3.50 * CU9)
elif score9 <= 79:
    TP9 = int(3.75 * CU9)
elif score9 <= 100:
    TP9 = int(4.00 * CU9)
else:
    print("Invalid input ")

courseName10 = input("Enter the course name ")
score10 = int(input("Enter score "))
CU10 = int(input("Enter the Credit Unit: "))
if score10 <= 34:
    TP10 = int(1.50 * CU10)
elif score10 <= 39:
    TP10 = int(1.75 * CU10)
elif score10 <= 44:
    TP10 = int(2.00 * CU10)
elif score10 <= 49:
    TP10 = int(2.25 * CU10)
elif score10 <= 54:
    TP10 = int(2.50 * CU10)
elif score10 <= 59:
    TP10 = int(2.75 * CU10)
elif score10 <= 64:
    TP10 = int(3.00 * CU10)
elif score10 <= 69:
    TP10 = int(3.25 * CU10)
elif score10 <= 74:
    TP10 = int(3.50 * CU10)
elif score10 <= 79:
    TP10 = int(3.75 * CU10)
elif score10 <= 100:
    TP10 = int(4.00 * CU10)
else:
    print("Invalid input ")

courseName11 = input("Enter the course name ")
score11 = int(input("Enter score "))
CU11 = int(input("Enter the Credit Unit: "))
if score11 <= 34:
    TP11 = int(1.50 * CU11)
elif score11 <= 39:
    TP11 = int(1.75 * CU11)
elif score11 <= 44:
    TP11 = int(2.00 * CU11)
elif score11 <= 49:
    TP11 = int(2.25 * CU11)
elif score11 <= 54:
    TP11 = int(2.50 * CU11)
elif score11 <= 59:
    TP11 = int(2.75 * CU11)
elif score11 <= 64:
    TP11 = int(3.00 * CU11)
elif score11 <= 69:
    TP11 = int(3.25 * CU11)
elif score11 <= 74:
    TP11 = int(3.50 * CU11)
elif score11 <= 79:
    TP11 = int(3.75 * CU11)
elif score11 <= 100:
    TP11 = int(4.00 * CU11)
else:
    print("Invalid input ")

courseName12 = input("Enter the course name ")
score12 = int(input("Enter score "))
CU12 = int(input("Enter the Credit Unit: "))
if score12 <= 34:
    TP12 = int(1.50 * CU12)
elif score12 <= 39:
    TP12 = int(1.75 * CU12)
elif score12 <= 44:
    TP12 = int(2.00 * CU12)
elif score12 <= 49:
    TP12 = int(2.25 * CU12)
elif score12 <= 54:
    TP12 = int(2.50 * CU12)
elif score12 <= 59:
    TP12 = int(2.75 * CU12)
elif score12 <= 64:
    TP12 = int(3.00 * CU12)
elif score12 <= 69:
    TP12 = int(3.25 * CU12)
elif score12 <= 74:
    TP12 = int(3.50 * CU12)
elif score12 <= 79:
    TP12 = int(3.75 * CU12)
elif score12 <= 100:
    TP12 = int(4.00 * CU12)
else:
    print("Invalid input ")

    TCU = CU1 + CU2 + CU3 + CU4 + CU5 + CU6 + CU7 + CU8 + CU9 + CU10 + CU11 + CU12
    STP = TP1 + TP2 + TP3 + TP4 + TP5 + TP6 + TP7 + TP8 + TP9 + TP10 + TP11 + TP12
    print(TCU)
    print(STP)
    CGPA = int(int(STP) / int(TCU))

print("wait " + name + "," + " while I process your inputs..........................")

print("I am done processing your input...")
print(name + " your result is now ready!")

GL = ["Failed, you have F", "Poor, you have EF",
      "Bad, you have E", "Try harder, you have DE", "Try harder, you have D",
      "Average, you have CD", "Average, you have C", "Cool, you have BC", "Nice, you have B",
      "Good, you have AB", "Wow,you got A"]

if score1 <= 34:
    print(GL[0] + " in " + courseName1)
elif score1 <= 39:
    print(GL[1] + " in " + courseName1)
elif score1 <= 44:
    print(GL[2] + " in " + courseName1)
elif score1 <= 49:
    print(GL[3] + " in " + courseName1)
elif score1 <= 54:
    print(GL[4] + " in " + courseName1)
elif score1 <= 59:
    print(GL[5] + " in " + courseName1)
elif score1 <= 64:
    print(GL[6] + " in " + courseName1)
elif score1 <= 69:
    print(GL[7] + " in " + courseName1)
elif score1 <= 74:
    print(GL[8] + " in " + courseName1)
elif score1 <= 79:
    print(GL[9] + " in " + courseName1)
elif score1 <= 100:
    print(GL[10] + " in " + courseName1)
else:
    print("Invalid input ")

if score2 <= 34:
    print(GL[0] + " in " + courseName2)
elif score2 <= 39:
    print(GL[1] + " in " + courseName2)
elif score2 <= 44:
    print(GL[2] + " in " + courseName2)
elif score2 <= 49:
    print(GL[3] + " in " + courseName2)
elif score2 <= 54:
    print(GL[4] + " in " + courseName2)
elif score2 <= 59:
    print(GL[5] + " in " + courseName2)
elif score2 <= 64:
    print(GL[6] + " in " + courseName2)
elif score2 <= 69:
    print(GL[7] + " in " + courseName2)
elif score2 <= 74:
    print(GL[8] + " in " + courseName2)
elif score2 <= 79:
    print(GL[9] + " in " + courseName2)
elif score2 <= 100:
    print(GL[10] + " in " + courseName2)
else:
    print("Invalid input ")

if score3 <= 34:
    print(GL[0] + " in " + courseName3)
elif score3 <= 39:
    print(GL[1] + " in " + courseName3)
elif score3 <= 44:
    print(GL[2] + " in " + courseName3)
elif score3 <= 49:
    print(GL[3] + " in " + courseName3)
elif score3 <= 54:
    print(GL[4] + " in " + courseName3)
elif score3 <= 59:
    print(GL[5] + " in " + courseName3)
elif score3 <= 64:
    print(GL[6] + " in " + courseName3)
elif score3 <= 69:
    print(GL[7] + " in " + courseName3)
elif score3 <= 74:
    print(GL[8] + " in " + courseName3)
elif score3 <= 79:
    print(GL[9] + " in " + courseName3)
elif score3 <= 100:
    print(GL[10] + " in " + courseName3)
else:
    print("Invalid input ")

if score4 <= 34:
    print(GL[0] + " in " + courseName4)
elif score1 <= 39:
    print(GL[1] + " in " + courseName4)
elif score4 <= 44:
    print(GL[2] + " in " + courseName4)
elif score4 <= 49:
    print(GL[3] + " in " + courseName4)
elif score4 <= 54:
    print(GL[4] + " in " + courseName4)
elif score4 <= 59:
    print(GL[5] + " in " + courseName4)
elif score4 <= 64:
    print(GL[6] + " in " + courseName4)
elif score4 <= 69:
    print(GL[7] + " in " + courseName4)
elif score4 <= 74:
    print(GL[8] + " in " + courseName4)
elif score4 <= 79:
    print(GL[9] + " in " + courseName4)
elif score4 <= 100:
    print(GL[10] + " in " + courseName4)
else:
    print("Invalid input ")

if score5 <= 34:
    print(GL[0] + " in " + courseName5)
elif score5 <= 39:
    print(GL[1] + " in " + courseName5)
elif score5 <= 44:
    print(GL[2] + " in " + courseName5)
elif score5 <= 49:
    print(GL[3] + " in " + courseName5)
elif score5 <= 54:
    print(GL[4] + " in " + courseName5)
elif score5 <= 59:
    print(GL[5] + " in " + courseName5)
elif score5 <= 64:
    print(GL[6] + " in " + courseName5)
elif score5 <= 69:
    print(GL[7] + " in " + courseName5)
elif score5 <= 74:
    print(GL[8] + " in " + courseName5)
elif score5 <= 79:
    print(GL[9] + " in " + courseName5)
elif score5 <= 100:
    print(GL[10] + " in " + courseName5)
else:
    print("Invalid input ")

if score6 <= 34:
    print(GL[0] + " in " + courseName6)
elif score6 <= 39:
    print(GL[1] + " in " + courseName6)
elif score6 <= 44:
    print(GL[2] + " in " + courseName6)
elif score6 <= 49:
    print(GL[3] + " in " + courseName6)
elif score6 <= 54:
    print(GL[4] + " in " + courseName6)
elif score6 <= 59:
    print(GL[5] + " in " + courseName6)
elif score6 <= 64:
    print(GL[6] + " in " + courseName6)
elif score6 <= 69:
    print(GL[7] + " in " + courseName6)
elif score6 <= 74:
    print(GL[8] + " in " + courseName6)
elif score6 <= 79:
    print(GL[9] + " in " + courseName6)
elif score6 <= 100:
    print(GL[10] + " in " + courseName6)
else:
    print("Invalid input ")

if score7 <= 34:
    print(GL[0] + " in " + courseName7)
elif score7 <= 39:
    print(GL[1] + " in " + courseName7)
elif score7 <= 44:
    print(GL[2] + " in " + courseName7)
elif score7 <= 49:
    print(GL[3] + " in " + courseName7)
elif score7 <= 54:
    print(GL[4] + " in " + courseName7)
elif score7 <= 59:
    print(GL[5] + " in " + courseName7)
elif score1 <= 64:
    print(GL[6] + " in " + courseName7)
elif score7 <= 69:
    print(GL[7] + " in " + courseName7)
elif score7 <= 74:
    print(GL[8] + " in " + courseName7)
elif score7 <= 79:
    print(GL[9] + " in " + courseName7)
elif score7 <= 100:
    print(GL[10] + " in " + courseName7)
else:
    print("Invalid input ")

if score8 <= 34:
    print(GL[0] + " in " + courseName8)
elif score8 <= 39:
    print(GL[1] + " in " + courseName8)
elif score8 <= 44:
    print(GL[2] + " in " + courseName8)
elif score1 <= 49:
    print(GL[3] + " in " + courseName8)
elif score8 <= 54:
    print(GL[4] + " in " + courseName8)
elif score8 <= 59:
    print(GL[5] + " in " + courseName8)
elif score8 <= 64:
    print(GL[6] + " in " + courseName8)
elif score8 <= 69:
    print(GL[7] + " in " + courseName8)
elif score8 <= 74:
    print(GL[8] + " in " + courseName8)
elif score8 <= 79:
    print(GL[9] + " in " + courseName8)
elif score8 <= 100:
    print(GL[10] + " in " + courseName8)
else:
    print("Invalid input ")

if score9 <= 34:
    print(GL[0] + " in " + courseName9)
elif score9 <= 39:
    print(GL[1] + " in " + courseName9)
elif score9 <= 44:
    print(GL[2] + " in " + courseName9)
elif score9 <= 49:
    print(GL[3] + " in " + courseName9)
elif score9 <= 54:
    print(GL[4] + " in " + courseName9)
elif score9 <= 59:
    print(GL[5] + " in " + courseName9)
elif score9 <= 64:
    print(GL[6] + " in " + courseName9)
elif score9 <= 69:
    print(GL[7] + " in " + courseName9)
elif score9 <= 74:
    print(GL[8] + " in " + courseName9)
elif score9 <= 79:
    print(GL[9] + " in " + courseName9)
elif score9 <= 100:
    print(GL[10] + " in " + courseName9)
else:
    print("Invalid input ")

if score10 <= 34:
    print(GL[0] + " in " + courseName10)
elif score10 <= 39:
    print(GL[1] + " in " + courseName10)
elif score1 <= 44:
    print(GL[2] + " in " + courseName10)
elif score10 <= 49:
    print(GL[3] + " in " + courseName10)
elif score10 <= 54:
    print(GL[4] + " in " + courseName10)
elif score10 <= 59:
    print(GL[5] + " in " + courseName10)
elif score10 <= 64:
    print(GL[6] + " in " + courseName10)
elif score10 <= 69:
    print(GL[7] + " in " + courseName10)
elif score10 <= 74:
    print(GL[8] + " in " + courseName10)
elif score10 <= 79:
    print(GL[9] + " in " + courseName10)
elif score10 <= 100:
    print(GL[10] + " in " + courseName10)
else:
    print("Invalid input ")

if score11 <= 34:
    print(GL[0] + " in " + courseName11)
elif score11 <= 39:
    print(GL[1] + " in " + courseName11)
elif score11 <= 44:
    print(GL[2] + " in " + courseName11)
elif score11 <= 49:
    print(GL[3] + " in " + courseName11)
elif score11 <= 54:
    print(GL[4] + " in " + courseName11)
elif score11 <= 59:
    print(GL[5] + " in " + courseName11)
elif score11 <= 64:
    print(GL[6] + " in " + courseName11)
elif score1 <= 69:
    print(GL[7] + " in " + courseName11)
elif score11 <= 74:
    print(GL[8] + " in " + courseName11)
elif score11 <= 79:
    print(GL[9] + " in " + courseName11)
elif score11 <= 100:
    print(GL[10] + " in " + courseName11)
else:
    print("Invalid input ")

if score12 <= 34:
    print(GL[0] + " in " + courseName12)
elif score12 <= 39:
    print(GL[1] + " in " + courseName12)
elif score12 <= 44:
    print(GL[2] + " in " + courseName12)
elif score12 <= 49:
    print(GL[3] + " in " + courseName12)
elif score12 <= 54:
    print(GL[4] + " in " + courseName12)
elif score12 <= 59:
    print(GL[5] + " in " + courseName12)
elif score12 <= 64:
    print(GL[6] + " in " + courseName12)
elif score12 <= 69:
    print(GL[7] + " in " + courseName12)
elif score12 <= 74:
    print(GL[8] + " in " + courseName12)
elif score12 <= 79:
    print(GL[9] + " in " + courseName12)
elif score12 <= 100:
    print(GL[10] + " in " + courseName12)
else:
    print("Invalid input ")

print("Your CGPA is " + CGPA)

if CGPA <= 1.99:
    print("YOU FAILED, GO BACK TO YOUR FATHER'S HOUSE!")
elif CGPA <= 2.49:
    print("YOU HAD A PASS!")
elif CGPA <= 2.99:
    print("YOU TRIED, YOU HAVE LOWER CREDIT!")
elif CGPA <= 3.49:
    print("GOOD, YOU GRADUATED WITH UPPER CREDIT!")
elif CGPA <= 4.00:
    print("EXCELLENT, ACCEPT MY CONGRATULATIONS, YOU GRADUATED WITH DISTINCTION!")
else:
    print("YOU DON'T HAVE A RESULT, GET OUT!")

print("Thanks for checking your result with us" + ", " + name + "!")
