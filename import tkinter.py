from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
import webbrowser,datetime
from calendar import *
from time import *







def calc():
    
    root=Tk()
    root.title('python calculator')
    root.resizable(False,False)

    entry=Entry(root,width=20,font=('arial',15,'bold'))
    entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10,ipady=6)

    

    def show(number):
        current=entry.get()
        entry.delete(0, END)
        entry.insert(0, str(current)+str(number))
    def clear():
        entry.delete(0, END)
    def equal():
        c=entry.get()
        r=eval(c)
        entry.delete(0, END)
        entry.insert(0, r)

    b1=Button(root,text='1',padx=30,pady=20,command=lambda: show(1)).grid(row=1,column=0)
    b2=Button(root,text='2',padx=30,pady=20,command=lambda: show(2)).grid(row=1,column=1)
    b3=Button(root,text='3',padx=30,pady=20,command=lambda: show(3)).grid(row=1,column=2)
    b4=Button(root,text='4',padx=30,pady=20,command=lambda: show(4)).grid(row=2,column=0)
    b5=Button(root,text='5',padx=30,pady=20,command=lambda: show(5)).grid(row=2,column=1)
    b6=Button(root,text='6',padx=30,pady=20,command=lambda: show(6)).grid(row=2,column=2)
    b7=Button(root,text='7',padx=30,pady=20,command=lambda: show(7)).grid(row=3,column=0)
    b8=Button(root,text='8',padx=30,pady=20,command=lambda: show(8)).grid(row=3,column=1)
    b9=Button(root,text='9',padx=30,pady=20,command=lambda: show(9)).grid(row=3,column=2)
    b0=Button(root,text='0',padx=30,pady=20,command=lambda: show(0)).grid(row=4,column=0)
    bp=Button(root,text='.',padx=31,pady=20,command=lambda: show('.')).grid(row=4,column=1)

    beeqls=Button(root,text='=',padx=29,pady=20,bg='LightBlue',command=equal).grid(row=4,column=2)
    beeclear=Button(root,text='C',padx=28,pady=20,bg='Pink',command=clear).grid(row=0,column=4)
    badd=Button(root,text='+',padx=28,pady=20,bg='LightBlue',command=lambda:show('+')).grid(row=1,column=4)
    bsub=Button(root,text='-',padx=30,pady=20,bg='LightBlue',command=lambda:show('-')).grid(row=2,column=4)
    bdiv=Button(root,text='/',padx=30,pady=20,bg='LightBlue',command=lambda:show('/')).grid(row=3,column=4)
    bmul=Button(root,text='x',padx=30,pady=20,bg='LightBlue',command=lambda:show('*')).grid(row=4,column=4)

    root.mainloop()











def tic():
    #Tic Tac Toe game in python by techwithtim

    board = [' ' for x in range(10)]

    def insertLetter(letter, pos):
        board[pos] = letter

    def spaceIsFree(pos):
        return board[pos] == ' '

    def printBoard(board):
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        
    def isWinner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

    def playerMove():
        run = True
        while run:
            move = input('Please select a position to place an \'X\' (1-9): ')
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if spaceIsFree(move):
                        run = False
                        insertLetter('X', move)
                    else:
                        print('Sorry, this space is occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')
                

    def compMove():
        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0

        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = board[:]
                boardCopy[i] = let
                if isWinner(boardCopy, let):
                    move = i
                    return move

        cornersOpen = []
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
                
        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
                
        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
            
        return move

    def selectRandom(li):
        import random
        ln = len(li)
        r = random.randrange(0,ln)
        return li[r]
        

    def isBoardFull(board):
        if board.count(' ') > 1:
            return False
        else:
            return True

    def main():
        print('Welcome to Tic Tac Toe!')
        printBoard(board)

        while not(isBoardFull(board)):
            if not(isWinner(board, 'O')):
                playerMove()
                printBoard(board)
            else:
                print('Sorry, O\'s won this time!')
                break

            if not(isWinner(board, 'X')):
                move = compMove()
                if move == 0:
                    print('')
                else:
                    insertLetter('O', move)
                    print('Computer placed an \'O\' in position', move , ':')
                    printBoard(board)
            else:
                print('X\'s won this time! Good Job!')
                break

        if isBoardFull(board):
            print('Tie Game!')
    answer='Y'
    while True:
        answer = input('Do you want to play again? (Y/N)')
        if answer.lower() == 'y' or answer.lower == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
        else:
            break












