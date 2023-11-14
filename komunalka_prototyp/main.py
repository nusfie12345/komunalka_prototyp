import tkinter as tk

mainwindow = tk.Tk()
mainwindow.title("Головна")
mainwindow.geometry("400x300")

def to_payment():
    paymentwindow = tk.Toplevel(mainwindow)
    paymentwindow.title("Оплата")

def to_services():
    serviceswindow = tk.Toplevel(mainwindow)
    serviceswindow.title("Послуги")

to_payment_btn = tk.Button(mainwindow, text="Оплата", command=to_payment, height=3, bg="red")
to_payment_btn.place(x=160, y=55)

to_services_btn = tk.Button(mainwindow, text="Послуги", command=to_services, height=3, bg="red")
to_services_btn.place(x=160, y=105)

mainwindow.mainloop()

# спроба застосунку на пайтоні, але закинув у зв'язку з тим, що на html простіше і ефективніше це зробити