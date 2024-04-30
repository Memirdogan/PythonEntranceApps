import tkinter as tk


# FUNCS

def sum():
    try:
        Tnum1 = int(num1.get())
        Tnum2 = int(num2.get())
        final = Tnum1 + Tnum2
        labelFinal.config(text="Sonuç: " + str(final))
    except ValueError:
        labelFinal.config(text="Gecerli bir sayı giriniz!")


"""
def minus():
    return x - y


def multip():
    return x * y


def div():
    if y == 0:
        return "sıfıra bolme hatası"
    else:
        return x / y
"""
# form
form = tk.Tk() #creating obj
form.geometry("475x320+600+250") #size
form.resizable(False, False)
form.title("Calculator")

label = tk.Label(form, text="Calculator by Musa Emir Dogan", fg="brown", bg="bisque1", font="Times 8 italic") #fg = foreground
label.pack() # label show

# input label 1
label1 = tk.Label(form,text="Sayı 1: ", font="Times 17")
label1.place(x=70,y=60)
# input Entry 1
num1 = tk.Entry(form, width=25, font="Times 12 bold")
num1.place(x=150,y=65)

# input label 2
label2 = tk.Label(form,text="Sayı 2: ", font="Times 17")
label2.place(x=70,y=105)
# input Entry 2
num2 = tk.Entry(form, width=25, font="Times 12 bold")
num2.place(x=150,y=110)

# out label
labelFinal = tk.Label(form,text="Sonuc: ", font="Times 17")
labelFinal.place(x=200,y=150)

# buttons
button1 = tk.Button(form, text="Topla", font="Times 17",command=sum)
button1.place(x=70,y=210)

button2 = tk.Button(form, text="Çıkart", font="Times 17",command=sum)
button2.place(x=160,y=210)

button3 = tk.Button(form, text="Çarp", font="Times 17",command=sum)
button3.place(x=255,y=210)

button4 = tk.Button(form, text="Böl", font="Times 17",command=sum)
button4.place(x=340,y=210)

form.mainloop()
