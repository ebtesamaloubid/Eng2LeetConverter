#Ebtesam Aloubid-101260655
#  function replace lowercase letters with uppercase using ord() and chr()
def upper(string):
    a = ''
    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        a += char
    return a

# function replace  four different phrases with acronyms
def acronyms(string):
    a = ("by the way","laughing out loud","i do not know","what do you mean") # phrases
    b = ("btw ","lol ","idk ","wdym ") #acronyms
# for loop to replace phrases with acronyms
    for i in range(len(a)):
        c = len(a[i])
        d = 0 
        for j in range(len(string)):
            # if the user inter the phase
            if(string[j] == a[i][d]):
                d+= 1 
                # if not dont do anything
            else:
                d = 0
            if d == c:
                string = string[:((j+1)-c)] + b[i] + string[j+1:]
                break
     # return the acronyms
    return string 
# functions replaces four different letters with homoglyphs
def homoglyphs(string):

    a = ("C","A","I","H") # letters from the user 
    b = ("<","@","][","#") # homoglyphs
# for loop replaces  letters with homoglyphs
    for i in range(len(string)):
        for j in range(len(a)): 
            # if the user ented the letter 
            if string[i] == a[j]:
                string = string[:i] + b[j] + string[i+1:]
                break

# returing the homoglyphs
    return string

# a main function that prompts the user for a string and removes all punctuation
def main():
    a = str(input ("please enter a phrase \n"))
# deffined the punctuation 
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    b = " "
    for i in a:
        if i not in punctuation:
            b = b + i
    
    # calling the functions 
    print(acronyms(upper(b)))
    print(homoglyphs(upper(acronyms(b))))

main()
