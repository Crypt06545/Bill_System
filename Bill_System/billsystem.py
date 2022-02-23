#Give me credit if you copy me###
##########IMPORTS#######
from tkinter import*
import math,random,os
from tkinter import messagebox

# Newfolder='bills'
# os.mkdir(Newfolder)

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software Develop | By MEHADI")
        bg_olor="#002cbf"
        title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg=bg_olor,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #======variables==========#
        #========🎭Cosmetic👩‍🦰==========#
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

        #========🧂Grocery🥚============#
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
               
        #==========🧃Cold Drinks🧃=========#
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limcha=IntVar()
        self.sprite=IntVar()

        #==========Total Product Price💲💲 & Tax Variables===========#
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        
        #=========Tax============#
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #===========Customer================3
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1,99999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
  
        #===============Customer Detail Frame Frame==================#
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_olor)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_olor,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",bg=bg_olor,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_olor,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        
        #=======Cosmetics🎭 Frame==================#
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_olor)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face cream",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        
        #=======Grocery Frame==================#
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_olor)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Dall",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        
        
        #=======Cold Drinks Frame==================#
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_olor)
        F4.place(x=670,y=180,width=325,height=380)

        C1_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        C1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        C2_lbl=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        C2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        C3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        C3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        C4_lbl=Label(F4,text="Thumbs up",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        C4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        C5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        C5_txt=Entry(F4,width=10,textvariable=self.limcha,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        C6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_olor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        C6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        #=========Bill Area==============#
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=335,height=380)
        bill_title=Label(F5,text="Name Of Your Resturent",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



        #==========Button Frame=========#
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_olor)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_olor,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=1,sticky=W)
        m1=Entry(F6,width=15,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Grocery",bg=bg_olor,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=1,sticky=W)
        m2=Entry(F6,width=15,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Cold Drinks",bg=bg_olor,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=1,sticky=W)
        m3=Entry(F6,width=15,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1=Label(F6,text="Cosmetic Tax",bg=bg_olor,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=1,sticky=W)
        c1=Entry(F6,width=15,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Grocery Tax",bg=bg_olor,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=1,sticky=W)
        c2=Entry(F6,width=15,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Cold Drinks Tax",bg=bg_olor,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=1,sticky=W)
        c3=Entry(F6,width=15,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)


        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,bd=2,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,bd=2,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,bd=2,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,bd=2,width=10 ,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        #===============cosmetic🎭 pricrs==============#
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180
                
        self.total_cosmetic_price=float(
                                  self.c_s_p+
                                  self.c_fc_p+
                                  self.c_fw_p+
                                  self.c_hs_p+
                                  self.c_hg_p+
                                  self.c_bl_p
                                  )
                                  
        self.cosmetic_price.set("Tk "+str(self.total_cosmetic_price))
        self.c_tax=(self.total_cosmetic_price*0.02)
        self.cosmetic_tax.set("Tk "+str(self.c_tax))
        



        #===============Grocery🥚 pricrs==============#
        self.g_r_p=self.rice.get()*65
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*65
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*85
        self.g_t_p=self.tea.get()*60

        self.total_grocery_price=float(
                                  self.g_r_p+
                                  self.g_f_p+
                                  self.g_d_p+
                                  self.g_w_p+
                                  self.g_s_p+
                                  self.g_t_p
                                  )
        self.grocery_price.set("Tk "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Tk "+str(self.g_tax))



        #===============cold Drinks🧃 pricrs==============#
        self.d_m_p=self.maza.get()*60
        self.d_c_p=self.cock.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_t_p=self.thumbsup.get()*45
        self.d_l_p=self.limcha.get()*40
        self.d_s_p=self.sprite.get()*60

        self.total_drinks_price=float(
                                  self.d_m_p+
                                  self.d_c_p+
                                  self.d_f_p+
                                  self.d_t_p+
                                  self.d_l_p+
                                  self.d_s_p
                                  )
        self.cold_drink_price.set("Tk "+str(self.total_drinks_price))
        self.c_d_tax=round((self.total_drinks_price*0.5),2)
        self.cold_drink_tax.set("Tk "+str(self.c_d_tax))
        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_drinks_price+
                                self.c_tax+
                                self.g_tax+
                                self.c_d_tax
                              )
        

    #=============Welcome Screen================#
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome Your Resturent\n")
        self.textarea.insert(END,f"\n Bill Number    : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Coustomer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Numbe    : {self.c_phone.get()}")
        self.textarea.insert(END,f"\n====================================")
        self.textarea.insert(END,f"\nProducts\t\tQTY\tPrice")
        self.textarea.insert(END,f"\n====================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")

        else: 
            self.welcome_bill()    
            #===================Cosmetics==================#
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")


            #===================Grocery🥚==================#
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Dall\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n SUgar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")


            #===================Cold Drinks🧃==================#
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limcha.get()!=0:
                self.textarea.insert(END,f"\n Limcha\t\t{self.limcha.get()}\t\t{self.d_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            #=====================Tax Bar============#
            self.textarea.insert(END,f"\n------------------------------------")
            if self.cosmetic_tax.get()!="Tk. 0.0":
                self.textarea.insert(END,f"\n Cosmetics Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Tk. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            
            if self.cold_drink_tax.get()!="Tk. 0.0":
                self.textarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")
                self.textarea.insert(END,f"\n Total Bill: \t\t\t{self.Total_bill}")
            self.textarea.insert(END,f"\n------------------------------------")
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        
        if op>0:
            self.bill_data=self.textarea.get("1.0" ,END )
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} Saved Succesfully")
        
        else:
            return

    def find_bill(self):
        present="no"
        for find in os.listdir("Bills/"):
            if find.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{find}","r")
                self.textarea.delete("1.0",END)
                for i in f1:
                    self.textarea.insert(END,i)                
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invaild bill no. ")
    
    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you Really Want To Clear Data?")
        if op>0:
            #========Cosmetic👩‍🦰🎭==========#
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            #========Grocery🥚============#
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #==========Cold Drinks🧃=========#
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limcha.set(0)
            self.sprite.set(0)
            #==========Total Product Price & Tax Variables===========#
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            #=========Tax============#
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #===========Customer================3
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1,99999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you wany to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
# img=PhotoImage(file='D:\\bill project\\tt.png')#####This is for my file path
img=PhotoImage(file='\\Bill_system\\tt.png')
root.iconphoto(False,img)
obj = Bill_App(root)
root.mainloop()