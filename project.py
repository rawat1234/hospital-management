from tkinter import *
program=Tk()
program.config(bg="light green")
count=0
def add():
    f=open('hospital.txt','a')            
    deptname=s1.get()
    deptid=s2.get()
    hod=s3.get()
    doctors=s4.get()
    patients=s5.get()
    f.writelines(deptname.zjust(10)+deptid.zjust(30)+hod.zjust(30)+doctors.zjust(30)+patients.zjust(20)+"\n")
    f.close()
def delete():
    record=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()]
    f=open('hospital.txt','r')           
    read=f.readlines()
    print(read)
    print(record)
    f.close()
    f=open('hospital.txt','w')           
    for i in read:
        x=i.split()
        print(x)
        if(x!=record):
             f.writelines(x[0].ljust(10)+x[1].ljust(30)+x[2].ljust(30)+x[3].ljust(30)+x[4].ljust(20)+"\n")
    f.close()
def update():
    u1=s1.get()
    u2=s2.get()
    u3=s3.get()
    u4=s4.get()
    u5=s5.get()
    f=open('hospital.txt','r')          
    read1=f.readlines()
    f.close()
    f=open('hospital.txt','w')          
    flag=0
    for i in read1:
        j=i.split()
        if(j[0]!=u1):
            f.writelines(j[0].zjust(10)+j[1].zjust(30)+j[2].zjust(30)+j[3].zjust(30)+j[4].zjust(20)+"\n")
    
        else:
            f.writelines(u1.ljust(10)+u2.ljust(30)+u3.ljust(30)+u4.ljust(30)+u5.ljust(20)+"\n")
            flag=1
    f.close()
def search():
    element=s1.get()
    f=open('hospital.txt','r')         
    read1=f.readlines()
    for i in read1:
        j=i.split()
        if(j[0]==element): 
            print("searched element is available in records")
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()  
def nextrecord():
    f=open('hospital.txt','r')         
    i=0
    global count
    while(i<=count):
        z=f.readline()
        i=i+1
    info=z.split()
    s1.set(info[0])	
    s2.set(info[1])
    s3.set(info[2])
    s4.set(info[3])
    s5.set(info[4])
    count=count+1
    f.close()
def previous():
    global count
    i=0
    count=count-1
    print(count)
    f=open("hospital.txt","r")        
    while(i<=count-1):
        z=f.readline()
        i=i+1
        print(z)
    rec=z.split()
    s1.set(rec[0])
    s2.set(rec[1])
    s3.set(rec[2])
    s4.set(rec[3])
    s5.set(rec[4])
def begin():
    f=open("hospital.txt",'r')       
    y=f.readlines()[0]
    j=y.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
def end():
    f=open("hospital.txt",'r')       
    p=sum(1 for i in open("hospital.txt"))-1
    print(p)
    y=f.readlines()[p]
    j=y.split()
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
z0=Label(program,text="RAWAT HOSPITAL",bd=10,fg="purple",bg="pink",width=25)
z1=Label(program,text="Name of Department",bg="light green")
z2=Label(program,text="Id of Department",bg="light green")
z3=Label(program,text="Head Of Deptartment",bg="light green")
z4=Label(program,text="No. Of Doctors",bg="light green")
z5=Label(program,text="No. Of Patients",bg="light green")
e1=Entry(program,textvariable=s1,bd=5)
e2=Entry(program,textvariable=s2,bd=5)
e3=Entry(program,textvariable=s3,bd=5)
e4=Entry(program,textvariable=s4,bd=5)
e5=Entry(program,textvariable=s5,bd=5)
o1=Button(program,text="ADD",command=add,bd=5,fg="blue",bg="light green")
o2=Button(program,text="DELETE",command=delete,bd=5,fg="red",bg="light green")
o3=Button(program,text="UPDATE",command=update,bd=5,fg="dark violet",bg="light green")
o4=Button(program,text="SEARCH",command=search,bd=5,fg="blue4",bg="light green")
o5=Button(program,text="NEXT",command=nextrecord,bd=5,fg="brown",bg="light green")
o6=Button(program,text="PREVIOUS",command=previous,bd=5,fg="dark green",bg="light green")
o7=Button(program,text="FIRST",command=begin,bd=5,fg="magenta",bg="light green")
o8=Button(program,text="LAST",command=end,bd=5,fg="black",bg="light green")
z0.grid(row=1,column=2)
z1.grid(row=2,column=1)
z2.grid(row=3,column=1)
z3.grid(row=4,column=1)
z4.grid(row=2,column=3)
z5.grid(row=3,column=3)	
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
e3.grid(row=4,column=2)
e4.grid(row=2,column=4)
e5.grid(row=3,column=4)
o1.grid(row=7,column=1)
o2.grid(row=7,column=2)
o3.grid(row=7,column=3)
o4.grid(row=8,column=3)
o5.grid(row=8,column=1)
o6.grid(row=8,column=2)
o7.grid(row=7,column=4)
o8.grid(row=8,column=4)
program.mainloop()
