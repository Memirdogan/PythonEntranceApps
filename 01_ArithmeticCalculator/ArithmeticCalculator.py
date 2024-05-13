import tkinter as tk


# calculation functions
def _sum():
    try:
        _num1 = int(num1.get())
        _num2 = int(num2.get())
        final = _num1 + _num2
        labelFinal.config(text="      Sonuç: " + str(final))
    except ValueError:
        labelFinal.config(text="Gecerli bir sayı giriniz!")


def _minus():
    try:
        _num1 = int(num1.get())
        _num2 = int(num2.get())
        final = _num1 - _num2
        labelFinal.config(text="      Sonuç: " + str(final))
    except ValueError:
        labelFinal.config(text="Geçerli bir sayı giriniz!")


def _multip():
    try:
        _num1 = int(num1.get())
        _num2 = int(num2.get())
        final = _num1 * _num2
        labelFinal.config(text="      Sonuç: " + str(final))
    except ValueError:
        labelFinal.config(text="Geçerli bir sayı giriniz!")


def _div():
    try:
        _num1 = float(num1.get())
        _num2 = float(num2.get())
        if _num2 != 0:
            final = _num1 / _num2
            labelFinal.config(text="      Sonuç: " + str(final))
        else:
            labelFinal.config(text="Geçerli bir sayı giriniz!")
    except ValueError:
        labelFinal.config(text="Geçerli bir sayı giriniz!")


# form
form = tk.Tk()
form.geometry("475x320+600+250")
form.resizable(False, False)
form.title("Calculator")

label = tk.Label(form, text="Calculator by Musa Emir Dogan", fg="brown", bg="bisque1",
                 font="Times 8 italic")
label.pack()

# input label 1
label1 = tk.Label(form, text="Sayı 1: ", font="Times 17")
label1.place(x=70, y=60)
# input Entry 1
num1 = tk.Entry(form, width=25, font="Times 12 bold")
num1.place(x=150, y=65)

# input label 2
label2 = tk.Label(form, text="Sayı 2: ", font="Times 17")
label2.place(x=70, y=105)
# input Entry 2
num2 = tk.Entry(form, width=25, font="Times 12 bold")
num2.place(x=150, y=110)

# out label
labelFinal = tk.Label(form, text="        Sonuç:    ", font="Times 17")
labelFinal.place(x=142, y=150)

# buttons
button1 = tk.Button(form, text="Topla", font="Times 17", command=_sum)
button1.place(x=70, y=210)

button2 = tk.Button(form, text="Çıkart", font="Times 17", command=_minus)
button2.place(x=160, y=210)

button3 = tk.Button(form, text="Çarp", font="Times 17", command=_multip)
button3.place(x=255, y=210)

button4 = tk.Button(form, text="Böl", font="Times 17", command=_div)
button4.place(x=340, y=210)

form.mainloop()
