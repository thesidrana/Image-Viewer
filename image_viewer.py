from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.config(bg="black")
#root.iconbitmap('C:/Users/thesi/Desktop/PROG/Python Prog/Tkinter/firefox.ico')

my_img1 = ImageTk.PhotoImage(Image.open("Abbey.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("revolver.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("SgtPepper.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("white.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Yellow.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status = Label(root, text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)

my_lbl = Label(image=my_img1)
my_lbl.grid(row=0,column=0,columnspan=3,padx=10,pady=30)
#my_lbl.config()

def forward(image_number):
	global my_lbl
	global button_forward
	global button_back

	my_lbl.grid_forget()
	my_lbl = Label(image=image_list[image_number-1])
	button_forward = Button(root,text=">>",command= lambda:forward(image_number+1),width=5)
	button_back = Button(root,text="<<",command=lambda:back(image_number-1),width=5)
	
	if image_number==5:
		button_forward = Button(root,text=">>",state=DISABLED,width=5)

	button_back.config(bg="#85898d",fg="white")
	button_forward.config(bg="#85898d",fg="white")
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)
	my_lbl.grid(row=0,column=0,columnspan=3,padx=10,pady=30)
	#my_lbl.config(padx=10,pady=30)
	status = Label(root, text="Image "+str(image_number)+" of "+str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=E+W)

	return

def back(image_number):
	
	global my_lbl
	global button_forward
	global button_back

	my_lbl.grid_forget()
	my_lbl = Label(image=image_list[image_number-1])
	button_forward = Button(root,text=">>",command= lambda:forward(image_number+1),width=5)
	button_back = Button(root,text="<<",command=lambda:back(image_number-1),width=5)
	
	if image_number ==1:
		button_back= Button(root,text="<<",state=DISABLED,width=5)

	button_back.config(bg="#85898d",fg="white")
	button_forward.config(bg="#85898d",fg="white")
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)
	my_lbl.grid(row=0,column=0,columnspan=3,padx=10,pady=30)
	#my_lbl.config(padx=10,pady=30)
	status = Label(root, text="Image "+str(image_number)+" of "+str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=E+W)
	return	

button_back=Button(root,text="<<",command=back,state=DISABLED,width=5)
button_exit=Button(root,text="E X I T", command=root.quit,padx=20,pady=10)
button_forward=Button(root,text=">>",command=lambda: forward(2),width=5)

button_back.config(bg="#85898d",fg="white")
button_forward.config(bg="#85898d",fg="white")
button_exit.config(bg="#85898d",fg="black")

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3,sticky=E+W)

root.mainloop()
