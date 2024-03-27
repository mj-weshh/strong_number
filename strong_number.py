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
#factorail function takes in a string input, conver
def factorial(num):
     factorail_product = 1
     num = int(num)
     
     while num >= 1:
          factorail_product *= num
          num -=1
     
     return factorail_product

def strong(number):
     number_int = int(number)
     factorials= []
     sum = 0
     status = ''
     
     for i in number:
          factorials.append(i)
     
     for j in factorials:
          sum += int(factorial(j))
     print(f"Sum of factorials is: {sum}")
     
     if sum == number_int:
          status = "Strong!!!"
     else:
          status = "Not Strong!!"
     
     return status


def main():
     number = input("Enter number: ")
     status =  strong(number)
     print(f"{number} is {status}")


if __name__ == "__main__":
     main()