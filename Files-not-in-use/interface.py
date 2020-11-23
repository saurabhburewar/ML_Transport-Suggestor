from tkinter import *

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        q1 = Frame(self, bg="red", height=10).pack(side="top", fill="both")
        q1text = Label(q1, text="Is there any transport you would like to avoid ?", bg="red")
        q1text.pack(side="top", fill="x")
        Checkop1 = IntVar()
        checkop1 = Checkbutton(q1, text="Air", variable = Checkop1, width=10, height=5).pack()
        Checkop2 = IntVar()
        checkop2 = Checkbutton(q1, text="Road", variable = Checkop2, width=10, height=5).pack()


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

        
class Mainview(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="bottom", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="right")
        b2.pack(side="right")
        b3.pack(side="right")

        p1.show()



if __name__ == "__main__":
    
    root = Tk()
    root.geometry("500x500")
    main = Mainview(root)
    main.pack(side="top", fill="both", expand=True)
    # graph =  PhotoImage(file="RoadGraph.png")
    # graphLabel = Label(Transport_Suggester, image = graph)
    # graphLabel.pack()

    root.mainloop()