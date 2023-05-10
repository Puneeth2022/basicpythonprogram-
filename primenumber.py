print("welcom to  prime number checker")

#defining a function for prime number check
def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")


        
#taking an input to check whether is it prime number
number =int(input("enter the number to check\n"))
#calling prime checker function
prime_checker(number)