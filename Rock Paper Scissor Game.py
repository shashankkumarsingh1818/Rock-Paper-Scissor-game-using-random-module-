import random
l=["rock", "scissor", "paper"]

'''
    rock vs paper = paper wins 
    rock vs scissor = rock wins 
    paper vs scissor = scissor wins 
    
'''

while True:
    Ccount = 0
    Ucount = 0
    uc = int(input('''
    
Game start...
1 Yes 
2 No | Exit
                   
        '''))
    if uc == 2:
        print("Game Exit")
        break
    
    if uc == 1:
        for a in range(1,6):
            userInput = int(input('''
1 rock
2 scissor
3 paper 
        '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                 uchoice = "scissor"
            elif userInput == 3:
                uchoice =  "paper"
            Cchoice = random.choice(l) 
        
        #  when both choose same output 
            if Cchoice == uchoice: 
               print("Computer value", Cchoice)
               print("User value", uchoice)
               print("Game Draw")
               Ucount = Ucount + 1
               Ccount = Ccount + 1

            # when user win 
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("Computer value", Cchoice)
                print("User value", uchoice)  
                print("You Win")
                Ucount = Ucount + 1

            # when computer win
            else:
                print("Computer value", Cchoice)
                print("User value", uchoice)  
                print("Computer Win")
                Ccount = Ccount + 1
            
        if Ucount == Ccount:
            print("Final Game Draw....")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
        elif Ucount > Ccount:
            print("Final You Win The Game...")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
        else:
            print("Final Computer Win The Game...")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
    else:
     break