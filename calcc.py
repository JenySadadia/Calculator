op=int(input('''Enter the operation which you would like to b performed :-
....1.Addition
....2.Subtracton
....3.Multiplication
....4.Division'''))


x=int(input("enter x")) 
y=int(input("enter y"))

while 0<op<5:

    if op==1:
        print(x+y)
        break
    	
    
    elif op==2:
        print(x-y)
        break
    
    elif op==3:
        print(x*y)
        break
 
    elif op==4:
        print(x/y)
        break
  
    else:
        print("invalid choice")
        break
        
    