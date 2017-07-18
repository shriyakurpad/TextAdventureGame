print("Captain Jack Sparrow just stole your ship! Arghhh! Do you hunt him down or do nothing?")
choice = input("Enter 1 to find him or 2 to do nothing >") #choice 1
if choice.isnumeric() == True: #check if input is a number
    choice = int(choice)
    if choice == 1:
        print("Wise choice, matey! Now you've returned to the high seas. Will you sail to England or to Italy?")
        choice = input("Enter 1 for England or 2 for Italy >") #choice 2
        if choice.isnumeric() == True:
            choice = int(choice)
            if choice == 1:
                print("Englishmen hate pirates! You are hanged.")
            elif choice == 2:
                print("Ciao! Pizza! You've arrived in Italy. Do you rob a bank of all its gold or stop your life of crime and live happily ever after in Italy?")
                choice = input("Enter 1 to rob the bank or 2 to retire in Italy >") #choice 3
                if choice.isnumeric() == True:
                    choice = int(choice)
                    if choice == 1:
                        print("As you commit your crime, you spot that devious Captain Sparrow trying to rob the same bank! You confront him, fight him and win your ship and your glory back. Huzzah!")
                    elif choice == 2:
                        print ("While eating spaghetti in your new crime-free Italian life, you are poisoned by an old enemy. What a shame.")
                    else:
                        print("Arghhhh, not a valid option")
                else:
                    print("Arghhhh, not a valid option")
            else:
                print("Arghhhh, not a valid option")
        else:
            print("Arghhhh, not a valid option")
    elif choice == 2:
        print ("Disgraceful! Your crew is disgusted by your cowardice and makes you walk the plank.")
    else:
        print("Arghhhh, not a valid option")
else:
    print("Arghhhh, not a valid option")
