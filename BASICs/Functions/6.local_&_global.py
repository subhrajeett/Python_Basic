#Part1
#Local var: scope only inside its function 
#Global var: Accessible through out 

#global
name = "Rahul"
def greet():
    #name here is local and its nothing related to global "name"
    #local doesnt over writes a global
    name="Modi Ji"
    print(f"Hello {name}")
greet()
print(f"Ayoo {name}")

#-----------------------------
#part2
# global key_word 
#If we want to change the global itself in a function scope,we can use global keyword
fruit = "lemon"
def fruit_Name():
    #global keyword
    global fruit
    fruit="Mangoo"
    print(f"Inside func {fruit}")

fruit_Name()
print(f"Outside func {fruit}")
