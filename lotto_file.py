from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(" Figure Lottery!!!")
window.geometry("500x200")
window.configure(bg='blue')
import random
from datetime import *



Time = Label(window ,bg='Yellow', text ='Datetime' ,font=("helvetica", 10))
Time.place (x=50, y=25)

clock = datetime.now()
Time.config(text = clock.strftime("%d/%m/%y  %a-%b"  '%H:%M:%S %p' ))

def confirm():
    pass

# creating the labels


code1 = IntVar()
code2 = IntVar()
code3 = IntVar()
code4 = IntVar()
code5 = IntVar()
code6 = IntVar()

lb3 = Label(window, text="Welcome to Ithuba National Lottery", bg='Orange',font = "helvetica")
lb3.pack(side=LEFT)
lb3.place(x=50, y=50)

lb3 = Label(window, text=" Enter Lottery Number :" ,font = ("helvetica " ,12))
lb3.pack(side=LEFT)
lb3.place(x=50, y=90)




lb4 = Entry(window, textvariable=code1)
lb4.pack(side=RIGHT)
lb4.place(x=220, y=115, width=50)

lb5 = Entry(window, textvariable=code2)
lb5.pack(side=RIGHT)
lb5.place(x=300, y=115, width=50)

lb6 = Entry(window, textvariable=code3)
lb6.pack(side=RIGHT)
lb6.place(x=380, y=115, width=50)

lb7 = Entry(window, textvariable=code4)
lb7.pack(side=RIGHT)
lb7.place(x=450, y=115, width=50)

lb8 = Entry(window, textvariable=code5)
lb8.pack(side=RIGHT)
lb8.place(x=550, y=115, width=50)

lb9 = Entry(window, textvariable=code6)
lb9.pack(side=RIGHT)
lb9.place(x=650, y=115, width=50)

answer = Label(window, bg='red', width=60, height=10)
answer.place(x=50, y=200)



def func():


    m = code1.get()
    i = code2.get()
    h = code3.get()
    k = code4.get()
    a = code5.get()
    z = code6.get()

    ma_list = [m, i, h, k, a, z]
    ma_list.sort()

    lott_numb = sorted(random.sample(range(1, 49), 6))


    if len(lott_numb) == len(ma_list):
            same = set(lott_numb).intersection(set(ma_list))
            if len(same) == 6:
                answer.config(text=" YOU WON JUST WON A  !!!!!!!!!!!\n" + "R10 000 000.00" + "\n lotto numbers " + str(lott_numb))

            elif len(same) == 5:
                answer.config(text=" YOU WON !!!!!!!!!!!!\n" + " R R8584.00" + "\n lotto numbers " + str(lott_numb))

            elif len(same) == 4:
                answer.config(text=" WELL DONE!!!!!!!!!!!!\n" + " RR2384.50" + "\n lotto numbers " + str(lott_numb))

            elif len(same) == 3:
                answer.config(text=" Congratulations you won !!! !!!!!!!!!!!!\n" + " R8584.00" + "\n lotto numbers " + str(lott_numb))

            elif len(same) == 2:
                answer.config(text=" You at least won!!!!!!!!!!!!\n" + " R20" + "\n lotto numbers " + str(lott_numb))

            elif len(same) == 1:
                answer.config(text=" Boooooooo !!!!!!!!!!! sorry you did'nt win anything \n" + " R0" + "\n lotto numbers " + str(lott_numb))

            with open("text.txt" ,"w") as results :
                for i in range(1):
                    res = answer.cget("text") + "\n" + Time.cget("text")
                results.write(res)



lbButton = Button(window, text='Play', command=func)
lbButton.pack(side=RIGHT)
lbButton.place(x=50, y=150)

window.mainloop()
