from tkinter import*
from tkinter import messagebox
from time import localtime,strftime

def transaction(accnt):
    display=Tk()
    display.geometry("900x900")
    display.title("Transaction History")
    display.configure(bg="orange")
    l1=Label(display,text=' LIVEWIRE BANKING SYSTEM',font=('arial',50),bg="black",fg="red",width=2000)
    l1.config(font=("courier","50","bold"))
    l1.pack(side="top")
    l2=Label(display,text="YOUR TRANSACTION HISTORY",padx=50,pady=20,width=500,fg="black",font=('arial',22),bg="lightblue")
    l2.pack(side="top")
    frec=open(accnt+"-rec.txt",'r')
    for line in frec:
        l3=Label(display,text=line,width=2000)
        l3.pack(side="top")
    bt1=Button(display,text="Quit",command=display.destroy)
    bt1.pack(side="top")
    frec.close()

def check_bal(accnt):
    fdet=open(accnt+".txt",'r')
    fdet.readline()
    bal=fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance",f'Your Account Balance is:{bal}')
    return


def deb_write(master,amt,accnt,name):
    if(is_number(amt)==0):
        messagebow.showinfo("Error","invalid debits\n Please try again.")
        master.destroy()
        return
    fdet=open(accnt+".txt","r")
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    

    if(int(amt)>camt):
        messagebox.showinfo("Error!!","You dont have enough balance")
    else:
        #amti=int(amt)
        cb=camt-int(amt)

        fdet=open(accnt +".txt","w")
        fdet.write(pin)
        fdet.write(str(cb)+"\n")
        fdet.write(accnt +"\n")
        fdet.write(name +"\n")
        fdet.close()

        frec=open(str(accnt)+"-rec.txt",'a+')
        frec.write(str(strftime("[%Y-%m-%d][%H:%M:%S]",localtime()))+"       " +amt+"       "+str(cb)+"\n")
        frec.close()

        messagebox.showinfo("operation Successfull!!","Amount debited Successfully\n")
        master.destroy()
    return
    
def crdt_write(master,amt,accnt,name):
    if(is_number(amt)==0):
        messagebow.showinfo("Error","invalid credentials\n Please try again.")
        master.destroy()
        return
    fdet=open(accnt+".txt","r")
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    cb=int(amt)+camt

    fdet=open(accnt +".txt","w")
    fdet.write(pin)
    fdet.write(str(cb)+"\n")
    fdet.write(accnt +"\n")
    fdet.write(name +"\n")
    fdet.close()

    frec=open(str(accnt)+"-rec.txt",'a+')
    frec.write(str(strftime("[%Y-%m-%d][%H:%M:%S]",localtime()))+"       " +amt+"       "+str(cb)+"\n")
    frec.close()

    messagebox.showinfo("operation Successfull!!","Amount credited Successfully\n")
    master.destroy()
    return
    
    
def deb_amt(acc_num,name):
    root2=Tk()
    root2.geometry("1600x1600")
    root2.title("Livewire Bank")
    root2.configure(background='orange')
    l2=Label(root2,text=' LIVEWIRE BANKING SYSTEM',font=('arial',50),bg="black",fg="red",width=2000)
    l2.pack()
    f4=Frame(root2,bg="lightblue")
    f4.pack(side="top",pady=10)
    
    l1=Label(f4,text="ENTER AMOUNT TO BE DEBITED",fg="black",font=('arial',12),bg="lightblue")
    l1.pack(side="left",padx=10)
    e1=Entry(f4,font=("arial",15))
    e1.pack(padx=10)

    b1=Button(root2,text="debit",command=lambda:deb_write(root2,e1.get().strip(),acc_num,name))
    b1.pack(side="top",pady=10)
    root2.bind("<Return>",lambda x:deb_write(root2,e1.get().strip(),acc_num,name))
     
    root2.mainloop()
    return

