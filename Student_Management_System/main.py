
from tkinter import *
from tkinter import ttk
from click.decorators import command
import pymysql





class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        title = Label(self.root,text = "Student Management System",bd=10,relief=GROOVE,font = ("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        
        
        


        
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.regstatus_var=StringVar()
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        


       
        
        
        
        
        

  
     
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=590)
        
        
        m_title = Label(Manage_Frame,text="Manage Students",bg="yellow",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
 


      
        
        lbl_id = Label(Manage_Frame,text="Student ID",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        
        txt_id = Entry(Manage_Frame,textvariable=self.id_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        
        


 

        
        lbl_name = Label(Manage_Frame,text="Name",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        
        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")




   
        
        
        lbl_Email = Label(Manage_Frame,text="Email",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        
        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
         
        
        




          
        lbl_Gender = Label(Manage_Frame,text="Gender",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        
        
        
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=25,pady=15)
        

         
        




         
        lbl_Contact = Label(Manage_Frame,text="Contact",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        
        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")


         
        
  

        
        lbl_Regstatus = Label(Manage_Frame,text="Reg.Status",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Regstatus.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        
      
        
        
        combo_regstatus=ttk.Combobox(Manage_Frame,textvariable=self.regstatus_var,font=("times new roman",13,"bold"),state='readonly')
        combo_regstatus['values']=("Pending","Partialy Complete","Complete")
        combo_regstatus.grid(row=6,column=1,padx=25,pady=15)
        

 



        
        lbl_Address = Label(Manage_Frame,text="Address",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        
        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        


     
     
        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=15,y=520,width=410)
        
        
        Addbtn = Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=15)
        updatebtn = Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=15)
        deletebtn = Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=15)
        Clearbtn = Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=15)
        
 
 




         
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Detail_Frame.place(x=500,y=100,width=830,height=590)
        
        
        
        lbl_search = Label(Detail_Frame,text="Search By",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
       
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=12,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("id","name","contact")
        combo_search.grid(row=0,column=1,padx=25,pady=15)
        
        
        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        
        
        searchbtn = Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=15)
        showallbtn = Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=15)




       


        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=800,height=500)
        
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
        
        self.Student_table=ttk.Treeview(Table_Frame,columns=("id","name","email","gender","contact","reg.status","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        
        self.Student_table.heading("id",text="Student ID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("reg.status",text="Reg.Status")
        self.Student_table.heading("Address",text="Address")
        
        
        self.Student_table['show']='headings'
        
        
        self.Student_table.column("id",width=110)
        self.Student_table.column("name",width=110)
        self.Student_table.column("email",width=110)
        self.Student_table.column("gender",width=110)
        self.Student_table.column("contact",width=110)
        self.Student_table.column("reg.status",width=110)
        self.Student_table.column("Address",width=110)
        
        
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        self.fetch_data()




    
    def add_students(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.id_var.get(),
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.regstatus_var.get(),
                    self.txt_Address.get('1.0',END)
            ))
            
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            




           
            
    def fetch_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("Select * from students")
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert('',END,values=row)
                    con.commit()
            con.close()
     


 
   
     
     
    def clear(self):
            self.id_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.regstatus_var.set("")
            self.txt_Address.delete("1.0",END)
            
            
            
  

          
            
            
    def get_cursor(self,ev):
            cursor_row=self.Student_table.focus()
            contents=self.Student_table.item(cursor_row)
            row=contents['values']
            
            self.id_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.regstatus_var.set(row[5])
            self.txt_Address.delete("1.0",END)
            self.txt_Address.insert(END,row[6])
            
            



           
            
            
    def update_data(self): 
             con=pymysql.connect(host="localhost",user="root",password="",database="sms")
             cur=con.cursor()
             cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,regstatus=%s,address=%s where id=%s",(
                                                self.name_var.get(),
                                                self.email_var.get(),
                                                self.gender_var.get(),
                                                self.contact_var.get(),
                                                self.regstatus_var.get(),
                                                self.txt_Address.get('1.0',END),
                                                self.id_var.get()
             ))
            
             con.commit()
             self.fetch_data()
             self.clear()
             con.close()
             
             
             
           
             
             
             
    def delete_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("delete from students where id=%s",self.id_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()  
 
 
 

            
            
            
    def search_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            
            cur.execute("select * from students where"+str(self.search_by.get())+" 'LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert('',END,values=row)
                    con.commit()
            con.close()                          
                                             

           
            
            
            
    
root = Tk()
ob = Student(root)
root.mainloop()    
    
    
    
    