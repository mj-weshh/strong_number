"""
DESCRIPTION:
Strong number is a number with the sum of the factorial of its digits is equal to the number itself.
For example, 145 is strong, because 1! + 4! + 5! = 1 + 24 + 120 = 145.
Task
Given a positive number, find if it is strong or not, and return either "STRONG!!!!" or "Not Strong !!".
Examples
1 is a strong number, because 1! = 1, so return "STRONG!!!!".
123 is not a strong number, because 1! + 2! + 3! = 9 is not equal to 123, so return "Not Strong !!".
145 is a strong number, because 1! + 4! + 5! = 1 + 24 + 120 = 145, so return "STRONG!!!!".
150 is not a strong number, because 1! + 5! + 0! = 122 is not equal to 150, so return "Not Strong !!".
"""

def factorial(num):
     #converts the str argument to an int
     num = int(num)
     #initializes the factorial product to 1
     factorail_product = 1
     
     #calculates the factorial product
     while num >= 1:
          factorail_product *= num
          num -=1
     
     return factorail_product


def strong(number):
     #number is a str
     number_int = int(number)
     factorials= []
     sum = 0
     status = ''
     
     for i in number:
          #appends the digit elements into factorials
          factorials.append(i)
     
     for j in factorials:
          #calls factorial() and sums up all the factorials
          sum += int(factorial(j))
     #outputs sum of factorials
     print(f"Sum of factorials is: {sum}")

     #checks whether the number is strong or not
     if sum == number_int:
          status = "Strong!!!"
     else:
          status = "Not Strong!!"
     
     return status


def main():
     #user inputs a number (recieved as a str)
     number = input("Enter number: ")
     #calls strong() 
     status =  strong(number)
     #outputs the status of the number
     #whether strong or not strong
     print(f"{number} is {status}7")


if __name__ == "__main__":
     #calls main()
     main()