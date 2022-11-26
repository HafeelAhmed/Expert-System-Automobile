import time
print("\t\tWelcom to AutoMobile AI Expert System\t\t")
print("\n\nAI : Do You have any problem with your vehicle ? (yes or no)\n")
choice1 =input("You : ")

if choice1 == "yes":
    print("\nEnter the type of your issue listen down below :\n1. starting trouble\n2. woubble while driving\n3. I didn't have issue\n")
    choice2 =input("\nEnter Here (Numbers only): ")

    if choice2 > "3" or choice2 <"1":
        print("\nAI : Please Enter valid key..")
    
    elif choice2 == "3":
        print("\nAI : Then , Why are you enter Yes in the first question...You fool")
    
    elif choice2 == "2":
        print("\nAI :Ok let me think...!\n")
        for i in range(1,20):
            time.sleep(0.08)
            print(".",flush=True,end="")
        print("\nAI : When do you feel the woubbling\n1. while drive on the highway at terrible speed\n2.while drive normal road\n")
            
        choice3 =input("YOU : ")
            
        if choice3 == "1":
            print("\nAI : Please wait still...\nAI : I wanna call police...\nAI : Just kidding...Go slow my friend ")
        
        elif choice3 =="2":
            print("\nAI : Check you tire air pressure then check inform me kindly")
            print("\nAI: Still you feel woubble?(yes or no)\n")
            choice4 =input("YOU : ")
            
            if choice4 == "no":
                print("\nAI : I'm glad to helped you...\nThank you...!\Call me again")
            
            elif choice4 =="yes":
                
                print("\nAI : I think, you have to make a phone call to your service center....\n Thank you")
            else:
                print("\nAI : will you please enter the correct answer...\nGo on run agin me")
        else:
            print("\nAI : Please enter valid key...")
    else:
        print("\nAI : Let me remember that you have to check that the key is inserted?\nAI : Is it inserted?(yes or no)\n")
        choice5 = input("YOU : ")
        
        if choice5 =='no':
            print("\nAI : I think You have to study hard...better then ride a bike..\nAI : thank You..!")
        elif choice5 =='yes':
            print("\nAI : Oh i see.. let me think what to do wait a sec\n")
            
            for i in range(1,30):
                time.sleep(0.08)
                print(".",flush=True,end="")
            
            print("\n\nAI : sorry buddy I didn't get anything in my mind, I think you have to reach service center.")
        else:
            print("\ni'm getting bore when you enter wrong answer,' {} ' it doesn't make any sense".format(choice5))

elif choice1=='no':
    print("\nAI : Then why are you waste my time...")
else:
    print("AI : Enter valid key")
            