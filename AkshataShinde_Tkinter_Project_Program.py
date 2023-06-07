#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Login Credentials for first page of Restaurant Management System =
    Enter Username : Akshata
    Enter Password : 12345 """

from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
def main():
    aks=Tk()
    app=LoginPage(aks)
    aks.mainloop()

class LoginPage:
    def __init__(self,aks):
        self.aks=aks
        self.aks.geometry("1350x750+0+0")
        self.aks.title("Restaurant Management System")

        self.title_label=Label(self.aks,text="Restaurant Management System",font=('arial',35,'bold'),bg="red",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        
        self.main_frame=Frame(self.aks,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=300,y=150,width=750,height=450)
        
        self.login_lbl=Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgrey",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        
        self.entry_frame=LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)
        
        self.entus_lbl=Label(self.entry_frame,text="Enter Username:",bg="lightpink",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        username=StringVar()
        password=StringVar()
        
        self.entus_ent=Entry(self.entry_frame,font=('sans-serif',15),textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.entpass_lbl=Label(self.entry_frame,text="Enter Password:",bg="lightpink",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.entpass_ent=Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)
        
        def check_login():
            '''This function will check login'''
            if username.get() == "Akshata" and password.get()=="12345":
                self.billing_button.config(state="normal")
            else:
                pass
        def reset():
            username.set("")
            password.set("")
            
        def billing_sect():
            self.newwindow=Toplevel(self.aks)
            self.app=window2(self.newwindow)
            
        def check_menu():
            self.newwindow=Toplevel(self.aks)
            self.app=window3(self.newwindow)
            
    
        
        
        self.button_frame=LabelFrame(self.entry_frame,text="options",font=('Arial',15),bg="lightblue",bd=1,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=720,height=70)
        
        self.login_button=Button(self.button_frame,text="Login",font=('Arial',12),bd=5,width=12,command=check_login)
        self.login_button.grid(row=0,column=0,padx=20,pady=2)
        
        self.billing_button=Button(self.button_frame,text="Billing",font=('Arial',15),bd=5,width=12,command=billing_sect)
        self.billing_button.grid(row=0,column=1,padx=20,pady=2)
        self.billing_button.config(state="disabled")
        
        self.menu_button=Button(self.button_frame,text="Menu Card",font=('Arial',12),bd=5,width=12,command=check_menu)
        self.menu_button.grid(row=0,column=2,padx=20,pady=2)
        
        self.reset_button=Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=12,command=reset)
        self.reset_button.grid(row=0,column=3,padx=20,pady=2)
        
        
class window2:
    def __init__(self,aks):
        self.aks=aks
        self.aks.geometry("1350x750+0+0")
        self.aks.title("Restaurant Management System")
        
        self.title_label=Label(self.aks,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgreen",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        
        bill_no=random.randint(100,1000)
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)
        
        calc_var=StringVar()
        
        cust_nm=StringVar()
        cust_cot=StringVar()
        date_pr=StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()
        
        date_pr.set(datetime.now())
        
        total_list=[]
        self.grd_total=0
        
        
        
        self.entry_frame=LabelFrame(self.aks,text="Enter Details",background="lightpink",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=100,width=500,height=650)
        
        self.bill_no_lbl=Label(self.entry_frame,text="Bill Number",font=('Arial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        self.bill_no_ent=Entry(self.entry_frame,bd=5,textvariable=bill_no_tk,font=('Arial',15))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")
        
        self.date_lbl=Label(self.entry_frame,text="Date",font=('Arial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.date_ent=Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Item Purchased",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        
        self.item_pur_ent=Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)
        
        self.item_qty_lbl=Label(self.entry_frame,text="Item Quantity",font=('Arial',15),bg="lightgrey")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_qty_ent=Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)
        
        self.cone_lbl=Label(self.entry_frame,text="Cost of one",font=('Arial',15),bg="lightgrey")
        self.cone_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        self.cone_ent=Entry(self.entry_frame,bd=5,textvariable=cone,font=('Arial',15))
        self.cone_ent.grid(row=6,column=1,padx=2,pady=2)
        
        
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tPurna Restaurant")
            self.bill_txt.insert(END,"\n\t\t\tNational Highway,Near Bus Stop,Thane")
            self.bill_txt.insert(END,"\n\t\t\t\tContact-1012013400")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,f"\nBill number {bill_no_tk.get()}")
            
        def genbill():
            self.bill_txt.insert(END,f"\nCost Of Item: {cone.get()}")
            self.bill_txt.insert(END,f"\nItem Purchased :{item_pur.get()}")
            self.bill_txt.insert(END,f"\nItem Quantity :{item_qty.get()}")
            self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,"\nProduct Name\t\t     Quantity\t\t     Per Cost\t\t     Total")
            
        def clear_func():
            cone.set("")
            item_pur.set("")
            item_qty.set("")
            date_pr.set("")
            
        def reset_func():
            total_list.clear()
            self.grd_total=0
            self.bill_txt.delete("1.0",END)
            default_bill()
            
        def add_func():
            qty=int(item_qty.get())
            cones=int(cone.get())
            total=qty*cones
            total_list.append(total)
            self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t       {item_qty.get()}\t\t       Rs.{cone.get()}\t\t       Rs.{total}")
            
        def total_func():
            for item in total_list:
                self.grd_total=self.grd_total + item
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\tGrand Total : {self.grd_total}")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.save_btn.config(state="normal")
            
        def save_func():
            user_choice=messagebox.askyesno("Confirm?",f"Do you want to save the bill {bill_no_tk.get()}",parent=self.aks)
            if user_choice > 0:
                self.bill_content=self.bill_txt.get("1.0",END)
                try:
                    con=open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}",parent=self.aks)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Successful!",f"Bill{bill_no_tk.get()}has been saved successfully!",parent=self.aks)
            else:
                return
            
        self.button_frame=LabelFrame(self.entry_frame,bd=5,text="options",bg="lightgreen",font=("Arial",15))
        self.button_frame.place(x=20,y=200,width=360,height=350)
        
        self.add_btn=Button(self.button_frame,bd=4,text="ADD",font=("Arial",12),width=10,height=5,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        
        self.generate_btn=Button(self.button_frame,bd=4,text="GENERATE",font=("Arial",12),width=10,height=5,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)
        
        self.clear_btn=Button(self.button_frame,bd=4,text="CLEAR",font=("Arial",12),width=10,height=5,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)
        
        self.total_btn=Button(self.button_frame,bd=4,text="TOTAL",font=("Arial",12),width=10,height=5,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)
        
        self.save_btn=Button(self.button_frame,bd=4,text="SAVE",font=("Arial",12),width=10,height=5,command=save_func)
        self.save_btn.grid(row=1,column=1,padx=4,pady=2)
        
        self.reset_btn=Button(self.button_frame,bd=4,text="RESET",font=("Arial",12),width=10,height=5,command=reset_func)
        self.reset_btn.grid(row=1,column=2,padx=4,pady=2)
        
        
        #======Calculator Frame=====#
        self.calc_frame=Frame(self.aks,bd=3,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=570,y=120,width=720,height=320)
        
        self.txtDisplay=Entry(self.calc_frame,font=('sans-serif',16),textvariable=calc_var,bd=20,bg="lightgrey",insertwidth=4,justify="right",width=47)
        self.txtDisplay.grid(row=0,column=0,padx=2,columnspan=5)
        

        self.num_ent=Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('Arial',15),width=60,justify="right")
        self.num_ent.grid(row=0,column=0,columnspan=15)
        
        def press_btn(event):
            text=event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value=int(calc_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "AC":
                pass
            elif text == "DEL":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()
        
        self.btn1=Button(self.calc_frame,bg="lightgrey",text="1",bd=12,width=10,height=1,font=('Arial',15))
        self.btn1.grid(row=1,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>",press_btn)
        
        self.btn2=Button(self.calc_frame,bg="lightgrey",text="2",bd=12,width=10,height=1,font=('Arial',15))
        self.btn2.grid(row=1,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>",press_btn)
        
        self.btn3=Button(self.calc_frame,bg="lightgrey",text="3",bd=12,width=10,height=1,font=('Arial',15))
        self.btn3.grid(row=1,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>",press_btn)
        
        self.btn4=Button(self.calc_frame,bg="lightgrey",text="4",bd=12,width=10,height=1,font=('Arial',15))
        self.btn4.grid(row=1,column=3,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)
        
        self.btn5=Button(self.calc_frame,bg="lightgrey",text="5",bd=12,width=10,height=1,font=('Arial',15))
        self.btn5.grid(row=1,column=4,padx=2,pady=2)
        self.btn5.bind("<Button-1>",press_btn)
        
        self.btn6=Button(self.calc_frame,bg="lightgrey",text="6",bd=12,width=10,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=0,padx=2,pady=2)
        self.btn6.bind("<Button-1>",press_btn)
        
        self.btn7=Button(self.calc_frame,bg="lightgrey",text="7",bd=12,width=10,height=1,font=('Arial',15))
        self.btn7.grid(row=2,column=1,padx=2,pady=2)
        self.btn7.bind("<Button-1>",press_btn)
        
        self.btn8=Button(self.calc_frame,bg="lightgrey",text="8",bd=12,width=10,height=1,font=('Arial',15))
        self.btn8.grid(row=2,column=2,padx=2,pady=2)
        self.btn8.bind("<Button-1>",press_btn)
        
        self.btn9=Button(self.calc_frame,bg="lightgrey",text="9",bd=12,width=10,height=1,font=('Arial',15))
        self.btn9.grid(row=2,column=3,padx=2,pady=2)
        self.btn9.bind("<Button-1>",press_btn)
        
        self.btn10=Button(self.calc_frame,bg="lightgrey",text="0",bd=12,width=10,height=1,font=('Arial',15))
        self.btn10.grid(row=2,column=4,padx=2,pady=2)
        self.btn10.bind("<Button-1>",press_btn)
        
        self.btn11=Button(self.calc_frame,bg="lightgrey",text="+",bd=12,width=10,height=1,font=('Arial',15))
        self.btn11.grid(row=3,column=0,padx=2,pady=2)
        self.btn11.bind("<Button-1>",press_btn)
        
        self.btn12=Button(self.calc_frame,bg="lightgrey",text="-",bd=12,width=10,height=1,font=('Arial',15))
        self.btn12.grid(row=3,column=1,padx=2,pady=2)
        self.btn12.bind("<Button-1>",press_btn)
        
        self.btn13=Button(self.calc_frame,bg="lightgrey",text="*",bd=12,width=10,height=1,font=('Arial',15))
        self.btn13.grid(row=3,column=2,padx=2,pady=2)
        self.btn13.bind("<Button-1>",press_btn)
        
        self.btn14=Button(self.calc_frame,bg="lightgrey",text="/",bd=12,width=10,height=1,font=('Arial',15))
        self.btn14.grid(row=3,column=3,padx=2,pady=2)
        self.btn14.bind("<Button-1>",press_btn)
        
        self.btn15=Button(self.calc_frame,bg="lightgrey",text=".",bd=12,width=10,height=1,font=('Arial',15))
        self.btn15.grid(row=3,column=4,padx=2,pady=2)
        self.btn15.bind("<Button-1>",press_btn)
        
        self.btn16=Button(self.calc_frame,bg="lightgrey",text="AC",bd=12,width=10,height=1,font=('Arial',15))
        self.btn16.grid(row=4,column=1,padx=2,pady=2)
        self.btn16.bind("<Button-1>",press_btn)
        
        self.btn17=Button(self.calc_frame,bg="lightgrey",text="=",bd=12,width=10,height=1,font=('Arial',15))
        self.btn17.grid(row=4,column=2,padx=2,pady=2)
        self.btn17.bind("<Button-1>",press_btn)
        
        self.btn18=Button(self.calc_frame,bg="lightgrey",text="DEL",bd=12,width=10,height=1,font=('Arial',15))
        self.btn18.grid(row=4,column=3,padx=2,pady=2)
        self.btn18.bind("<Button-1>",press_btn)
        
        # ========Bill Frame ======= #
        
        self.bill_frame=LabelFrame(self.aks,text="Bill Area",font=("Arial",18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=580,y=450,width=700,height=300)
        
        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)
        
        default_bill()
        
        
class window3:
    def __init__(self,aks):
        self.aks=aks
        self.aks.geometry("1350x750+0+0")
        self.aks.title("Restaurant Management System")  
        
        
        self.title_label=Label(self.aks,text="Menu Card",font=('Arial',35,'bold'),bg="red",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.entry_frame=LabelFrame(self.aks,text="Starters",background="lightpink",font=('Arial',20),bd=5,relief=GROOVE)
        self.entry_frame.place(x=50,y=100,width=400,height=650)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Fried Papad",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=1,column=0,padx=4,pady=3)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Masala Papad",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=2,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Paneer Chilli",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Paneer 65",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Soyabeen Chilli",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken Chilli",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken 65",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=7,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken Lolipop",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=8,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Pizza",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=9,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Sandwich",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=10,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Burger",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=11,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="French Fries",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=12,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Noodles",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=13,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Maggie",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=14,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Veg Salad",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=15,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken Soup",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=16,column=0,padx=2,pady=2)
        
        
        
        self.entry_frame=LabelFrame(self.aks,text="Main Course",background="lightpink",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=530,y=100,width=400,height=650)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Daal Fry",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=1,column=0,padx=4,pady=3)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Daal Tadka",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=2,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Paneer Masala",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Paneer Tikka",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Paneer Hyderabadi",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Palak Paneer",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Paneer Bhurji",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=7,column=0,padx=2,pady=2)
    
        self.item_pur_lbl=Label(self.entry_frame,text="Veg Fry",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=8,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Veg Thali",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=9,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken Masala",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=10,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Kadhai Chicken",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=11,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Butter Chicken",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=12,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken Rada Masala",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=13,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Fish Masala",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=14,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chicken Biryani",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=15,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Mutton Biryani",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=16,column=0,padx=2,pady=2)
        
        
        
        self.entry_frame=LabelFrame(self.aks,text="Deserts",background="lightpink",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=1000,y=100,width=400,height=650)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Lassi",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=1,column=0,padx=4,pady=3)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Mango Lassi",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=2,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Strawberry Lassi",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Masala Milk",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Badam Shake",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Mango Juice",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Pineapple Juice",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=7,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Apple Juice",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=8,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chickoo Juice",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=9,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Orange Juice",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=10,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Mix Juice",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=11,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Cold Coffee",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=12,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Tea",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=13,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Vanila Ice Cream",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=14,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Butter Scotch Ice Cream",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=15,column=0,padx=2,pady=2)
        
        self.item_pur_lbl=Label(self.entry_frame,text="Chocolate Ice-Cream",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=16,column=0,padx=2,pady=2)
        
        
        

if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:




