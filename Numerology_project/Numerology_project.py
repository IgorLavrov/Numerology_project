from tkinter import *
from module1 import *
import tkinter as tk  
from functools import partial  

    
root = tk.Tk()  
root.geometry('400x200+400+500') 
  
root.title('Тайна Вашего имени скрыта здесь!')  
   
number1 = tk.StringVar() 
res=tk.IntVar()
  
labelNum1 = tk.Label(root, text="Введите ваше имя:").grid(row=1, column=0)   
  
labelResult = tk.Label(root)

  
labelResult.grid(row=7, column=2,sticky='w',pady=2)  
 
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  

entryNum2 = tk.Entry(root, textvariable=res).grid(row=25, column=2) 
  
 
call_result = partial(name,labelResult,number1)
aken2=partial(aken,res)
  
buttonCal = tk.Button(root, text="Вычислить", command=call_result).grid(row=3, column=0)  

buttonCal2 = tk.Button(root, text=" Узнать расшифровку своего имени",command=aken2).grid(row=20, column=0)  
labelNum2 = tk.Label(root, text="Введите число:").grid(row=21, column=0)   

  
root.mainloop() 


