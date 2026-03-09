'''
Ahmed Shihab AlMaamri
146313
Lab5 exercise 3
1. program prompts the user to input a sentence consisting of an even number of characters more than 2,
2. it validates the two conditions and if met, proceeds with the program, if not, the program exits an
appropriate message.
3. the program finds he
continue
'''
sentence = input("enter a sentence with an even number of characters more than 2 ")

sentLength = len(sentence)

if len(sentence) <= 2 or sentLength % 2 == 1:
    exit("invalid text, try again with an even number of characters more than 2")
    
else:
    halfSentence = sentLength / 2
    i = 0
    symmetry = True
    while i <= halfSentence and symmetry:
        if sentence[i] == sentence[-(i+1)]:
            symmetry = True
            
        else:
            symmetry = False
        
        i += 1
        
    print("the sentence is %s" %sentence)
    
    if symmetry:
        print("the sentence is symmetrical")
    else:
        print("the sentence is not symmetrical")