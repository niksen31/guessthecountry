
import time
import random


name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play Guess the Country!"

print ""


time.sleep(1)

print "Start guessing the country..."

time.sleep(0.5)
min=1;
max=55;
words=["Greece","Russia","Belarus","Georgia","Kazakhstan","Ukraine","Jamaica","Indonesia","Japan","South Korea","North Korea","Indonesia","Singapore","Malaysia","Taiwan","Japan","China","Thailand","Pakistan","Afghanistan","Tajikistan","Vanuatu","Solomon Islands","Fiji","Colombia","Venezuela","Peru","Chile","Uruguay","Finland","Norway","Denmark","Germany","Netherlands","Lesotho","Mauritius","Congo","Nigeria","Cameroon","Canada","Portugal","Poland","Hungary","Costa Rica","Bolivia","Guatemala","Northern Ireland","Ireland","England","Scotland","Czech Republic","Croatia","Slovenia","Slovakia","Serbia"]
x1=random.randint(min, max);
word = words[x1].lower();

guesses = ''


turns = 5;



while turns > 0:         

    
    failed = 0             

    
    for char in word:      

    
        if char in guesses:    
    
    
            print char,    

        else:
    
       
            print "_",     
       
        
            failed += 1    

    

   
    if failed == 0:        
        print "You won"  

    
        break              

    print

   
    guess = raw_input("guess a character:") 

    
    guesses += guess                    

   
    if guess not in word:  
 
     
        turns -= 1        
 
  
        print "Wrong"    
 
    
        print "You have", + turns, 'more guesses' 
 
        if turns == 0:           
    

            print "You Lose"  
            print "The secret country was " + word;