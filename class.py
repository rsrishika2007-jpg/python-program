class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.sno=a
        self.sname=b
        self.sage=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate():
        self.tot=self.mark1+self.mark2+self.mark3
        self.avg=self.tot/3

        
        if m1>=40 and m2>40 and m3>40:
            self.result("pass")
        else:
            self.result("fail")


    def display(self):
        print("student no:",self.sno)
        print("student name:",self.name)
        print("student age:",self.age)
        print("mark1=",self.mark1)
        print("mark2=",self.mark2)
        print("mark3=",self.mark3)
        print("total=",self.tot)
        print("average=",self.avg)
        print("result=",self.result)
        

x=int(input("enter roll no:"))
y=input("enter name:")
z=int(input("enter age:"))
mark1=int(input("enter mark1:"))
mark2=int(input("enter mark2:"))
mark3=int(input("enter mark3:"))

obj=stud(x,y,z,m1,m2,m3)
obj.calculate()
obj.display()
             
     
        
