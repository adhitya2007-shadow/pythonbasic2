a=input("age")
a=a.replace("1","8")
print(a)

text="python programming"
text=text.replace("p","9")
print(text)
#here the output will come as error due to the integer function 
a=int(input("age"))
a=a.replace("1","8")
print(a)
    #(or)
a=int(input("age"))
a=a.replace("a","c")
print(a)


#explecit type conversion

a=True
a=int(a)
print(a,type(a))
 

a=False
a=int(a)
print(a,type(a),sep=",")  

#f strings
name="adhitya harshith"
age=17
college="mrdu"
print(f"hello {name},your age is {age}")

name="prem kumar"
age=18
print("hello {} your {}years old!".format(name,age))
print("hello {} your age is{}".format("prem kumar",18))
print("hello {1} your age is{0}".format(" prem kumar",18))


name="john"
age=25
print("Hello {}, you are {} years old!".format(name,age))


text="python programming"
print("_".join(["python","programming"]))
# HERE ''' THIS SINGLE QUOTES ELIMINATES THE LINE WHEN WE KEEP IT IN FRONT AND BACK OF THE LINE

t1="pr"
t2="em"
print(t1+t2)

name ="Adhitya Harshith"
score ="92"
grade ="A+"

print("hello iam " +   name +" ,i secured "+ score+" ,iam in "+ grade)


name ="Adhitya harshith"
score ="92"
grade ="A+"
print(f"hello {name},you scored{score}%,and got {grade}")

#back_slash
print("line1line2")
print("line1\nline2")

#by using tab button ,it gives 4spaces at a time

print("line1\tline2\tline3")

print("hello\"hi how are you\"")

print("file path c: \\user\\")
print("unicode heart:\u2764")

print("hellohellohello")
