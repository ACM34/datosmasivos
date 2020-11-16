from tkinter import Tk, Label, Button




def startsave():
    naam = []
    saved = []
    target = []
    period = []
    delay = []

def periodeinwoorden(weken):
    if weken == 1:
        return (str(weken) + " week")
    elif weken > 52:
        jaren = weken // 52
        weken = weken % 52
        if jaren == 1 and weken == 1:
            return (str(jaren) + " jaar en " +str(weken)+ " week")
        elif jaren != 1 and weken !=1:
            return (str(jaren) + " jaren en " +str(weken) +" weken")
        elif jaren == 1:
            return (str(jaren) + " jaar en " +str(weken)+ " weken")
        elif weken == 1:
            return (str(jaren) + " jaren en " +str(weken)+ " week")
    else:
        return (str(weken) + " weken")


class Save:
    # the constructor
    def __init__(self, name, target, period, delay):
        self.name = name
        self.saved = 0
        self.target = target
        self.period = period
        self.delay = delay

    def adjust(self):
        keuzemenu()
        keuze = input()
        while keuze == "1" or keuze == "2":
            print("foute optie")
            keuzemenu()
        #vraag de variabelen
        target = float(input("target: "))
        period = int(input("period: "))
        delay = int(input("delay: "))
        if keuze == "1":
            self.overwrite(target, period, delay)
        elif keuze == "2":
            self.add(target, period, delay)

    def overwrite(self, target, period, delay):
        self.target = target
        self.period = period
        self.delay = delay

    def add(self, target, period, delay):
        self.target += target
        self.period += period
        self.delay += delay

def printsave(save):
    i = 0
    opbouw = ("%20s |%20s |%20s |%20s |\n" %("name", "target", "period", "delay"))
    for i in range(len(save)):
        a = str(save[i].name)
        b = str(save[i].target)
        c = periodeinwoorden(save[i].period)
        d = str(save[i].delay)
        opbouw += ("%20s |%20s |%20s |%20s \n" %(a, b, c, d))
    return opbouw

save = []
save.append(Save("erasmus", 500, 2, 1))
save.append(Save("test", 200, 53, 0))
save.append(Save("test", 200, 200, 0))
save.append(Save("idk", 200, 1, 0))
save.append(Save("idk", 200, 1, 0))

print(printsave(save))


def keuzemenu():
    print('''
    1. overwrite
    2. add
    ''')

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Accountable")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.label3 = Label(master, text="test")
        self.label3.pack()
        self.label3.place(relx=0.0, rely=1.0, anchor='sw')



        self.label2 = Label(master, text=printsave(save))
        self.label2.pack()


        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


root = Tk()
my_gui = MainGUI(root)
root.mainloop()
