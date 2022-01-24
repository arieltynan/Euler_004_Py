# Euler Problem 004
# Solved January 2021

# Largest palindrome product
# largest palindrome made from the product of two 3-digit numbers.

import math

pal = 999*999 # max possible number

while pal > 10000: #10000 is min possible product of two 3-digit numbers
    fpal = pal #forward palindrome number
    rpal = 0 #reverse palindrome number 
    while fpal > 0: #while loop to reverse integer
        rem = fpal % 10
        rpal = rpal * 10 + rem
        fpal = fpal // 10
    if pal == rpal: #if integer is equal to reverse of itself (palindrome)
        num = 999
        while num > 99: # 100 is minimum 3 digit integer 
            if pal % num != 0: #check for divisibility
                num = num - 1
            else:
                if pal // num > 999: #checks for both divisors being 3 digits
                    num = num - 1
                else:
                    print("Largest palindrome is: ", pal)
                    # print("Divisor: ", num)
                    num = 0 # exits loop
                    pal = 0 # exits loop

    pal = pal - 1