def clock():
    root = Tk()
    root.title('Clock')
    root.resizable(False,False)

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)
    
    lbl = Label(root, font = ('calibri', 40, 'bold'),
                background = 'purple',
                foreground = 'white')
    

    lbl.pack(anchor = 'center')
    time()
    
    mainloop()









def calender():
    #calendar 
    t=datetime.date.today()
    yy = t.year
    mm = t.month
    print(month(yy, mm))








def cricket():

    # Cricket Game
 
    print(""" ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~
    
    Instructions:
    
    1. You have to select any random number from 1 to 6.
    2. The computer will also select a number.
    3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
    If the number selected by you and computer is same, then you will lose your wicket.
    4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
    If the number selected by you and computer is same, then the computer will lose its wicket.
    5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
    6. The innings will end after either the three wickets fell or the overs end.
    7. The player with maximum runs wins. """)
    
    print("\n---------- Start Game ----------")
    
    import random
    
    # Toss 
    
    print("\nHere comes the Toss")
    toss = (input("Choose heads or tails: ")).lower()
    
    random_toss = random.randint(1,2)            # In random_toss (1 = Heads) and (2 = Tails)
    random_opt = random.randint(1,2)             # In random_opt (1 = bat) and (2 = ball)
    
    u_opt = 0
    c_opt = 0
    
    if random_toss == 1 and toss == "heads":
        print("\nYou won the toss")
        u_opt = (input("Choose bat or ball: ")).lower()
    
    elif random_toss == 2 and toss == "tails":
        print("\nYou won the toss")
        u_opt = (input("Choose bat or ball: ")).lower()    
    
    else:
        print("\nYou lost the toss")
    
        if random_opt == 1:
            c_opt = "bat"
            print("Computer choose to",c_opt)
    
        elif random_opt == 2:
            c_opt = "ball"
            print("Computer choose to",c_opt)
    
    # First Innings 
    
    print("\n---------- First Innings Begins ----------")
    
    runs_1 = 0
    wickets_1 = 0
    balls_1 = 0
    
    while wickets_1 != 2 and balls_1 != 12:
    
        u_choice = int(input("\nChoose any number from 1 to 6: "))
        c_choice = random.randint(1,6)
    
        if u_choice < 1 or u_choice > 6:
            print("\nPlease choose a value from 1 to 6.")
    
        else:
            print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
    
            if u_choice == c_choice:
                wickets_1 += 1
    
            else:
                if u_opt == "bat" or c_opt == "ball":
                    Bat_first = "You"
                    Ball_first = "Computer"
                    runs_1 += u_choice
    
                elif u_opt == "ball" or c_opt == "bat":
                    Bat_first = "Computer"
                    Ball_first = "You"
                    runs_1 += c_choice
    
            print("\nScore =",runs_1,"/",wickets_1)
    
            balls_1 += 1
    
            if balls_1 == 6:
                print("End of Over 1")
    
            elif balls_1 == 12:
                print("End of Over 2")
    
            print("Balls remaining: ",12 - balls_1)
    
    print("\n---------- End of Innings ----------") 
    
    print("\nFinal Score:")
    print("Runs =",runs_1)
    print("wickets =",wickets_1)
    
    print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
    
    # Second Innings 
    
    print("\n---------- Second Innings Begins ----------")
    
    runs_2 = 0
    wickets_2 = 0
    balls_2 = 0
    
    while wickets_2 != 2 and balls_2 != 12 and runs_2 <= runs_1:
    
        u_choice = int(input("\nChoose any number from 1 to 6: "))
        c_choice = random.randint(1,6)
    
        if u_choice < 1 or u_choice > 6:
            print("\nPlease choose a value from 1 to 6.")
    
        else:
            print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
    
            if u_choice == c_choice:
                wickets_2 += 1
    
            else:
                if Bat_first == "Computer": 
                    runs_2 += u_choice
                    Bat_second = "You"
    
                elif Bat_first == "You":
                    runs_2 += c_choice
                    Bat_second = "Computer"
    
            print("\nScore =",runs_2,"/",wickets_2)
    
            balls_2 += 1
    
            if balls_2 == 6:
                print("End of Over 1")
    
            elif balls_2 == 12:
                print("End of Over 2")
    
            if runs_2 <= runs_1 and balls_2 <= 11 and wickets_2 != 2:
                print("To win:",runs_1 - runs_2 + 1,"runs needed from",12 - balls_2,"balls.")
    
    print("\n---------- End of Innings ----------") 
    
    print("\nFinal Score:")
    print("Runs =",runs_2)
    print("wickets =",wickets_2)
    
    # Result of Match 
    
    print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
    
    if runs_1 > runs_2:
    
        if Bat_first == "You": 
            print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
    
        else:
            print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.") 
    
    elif runs_2 > runs_1:
    
        if Bat_second == "You": 
            print("\nCongratulations! You won the Match by",2 - wickets_2,"wickets.")
    
        else:
            print("\nBetter luck next time! The Computer won the Match by",2 - wickets_2,"wickets.")
    
    else:
        print("The Match is a Tie.","\nNo one Wins.")







