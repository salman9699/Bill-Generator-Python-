import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

d_date = datetime.datetime.now()
# create root window
root=Tk()
root.title("Billing")
# get screen resolution
rw=root.winfo_screenwidth()
rh=root.winfo_screenheight()
root.geometry("1000x600")
#=================MainTreeView======================
billsTV = ttk.Treeview(root,height=15)

#-----------------Assigning list---------------------
itemnamelist=[]
ratelist=[]
quantitylist=[]
costlist=[]
#----------------ENTRY VARIABLES----------------------
addItemNameVar=StringVar()
addItemRateVar=StringVar()
addItemQuantityVar=StringVar()
addItemCostVar=StringVar()
addItemNoVar=StringVar()
addFileNameVar=StringVar()
deleteItemNameVar=StringVar()

def quantityFieldListener(a,b,c):
    global addItemQuantityVar
    global addItemCostVar
    global addItemRateVar
    rate=addItemRateVar.get()
    quantity = addItemQuantityVar.get()
    if quantity != "":
        try:
            quantity=int(quantity)
            rate=int(rate)
            cost = quantity*rate
            addItemQuantityVar.set(quantity)
            addItemCostVar.set("%.2f"%cost)
        except ValueError:
            quantity=quantity[:-1]
            addItemQuantityVar.set(quantity)
    else:
        quantity=""
        addItemQuantityVar.set(quantity)

def costFieldListener(a,b,c):
    global addItemQuantityVar
    global addItemCostVar
    global addItemRateVar
    rate=addItemRateVar.get()
    cost = addItemCostVar.get()
    if cost !="":
        try:
            cost = float(cost)
            rate=float(rate)
            quantity=cost/rate
            quantity_int=int(quantity)
            addItemQuantityVar.set(quantity_int)
            addItemCostVar.set("%.2f"%cost)
        except ValueError:
            cost=cost[:-1]
            addItemCostVar.set(cost)
    else:
        cost=""
        addItemCostVar.set(cost)
#---------------------Tracing the Entries-------------------
addItemQuantityVar.trace('w',quantityFieldListener)
addItemCostVar.trace('w',costFieldListener)

def remove_all_widgets():
    global root
    for widget in root.winfo_children():
        widget.place_forget()   

def mainlogin():
    titlelabel=Label(root,text="Billing System ",font=('Arial',40),fg="gray25",bg="PeachPuff2")
    titlelabel.place(x=600,y=50)

    startbutton=Button(root,text="START",width=20,bg="NavajoWhite4",cursor="hand2",height=2,command=mainwindow)
    startbutton.place(x=650,y=250)

    Exitbutton=Button(root,text="EXIT",bg="NavajoWhite4",cursor="hand2",width=20,height=2,command=root.destroy)
    Exitbutton.place(x=650,y=350)
    root.configure(bg="PeachPuff2")

