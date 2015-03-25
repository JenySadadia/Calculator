
while True:
    op=int(input('''Enter the operation which you would like to b performed :-
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division'''))


    if op==1:
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x+y)
        
    	
    
    elif op==2:
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x-y)
       
    
    elif op==3:
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x*y)
        
 
    elif op==4:
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x/y)
       
  
    else:
        print("invalid choice")
        
        
    