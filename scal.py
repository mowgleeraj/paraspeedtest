from time import *
import random as r

def mistake(para,usertest):
    error=0
    for i in range(len(para)):
        try:
            if para[i] != usertest[i]:
                error =error +1
        except :
            error =error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round (time_delay,2)
    speed = len (userinput)/time_r
    return round(speed)

test = [" n the heart of an enchanting forest, where the emerald leaves whispered secrets to the breeze",
       "a forgotten path meandered through the dappled sunlight. Amongst the ancient trees, mystical",
       "creatures danced"]
test1= r.choice(test)
print('   ********* typing speed **********  ')
print(test1)
print()
print()
time_1 = time()
testinput=input("Enter the para : ")
time_2 = time()

print('speed:' ,speed_time(time_1,time_2,testinput),"w/sec")
print ("Error :", mistake(test1,testinput) )