def mainwindow():
    
    remove_all_widgets()
    showitem()
    
    titlelabel=Label(root,text="Billing System ",font=('Arial',40),fg="gray25",bg="PeachPuff2")
    titlelabel.place(x=600,y=50)

    itemNameLabel= Label(root, text="Item Name",font=('Arial',14),bg="PeachPuff2")
    itemNameLabel.place(x=400, y=150)

    itemNameEntry= Entry(root,textvariable=addItemNameVar, width=25,bd=5)
    itemNameEntry.place(x=550, y=150)

    itemRateLabel= Label(root, text="Rate",font=('Arial',14),bg="PeachPuff2")
    itemRateLabel.place(x=775, y=150)
    
    itemRateEntry= Entry(root,textvariable=addItemRateVar,width=25,bd=5)
    itemRateEntry.place(x=850, y=150)
    
    itemQuantityLabel= Label(root, text="Quantity",font=('Arial',14),bg="PeachPuff2")
    itemQuantityLabel.place(x=400, y=200)
    
    itemQuantityEntry= Entry(root,textvariable=addItemQuantityVar,width=25,bd=5)
    itemQuantityEntry.place(x=550, y=200)
    
    itemCostLabel= Label(root, text="Cost",font=('Arial',14),bg="PeachPuff2")
    itemCostLabel.place(x=775, y=200)

    itemCostEntry= Entry(root,textvariable=addItemCostVar,width=25,bd=5)
    itemCostEntry.place(x=850, y=200)
    
    updateitembutton=Button(root,text="Update Item",width=15,bg="NavajoWhite4",bd=1,cursor="hand2",height=2,command=updateitem)
    updateitembutton.place(x=830,y=250)

    cancelbutton=Button(root,text="Close",width=15,height=2,bg="NavajoWhite4",bd=1,cursor="hand2",command=root.destroy)
    cancelbutton.place(x=150,y=150)

    billLabel=Label(root, text="Bill Preview", font="Arial 25",fg="gray25",bg="PeachPuff2")
    billLabel.place(x=600,y=340)

    billsTV.place(x=150,y=400)

    scrollBar = ttk.Scrollbar(root, orient="vertical",command=billsTV.yview)
    scrollBar.place(x=1150,y=400,height=330)

    billsTV.configure(yscrollcommand=scrollBar.set)
    
    billsTV["columns"]=("1","2","3","4")
    #billsTV['show']='headings'      //removes th 0th column
    
    billsTV.heading('#0',text="NO.")
    billsTV.heading('#1',text="ITEM NAME")
    billsTV.heading('#2',text="RATE")
    billsTV.heading('#3',text="QUANTITY")
    billsTV.heading('#4',text="COST")
    
    def clearEntry():
        itemNameEntry.delete(0,END)
        itemQuantityEntry.delete(0,END)
        itemCostEntry.delete(0,END)
        itemRateEntry.delete(0,END)
    def additem():
        str1=addItemNameVar.get()
        str2=addItemRateVar.get()
        str3=addItemQuantityVar.get()
        str4=addItemCostVar.get()
        if str1.isalnum():
            if str2.isdigit() and str3.isdigit():
                itemnamelist.append(str1)
                ratelist.append(str2)
                quantitylist.append(str3)
                costlist.append(str4)
                placeitem()
                clearEntry()
            else:
                messagebox.showinfo("Note","Rate & Quantity value should be numeric")
                root.deiconify()
    printbillbutton=Button(root,text="Print Bill",bd=1,width=15,bg="NavajoWhite4",cursor="hand2",height=2,command=printbill)
    printbillbutton.place(x=1030,y=250)

    additembutton=Button(root,text="Add Item",bg="NavajoWhite4",bd=1,width=15,height=2,cursor="hand2",command=additem)
    additembutton.place(x=400,y=250)

    deletebutton=Button(root,text="Delete Selected Item",bg="NavajoWhite4",bd=1,width=19,height=2,cursor="hand2", command=delete_selected)
    deletebutton.place(x=600,y=250)

def addupdateitem():
    str1=addItemNameVar.get()
    str2=addItemRateVar.get()
    str3=addItemQuantityVar.get()
    str4=addItemCostVar.get()
    str5=addItemNoVar.get()
    new=int(str5)
    if str1.isalnum():
        if str2.isdigit() and str3.isdigit():
            itemnamelist[new-1]=str1
            ratelist[new-1]=str2
            quantitylist[new-1]=str3
            costlist[new-1]=str4
            showitem()
        else:
            messagebox.showinfo("Note","Rate & Quantity value should be numeric")
            root.deiconify()

def Deleteitem():
    top=Toplevel()
    top.title("Delete Item")
    top.geometry("300x200+600+180")
    def Delete_item():
        NO=deleteItemNameVar.get()
        itemNO=int(NO,10)
        del itemnamelist[itemNO-1]
        del ratelist[itemNO-1]
        del quantitylist[itemNO-1]
        del costlist[itemNO-1]
        top.deiconify()
        top.destroy()
        top.mainloop()
    L1=Label(top,text="Enter Item No and press Enter",font=('Arial',14),fg="red")
    filename=Entry(top,textvariable=deleteItemNameVar, bd=5)
    button=Button(top,text="Enter",cursor="hand2",width=15,height=2,command=Delete_item)
    L1.pack()
    filename.pack()
    button.pack()
    #showitem()

def delete_selected():
    selected_item= billsTV.selection()[0]
    str1=selected_item[len(selected_item)-1]
    print(str1)
    n=int(str1,10)
    billsTV.delete(selected_item)
    showitem()
    del itemnamelist[n-1]
    del ratelist[n-1]
    del quantitylist[n-1]
    del costlist[n-1]
    showitem()

def placeitem():
    n=len(itemnamelist)
    billsTV.insert("",'end',text=n,values=(itemnamelist[n-1],ratelist[n-1],quantitylist[n-1],costlist[n-1]))

def showitem():
    n=len(itemnamelist)
    for i in billsTV.get_children():
        billsTV.delete(i)
    for i in range(0,n):
        billsTV.insert("",'end',text=i+1,values=(itemnamelist[i],ratelist[i],quantitylist[i],costlist[i]))

