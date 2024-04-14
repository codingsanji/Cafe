from tkinter import*
import random
import time

root=Tk()
root.geometry("1200x850")
root.title("CAFE MANAGEMENT")
root.state('zoomed')
root.configure(bg="#E9CBA7")
#bg = PhotoImage(file = "‪‪C:\\Users\\501676\\Desktop\\Project\\Library\\Working one\\download.png") 
#image = root.PhotoImage(file="cafe_background___project_cappuccino_by_dokucchi_dc3w01p-fullview.png")
#root.Label(root, image=image).pack()

Tops=Frame(root,width=1350,height=100,bd=20,relief='sunken')
Tops.pack(side=TOP)

f1=Frame(root,width = 900,height=550,bd=8,relief='raise',bg="#D0D5F7")
f1.pack(side=LEFT)
f1.place(relx=0.0,rely=0.27)

fcof=Frame(root,width=100,height=100,bd=5,relief='ridge')
fcof.pack(side=LEFT)
fcof.place(relx=0.1,rely=0.2)

f2=Frame(root,width=600,height=650,bd=8,relief='raise',bg='#f6dae4')
f2.pack(side=RIGHT)
f2.place(relx=.26,rely=0.27)

fbake=Frame(root,width=100,height=100,bd=5,relief='ridge')
fbake.pack(side=RIGHT)
fbake.place(relx=0.31,rely=0.2)

f3=Frame(root,width=600,height=650,bd=8,relief='raise',bg='#D4F0F7')
f3.pack(side=RIGHT)
f3.place(relx=0.51,rely=0.34)

fscoop=Frame(root,width=600,height=650,bd=8,relief='raise',bg='#D4F0F7')
fscoop.pack(side=RIGHT)
fscoop.place(relx=0.51,rely=0.6)

fflav=Frame(root,width=100,height=100,bd=5,relief='ridge')
fflav.pack(side=RIGHT)
fflav.place(relx=0.577,rely=0.27)

ficecream=Frame(root,width=100,height=100,bd=5,relief='ridge')
ficecream.pack(side=RIGHT)
ficecream.place(relx=0.57,rely=0.2)

ftotal = Frame(root,width = 440,height=650,bd=8,relief='raise',bg='#b8cfec')
ftotal.pack(side=RIGHT)
ftotal.place(relx=.75,rely=.35)

fbutton=Frame(root,width=440,height=650,bd=8,relief='raise')
fbutton.pack(side=RIGHT)
fbutton.place(relx=.01,rely=.84)

fo=Frame(root,width=440,height=650,bd=8,relief='raise')
fo.pack(side=RIGHT)
fo.place(relx=.75,rely=.25)

#-----------------TOP INFO-----------------
lblinfo=Label(Tops,font=('Lucida Fax',40,'bold'),text="CAFE MANAGEMENT SYSTEM",fg="#98694F",bg='#F5EDDA',bd=20,pady=2)
lblinfo.grid()
#-----------------------------------------------------

def Ref():
    x=random.randint(1,1000)
    randomRef=str(x)
    rand.set(randomRef)

    if Expresso.get()=="":
        coExpresso=0
    else:
        coExpresso=float(Expresso.get())
    if DblExpresso.get()=="":
        coDblExpresso=0
    else:
        coDblExpresso=float(DblExpresso.get())
    if ExpMachiato.get()=="":
        coExpMachiato=0
    else:
        coExpMachiato=float(ExpMachiato.get())
    if CafeGlace.get()=="":
        coCafeGlace=0
    else:
        coCafeGlace=float(CafeGlace.get())
    if Mocha.get()=="":
        coMocha=0
    else:
        coMocha=float(Mocha.get())
    if CinnLatte.get()=="":
        coCinnLatte=0
    else:
        coCinnLatte=float(CinnLatte.get())
    if Americano.get()=="":#d9a38d
        coAmericano=0
    else:
        coAmericano=float(Americano.get())
    if Latte.get()=="":
        coLatte=0
    else:
        coLatte=float(Latte.get())
    if Cappuccino.get()=="":
        coCappuccino=0
    else:
        coCappuccino=float(Cappuccino.get())
    if Croissant.get()=="":
        coCroissant=0
    else:
        coCroissant=float(Croissant.get())
    if Cupcake.get()=="":
        coCupcake=0
    else:
        coCupcake=float(Cupcake.get())
    if CheeseSand.get()=="":
        coCheeseSand=0
    else:
        coCheeseSand=float(CheeseSand.get())
    if Cinnroll.get()=="":
        coCinnroll=0
    else:
        coCinnroll=float(Cinnroll.get())
    if Cheesecake.get()=="":
        coCheesecake=0
    else:
        coCheesecake=float(Cheesecake.get())
    if CheeseDan.get()=="":
        coCheeseDan=0
    else:
        coCheeseDan=float(CheeseDan.get())
    if ChocCake.get()=="":
        coChocCake=0
    else:
        coChocCake=float(ChocCake.get())
    if BlubScone.get()=="":
        coBlubScone=0
    else:
        coBlubScone=float(BlubScone.get())
    if SmallScoop.get()=="":
        coSmallScoop=0
    else:
        coSmallScoop=float(SmallScoop.get())
    if RegScoop.get()=="":
        coRegScoop=0
    else:
        coRegScoop=float(RegScoop.get())
    if LargeScoop.get()=="":
        coLargeScoop=0
    else:
        coLargeScoop=float(LargeScoop.get())

    costofexpresso= coExpresso*2.80
    costofDblExpresso= coDblExpresso*5.60
    costofexpmachiato= coExpMachiato*5
    costofcafeglace= coCafeGlace*7.20
    costofmocha= coMocha*8.90
    costofCinnLatte=coCinnLatte*4.25
    costofAmericano=coAmericano*3.20
    costofLatte=coLatte*4.35
    costofCappuccino=coCappuccino*5.50
    costofCroissant=coCroissant*3.00
    costofCupcake=coCupcake*2.40
    costofCheeseSand=coCheeseSand*4.00
    costofCinnroll=coCinnroll*4.00
    costofCheesecake=coCheesecake*2.90
    costofCheeseDan=coCheeseDan*2.45
    costofChocCake=coChocCake*3.00
    costofBlubScone=coBlubScone*2.50
    costofSmallScoop=coSmallScoop*2.00
    costofRegScoop=coRegScoop*3.40
    costofLargeScoop=coLargeScoop*5.00

    costofmeal =str('%.2f'% (costofexpresso +  costofDblExpresso + costofexpmachiato + costofcafeglace + costofmocha + costofCinnLatte + costofAmericano + costofLatte + costofCappuccino + costofCroissant + costofCupcake + costofCheeseSand + costofCinnroll + costofCheesecake + costofCheeseDan + costofChocCake + costofBlubScone + costofSmallScoop + costofRegScoop + costofLargeScoop))
    PayTax=((costofexpresso + costofDblExpresso + costofexpmachiato + costofcafeglace + costofmocha + costofCinnLatte + costofAmericano + costofLatte + costofCappuccino + costofCroissant + costofCupcake + costofCheeseSand + costofCinnroll + costofCheesecake + costofCheeseDan + costofChocCake + costofBlubScone + costofSmallScoop + costofRegScoop + costofLargeScoop)*0.1)
    Totalcost=(costofexpresso + costofDblExpresso + costofexpmachiato + costofcafeglace + costofmocha + costofCinnLatte + costofAmericano + costofLatte + costofCappuccino + costofCroissant + costofCupcake + costofCheeseSand + costofCinnroll + costofCheesecake + costofCheeseDan + costofChocCake + costofBlubScone + costofSmallScoop + costofRegScoop + costofLargeScoop)
    Ser_Charge=((costofexpresso +  costofDblExpresso + costofexpmachiato + costofcafeglace + costofmocha + costofCinnLatte + costofAmericano + costofLatte + costofCappuccino + costofCroissant +costofCupcake + costofCheeseSand + costofCinnroll + costofCheesecake + costofCheeseDan + costofChocCake + costofBlubScone + costofSmallScoop + costofRegScoop + costofLargeScoop)/99)
    Service= str('%.2f'% Ser_Charge)
    OverAllCost= str('%.2f'% (PayTax + Totalcost + Ser_Charge))
    PaidTax= str('%.2f'% PayTax)

    Service_Charge.set('$ '+ Service)
    cost.set('$ '+ costofmeal)
    Tax.set('$ '+ PaidTax)
    Subtotal.set('$ '+ costofmeal)
    Total.set('$ '+ OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Expresso.set("")
    DblExpresso.set("")
    ExpMachiato.set("")
    CafeGlace.set("")
    Mocha.set("")
    CinnLatte.set("")
    Americano.set("")
    Latte.set("")
    Cappuccino.set("")
    Croissant.set("")
    Cupcake.set("")
    CheeseSand.set("")
    Cinnroll.set("")
    Cheesecake.set("")
    CheeseDan.set("")
    ChocCake.set("")
    BlubScone.set("")
    SmallScoop.set("")
    RegScoop.set("")
    LargeScoop.set("")
    Total.set("")
    Service_Charge.set("")
    Tax.set("")
    Subtotal.set("")
    cost.set("")


#---------------------------------------------------------------------------------------
rand= StringVar()
Expresso =StringVar()
DblExpresso= StringVar()
ExpMachiato= StringVar()
CafeGlace= StringVar()
Mocha= StringVar()
CinnLatte= StringVar()
Americano= StringVar()
Latte= StringVar()
Cappuccino= StringVar()
Croissant=StringVar()
Cupcake=StringVar()
CheeseSand=StringVar()
Cinnroll=StringVar()
Cheesecake=StringVar()
CheeseDan=StringVar()
ChocCake=StringVar()
BlubScone=StringVar()
SmallScoop=StringVar()
RegScoop=StringVar()
LargeScoop=StringVar()

Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Subtotal = StringVar()
cost = StringVar()

#----------------------------------------LABELS-------------------------------------------------------

lblorder = Label(fo, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="green",bd=10,anchor='w')
lblorder.grid(row=0,column=0)
txtorder = Entry(fo,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,width=18,bg="#a9eed1",justify='right')
txtorder.grid(row=0,column=1)

lblcof = Label(fcof, font=( 'aria' ,20, 'bold','underline' ),text="COFFEE",bd=5,fg="Maroon",anchor='w')
lblcof.grid(row=1,column=1)

lblExpresso= Label(f1,font=('aria',16,'bold'),text="Expresso",fg="blue",bd=10,anchor='w',bg="#D0D5F7")
lblExpresso.grid(row=2,column=0)
txtExpresso= Entry(f1,font=('ariel',16,'bold'),textvariable=Expresso,bd=6,insertwidth=4,width=12,bg="white",justify='right')
txtExpresso.grid(row=2,column=1)

lblDblExpresso= Label(f1, font=( 'aria' ,16, 'bold' ),text="Double Expresso",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblDblExpresso.grid(row=3,column=0)
txtDblExpresso= Entry(f1,font=('ariel' ,16,'bold'), textvariable=DblExpresso, bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtDblExpresso.grid(row=3,column=1)

lblExpMachiato= Label(f1, font=( 'aria' ,16, 'bold' ),text="Expresso Machiato",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblExpMachiato.grid(row=4,column=0)
txtExpMachiato= Entry(f1,font=('ariel' ,16,'bold'), textvariable=ExpMachiato, bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtExpMachiato.grid(row=4,column=1)

lblCafeGlace= Label(f1, font=( 'aria' ,16, 'bold' ),text="White Café Glacé",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblCafeGlace.grid(row=5,column=0)
txtCafeGlace= Entry(f1,font=('ariel' ,16,'bold'), textvariable=CafeGlace, bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCafeGlace.grid(row=5,column=1)

lblMocha = Label(f1, font=( 'aria' ,16, 'bold' ),text="Mocha",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblMocha.grid(row=6,column=0)
txtMocha = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Mocha , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtMocha.grid(row=6,column=1)

lblCinnLatte = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cinnamon Latte",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblCinnLatte.grid(row=7,column=0)
txtCinnLatte = Entry(f1,font=('ariel' ,16,'bold'), textvariable=CinnLatte , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCinnLatte.grid(row=7,column=1)

lblAmericano = Label(f1, font=( 'aria' ,16, 'bold' ),text="Americano",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblAmericano.grid(row=8,column=0)
txtAmericano = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Americano , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtAmericano.grid(row=8,column=1)

lblLatte = Label(f1, font=( 'aria' ,16, 'bold' ),text="Latte",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblLatte.grid(row=9,column=0)
txtLatte = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Latte , bd=6,insertwidth=4,width=12,bg="white",justify='right')
txtLatte.grid(row=9,column=1)

lblCappuccino = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cappuccino",fg="blue",bg="#D0D5F7",bd=10,anchor='w')
lblCappuccino.grid(row=10,column=0)
txtCappuccino = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cappuccino , bd=6,insertwidth=4,width=12,bg="white",justify='right')
txtCappuccino.grid(row=10,column=1)

lblbaked = Label(fbake, font=( 'aria' ,20, 'bold','underline' ),text="BAKED GOODS",bd=5,fg="Maroon",anchor='w')
lblbaked.grid(row=1,column=2)

lblCroissant=Label(f2,font=('aria',16,'bold'),text='Croissant',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblCroissant.grid(row=2,column=2)
txtCroissant=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Croissant , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCroissant.grid(row=2,column=3,sticky='w')

lblCupcake=Label(f2,font=('aria',16,'bold'),text='Cupcake',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblCupcake.grid(row=3,column=2)
txtCupcake=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Cupcake , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCupcake.grid(row=3,column=3,sticky='w')

lblCheeseSand=Label(f2,font=('aria',16,'bold'),text='Cheese Sandwich',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblCheeseSand.grid(row=4,column=2)
txtCheeseSand=Entry(f2,font=('ariel' ,16,'bold'), textvariable=CheeseSand , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCheeseSand.grid(row=4,column=3,sticky='w')

lblCinnroll=Label(f2,font=('aria',16,'bold'),text='Cinnamon Roll',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblCinnroll.grid(row=5,column=2)
txtCinnroll=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Cinnroll , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCinnroll.grid(row=5,column=3,sticky='w')

lblCheesecake=Label(f2,font=('aria',16,'bold'),text='Cheesecake',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblCheesecake.grid(row=6,column=2)
txtCheesecake=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Cheesecake , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCheesecake.grid(row=6,column=3,sticky='w')

lblCheeseDan=Label(f2,font=('aria',16,'bold'),text='Cheese Danish',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblCheeseDan.grid(row=7,column=2)
txtCheeseDan=Entry(f2,font=('ariel' ,16,'bold'), textvariable=CheeseDan , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtCheeseDan.grid(row=7,column=3,sticky='w')

lblChocCake=Label(f2,font=('aria',16,'bold'),text='Chocolate Cake',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblChocCake.grid(row=8,column=2)
txtChocCake=Entry(f2,font=('ariel' ,16,'bold'), textvariable=ChocCake , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtChocCake.grid(row=8,column=3,sticky='w')

lblBlubScone=Label(f2,font=('aria',16,'bold'),text='Blueberry Scone',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblBlubScone.grid(row=9,column=2)
txtBlubScone=Entry(f2,font=('ariel' ,16,'bold'), textvariable=BlubScone , bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtBlubScone.grid(row=9,column=3,sticky='w')

lblspace=Label(f2,font=('aria',16,'bold'),text='       ',fg="blue",bg='#f6dae4',bd=10,anchor='w')
lblspace.grid(row=10,column=2)

lblicecream = Label(ficecream, font=( 'aria' ,20, 'bold','underline' ),text="ICE CREAM",bd=5,fg="Maroon",anchor='w')
lblicecream.grid(row=1,column=5)

lblflavours=Label(fflav,font=('aria',17,'bold','underline'), text="FLAVOURS",bd=5,fg="Maroon",anchor='w')
lblflavours.grid(row=2,column=5)

lblVanilla=Label(f3,font=('aria',16,'bold'),text='Vanilla',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblVanilla.grid(row=3,column=2)

lblChocolate=Label(f3,font=('aria',16,'bold'),text='Chocolate',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblChocolate.grid(row=4,column=2)

lblCookiedough=Label(f3,font=('aria',16,'bold'),text='Cookie Dough',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblCookiedough.grid(row=5,column=2)

lblButterscotch=Label(f3,font=('aria',16,'bold'),text='Butterscotch',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblButterscotch.grid(row=6,column=2)

lblMintchocolate=Label(f3,font=('aria',16,'bold'),text='Mint Chocolate',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblMintchocolate.grid(row=3,column=3)

lblPistachio=Label(f3,font=('aria',16,'bold'),text='Pistachio',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblPistachio.grid(row=4,column=3)

lblMango=Label(f3,font=('aria',16,'bold'),text='Mango Tango',bg='#D4F0F7',fg="blue",bd=10,anchor='w')
lblMango.grid(row=5,column=3)

lblStrawberry=Label(f3,font=('aria',16,'bold'),text='Strawberry',bg='#D4F0F7',fg="blue",bd=10,anchor='w')
lblStrawberry.grid(row=6,column=3)

lblSmall=Label(fscoop,font=('aria',16,'bold'),text='Small Scoop',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblSmall.grid(row=1,column=2)
txtSmall=Entry(fscoop,font=('ariel' ,16,'bold'), textvariable=SmallScoop, bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtSmall.grid(row=1,column=3)

lblRegular=Label(fscoop,font=('aria',16,'bold'),text='Regular Scoop',fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblRegular.grid(row=2,column=2)
txtRegular=Entry(fscoop,font=('ariel' ,16,'bold'),textvariable=RegScoop, bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtRegular.grid(row=2,column=3)

lblDouble=Label(fscoop,font=('aria',16,'bold'),text="Double Scoop",fg="blue",bg='#D4F0F7',bd=10,anchor='w')
lblDouble.grid(row=3,column=2)
txtDouble=Entry(fscoop,font=('ariel' ,16,'bold'),textvariable=LargeScoop, bd=6,insertwidth=4,width=12,bg="white" ,justify='right')
txtDouble.grid(row=3,column=3)

lblcost = Label(ftotal, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bg='#b8cfec',bd=10,anchor='w')
lblcost.grid(row=2,column=1)
txtcost = Entry(ftotal,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,width=12,bg="#f5e1fd" ,justify='right')
txtcost.grid(row=2,column=2)

lblService_Charge = Label(ftotal, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bg='#b8cfec',bd=10,anchor='w')
lblService_Charge.grid(row=3,column=1)
txtService_Charge = Entry(ftotal,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,width=12,bg="#f5e1fd" ,justify='right')
txtService_Charge.grid(row=3,column=2)

lblTax = Label(ftotal, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bg='#b8cfec',bd=10,anchor='w')
lblTax.grid(row=4,column=1)
txtTax = Entry(ftotal,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,width=12,bg="#f5e1fd" ,justify='right')
txtTax.grid(row=4,column=2)

lblSubtotal = Label(ftotal, font=( 'aria' ,16, 'bold' ),text="Subtotal",bg='#b8cfec',fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=1)
txtSubtotal = Entry(ftotal,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,width=12,bg="#f5e1fd" ,justify='right')
txtSubtotal.grid(row=5,column=2)

lblTotal = Label(ftotal, font=( 'aria' ,16, 'bold' ),text="Total",bg='#b8cfec',fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=1)
txtTotal = Entry(ftotal,font=('ariel' ,16,'bold'),textvariable=Total , bd=6,insertwidth=4,width=12,bg="#f5e1fd" ,justify='right')
txtTotal.grid(row=6,column=2)


#----------------------------MENU-------------------------------------
def create_frame(root, width, height, side, relx, rely, offset=0):
    frame = Frame(root, width=width, height=height, bd=8, relief='raise', bg='#FCDD9E')
    frame.pack(side=side)
    frame.place(relx=relx, rely=rely+offset)
    return frame

def create_label(frame, text, row, column, font=('aria', 18, 'bold'), fg="black", bg='#FCDD9E', anchor='w'):
    label = Label(frame, text=text, font=font, fg=fg, bg=bg, anchor=anchor)
    label.grid(row=row, column=column)
    return label

def menu():
    rootm = Tk()
    rootm.state('zoomed')
    rootm.title("Menu")
    rootm.configure(bg='brown')


    f_menu_heading = create_frame(rootm, 600, 80, 'top', 0.45, 0.0, offset=0.05)
    lbl_menu_heading = Label(f_menu_heading, text="MENU", font=('aria', 40, 'bold'), fg='black')
    lbl_menu_heading.pack(side=TOP, pady=10)  

    ftop1 = create_frame(rootm, 220, 50, 'top', 0.085, 0.1, offset=0.15)
    ftop2 = create_frame(rootm, 220, 50, 'top', 0.315, 0.1, offset=0.15)
    ftop3 = create_frame(rootm, 220, 50, 'top', 0.6, 0.1, offset=0.15)
    f1m = create_frame(rootm, 350, 350, 'left', 0.03, 0.37)
    f2m = create_frame(rootm, 350, 350, 'right', 0.3, 0.37)
    f3m = create_frame(rootm, 350, 350, 'right', 0.599, 0.37)
    f4m = create_frame(rootm, 350, 350, 'right', 0.75, 0.37)

    create_label(ftop1, "COFFEE", 0, 0, font=('aria', 22, 'bold', 'underline'))
    create_label(ftop2, "BAKED GOODS", 0, 0, font=('aria', 22, 'bold', 'underline'))
    create_label(ftop3, "ICE CREAM", 0, 0, font=('aria', 22, 'bold', 'underline'))

    coffee_menu = [
        ("Expresso", "2.80$"), ("Double Expresso", "5.60$"), ("Expresso Machiato", "5.00$"),
        ("White Café Glacé", "7.20$"), ("Mocha", "8.90$"), ("Cinnamon Latte", "4.25$"),
        ("Americano", "3.20$"), ("Latte", "4.35$"), ("Cappuccino", "5.50$")
    ]
    for i, (item, price) in enumerate(coffee_menu, start=1):
        create_label(f1m, item, i, 0)
        create_label(f1m, price, i, 2)

    baked_goods_menu = [
        ("Croissant", "3.00$"), ("Cupcake", "2.40$"), ("Cheese sandwich", "4.00$"),
        ("Cinnamon Roll", "4.00$"), ("Cheesecake", "2.90$"), ("Cheese Danish", "2.45$"),
        ("Chocolate Cake", "3.00$"), ("Blueberry Scone", "2.50$")
    ]
    for i, (item, price) in enumerate(baked_goods_menu, start=1):
        create_label(f2m, item, i, 3)
        create_label(f2m, price, i, 4)

    ice_cream_flavors = [
        "Vanilla", "Chocolate", "Cookie Dough", "Butterscotch", "Mint Chocolate",
        "Pistachio", "Mango Tango", "Strawberry"
    ]
    create_label(f3m, "FLAVOURS:", 1, 6, font=('aria', 18, 'bold', 'underline'))
    for i, flavor in enumerate(ice_cream_flavors, start=2):
        create_label(f3m, flavor, i, 6)

    ice_cream_prices = [("Small Scoop", "2.00$"), ("Regular Scoop", "3.40$"), ("Double Scoop", "5.00$")]
    for i, (item, price) in enumerate(ice_cream_prices, start=9):
        create_label(f4m, item, i, 6)
        create_label(f4m, price, i, 7)

    rootm.mainloop()


#-----------------------------------------buttons------------------------------------------

btnTotal=Button(fbutton,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="#03c04a",command=Ref)
btnTotal.grid(row=12, column=1)

btnreset=Button(fbutton,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="yellow",command=reset)
btnreset.grid(row=12, column=2)

btnexit=Button(fbutton,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="#d21404",command=qexit)
btnexit.grid(row=12, column=3)

btnmenu=Button(fbutton,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="MENU", bg="#b47ede",command=menu)
btnmenu.grid(row=12, column=0)

root.mainloop()