def cr_amt(acc_num,name):
    root2=Tk()
    root2.geometry("1600x1600")
    root2.title("Livewire Bank")
    root2.configure(background='orange')
    l2=Label(root2,text=' LIVEWIRE BANKING SYSTEM',font=('arial',50),bg="black",fg="red",width=2000)
    l2.pack()
    f4=Frame(root2,bg="lightblue")
    f4.pack(side="top",pady=10)
    
    l1=Label(f4,text="ENTER AMOUNT TO BE CREDITED",fg="black",font=('arial',12),bg="lightblue")
    l1.pack(side="left",padx=10)
    e1=Entry(f4,font=("arial",15))
    e1.pack(padx=10)

    b1=Button(root2,text="credit",command=lambda:crdt_write(root2,e1.get().strip(),acc_num,name))
    b1.pack(side="top",pady=10)
    root2.bind("<Return>",lambda x:crdt_write(root2,e1.get().strip(),acc_num,name))
    
    root2.mainloop()
    return
    
def logged_in_menu(acc_num,name):
    root1=Tk()
    root1.geometry("1600x1600")
    root1.title("Livewire Bank")
    root1.configure(background='orange')
    
    l1=Label(root1,text=' LIVEWIRE BANKING SYSTEM',font=('arial',50),bg="black",fg="red",width=2000)
    l1.pack()
    l2=Label(root1,text='LOGGED IN AS:'+name,font=('arial',50),bg="black",fg="red",width=2000)
    l2.pack(side="top")

    
    img1=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\credit.gif")
    img11=img1.subsample(2,2)
    b1=Button(root1,image=img11,command=lambda:cr_amt(acc_num,name))
    b1.image=img11
    b1.place(x=100,y=150)
    
    
    img2=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\debit.gif")
    img22=img2.subsample(2,2)
    b2=Button(root1,image=img22,command=lambda:deb_amt(acc_num,name))
    b2.image=img22
    b2.place(x=100,y=220)
    
    
    img3=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\logout.gif")
    img33=img3.subsample(2,2)
    b3=Button(root1,image=img33,command=lambda:home_return(root1))
    b3.image=img33
    b3.place(x=500,y=400)

    img4=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\balance1.gif")
    img44=img4.subsample(2,2)
    b4=Button(root1,image=img44,command=lambda:check_bal(acc_num))
    b4.image=img44
    b4.place(x=1000,y=220)

    img5=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\transaction.gif")
    img55=img5.subsample(2,2)
    b5=Button(root1,image=img55,command=lambda:transaction(acc_num))
    b5.image=img55
    b5.place(x=1000,y=150)


    root1.mainloop()
    

def check_login(master,name,acc_num,pin):
    if(check_acc_num(acc_num)==0):
        master.destroy()
        main_menu()
        return
    if(is_number(name)==1)or(is_number(pin)==0):
        messagebox.showinfo("error","invalid credentials\nPlease try again")
        master.destroy()
        main_menu()
    else:
            master.destroy()
            logged_in_menu(acc_num,name)

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0
    
def check_acc_num(num):
    try:
        fpin=open(num+".txt",'r')
    except FileNotFoundError:
            messagebox.showinfo("Error","Invalid Credentials!\nTry again!")
            return 0
    fpin.close()
    return

def home_return(master):
    master.destroy()
    main_menu()
    
