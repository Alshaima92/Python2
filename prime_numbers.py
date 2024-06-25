

import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  
    

    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    
    return True  
     
      
x = int(input("Enter any number: "))

if x== 0:
    print ("Zero is neither prime nor composite. ")
elif is_prime(x):
  print(x, "is a prime number.")
else: 
  print(x, "is not a prime number.")



