from tkinter import *
import random

root = Tk()
root.title('Password Generator')
root.geometry('500x500')

inputPass = Entry(root)
guessedPass = Label(root)
label = Label(root)

array1 = [[['0','1','2','3','4','5','6','7','8','9'],['!','@','#','$','%','^','&','*'],['a','e','f','r','j','m','x','d','i','k']]]

def stuff():
    randomNum1 = random.randint(0,9)
    randomSym1 = random.randint(0,7)
    randomAlpha1 = random.randint(0,9)
    randomNum2 = random.randint(0,9)
    randomAlpha2 = random.randint(0,9)
    randomSym2 = random.randint(0,7)
    
    char1 = array1[0][0][randomNum1]
    char2 = array1[0][1][randomSym1]
    char3 = array1[0][2][randomAlpha1]
    char4 = array1[0][0][randomNum2]
    char5 = array1[0][2][randomAlpha2]
    char6 = array1[0][1][randomSym2]
    
    passInputed = inputPass.get()
    guessedPass['text'] = 'Guessed Password: ' + str(passInputed)
    
    label['text'] = 'Generated Password: ' + str(char1) + char2 + char3 + str(char4) + char5 + char6


btn = Button(root,text = 'new password',command = stuff)
inputPass.place(relx = 0.5,rely = 0.2,anchor=CENTER)
guessedPass.place(relx = 0.5,rely = 0.3,anchor = CENTER)
btn.place(relx = 0.5,rely = 0.4,anchor = CENTER)
label.place(relx = 0.5,rely = 0.5,anchor = CENTER)

mainloop()
