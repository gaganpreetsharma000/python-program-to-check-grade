def greet():
    return "Hello Students, Good Luck"
print(greet())
    
Score = int(input("Enter your score \n"))

if 90 <= Score <= 100:
    print("You have got A+")
elif 80 <= Score <= 89:
    print("You have got A")    
elif 70 <= Score <= 79:
    print("You have got B+")
elif 60 <= Score <= 69:
    print("You have got C")
elif 50 <= Score <= 59:
    print("You have got D")
elif 40 <= Score <= 49:
    print("You have got E ")
elif Score < 40:
    print("You have Failed")  
else:
    print("Enter the valid Score as mentioned in your Marksheet")
         
Feedback = input("Please submit your feedback, Thankyou \n")    
                         