from tkinter import*
root= Tk()
root.title("procent")
root.geometry("400x500")
root["bg"]="grey"

Text_top = Label(text="Enter number")
Text_top.place(x=160,y=20,)
Text_top["bg"]="grey"

Input_number = Entry(root, justify='center')
Input_number["bg"]="white"
Input_number.place(x=10,y=60,width=380,height=50)

Office=IntVar()
office_1=Radiobutton(text="5%",variable=Office,font=16,fg="#52483C",bg="grey",value=1)
office_1.place(x=180,y=140)	

office_2=Radiobutton(text="10%",variable=Office,font=16,fg="#52483C",bg="grey",value=2)
office_2.place(x=180,y=200)	

office_3=Radiobutton(text="15%",variable=Office,font=16,fg="#52483C",bg="grey",value=3)
office_3.place(x=180,y=260)	

def on_check():
    Number = Input_number.get()
    if Office.get() == 1:
        Answer = int(Number) * 0.05
        print(Answer)
    elif Office.get() == 2:
        Answer = int(Number) * 0.1
        print(Answer)
    elif Office.get() == 3:
        Answer = int(Number) * 0.15
        print(Answer)

    root.after(100, show_answer,Answer)


def show_answer(Answer):
    popup = Toplevel()
    popup.title("Your Answer")
    popup.geometry("200x100")
    message = Label(popup, text="Answer is: " + str(Answer))
    message.pack()

	

    
		
button_check = Button(root, text="Check", command=on_check)
button_check.place(x=160, y=380, width=80, height=50)


	
