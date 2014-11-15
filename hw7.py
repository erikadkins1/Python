#simple "printing" calulator" program in Python

# initial values defined

total = 0.0

value = ["E","e","A","s","S","a","m","M","D","d","P","p"]

#start of operations

while (1):
        
        # user input gathered, split, converted, and stored
	
        store = raw_input("enter number and operator:")
	
        var = store.split(",")	
	
        num = float(var[0])
	
        #inital accumulator input
        
        if var[1] == "e" or var[1] == "E":
                
                total = num
	        
                print(total)
        
        #addition funtion
	
        if var[1] == "a" or var[1] == "A":
                
                total = total + num
                
                print(total)
        
        #subtraction function
        
        if var[1] == "S" or var[1] =="s":
                
                total = total - num
                
                print(total)
        
        # multiplication function
	
        if var[1] == "M" or var[1] =="m":
                
                total = total * num
                
                print(total)
        
        # division function

	if var[1] == "D" or var[1] =="d":

                if var[0]=="0":  # error protection statment

                        print("attempt to divide by zero - please re-enter")
                else:
                        total = total / num
                        
                        print(total)
        
        # power function
	
        if var[1] == "p" or var[1] =="P":
                
                if num < 0:      #error prtection statment

                        print("negative powers are not allowed - please re-enter")
                else:
                        total = total ** num
                        
                        print(total)
        
        #termination function
        
        if var[1]=="t" or var[1]=="T":
                
                break # dont know if this was ok dont know another way to terminate
        
        if not var[1] in value: #compares  array to input for invalid operators
                
                print("an invalid operator was entered - please re-enter")
