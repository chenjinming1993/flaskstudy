#encoding:utf-8
import random
guess = ''  
while guess not in ('heads', 'tails'):  
    print('Guess the coin toss! Enter heads or tails:')  
    guess = raw_input()   #python2.7输入需要为"raw_input()",如果为"input()"会出错。
toss = random.randint(0, 1)  # 0 is tails, 1 is heads  
if toss==0:  
    toss='tails'  
else:  
    toss = 'heads'  
if toss == guess:  
    print('You got it!')  
else:  
    print('Nope! Guess again!')  
    guess = raw_input()
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads  
    if toss == 0:  
        toss = 'tails'  
    else:  
        toss = 'heads'  
    if toss == guess:  
        print('You got it!')  
    else:  
        print('Nope. You are really bad at this game.')  