def login(master):
    master.destroy()
    login=Tk()
    login.geometry("700x700")
    login.title("LOGIN")
    login.configure(background='orange')
    label1=Label(login,text="LIVEWIRE BANK",width=3000,padx=600,pady=0,fg="red",bg="black",font=('Arial',50))
    label1.pack()
    f1=Frame(login,bg="lightblue")
    f1.pack(pady=10)

    b1=Button(login,text="submit",command=lambda:check_login(login,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b1.pack()
    login.bind("<Return>",lambda x:check_login(login,e1.get().strip(),e2.get().strip(),e3.get().strip()))

    b2=Button(login,text="HOME",bg="blue",command=lambda:home_return(login))
    b2.pack()
    
    f2=Frame(f1,bg="lightblue")
    f2.pack()
    l1=Label(f2,text="Enter name",fg="black",font=('arial',12),bg="lightblue")
    l1.pack(side="left",padx=5)
    e1=Entry(f2,font=("arial",15))
    e1.pack()

    f3=Frame(f1,bg="lightblue")
    f3.pack()
    l2=Label(f3,text="ENTER ACCOUNT NO",fg="black",font=('arial',12),bg="lightblue")
    l2.pack(side="left",padx=5)
    e2=Entry(f3,font=("arial",15))
    e2.pack()

    f4=Frame(f1,bg="lightblue")
    f4.pack()
    l3=Label(f4,text="enter pin",fg="black",font=('arial',12),bg="lightblue")
    l3.pack(side="left",padx=5)
    e3=Entry(f4,font=("arial",15),show="*")
    e3.pack()
    
    login.mainloop()
    return
    
    
def write(master,name,oc,pin):
    if(is_number(name))or(is_number(oc)==0)or(is_number(pin)==0):
        messagebox.showinfo("ERROR","invalid credentials please try again ")
        master.destroy()
        return
    
    if int(oc)<500:
        messagebox.showinfo("insufficient minimum amount","you should start the amount minimum 500")
        master.destroy()
        return
    f1=open("C:\\Users\\ASUS\\Documents\\ajay.c\\Accnt_record.txt","r")
    accnt=int(f1.readline())
    accnt+=1
    f1.close()

    f1=open("C:\\Users\\ASUS\\Documents\\ajay.c\\Accnt_record.txt","w")
    f1.write(str(accnt))
    f1.close()

    fdet=open(str(accnt)+".txt","w")
    fdet.write(pin+'\n')
    fdet.write(oc+"\n")
    fdet.write(str(accnt)+"\n")
    fdet.write(name+"\n")
    fdet.close()

    frec=open(str(accnt)+"-rec.txt","w")
    frec.write("Date                          Credit          Debit           Balance\n")
    frec.write(str(strftime("[%Y-%m-%d][%H:%M:%S]",localtime()))+"    "+oc+"                       "+oc+"\n")
    frec.close()

    messagebox.showinfo("Details","Your Account Number is:"+str(accnt))
    master.destroy()
    return

    
def create():
    crwn=Tk()
    crwn.geometry("700x700")
    crwn.title("create account")
    crwn.configure(background='orange')
    label1=Label(crwn,text="LIVEWIRE BANK",width=3000,padx=600,pady=0,fg="red",bg="black",font=('Arial',50))
    label1.pack()
    
    f1=Frame(crwn,bg="lightblue")
    f1.pack(pady=10)

    b1=Button(crwn,text="submit",command=lambda:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b1.pack()
    crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    
    

    
    f2=Frame(f1,bg="lightblue")
    f2.pack()
    l1=Label(f2,text="enter name",fg="black",font=('arial',12),bg="lightblue")
    l1.pack(side="left",padx=5)
    e1=Entry(f2,font=("arial",15))
    e1.pack()

    f3=Frame(f1,bg="lightblue")
    f3.pack()
    l2=Label(f3,text="opening credit",fg="black",font=('arial',12),bg="lightblue")
    l2.pack(side="left",padx=5)
    e2=Entry(f3,font=("arial",15))
    e2.pack()

    f4=Frame(f1,bg="lightblue")
    f4.pack()
    l3=Label(f4,text="enter pin",fg="black",font=('arial',12),bg="lightblue")
    l3.pack(side="left",padx=5)
    e3=Entry(f4,font=("arial",15),show="*")
    e3.pack()
    
    crwn.mainloop()
def main_menu():
    root=Tk()
    root.geometry("1600x1600")
    root.title("Livewire Bank")
    root.configure(background='orange')
    bg_image=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\m.gif")
    l2=Label(root,text='BANKING SYSTEM',font=('arial',50),bg="black",fg="red",width=2000)
    l2.pack()
    l1=Label(root,image=bg_image)
    l1.image=bg_image
    l1.pack()
    
    img1=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\login.gif")
    img11=img1.subsample(2,2)
    b1=Button(root,image=img11,command=lambda:login(root))
    b1.image=img11
    b1.place(x=500,y=250)
    
    
    img2=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\new.gif")
    img22=img2.subsample(2,2)
    b2=Button(root,image=img22,command=create)
    b2.image=img22
    b2.place(x=400,y=150)
    
    
    img3=PhotoImage(file="C:\\Users\\ASUS\\Documents\\ajay.c\\quit.GIF")
    img33=img3.subsample(2,2)
    b3=Button(root,image=img33,command=root.destroy)
    b3.image=img33
    b3.place(x=650,y=450)
    
    root.mainloop()
main_menu()




