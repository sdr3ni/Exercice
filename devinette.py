import random
réponse = random.randint(1,100)
essai = 0

print

while essai != réponse:
        essai = int(input("Devine entre 1 et 100: "))
        if essai < réponse:
                print("Plus grand")

        elif essai > réponse:
                print ("Plus petit")
        else:
                print("Félicitations")
                    
        

                        
