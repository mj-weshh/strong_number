"""
Strong number code task
Link: https://www.codewars.com/kata/5a4d303f880385399b000001
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
     print(f"{number} is {status}")


if __name__ == "__main__":
     #calls main()
     main()

     