def google():
    webbrowser.open('http://www.google.com')
    print('GOOGLE IS OPENING.....')







def textapp():
    root=Tk()
    root.geometry('500x500')
    root.title('Text')
    def savefile():
        newfile=asksaveasfile(mode='w',filetypes=[('text files','.txt')])
        if newfile is None:
            return
        text=str(entry.get(1.0, END))
        newfile.write(text)
        newfile.close()

    def openfile():
        file=askopenfile(mode='r',filetypes=[('text files','*.txt')]) 
        if file is not None:
            content=file.read()
        entry.insert(INSERT, content)

    entry=Text(root,height=44,width=60,wrap=WORD)
    entry.pack(expand= TRUE, fill= BOTH)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    root.mainloop()







def sps():
    import random

    c='y'
    while c=='y':
        user_action = input("Enter a choice (1.rock, 2.paper, 3.scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "1":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            elif computer_action=="paper":
                print("Paper covers rock! You lose.")
            else:
                print("Its a tie.")
        
        elif user_action == "2":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            elif computer_action=="scissors":
                print("Scissors cut paper! You lose.")
            else:
                print("Its a tie.")
        
        elif user_action == "3":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            elif computer_action=="rock":
                print("Rock smashes scissors! You lose.")
            else:
                print("Its a tie.")
        c=input("Do you want to play again?(y/n)?")










#main part

print("------Welcome To Python Computer-------")
sleep(3)
c=input("""1)GO TO APPS 
2)SHUT DOWN
enter """).lower()
while c not in ['2','shut down:']:
    
    if c in ['1','go to apps','gotoapps','apps','app']:
        appch=''
        while appch not in ['0','exit']:
            sleep(1)
            print("""=========APPLICATIONS=========
1)CALCULATOR
2)CALENDAR
3)CLOCK
4)GOOGLE
5)GAMES
6)NOTEPAD
0)EXIT
""")
            appch=input("enter app to open: ").lower()
            if appch in ['1','calculator']:
                sleep(2)
                calc()
            elif appch in ['2','calendar']:
                calender()
            elif appch in ['3','clock']:
                sleep(2)
                clock()
            elif appch in ['4','google']:
                print('Opening Google.....')
                sleep(2)
                google()
            elif appch in ['5','games']:
                gam=''
                while gam not in ['exit','0']:
                    print("""======GAMES======
1)CRICKET
2)TIC-TAC-TOE
3)STONE PAPER SCISSORS
0)EXIT""")
                    gam=input("enter the game you want to play: ").lower()
                    if gam in ['1','cricket']:
                        cricket()
                    elif gam in ['2','tictactoe','tictac','tic']:
                        tic()
                    elif gam in ['3','stone paper scissor','stone paper','stone']:
                        sps()
                    elif gam in ['0','exit']:
                        continue
            elif appch in ['6','notepad']:
                sleep(2)
                textapp()
            elif appch in ['0','exit']:
                
                c=input("""1)GO TO APPS 
2)SHUT DOWN
""").lower()
            
                if c in ['2','shut down']:
                    print("SHUTTING DOWN...")
                    sleep(3)
                    break            
                else:
                    print('invalid selection')
