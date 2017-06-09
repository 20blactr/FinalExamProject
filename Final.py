import random
import tweepy, time
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)
print(".")
print(".")
print("Welcome to my trivia/quiz thing!")
print("The User chooses their category of")
print("quiz from a list of three. The")
print("computer will keep track of score.")
print(".")
name=input("What is your name?")
score = 0
quiz = ""
done = False
if name.upper()=="CARL":
    print("No chumps allowed")
    done=True
else:
    print(".")
    print("1.Animals")
    print("2.Sports")
    print("3.Random")
    print("4.Quit")
    print("Pick 1,2,3, or 4")
    print(".")
    category=int(input("What category would you like to quiz?"))
while done == False:
    if category == 4:
        done=True
    if category == 1:
        print("You chose animals!")
        print(".")
        print("What is the fastest animal on earth?")
        print("A.Cheetah")
        print("B.Pererine Falcon")
        print("C.Sail Fish")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="B":
            score=score+1
            print("Correct!")
        else:
            print("Wrong")
        print(".")
        print("Which weighs more?")
        print("A.One Blue Whale")
        print("B.Ten Whale Sharks")
        print("C.Twenty-Five African Elephants")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="A":
            score=score+1
            print("Correct!")
        else:
            print("Wrong")
        print(".")
        print("What is a group of owls called?")
        print("A.a Hoot")
        print("B.a Flock")
        print("C.a Parliament")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="C":
            score=score+1
            print("Correct")
        else:
            print("Wrong")
        print(".")
        print("What is a baby turkey called?")
        print("A.a cluck")
        print("B.a chick")
        print("C.a gobble")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="B":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("What animal has the longest tongue relative to its total size?")
        print("A.Frog")
        print("B.Blue Whale")
        print("C.Chameleon")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="C":
            print("Correct!")
            score=score+1
            
        print(str(name)+ "'s Score:")
        print(str(score)+"/5")
        done = True
    elif category==2:
        print("You chose sports!")
        print(".")
        print("What is the name of Atlanta's Baseball team called?")
        print("A.Atlanta Braves")
        print("B.Atlanta Hearts")
        print("C.Atlanta Falcons")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="A":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("How long is a period of hockey at the professional level")
        print("A.15 minutes")
        print("B.30 minutes")
        print("C.20 minutes")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="C":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("In what year was the 4 minute mile first achieved?")
        print("A.1954")
        print("B.1964")
        print("C.1974")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="A":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("How man teams are in the NFL?")
        print("A.32")
        print("B.25")
        print("C.29")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="A":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("What was banned in basketball from 1967 to 1976?")
        print("A.Posting Up")
        print("B.Nike Footwear ")
        print("C.Dunking")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="C":
            print("Correct!")
            score=score+1
        print(str(name)+ "'s Score:")
        print(str(score)+"/5")
        done= True
    elif category==3:
        print("You chose random!")
        print(".")
        print("Which animal has the most chromosomes?")
        print("A.Hermit Crabs")
        print("B.Humans")
        print("C.Dolphins")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="A":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("In 2005, Bhutan became the first country to ban what?")
        print("A.Alchohol")
        print("B.Tobacco")
        print("C.Forheign Religion")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="B":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("What is the heaviest breed of bear?")
        print("A.Grizzly Bear")
        print("B.Black Bear")
        print("C.Polar Bear")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="C":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("Zion National Park is located in which state?")
        print("A.Utah")
        print("B.Idaho")
        print("C.Oregon")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="A":
            print("Correct!")
            score=score+1
        else:
            print("Wrong")
        print(".")
        print("Which continent is the Ostrich native to?")
        print("A.Asia")
        print("B.Africa")
        print("C.Australia")
        print(".")
        choice=input("Choose One!")
        if choice.upper()=="B":
            print("Correct!")
            score=score+1
        print(str(name)+ "'s Score:")
        print(str(score)+"/5")
        
    
        done = True
if category==1:
    quiz="Animals"
if category==2:
    quiz="Sports"
if category==3:
    quiz="Random"
api.update_status(str(name)+"'s score on " + (quiz) + " was " + (str(score)) + "/5.")