def updateitem():

    remove_all_widgets()
    showitem()
    
    titlelabel=Label(root,text="Billing System ",font=('Arial',40),bg="PeachPuff2")
    titlelabel.place(x=600,y=50)

    itemNOLabel= Label(root, text="Item NO",font=('Arial',14),bg="PeachPuff2")
    itemNOLabel.place(x=60, y=150)

    itemNOEntry= Entry(root,textvariable=addItemNoVar,width=25,bd=5)
    itemNOEntry.place(x=160, y=150)

    itemNameLabel= Label(root, text="Item Name",font=('Arial',14),bg="PeachPuff2")
    itemNameLabel.place(x=400, y=150)

    itemNameEntry= Entry(root,textvariable=addItemNameVar, width=25,bd=5)
    itemNameEntry.place(x=550, y=150)

    itemRateLabel= Label(root, text="Rate",font=('Arial',14),bg="PeachPuff2")
    itemRateLabel.place(x=775, y=150)
    
    itemRateEntry= Entry(root,textvariable=addItemRateVar,width=25,bd=5)
    itemRateEntry.place(x=850, y=150)

    itemQuantityLabel= Label(root, text="Quantity",font=('Arial',14),bg="PeachPuff2")
    itemQuantityLabel.place(x=400, y=200)
    
    itemQuantityEntry= Entry(root,textvariable=addItemQuantityVar,width=25,bd=5)
    itemQuantityEntry.place(x=550, y=200)

    itemCostLabel= Label(root, text="Cost",font=('Arial',14),bg="PeachPuff2")
    itemCostLabel.place(x=775, y=200)
    
    itemCostEntry= Entry(root,textvariable=addItemCostVar,width=25,bd=5)
    itemCostEntry.place(x=850, y=200)

    def clearEntry():
        itemNOEntry.delete(0,END)
        itemNameEntry.delete(0,END)
        itemQuantityEntry.delete(0,END)
        itemCostEntry.delete(0,END)
        itemRateEntry.delete(0,END)
    clearEntry()

    clearentrybutton=Button(root,text="Clear Entry",bd=1,width=15,height=2,bg="NavajoWhite4",cursor="hand2",command=clearEntry)
    clearentrybutton.place(x=700,y=250)

    backbutton=Button(root,text="<< Back",width=15,bd=1,height=2,bg="NavajoWhite4",cursor="hand2",command=mainwindow)
    backbutton.place(x=450,y=250)

    billLabel=Label(root, text="Bill Preview", font="Arial 25",fg="gray25",bg="PeachPuff2")
    billLabel.place(x=600,y=340)

    billsTV.place(x=150,y=400)

    scrollBar = ttk.Scrollbar(root, orient="vertical",command=billsTV.yview)
    scrollBar.place(x=1150,y=400,height=330)

    billsTV.configure(yscrollcommand=scrollBar.set)
    
    billsTV["columns"]=("1","2","3","4")
    #billsTV['show']='headings'      //removes th 0th column
    
    billsTV.heading('#0',text="NO.")
    billsTV.heading('#1',text="ITEM NAME")
    billsTV.heading('#2',text="RATE")
    billsTV.heading('#3',text="QUANTITY")
    billsTV.heading('#4',text="COST")

    updateitembutton=Button(root,text="Update Item",bd=1,width=15,height=2,cursor="hand2",bg="NavajoWhite4",command=addupdateitem)
    updateitembutton.place(x=900,y=250)

def printbill():
    top=Toplevel()
    top.title("Save Bill")
    top.geometry("350x200+600+350")
    def createfile():
        amount=0
        costint=[]
        filename=addFileNameVar.get()
        fob=open(filename+'.txt','w+')
        fob.write('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        filedatetime=d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Bill Generator\t\t\t\t\t  %I:%M:%S %p")
        fob.write(filedatetime)
        fob.write('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n')
        fob.write('\t\t\tItemname\t\t\t'+'Rate\t\t'+'Quantity\t'+'\tAmount\n')
        for i in range(0,len(itemnamelist)):
            fob.write('\n\t\t\t{0}\t\t\t  {1}\t\t   {2}\t\t   {3}'.format(itemnamelist[i],ratelist[i],quantitylist[i],costlist[i]))
        for i in range(0,len(costlist)):
            new=float(costlist[i])
            costint.append(new)
            amount=amount+costint[i]
        fob.write('\n-----------------------------------------------------------------------------------------------------------------------')
        fob.write('\n\t\t\tTotal amount:\t\t\t\t\t\t   {0} Rs'.format(amount))
        fob.write('\n-----------------------------------------------------------------------------------------------------------------------')
        fob.close()
        
        messagebox.showinfo("Note","Your bill file is successfully saved in .txt format")
        top.deiconify()
        top.destroy()
        top.mainloop()
    
    L1=Label(top,text="Enter File name and press Enter",font=('Arial',14),fg="red")
    filename=Entry(top,textvariable=addFileNameVar, bd=5)
    button=Button(top,text="Enter",width=15,height=2,cursor="hand2",command=createfile)
    L1.pack()
    filename.pack()
    button.pack()
   

mainlogin()
# the root window handles the mouse click event
root.mainloop()
