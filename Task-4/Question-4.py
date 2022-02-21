def palindrome(n) :
    if (rev == n) :
        print("True")
    else :
        print("False")
    
n = int(input("Number: "))
num = n
rev = 0
while (num > 0) :
    rev = rev*10+num%10
    num = num//10
    
palindrome(n)
