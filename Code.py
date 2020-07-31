from tkinter import*
import time
from tkinter import ttk

def btn(numbers):
    global__operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def Clear():
    global__operator
    operator = ''
    txt_input.set('')
    Display.insert(0,'Start Calculating.....')

def Equal():
    global__operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''    

root=Tk()
root.geometry('1600x800+0+0')
root.title("Hotel Management System")


# -------------------Window's Partition---------------
tops=Frame(root,width=1600,height=100,bg='blue',relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3=Frame(root,width=35,height=700,relief=SUNKEN)
f3.pack(side=LEFT)

f4=Frame(root,width=100,height=700,relief=SUNKEN)
f4.pack(side=LEFT)


# -------------------Main Screen--------------------
txt_input=StringVar(value = "Welcome!")

Display=Entry(tops,font=('arial',97,'bold'),fg='white',bd=50,bg='blue',justify='right',textvariable=txt_input)
Display.grid(columnspan=4)

#-------------------Date and Time--------------------
localtime=time.asctime(time.localtime(time.time()))
lblInfo = Label(f2,font=('arial',20,'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
lblInfo.grid(row=0,column=0,columnspan=4)

# ------------------------Row-1-------------------------
operator=''

btn7 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='7',command=lambda:btn(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='8',command=lambda:btn(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='9',command=lambda:btn(9)).grid(row=1,column=2)
btnC = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='C',bg='green',command=Clear).grid(row=1,column=3)

# ------------------------Row-2-------------------------
btn4 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='4',command=lambda:btn(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='5',command=lambda:btn(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='6',command=lambda:btn(6)).grid(row=2,column=2)
btnplus = Button(f2,padx=18,pady=5,bd=8,font=('aerial',30,'bold'),text='+',bg='yellow',command=lambda:btn('+')).grid(row=2,column=3)

# ------------------------Row-3-------------------------
btn1 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='1',command=lambda:btn(1)).grid(row=3,column=0)
btn1 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='2',command=lambda:btn(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='3',command=lambda:btn(3)).grid(row=3,column=2)
btnminus = Button(f2,padx=23,pady=5,bd=8,font=('aerial',30,'bold'),text='-',bg='yellow',command=lambda:btn('-')).grid(row=3,column=3)
# ------------------------Row-4-------------------------
btn0 = Button(f2,padx=15,pady=5,bd=8,font=('aerial',30,'bold'),text='0',command=lambda:btn(0)).grid(row=4,column=0)
btndot = Button(f2,padx=21,pady=5,bd=8,font=('aerial',30,'bold'),text='.',bg='yellow',command=lambda:btn('.')).grid(row=4,column=1)
btndivision = Button(f2,padx=20,pady=5,bd=8,font=('aerial',30,'bold'),text='/',bg='yellow',command=lambda:btn('/')).grid(row=4,column=2)
btnmul = Button(f2,padx=19,pady=5,bd=8,font=('aerial',30,'bold'),text='x',bg='yellow',command=lambda:btn('*')).grid(row=4,column=3)

# ------------------------Row-5-------------------------
btnequal = Button(f2,padx=64,pady=2,bd=8,font=('aerial',30,'bold'),text='=',bg='green',command=Equal).grid(row=5,column=0,columnspan=2)
btnopenbracket = Button(f2,padx=19,pady=2,bd=8,font=('aerial',30,'bold'),text='(',bg='yellow',command=lambda:btn('(')).grid(row=5,column=2)
btnclosecracket = Button(f2,padx=23,pady=2,bd=8,font=('aerial',30,'bold'),text=')',bg='yellow',command=lambda:btn(')')).grid(row=5,column=3)

#-------------------------Choose Meal-------------------
Meal1 =IntVar()
Mealdicator=StringVar(value='Delicious Meals')

lblMeal = Label(f1,font=('aerial',16,'bold'),text='Choose Meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal=ttk.Combobox(f1,font=('aerial',16,'bold'),textvariable=Mealdicator)
txtMeal['values']=('Fried Rice','Fried rice and Chicken','Chilli chicken','HamBurger','CheesePizza')
txtMeal.grid(row=0,column=1)

lblQtofMeal = Label(f1,font=('aerial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
lblQtofMeal.grid(row=1,column=0)
txtQtofMeal = Entry(f1,font=('aerial',16,'bold'),textvariable=Meal1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtofMeal.grid(row=1,column=1)

#--------------------Choose Drinks-------------------------
Drink1 =IntVar()
Drinkdicator=StringVar(value='Fresh Drinks')

lblDrink = Label(f1,font=('aerial',16,'bold'),text='Choose Drink',bd=10,anchor=W)
lblDrink.grid(row=2,column=0)
txtDrink=ttk.Combobox(f1,font=('aerial',16,'bold'),textvariable=Drinkdicator)
txtDrink['values']=('Bottled water','Lime Juice','Cold Coffee','Heineken','Red Wine')
txtDrink.grid(row=2,column=1)

lblQtofDrink = Label(f1,font=('aerial',16,'bold'),text='Qty. of Drink',bd=10,anchor=W)
lblQtofDrink.grid(row=1,column=0)
txtQtofDrink = Entry(f1,font=('aerial',16,'bold'),textvariable=Drink1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtofDrink.grid(row=3,column=1)

#-------------------Order Delivery------------------------
chkb1 = IntVar()

lblHomeDev = Label(f1,font=("aerial",16,'bold'),text='Order Delivery',bd=10,anchor=W)
lblHomeDev.grid(row=4,column=0)
check1 = Checkbutton(f1,text='Yes',variable=chkb1,font=('aerial',16,'bold'))
check1.grid(row=4,column=1)

#-----------------Book a Room --------------------------
v= IntVar()
v.set(3)
lblRoom = Label(f1,font=('aerial',16,'bold'),text='Book a Room',bd=10,anchor=W)
lblRoom.grid(row=5,column=0)
MyRadio = Radiobutton(f1,text='VIP',font=("aerial",16,"bold"),variable=v,value=1)
MyRadio.grid(row=5,column=1,sticky=W)
MyRadio = Radiobutton(f1,text='Normal',font=("aerial",16,"bold"),variable=v,value=2)
MyRadio.grid(row=5,column=1)
MyRadio = Radiobutton(f1,text='No',font=("aerial",16,"bold"),variable=v,value=3)
MyRadio.grid(row=5,column=1,sticky=E)

#-------------------Cost Display Screen-----------------
Cost=StringVar()
lblMeal1 = Label(f1,font=('aerial',16,'bold'),text="Cost of Meal(Rs.)",bd=16,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1=Entry(f1,font=('aerial',16,'bold'),textvariable=Cost,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtMeal1.grid(row=0,column=3)

Drinks=StringVar()
lblDrink1 = Label(f1,font=('aerial',16,'bold'),text="Cost of Drink(Rs.)",bd=16,anchor=W)
lblDrink1.grid(row=1,column=2)
txtDrink1=Entry(f1,font=('aerial',16,'bold'),textvariable=Drinks,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtDrink1.grid(row=1,column=3)

DevCost=StringVar()
lblDev = Label(f1,font=('aerial',16,'bold'),text="Delivery Cost(Rs.)",bd=16,anchor=W)
lblDev.grid(row=2,column=2)
txtDev=Entry(f1,font=('aerial',16,'bold'),textvariable=DevCost,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtDev.grid(row=2,column=3)

RoomCost=StringVar()
lblRoom = Label(f1,font=('aerial',16,'bold'),text="Cost of Room(Rs.)",bd=16,anchor=W)
lblRoom.grid(row=3,column=2)
txtRoom=Entry(f1,font=('aerial',16,'bold'),textvariable=RoomCost,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtRoom.grid(row=3,column=3)

ServiceCharge=StringVar()
lblService = Label(f1,font=('aerial',16,'bold'),text="Servive Fee(Rs.)",bd=16,anchor=W)
lblService.grid(row=4,column=2)
txtService=Entry(f1,font=('aerial',16,'bold'),textvariable=ServiceCharge,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtService.grid(row=4,column=3)

Total=StringVar()
lblTotal = Label(f1,font=('aerial',16,'bold'),text="Total Cost(Rs.)",bd=16,anchor=W)
lblTotal.grid(row=4,column=2)
txtTotal=Entry(f1,font=('aerial',16,'bold'),textvariable=Total,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtTotal.grid(row=4,column=3)

#---------------------Currency Converter---------------------------
var1 = IntVar()
indicator = StringVar(value='Choose a Country')

lblCunCon = Label(f1,font=('aerial',16,'bold italic'),text='----------------------Currency Converter----------------',bd=20,anchor=W)
lblCunCon.grid(row=6,column=0,columnspan=4)

lblCountry = Label(f1,font=('aerial',16,'bold'),text='Nationality',bd=20,anchor=W)
lblCountry.grid(row=7,column=0)
txtCountry = ttk.Combobox(f1,font=('aerial',16,'bold'),textvariable=indicator)
txtCountry['values']=('China','France','Ghana','USA','Mexico','Nigeria')
txtCountry.grid(row=7,column=1)

lblAmount = Label(f1,font=('aerial',16,'bold'),text='Amount(Rs. )',bd=20,anchor=W)
lblAmount.grid(row=7,column=2)
txtAmount=Entry(f1,font=('aerial',16,'bold'),textvariable=var1,bd=10,insertwidth=4,bg='white',justify='right')
txtAmount.grid(row=7,column=3)

#---------------------Control Buttons---------------------------------
btnConvert= Button(f1,padx=7,pady=4,bd=16,fg='white',font=('aerial',16,'bold'),width=10,text='Convert',bg='orange')
btnConvert.grid(row=8,column=2)

btnTotal= Button(f4,padx=10,pady=8,bd=16,fg='white',font=('aerial',16,'bold'),width=10,text='Total',bg='orange')
btnTotal.grid(row=0,column=0)

btnScreen= Button(f4,padx=10,pady=8,bd=16,fg='white',font=('aerial',16,'bold'),width=10,text='Clear',bg='blue')
btnScreen.grid(row=1,column=0)

btnReset= Button(f4,padx=10,pady=8,bd=16,fg='white',font=('aerial',16,'bold'),width=10,text='Reset',bg='green')
btnReset.grid(row=2,column=0)

btnExit= Button(f4,padx=10,pady=8,bd=16,fg='white',font=('aerial',16,'bold'),width=10,text='Exit',bg='red')
btnExit.grid(row=3,column=0)

#--------------------------Logo----------------------------------------
photo=PhotoImage(file='logo.png') ## Write the full path of image
myphoto = Label(f1,image=photo)
myphoto.grid(row=8,column=0)




root.mainloop()
