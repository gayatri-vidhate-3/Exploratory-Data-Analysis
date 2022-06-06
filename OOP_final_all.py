'''
-----------------------------------------------------------------------
## ##########################13-01-2022#####################################
----------------------------------------------------------------------
OOP: Object oriented programming
Everything in python is an object

What is object????
Is an entity exist in a memory
which has an id/address assigned

How object gets created??
==> it gets created using a class

what is class ??
class is template, its a blueprint, structure, plan, architecture

class in our case:
collection of 2 things
1. Properties: attributes, variables, identifiers
2. Behaviour: methods/functions
Example:
class Mobile:
    os
    RAM
    processor
    camera
    pixel
    color
    .
    .
    shutdown()
    powerOn()
    restart()
    reboot()
    backup()


class Human:
    properties:
                eyes
                hands
                legs
                ht
                wt
                color
                ......
    behaviour:operations/methods/function/processing
                talk()
                walk()
                speak()
                hear()
                run()
                sense()

print(id(23))
a = 23
print(id(a))
print(type(a))

How many objects we can create???
:- n no. of objects

How to check object size of object?
a = 78
# will tell u size in  bytes
print(a.__sizeof__())

---------------------------------------------------------------
Lets start with class and object
e307
---------------------------------
# there is no inherent limit for int value
#a = 2342355555555552423444444444444444444444444444444444444444442342424234234242342342423444444442342
#print(a)
#for float we have limit of e^307
a  =2.0**10057
print(a)
-------------------------------------

# Class + object
# while writing a class follow CamelCase

class Sample:
    s1 = 20
    s2 = 'java'

    def method(self):
        print('this is first method')

# Now we have just created structure of Sample

# in order to make it available in the memory we need to create an object
# to create an object we need a constructor
# what is constructor??
# constructor is nothing but calling of a class
# in current case: Sample() is a constructor
# why it is needed???
# it is need to allocate a memory

s = Sample()    # sample is constructor
print(s.s1)
print(s.s2)
s.method()
------------------------------------------------------------
# if we are not creating an object, we don't have an access to members inside a class

s1
s2
method()

class Car:
    wheels = 4
    color = "red"

    def drive(self):
        print('start car')
    def gear(self):
        print('use gears')

#without object
print(Car().wheels)
print(Car().color)
print('----------------------------------')
# with object
o = Car()
print(o.wheels)
print(o.color)
o.gear()
o.drive()
------------------------------------------
class Test:
    x = 10
    y = 20

print(Test().x)
Test().x = 100
print(Test().x)
print(id(Test().x))
print('-------------------------')
t = Test()
print(t.x)
print(id(t.x))
t.x = 100
print(t.x)
print(id(t.x))
--------------------------------------------------
class Test:
    x = 40
    def m1(self):
        print('m1 test')

t1 = Test()
t1.m1()

t2 = Test()
print(t2.x)

t3 = Test()
t3.m1()
print(t3.x)

-------------------------------------------------------------------
##########################15-01-2022#####################################
----------------------------------------------------------------------

Class :
is a collection of Properties and behaviour
properties can be represented by variables/ attributes
behaviours can be implementd by Methods

Define???
class ClassName:
    """This is my first class"""
    variables: instance,static,local
    +
    methods: instance, class method,static method
-------------------------------------
class Cake:
    """
    this is first  class
    """
#print(Cake.__doc__)
#print(help(Cake))
print(help(int))
-------------------------------------------------------------------

Object:
Instance of a class==> that object will be present in a memory
# means exists Physically
Physical existence of a class is nothing but object
Syntax:
reference_variable = ClassName()

Example:
simple_cake = Cake()
sugar_free_cake = Cake()
ice_cake = Cake()
---------------------------------------------
REFERENCE VARIABLE:

The variable which can be used to refer object is called reference variable
Example:
class Cake:
    d = 87

c1 = Cake()
print(c1.d)
In above example d is reference variable

There is another reference variable: className

class Cake:
    d = 87
print(Cake.d)

in above example Cake which is class name , acts as a reference variable

Conclusion: Outside the class we have 2 ref. variables
1. object
2. className
---------------------------------------------------------
class Cricket:
    team1 = 'IND'
    team2 = "ENG"

# by using object
c1 = Cricket()
print(c1.team1)
print(c1.team2)
c1.team2 = "SA"
print(c1.team2)
print('-----------using class------------')
print(Cricket().team1)
print(Cricket().team2)
Cricket().team2 = 'SL'
print(Cricket().team2)
print(c1.team2)
----------------------------------------------------------------
How to access members of a class???
using ref variable
object
className
---------------------------------
Lets add new members to a class
-------------------------------------
class Student:
    #pass
    country = 'IND'
    state = 'MAH'

s1 = Student()
s1.name = 'Amol'
s1.age = 34
#print(s1.age)
#print(s1.name)
# in above case also we can acess but at a single time we can get all instances by below way;
# country and state will not be there as name and age seperate instances we have created outside class
# and if we want to access state and country then
print(s1.state)
print(s1.country)
print("----------------------------")
print(dir(s1))
print(s1.__dict__)
print("-----------------------")
print('creating second object')

s2 = Student()
s2.name = 'Shital'
s2.age = 22
s2.palce = 'pune'
print(s2.__dict__)

-----------------------------------------------
##########################17-01-2022#####################################
----------------------------------------------------------------------

Types of variables:
1) local variable:
        the variable declared inside a class/method
        is a local variable
        & that var. is only accessible inside the class+ inside the method resp.
----------------------------------------------------------------------------------------------------------------------
class Sample:
    x = 90 #local to class
    def test(self):
        a = 'py' #local to method
    print(a) #here we r trying to access a outside the block
print(x)#hre we r trying to access x outside the class
-----------------------------------------------------
class Sample:
    # variable declared inside a method is local variable
    def test(self):
        a = 'py'           #pure local var. to method
        print(a)           # inside a method , a will be accessible

s = Sample()
print(s.a) # outside class it wont be accessible
-----------------------------------------------------------------------------------
2) instance variable: if we want to access or modify local variables inside a class
+ outside a class too

class Sample:
    def add(self,a,b):
        print('a:',a)
        print('b:', b)
        print(a+b)
    def another(self):
        # in this way we cant access local variables of add into another
        # we need to make them instance
        print('a:', a)
        print('b:', b)
s = Sample()
s.add(20,30)
s.another()
print(s.a)
---------------------------------------------------------
# we can make local var. instance  using self keyword
class Sample:
    def add(self,a,b):
        #print(a+b)
        # lets make a and b as an instance
        self.a = a
        self.b = b
    def another(self):
        # in this way we cant access local variables of add into another
        # we need to make them instance
        print('lets print a and b')
        print(' Inside a:', self.a)
        print('Inside b:', self.b)
s = Sample()
s.add(20,30)
s.another()
print('Outside a:',s.a)
-------------------------------------------
Lets change the value of instance variable
class Sample:
    def m1(self,name):
        #p-rint(name)
        self.n = name
        # in above case self.n is instance and name is local
    def disp(self):
        print('Your name is:',self.n)
    def change(self):
        self.n = 'Java'
        print('After change, ur name is:', self.n)

s = Sample()
s.m1('Python')
s.disp()
s.change()
-------------------------------------------------------
ANother example:

class Sample:
    def m1(self,name):
        self.n  = name
    def change(self):
        print('my name is:',self.n)
        self.n = 'java'
        print('my name is:', self.n)

s = Sample()
s.m1('gayatri')
s.change()
--------------------------------------
Instance method: The method with self as ref. variable are instance method
Example:

def m1(self):
def add(self):

All default methods in python are instance
-----------------------------------------------------
class Sample:
    x = 1
    y = 2
    def t1(self):
        self.a = 'amit'
        self.b = 'baban'
    def t2(self):
        pass
        print('a from t2:',self.a)

# self: self in ref variable, it access everything inside a class
s = Sample()
s.t1()
print('a from t1:',s.a)
s.t2()
--------------------------------
instead of self we can use any variable
self acts same as that of this pointer in java
it points to current object: it access to each n everything present inside a class
------------------------------------------------------
class Sample:
    def m1(s):
        s.x = 800

    def m2(s):
        print(s.x)
------------------------------------------------------
Static var. :
the variable declared inside a class and outside a method
Example 1 by me:-
class Sample:
    IFSC = 'SBI5678'
    def m1(self):
        print('Variable aceesible inside the class using self:',self.IFSC)
        print('Variable aceesible inside the class using class name:', self.IFSC)

s = Sample()
print('Variable aceesible outside the class using object:',s.IFSC)
print('Variable aceesible outside the class using class name:',Sample.IFSC)
s.m1()
-----------------------------------------------------------------
Example by sir-
class Sample:
    ifsc = 'SBI2343'
    # static or class level var.

    #lets access clas var. inside a method m1
    def m1(self):

        print('m1:',self.ifsc)
        print('m1 Sample:', Sample.ifsc)
        # self and Sample will work inside method only

    print(Sample.ifsc) # they wont work outside method
    print(self.ifsc)
    print('IFSC:',ifsc)

s = Sample()
print('object:',s.ifsc)
print('Clas:',Sample.ifsc)
s.m1()
--------------------------
class Sample:
    ifsc = 'SBI2343'
    # static or class level var.

    #lets access clas var. inside a method m1
    def m1(self):

        print('m1:',self.ifsc)
        print('m1 Sample:', Sample.ifsc)
        # self and Sample will work inside method only

    print(Sample.ifsc) # they wont work outside method
    print(self.ifsc)
    print('IFSC:',ifsc)

s = Sample()
print('object:',s.ifsc)
print('Clas:',Sample.ifsc)
s.m1()
--------------------------
class ATM:
    pin = 1234

    def m1(self):
        pass
        print(self.pin)
        print(ATM.pin)

a = ATM()
a.m1()
print(a.pin)
print(ATM.pin)

----------------------------------
##########################18-01-2022#####################################
----------------------------------------------------------------------
Variables: Local, instance, static/class level
Methods: instance,class method, static method
----------------------------------------------------
Constructor:
It is used to allocate a memory
or
it initializes member of class and make them available outside the class

Features of constructor:
Constructor has same name as that of class name
We can create/call constructor multiple times
class Sample:
    f = 67
    def m1(self):
        pass
Sample()
-----------------------------------------------------------------
Using constructor we can build an object

s = Sample()
-----------------------------------------------------------
If we want to write a method of a constructor then use def __init__(self): method
----------------------------------------------------
class Sample:
    def __init__(self):
        print('This is init...')

# Constructor calling means __init__ calling
Sample()
Sample()
------------------------------------------------
Lets use instance variables in init
--------------------------------------------
class Bank:
    def __init__(self):
        self.branch = 'Pune'
        self.ifsc = 'SBI7523'
        self.micr = 12324

    def display(self):
        #print('Branch is:{} IFSC is:{},MICR is:{}'.format(self.branch,self.ifsc,self.micr))
        print('Branch is:%s IFSC is:%s,MICR is:%d'%(self.branch,self.ifsc,self.micr))
        # % is format specifier
b = Bank()
b.display()
------------------------------------------
If i want to supply member through instance method __init__
----------------------------------------------------------------
class Bank:
    def __init__(self,b,i,m):
        self.branch = b
        self.ifsc = i
        self.micr = m

    def display(self):
        #print('Branch is:{} IFSC is:{},MICR is:{}'.format(self.branch,self.ifsc,self.micr))
        print('Branch is:%s IFSC is:%s,MICR is:%d'%(self.branch,self.ifsc,self.micr))
        # % is format specifier
"""
b = Bank('Kop','BOI2345',98793)
b.display()

b1 = Bank('Pune','BOM34345',567567)
b1.display()
"""
# ask user to supply the values
br = input('Enter the Branch:')
ifs = input('Enter the IFSC:')
mi = input('Enter the MICR:')
b = Bank(br,ifs,int(mi))
b.display()
-------------------------------------------------------
class Bank:
    def __init__(self,nm):
        self.nm = nm
        print('Name:',self.nm)
        print('We can change value of instance variable')
        #chagge nm
        self.nm = 'BOI'
        print('changed Name:', self.nm)

b = Bank('SBI')
print(b.nm)
----------------------------------------------------
To pass values, only constructor is not an option
 we can do the same thing using instance method also
---------------------------------------
class Student:
    def display(self,nm,age,place='Pune'):
        self.nm = nm
        self.age= age
        print(self.nm,self.age,place)

s = Student()
s.display('Amol', 30)

s1 = Student()
s1.display('Janvi',34,'Satara')
--------------------------------------------------------------
Class Method:
Q. What is class method? why we need???? when to use?? How its different from others/??

A method which is used to access class level or static variables is known as  class method

in order to create a class method we need @classmethod decorator
and instead of self we use cls as a reference variable
-------------------------------------class Test:
    x = 66 #static or class level vr.

    @classmethod
    def catch(cls):
        print(cls.x)

t =  Test()
t.catch()

# Assignment: What is difference btwn instance and class method???
----------------------------------------------------
Static method:
A method which contains static variables and decorated with @staticmethod decorator
is known as static method.

which we can not access in any other method???or member of that method cannot be accessible
to any other

When we need static method????
When we want to perform operations only once,
or we dont want to change the supplied values

In this case we don't require self
--------------------------------------------------------------
class Test:
    @staticmethod
    def m1(a,b):
        print(a+b)

t = Test()
t.m1(20,40)

---------------------------------------------------------------
##########################24-01-2022#####################################
----------------------------------------------------------------------
Setter and getter method:

These methods are associated with instance variables
We can set and get the values using these methods
------------------------------------------
Setter method:
used to set values to the instance variable
setter method os also known as Mutator method
-----------------
Syntax:
def set_method_name(self,var):
        self.var = var
----------------------------------------
getter method:
used to get the values from instance variable
gettter methods as also known as Accessor method

syntax:
def get_method_name(self):
    return self.var
-------------------------------------------------------------------
class Student:

    #setter method
    def details(self,roll_no):
        self.roll_no = roll_no

    #getter method
    def display(self):
        return self.roll_no

s = Student()
s.details(101)
print(s.display())

----------------------------------------------------------------------
Constructor allocates a memory to a class/ object
Immediately Destructor de-allocates a memory
--------------------------------------------------------
#Assignment: set Name,age, adress, place, pin and return also
ANswer:-
class Student:

    def details(self,name,age,adress,place,pin):
        self.name = name
        self.age = age
        self.adress = adress
        self.place = place
        self.pin = pin

    def display(self):
        return self.name,self.age,self.adress,self.place,self.pin

s = Student()
#s.details('Mohan',32,'Nova APartment,Magarpatta','Pune',411036)
n = input('Enter name:')
a = int(input('Enter age:'))
adr = input('Enter adress:')
pl = input('Enter place:')
pin = int(input('Enter pincode:'))
s.details(n,a,adr,pl,pin)
print(s.display())
------------------------------------------------------------------
import time
class Student:
    def __init__(self):
        print('Constructor called')
        time.sleep(2)
    def __del__(self):
        print('Destructor gets called..')
        time.sleep(2)
# call the constructor
Student()
time.sleep(3)
Student()
time.sleep(3)
Student()
#
-------------------------------------------------------
import time
class Student:
    def __init__(self):
        print('construtcore')
    def __del__(self):
        print('destructor')

Student()
time.sleep(5)
Student()
-----------------------------------------------------

class Student:
    def __init__(self,name,age):
        self.n= name
        self.a = age
        self.std = 1

    def m1(self,x1):
        self.x = x1
        self.y = 340
        self.name = 'Swaroopa'

s = Student('AB',23)
s.m1(45)
-----------------------------------------
class Student:
    def __init__(self):
        pass
s1 = Student()
s1.name = 'Alok'
s1.age = 34
s1.salary = 67000
print('S1:',s1)

s2 = Student()
print('S2:',s2)
s2.name= 'Rashmi'
del s2
print('S2:',s2)
--------------------------------------------------------
How to add and delete instances
---------------------------------
class Student:
    def __init__(self,nm,age):
        self.nm = nm
        self.ag = age
        #del self.ag
s = Student('A',12)
print(s.__dict__)
print('Lets add new instance place')
s.place = 'Pune'
print(s.__dict__)
print('Lets remove age')
del s.ag
print(s.__dict__)
# if we want to add instances inside a class then use self
# if we want to add instances from outside the class the use object
------------------------------------------------------------
class Student:
    x = 67 #class level/static
    def m1(self):
        # print(self.x)
        # print(Student.x)
        pass

s = Student()
s.m1()
print(s.x) #67
s.x = 67000
print(s.x)
print(Student.x)

s2 = Student()
print('S2:',s2.x)
------------------------------------------------
Nested class: class inside another class
=============================================
class University:
    def __init__(self):
        print('init of university')
    def u1(self):
        print('u1 method')
    def u2(self):
        print('u2 method')
    class College:
        def __init__(self):
            print('init of college')
        def c1(self):
            print('c1 method')
        def c2(self):
            print('c2 method')
u =University()
#u.College()
u.u1()
u.u2()
print('##############################')
University.College()
print('##############################')
#c = University.College()
c = u.College()
c.c1()
c.c2()
-----------------------------------------------------------------
##########################26-01-2022#####################################
----------------------------------------------------------------------

OOP characteristics:
1. Inheritance
2. Abstraction
3. Encapsulation
4. Polymorphism
'''
'''
1. Inheritance:
Its a relationship
we inherit something from someone
Parent--- child relationship

Creating(deriving) a new class(child class) from parent class(base class) is nothing but 
an Inheritance

Example:
class Universty: #parent
        pass
class Institutes(Universty):
        pass
-------------------------------------------------------
class Parent:
    print('This is parent class')
    def m1(self):
        print('m1 method')
class child(Parent):
    print('This is child class')

c = child()
c.m1()
--------------------------------------------  
# Overriding in Python:
When we have same method with same name in both parent asn child class
then
Method in parent will be overridden in child    
and method in child overrides method in parent
---------------------------------------------------------
class Parent:
    print('This is parents class')
    def m1(self):
        print('This is parents method m1')
class Child(Parent):
    def m1(self):
        print('This is childs method m1')

c = Child()
c.m1()
------------------------------------------------
class Parent:
    print('This is parent class')
    def money(self):
        print('Parent money')
    def Car(self):
        pass
# now if child has very less amount
# then he/she must have to take help of Parent
class Child(Parent):
    def money(self):
        print('Child money')
        super().money()
    def budget(self):
        #super().money()
        #super(Child, self).money()
        super(Child, self).money()
        super(Child, self).Car()

c = Child()
c.money()
c.budget()
-----------------------------------------------------
class Parent:
    def __init__(self,place):
        self.plac =place
        print('Init of parent')
        #print(self.plac)

class Child(Parent):
    def __init__(self,nm,age):
        self.nm = nm
        self.age = age
        super().__init__('Pune')
        print('Init of Child')
        print(self.nm,self.age,self.plac)

c =  Child('Nilam',22)
------------------------------------------------
Types of Inheritance:
1. Single inheritance= One parent and One child
2. Multilevel inheritance = Super_Parent--Parent--child

class GrandFather:
    def money(self):
        print('Money from Grand father')

class Father(GrandFather):
    def money(self):
        #super().money()
        print('Money from father')

class Child(Father):
    def money(self):
        super().money()

c = Child()
c.money()

-----------------------------------------------------------------
##########################27-01-2022#####################################
----------------------------------------------------------------------

Multiple Inheritance:
We can have more than one Parent
and multiple child

-------------------------------------
class Father:
    def money(self):
        print('Father\'s money')
class Mother:
    pass
    def money(self):
        print('Mother\'s money')
# when we want to inherit multiple parents
# then we must have to think abt priority
class Child(Father,Mother):
    def money(self):
        super().money()
c = Child()
c.money()
--------------------------------------

class A:
    def m1(self):
        print('m1')
class B:
    pass
class C:
    def m1(self):
        print('m1')
class D(B,A,C):
    def m1(self):
        print('m1')
        super().m1()

d = D()

# MRO: Method resolution order
# It tell us how the methods are accessed from the class according to hierarchy/priority
# It gives a sequence of method access/how methods are accessed
# in order to check MRO we need a class(Child/Derived) name
print(D.mro())
-----------------------------------------------------------------
class X:
    pass
class Y:
    pass
class Z():
    pass
class P(X,Z):
    pass
class Q(Y,X):
    pass
class Child(X,Q,Z):
    pass
print(Child.mro())

-----------------------------------------------------------------
##########################28-01-2022#####################################
----------------------------------------------------------------------
Encapsulation in Python:
# class acts as a container in which we can hid Members
# members  means: Properties + behaviour
# Variables + Methods are hidden to outside world(direct access is not possible)

# Encapsulation == Data Hiding/Hiding of Members
-------------------------------------------------------
Example: class in python

class Sample:
    x = 60
    def m1(self):
        pass


# We cant access x and m1() directly outside the class
print(x)
m1()
_-----------------------------------
In other programming lang. we have specific access modifiers
public

private
protected

unfortunately we dont have these modifiers

Python does not contain Public private and protected terms

But we can implement then using _(underscore) convention
Variable/method without underscore is public in that scope
Variable/method with _ underscore is protected in that scope
Variable/method with __  underscore is private in that scope
--------------------------------------------
class Sample:
    public = 100
    _protected = 200
    __private = 300

    print(__private)
    print(_protected)

s = Sample()
print(s.public)
print(s._protected)
# private variable is completely hidden from outside world
#print(s.__private)
###########################################################
# If private member i want to access then we can access
# Using Name mangling technique
print(dir(s))
print(s._Sample__private)
s._Sample__private = 400
print(s._Sample__private)
---------------------------------------------------------
Hide the methods

---------------------------------------------------------
class Sample:
    def m1(self):
        print('Public m1 ')

    def _m2(self):
        print('Protected m2')

    def __m3(self):
        print('Private m3')

class Test(Sample):
    def m4(self):
        #self.m1()
        #Sample.m1()
        super().m1()
        super()._m2()
        super()._Sample__m3()

t = Test()
t.m4()
------------------------------------------
s = Sample()
s.m1() #directly available
s._m2() # indirectly its available

s._Sample__m3() # completely hidden
----------------------------------------------------------------
Abstraction:
Information Hiding
It is implemented using Abstract class


In python we have normal class.
If we want to make a normal as an abstract class then we have to first import
ABC(Abstract Base Class) class,Then this ABC class we have to inherit in normal class
This is just a partial abstraction
In order to make complete abstract class 
we have to add at least one abstract method

What is abstract method???
a normal/instance method if we want to make it abstract then 
use @abstractmethod decorator
To use above decorator we have to import it from abc module
-------------------------------------------------------
from abc import ABC,abstractmethod
class Sample(ABC):

    @abstractmethod
    def m1(self):
        pass

# We cant instantiate abstract class
# means we cant create an object of an abstract class
class Sampel2(Sample):
    pass
s2 = Sampel2()
----------------------------------------------

-----------------------------------------------------------------
##########################29-01-2022#####################################
----------------------------------------------------------------------
from abc import ABC,abstractmethod
class Sample(ABC):

    @abstractmethod
    def m1(self):
        pass
     # in abstract class we can also add non abstract methods
    #@abstractmethod
    def my_method(self):
        print('This is instance method')

# This is not allowed at all
# we cant instantiate ABC
#s =  Sample()
#s.m1()

#class Child(Sample):
    #pass
#c =  Child()
#c.m1()
#------------------------------------------------
# In above case we are just creating an object of child class
# and trying to access m1() from Sample class
# which is again not allowed
# why???????
# Rule is: As Sample class is not normal class, n its an abstract class
# so implementation of abstract method(m1()) in child class is Mandatory
class Child(Sample):
    def m1(self):
        print('Implementation of Abstract method m1')
    
c =  Child()
c.m1()
c.my_method()
--------------------------------------------------------

from abc import ABC
class Shape(ABC): #abstract classdef calculate_area(self): #abstract methodpassclass Rectangle(Shape):
  length = 5
  breadth = 3
  def calculate_area(self):
      return self.length * self.breadth

class Circle(Shape):
  radius = 4
  def calculate_area(self):
      return 3.14 * self.radius * self.radius

#rec = Rectangle() #object created for the class 'Rectangle'
cir = Circle() #object created for the class 'Circle'
#print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'
print("Area of a circle:", cir.calculate_area()) #call to 'calculate_area' method defined inside the class 'Circle'.

-----------------------------------------------------------------
##########################31-01-2022#####################################
----------------------------------------------------------------------
Polymorphism:
Poly(Many) + morphs(forms)

1 Norm and Many forms

Example: Human Nature
         operators in python : + *
---------------------------------------------------------------------
User define function specific polymorphism

def add(a,b,c=10):
    print(a+b+c)

add(1,2)
add(2,3,4)
-------------------------------------------------------------------

polymorphism means the same function name
(but different signatures) being used for different types.
--------------------------
def add(a, b, c=10):
    print(a + b + c)

add(1, 2)
add(2, 3, 4)
---------------------------------
def add(*args):
    print(sum(args))

add()
add(1,2)
add(2,3,5)
add(2,3,45,6,7)
------------------------------------------------------------------
Overloading Types:
Use same method but with different signature/no. of arguments
def m1()
def m1(a,b)
def m1(x,y,z)

1. Method Overloading
-------------------------------
class Sample:
    #lets implement different behaviour of m1()
    def m1(self):
        print('No arg')
    def m1(self,a):
        print('One arg')
    def m1(self,x,y):
        print('Two args')


s = Sample()
s.m1()
s.m1(10)
s.m1(10,70)
'''
'''
In python, method overloading is not possible,
bcz it will call last recent method always
so only
s.m1(10,70) will get executed
-----------------------------
If we still want to implement Method overloading then
use *args(variable length argument.

class Sample:
    def m1(self,*args):
        print('No arg')

s = Sample()
s.m1()
s.m1(10)
s.m1(10,70)
------------------------------------
Assignment: How to implement method overloading in Python??
--------------------------------------------------------------
2. Constructor overloading:
same name but different signature
def __init__()
def __init__(a)
def __init__(x,y,z)
----------------------------------------------
class Sample:
    def __init__(self):
        print('No arg')
    def __init__(self,x):
        print('One arg')
    def __init__(self,p,q):
        print('Two args')

#Sample() #this wont get executed
# constructor overloading is not possible
# bcz it wil also call last recent init method
# so u must have to pass 2 argumnts
s = Sample(2,3)
s.__init__(40,50)
----------------------------------------------------------------------
# Assignment: Implement Constructor overloading using Python
Ansr:-
class Sample:
   def __init__(self,*args):
       print('first')

s = Sample()
s.__init__()
s.__init__(1)
s.__init__(6,7)
--------------------------------------------------------------
Operator Overloading:
Different nature of operator on different inputs
----------------------------
class Library:
    def m1(self,books):
        self.books= books
        return self.books

l1 = Library()
print(l1.m1(500))

l2 = Library()
print(l2.m1(700))

print(l1.m1(500)+l2.m1(700))
print(l1.m1('500')+l2.m1('700'))
----------------------------------------------------------------

class Library:
    def __init__(self, books):
        self.books = books

    # Magic method/dunder method
    def __add__(self, other):
        return self.books + other.books

    def __mul__(self, other):
        return self.books * other.books


l1 = Library(100)
l2 = Library(200)
# lets add two objects
print(l1 + l2)
print(l2 * l1)
----------------------------------------------------------
'''
