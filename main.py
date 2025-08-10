
binary = input("Enter a binary number:")  
length = len(binary) 
result = 0  

for b in binary:
   int(b) 
   value = 2 ** (length - 1)  
   if b == "0":  
      final_value = 0 * value 
   elif b == "1": 
      final_value = 1 * value
   result += final_value  
   length -= 1

print("The decimal value is:", result) 
