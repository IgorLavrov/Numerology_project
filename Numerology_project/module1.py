from tkinter import *
from tkinter import ttk

def name(label_result,number1):
    list0=[1 , 2 , 3 , 4 , 5, 6 , 7 ,8 ,9]
    list1=["а" ,"б" ,"в","г" ,"д ", "е" ,"ё" , "ж" , "з"]
    list2=["и" ,"й","к" ,"л" ,"м" , "н" , "о" ,"п" ,"р"]
    list3=[ "с" ,"т" , "у" ,"ф" ,"х" ,"ц" ,"ч" ,"ш","щ"]
    list4=[ "ъ" ,"ы" ,"ь" ,"э" ,"ю" ,"я"]
    number=number1.get()
    list_answer=list(number)
    c=0
    result=0
    for i in range(len(list_answer)):
        letter=list_answer[i]
        if letter.lower() in list1:
                t=list1.index(letter.lower())
                c=list0[t]
        if letter.lower() in list2:
                t=list2.index(letter.lower())
                c=list0[t]      
        if letter.lower() in list3:
                t=list3.index(letter.lower())
                c=list0[t]  
        if letter.lower() in list4:
                t=list4.index(letter.lower())
                c=list0[t]
        result=result+c
        c=0
        res=10
        result1=0
        result2=0
    while(res>=10):
        result1=result//10
        result2=result%10
        res=result1+result2
        result=res
    label_result.config(text="Число = %d" % res) 
    return  

def aken(label_result):

    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    if(label_result==1):
        with open("File.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==2):
        with open("File2.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==3):
        with open("File3.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==4):
        with open("File4.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==5):
        with open("File5.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==6):
        with open("File6.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==7):
        with open("File7.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==8):
        with open("File8.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()
    elif(label_result==9):
        with open("File9.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()

    else:
        with open("File10.txt", "r") as f:
            Label(uusaken, text=f.read()).pack()

   
    uusaken.mainloop()

