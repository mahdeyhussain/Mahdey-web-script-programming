#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Mahdey Hussain
#student# 100874046

#calculator.py

#ask for input

op = ""
ans = 0
while op != 'exit' and op != 'stop':
    op = input("What mathematical operator would you like to use?: ") 
    if op == 'stop' or op == 'exit':
        break
        
    num1 = input("Enter a number: ")
    if num1 == 'stop' or num1 == 'exit':
        break
    elif num1 == "" :
        num1 = ans
        
    num2 = input("Enter a second number: ")
    if num2 == 'stop' or num2 == 'exit':
        break
    elif num2 == "" :
        num2 = ans  
    
    num1 = float(num1)
    num2 = float(num2)
    
    #identify operator
    if op == "+" or op == "add":
        ans = num1 + num2
    elif op == "-" or op == "subtract":
        ans = num1 - num2
    elif op == "*" or op == "multiply":
        ans = num1 * num2
    elif op == "/" or op == "divide":
        ans = num1 / num2
    elif op == "**" or op == "raise" or op == "exponent":
        ans=1
        for x in range(int(num2)):
            ans = ans * num1
        
        
    print(ans)


# In[ ]:




