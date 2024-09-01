from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="blue")
        self.root.title("Daffodil CaNnteen Billing System")
        title=Label(self.root,text="Daffodil Canteen Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="light blue",fg="black").pack(fill=X)
        #===================================variables=======================================================================================
        #############################Snacks Variable##################
        self.Cookies=IntVar()
        self.laddu=IntVar()
        self.chips=IntVar()
        self.candy=IntVar()
        self.ice=IntVar()
        self.silk=IntVar()
        self.licchi=IntVar()
        ##################################Drinks Variable##################
        self.sevenup=IntVar()
        self.mojo=IntVar()
        self.tiger=IntVar()
        self.clemon=IntVar()
        self.fanta=IntVar()
        self.jeera=IntVar()
        self.gear=IntVar()
        ###################Beauti Variables#######################
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
        #######################Total Variable#####################
        self.total_sna=StringVar()
        self.total_drinks=StringVar()
        self.total_beauti=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer Snacks label frame=================================================
        Snacks=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="light blue",fg="black",relief=RAISED,bd=10)
        Snacks.place(x=0,y=80,relwidth=1)
        cust_name=Label(Snacks,text="Customer Name",font=("Arial Black",14),bg="light blue",fg="black").grid(row=0,column=0,padx=15)
        
        cust_entry=Entry(Snacks,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(Snacks,text="Contact No.",font=("Arial Black",14),bg="light blue",fg="black").grid(row=0,column=2,padx=10)
        
        contact_entry=Entry(Snacks,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(Snacks,text="Bill No.",font=("Arial Black",14),bg="light blue",fg="black").grid(row=0,column=4,padx=10)
        
        bill_entry=Entry(Snacks,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Snacks Item=================================================================
        Snacks=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),bg="light blue",fg="black",relief=RAISED,bd=10)
        Snacks.place(x=5,y=180,height=380,width=325)
        
        item1=Label(Snacks,text="Cookies",font=("Arial Black",11),bg="light blue",fg="black").grid(row=0,column=0,pady=11)
        item1_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.Cookies).grid(row=0,column=1,padx=10)

        item2=Label(Snacks,text="Laddu(Per piece)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=1,column=0,pady=11)
        item2_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.laddu).grid(row=1,column=1,padx=10)

        item3=Label(Snacks,text="Chips(1pckt))",font=("Arial Black",11),bg="light blue",fg="black").grid(row=2,column=0,pady=11)
        item3_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.chips).grid(row=2,column=1,padx=10)

        item4=Label(Snacks,text="Ice Cream",font=("Arial Black",11),bg="light blue",fg="black").grid(row=3,column=0,pady=11)
        item4_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.candy).grid(row=3,column=1,padx=10)

        item5=Label(Snacks,text="Chocolate Candy",font=("Arial Black",11),bg="light blue",fg="black").grid(row=4,column=0,pady=11)
        item5_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.ice).grid(row=4,column=1,padx=10)

        item6=Label(Snacks,text="Dairy Milk Silk",font=("Arial Black",11),bg="light blue",fg="black").grid(row=5,column=0,pady=11)
        item6_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=10)

        item7=Label(Snacks,text="Licchi(Per piece)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=6,column=0,pady=11)
        item7_entry=Entry(Snacks,borderwidth=2,width=15,textvariable=self.licchi).grid(row=6,column=1,padx=10)
        #===================================Drinks Item=====================================================================================
        drinks=LabelFrame(self.root,text="Drinks",font=("Arial Black",12),relief=RAISED,bd=10,bg="light blue",fg="black")
        drinks.place(x=340,y=180,height=380,width=325)

        item8=Label(drinks,text="Seven UP(1ltr)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=0,column=0,pady=11)
        item8_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.sevenup).grid(row=0,column=1,padx=10)

        item9=Label(drinks,text="MOJO(250ml)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=1,column=0,pady=11)
        item9_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.mojo).grid(row=1,column=1,padx=10)

        item10=Label(drinks,text="Tiger(250ml)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=2,column=0,pady=11)
        item10_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.tiger).grid(row=2,column=1,padx=10)

        item11=Label(drinks,text="Clemon(500ml)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=3,column=0,pady=11)
        item11_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.clemon).grid(row=3,column=1,padx=10)

        item12=Label(drinks,text="Fanta(1ltr)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=4,column=0,pady=11)
        item12_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.fanta).grid(row=4,column=1,padx=10)

        item13=Label(drinks,text="Jeera Pani(500ml)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=5,column=0,pady=11)
        item13_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.jeera).grid(row=5,column=1,padx=10)

        item14=Label(drinks,text="Gear UP(500ml)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=6,column=0,pady=11)
        item14_entry=Entry(drinks,borderwidth=2,width=15,textvariable=self.gear).grid(row=6,column=1,padx=10)
        #========================================Beauty Item===============================================================================
        beauti=LabelFrame(self.root,text="Beauty",font=("Arial Black",12),relief=RAISED,bd=10,bg="light blue",fg="black")
        beauti.place(x=677,y=180,height=380,width=325)

        item15=Label(beauti,text="Bathing Soap",font=("Arial Black",11),bg="light blue",fg="black").grid(row=0,column=0,pady=11)
        item15_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.soap).grid(row=0,column=1,padx=10)

        item16=Label(beauti,text="Shampoo(1ltr)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=1,column=0,pady=11)
        item16_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.shampoo).grid(row=1,column=1,padx=10)

        item17=Label(beauti,text="Body Lotion(1ltr)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=2,column=0,pady=11)
        item17_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.lotion).grid(row=2,column=1,padx=10)

        item18=Label(beauti,text="Face Cream",font=("Arial Black",11),bg="light blue",fg="black").grid(row=3,column=0,pady=11)
        item18_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.cream).grid(row=3,column=1,padx=10)

        item19=Label(beauti,text="Shaving Foam",font=("Arial Black",11),bg="light blue",fg="black").grid(row=4,column=0,pady=11)
        item19_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.foam).grid(row=4,column=1,padx=10)

        item20=Label(beauti,text="Face Mask(1piece)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=5,column=0,pady=11)
        item20_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.mask).grid(row=5,column=1,padx=10)

        item21=Label(beauti,text="Hand Sanitizer(50ml)",font=("Arial Black",11),bg="light blue",fg="black").grid(row=6,column=0,pady=11)
        item21_entry=Entry(beauti,borderwidth=2,width=15,textvariable=self.sanitizer).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=RAISED,bg="light blue")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=RAISED,bg="light blue",fg="black").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=RAISED,bd=10,bg="light blue",fg="black")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_Snacks=Label(billing_menu,text="Total Snacks total",font=("Arial Black",11),bg="light blue",fg="black").grid(row=0,column=0)
        total_Snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)
        
        total_drinks=Label(billing_menu,text="Total drinks total",font=("Arial Black",11),bg="light blue",fg="black").grid(row=1,column=0)
        total_drinks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_drinks).grid(row=1,column=1,padx=10,pady=7)

        
        total_beauti=Label(billing_menu,text="Total Beauty",font=("Arial Black",11),bg="light blue",fg="black").grid(row=2,column=0)
        total_beauti_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_beauti).grid(row=2,column=1,padx=10,pady=7)

        tax_Snacks=Label(billing_menu,text="Snacks Tax",font=("Arial Black",11),bg="light blue",fg="black").grid(row=0,column=2)
        tax_Snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
        
        tax_drinks=Label(billing_menu,text="Drinks Tax",font=("Arial Black",11),bg="light blue",fg="black").grid(row=1,column=2)
        tax_drinks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)

        
        tax_beauti=Label(billing_menu,text="Beauty Tax",font=("Arial Black",11),bg="light blue",fg="black").grid(row=2,column=2)
        tax_beauti_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=RAISED,bg="white")
        button_frame.place(x=830,width=500,height=95)
        
        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="light blue",fg="black",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="light blue",fg="black",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="light blue",fg="black",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.co=self.Cookies.get()*120
    self.la=self.laddu.get()*5
    self.ch=self.chips.get()*15
    self.ca=self.candy.get()*20
    self.ic=self.ice.get()*30
    self.si=self.silk.get()*60
    self.li=self.licchi.get()*5
    total_Snacks_total=(
                self.co+
                self.la+
                self.ch+
                self.ca+
                self.ic+
                self.si+
                self.li)          
    self.total_sna.set(str(total_Snacks_total)+" TK")
    self.a.set(str(round(total_Snacks_total*0.05,3))+" TK")

    self.se=self.sevenup.get()*60
    self.mj=self.mojo.get()*30
    self.cl=self.clemon.get()*35
    self.ti=self.tiger.get()*25
    self.fa=self.fanta.get()*60
    self.ge=self.gear.get()*30
    self.je=self.jeera.get()*20
    total_drinks_total=(
        self.se+
        self.mj+
        self.cl+
        self.ti+
        self.fa+
        self.ge+
        self.je)
        
    self.total_drinks.set(str(total_drinks_total)+" TK")
    self.b.set(str(round(total_drinks_total*0.01,3))+" TK")

    self.so=self.soap.get()*30
    self.sh=self.shampoo.get()*180
    self.cr=self.cream.get()*130
    self.lo=self.lotion.get()*500
    self.fo=self.foam.get()*85
    self.ma=self.mask.get()*100
    self.sa=self.sanitizer.get()*20
    
    total_beauti_total=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)
        
    self.total_beauti.set(str(total_beauti_total)+" TK")
    self.c.set(str(round(total_beauti_total*0.10,3))+" TK")
    self.total_all_bill=(total_Snacks_total+
                total_drinks_total+
                total_beauti_total+
                (round(total_drinks_total*0.01,3))+
                (round(total_beauti_total*0.10,3))+
                (round(total_Snacks_total*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" TK"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO Daffodil Canteen")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\ttotal\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.Cookies.get()!=0:
        self.txtarea.insert(END,f"Cookies\t\t {self.Cookies.get()}\t{self.co}\n")
    if self.laddu.get()!=0:
        self.txtarea.insert(END,f"Laddu\t\t {self.laddu.get()}\t{self.la}\n")
    if self.chips.get()!=0:
        self.txtarea.insert(END,f"Chips\t\t {self.chips.get()}\t{self.ch}\n")
    if self.candy.get()!=0:
        self.txtarea.insert(END,f"Candy\t\t {self.candy.get()}\t{self.ca}\n")
    if self.ice.get()!=0:
        self.txtarea.insert(END,f"Ice CReam\t\t {self.ice.get()}\t{self.ic}\n")
    if self.silk.get()!=0:
        self.txtarea.insert(END,f"Dairy MilkSilk\t\t {self.silk.get()}\t{self.si}\n")
    if self.licchi.get()!=0:
        self.txtarea.insert(END,f"Licchi\t\t {self.licchi.get()}\t{self.li}\n")
    if self.sevenup.get()!=0:
        self.txtarea.insert(END,f"Sevenup\t\t {self.sevenup.get()}\t{self.se}\n")
    if self.mojo.get()!=0:
        self.txtarea.insert(END,f"Mojo\t\t {self.mojo.get()}\t{self.mj}\n")
    if self.tiger.get()!=0:
        self.txtarea.insert(END,f"Tiger\t\t {self.tiger.get()}\t{self.ti}\n")
    if self.clemon.get()!=0:
        self.txtarea.insert(END,f"Clemon\t\t {self.clemon.get()}\t{self.cl}\n")
    if self.fanta.get()!=0:
        self.txtarea.insert(END,f"Fanta\t\t {self.fanta.get()}\t{self.fa}\n")
    if self.jeera.get()!=0:
        self.txtarea.insert(END,f"Jeera Pani\t\t {self.jeera.get()}\t{self.je}\n")
    if self.gear.get()!=0:
        self.txtarea.insert(END,f"Gear UP\t\t {self.gear.get()}\t{self.ge}\n")
    if self.soap.get()!=0:
        self.txtarea.insert(END,f"Bath Soap\t\t {self.soap.get()}\t{self.so}\n")
    if self.shampoo.get()!=0:
        self.txtarea.insert(END,f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get()!=0:
        self.txtarea.insert(END,f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
    if self.cream.get()!=0:
        self.txtarea.insert(END,f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
    if self.foam.get()!=0:
        self.txtarea.insert(END,f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
    if self.mask.get()!=0:
        self.txtarea.insert(END,f"Face icesk\t\t {self.mask.get()}\t{self.ma}\n")
    if self.sanitizer.get()!=0:
        self.txtarea.insert(END,f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")
        
    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 TK":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 TK":
        self.txtarea.insert(END,f"Total drinks Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 TK":
        self.txtarea.insert(END,f"Total Beauty Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.Cookies.set(0)
        self.laddu.set(0)
        self.chips.set(0)
        self.candy.set(0)
        self.ice.set(0)
        self.silk.set(0)
        self.licchi.set(0)
        self.sevenup.set(0)
        self.mojo.set(0)
        self.tiger.set(0)
        self.clemon.set(0)
        self.fanta.set(0)
        self.jeera.set(0)
        self.gear.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)
        self.total_sna.set(0)
        self.total_drinks.set(0)
        self.total_beauti.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()
            
root=Tk()
obj=Bill_App(root)
root.mainloop()
    
