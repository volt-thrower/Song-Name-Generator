import os
import random

def title():
    print("""

                ███╗   ███╗███████╗████████╗ █████╗ ██╗         ███╗   ██╗ █████╗ ███╗   ███╗███████╗
                ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║         ████╗  ██║██╔══██╗████╗ ████║██╔════╝
                ██╔████╔██║█████╗     ██║   ███████║██║         ██╔██╗ ██║███████║██╔████╔██║█████╗  
                ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║         ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
                ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗    ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
                ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

                     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗     
                    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
                    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝    
                    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    
                    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
                     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
                                                                                     
""")                                                                                                                             

    print("::M for Menu::::::Q to quit::::::Press Enter to Generate::".center(115), "\n")

def nounPicker():

    #checks if txt file exists
    if os.path.exists('nouns.txt'):
        nounFile = open('nouns.txt', 'r') #if it exists opens in read mode
        nounData = nounFile.read()
        # splitting the text when newline ('\n') is seen. .split makes list
        nounList = nounData.split("\n")
        #print(nounList) # printing the list for debugging
        nounFile.close()
        #print(type(nounList)) #for debugging
    
    else: #if vehicles.txt does not exist prints msg
        print("'nouns.txt' does not exists :(")

    return random.choice(nounList)

def verbPicker():
    if os.path.exists('verbs.txt'): #checks if txt file exists
        verbFile = open('verbs.txt', 'r')
        verbData = verbFile.read()
        verbList = verbData.split("\n")
        verbFile.close()

    else:
        print("'verb.txt' does not exists :(")

    return random.choice(verbList)

def adjecPicker():
    if os.path.exists('adjecs.txt'): #checks if txt file exists
        adjecFile = open('adjecs.txt', 'r')
        adjecData = adjecFile.read()
        adjecList = adjecData.split("\n")
        adjecFile.close()

    else:
        print("'adjecs.txt' does not exists :(")

    return random.choice(adjecList)

def prepPicker():
    if os.path.exists('preps.txt'): #checks if txt file exists
        prepFile = open('preps.txt', 'r')
        prepData = prepFile.read()
        prepList = prepData.split("\n")
        prepFile.close()

    else:
        print("'preps.txt' does not exists :(")

    return random.choice(prepList)

title()

while True:
    
    wordCombo = input()
      
    if wordCombo == "M" or wordCombo == "m":    #wordCombo MENU
        os.system('cls')
        wordCombo = input("""

                ███╗   ███╗███████╗████████╗ █████╗ ██╗         ███╗   ██╗ █████╗ ███╗   ███╗███████╗
                ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║         ████╗  ██║██╔══██╗████╗ ████║██╔════╝
                ██╔████╔██║█████╗     ██║   ███████║██║         ██╔██╗ ██║███████║██╔████╔██║█████╗  
                ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║         ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
                ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗    ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
                ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

                     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗     
                    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
                    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝    
                    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    
                    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
                     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
                                                                
                                            Choose a word combo.
                            1. Preposition noun                 2. Verb Noun    
                            3. Noun Noun                        4. Adjective Noun
                            5. Preposition Verb Noun            6. Preposition Adjective Noun
                            7. Adjective Verb Noun              8. Verb Adjective Noun
                            9. Adjective Adjective Noun         10. Noun Preposition Noun
                            11. Adjective Noun Preposition Noun 12. Verb Noun Preposition Noun
                            13. Noun Preposition Adjective Noun
""")
        os.system('cls')
           
    elif wordCombo == "Q" or wordCombo == "q":
        break

    else:
    #random pick wordcombo
        wordCombo = str(random.randrange(10))
        os.system('cls')
                   
    #print(wordCombo) #For Troubleshooting

    #Word Combo Modules
    #1. preposition noun
    if wordCombo == "1":
        randPrep1 = prepPicker()
        randNoun1 = nounPicker()
        bandName = randPrep1 + " " + randNoun1
    #verb noun
    elif wordCombo == "2":
        randVerb1 = verbPicker()
        randNoun1 = nounPicker()
        bandName = randVerb1 + " " + randNoun1
    #noun noun
    elif wordCombo == "3":
        randNoun1 = nounPicker()
        randNoun2 = nounPicker()
        bandName = randNoun1 + " " + randNoun2
    #adjec noun
    elif wordCombo == "4":
        randAdjec1 = adjecPicker()
        randNoun1 = nounPicker()
        bandName = randAdjec1 + " " + randNoun1
    #Preposition Verb Noun
    elif wordCombo == "5":
        randPrep1 = prepPicker()
        randVerb1 = verbPicker()
        randNoun1 = nounPicker()
        bandName = randPrep1 + " " + randVerb1 + " " + randNoun1
    #Preposition Adjective Noun
    elif wordCombo == "6":
        randPrep1 = prepPicker()
        randAdjec1 = adjecPicker()
        randNoun1 = nounPicker()
        bandName = randPrep1 + " " + randAdjec1 + " " + randNoun1
    #adject verb noun
    elif wordCombo == "7":
        randAdjec1 = adjecPicker()
        randVerb1 = verbPicker()
        randNoun1 = nounPicker()
        bandName = randAdjec1 + " " + randVerb1 + " " + randNoun1
    #verb adjec noun
    elif wordCombo == "8":
        randVerb1 = verbPicker()
        randAdjec1 = adjecPicker()
        randNoun1 = nounPicker()
        bandName = randVerb1 + " " + randAdjec1 + " " + randNoun1
    #adjec adjec noun
    elif wordCombo == "9":
        randAdjec1 = adjecPicker()
        randAdjec2 = adjecPicker()
        randNoun1 = nounPicker()
        bandName = randAdjec1 + " " + randAdjec2 + " " + randNoun1                      
    #noun prep noun
    elif wordCombo == "10":
        randNoun1 = nounPicker()
        randPrep1 = prepPicker()
        randNoun2 = nounPicker()   
        bandName = randNoun1 + " " + randPrep1 + " " + randNoun2   
    #adjec noun prep noun
    elif wordCombo == "11":
        randAdjec1 = adjecPicker()    
        randNoun1 = nounPicker()
        randPrep1 = prepPicker()
        randNoun2 = nounPicker()   
        bandName = randAdjec1 + " " + randNoun1 + " " + randPrep1 + " " + randNoun2
    #Verb Noun Preposition Noun
    elif wordCombo == "12":
        randVerb1 = verbPicker()    
        randNoun1 = nounPicker()
        randPrep1 = prepPicker()
        randNoun2 = nounPicker()   
        bandName = randVerb1 + " " + randNoun1 + " " + randPrep1 + " " + randNoun2
    #11. noun preposition adjective noun
    elif wordCombo == "13":    
        randNoun1 = nounPicker()
        randPrep1 = prepPicker()
        randAdjec1 = adjecPicker()
        randNoun2 = nounPicker()   
        bandName = randNoun1 + " " + randPrep1 + " " +  randAdjec1 + " " +  randNoun2       

    title()


    bandName = bandName.title()
    line = len(bandName) * "="
    print(line.center(115), "\n")
    print(bandName.center(115), "\n")
    print(line.center(115))    

#lodovico was here 15/05/22