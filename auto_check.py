#is_next = None
#num = int(input("Enter the number of points: "))
#is_next = (num >= 83)
#if is_next:
#    print("Passed")
#else:
#    print("Failed")

#work_experience = int(input("Enter your full work experience in years: "))
#if work_experience > 1 and work_experience <=5:
#    developer_type = "Middle"
#elif work_experience <=1:
#    developer_type = "Junior"
#else:
#    developer_type = "Senior"
#print("Your work experience is", developer_type)

#num = int(input("Enter a number: "))
#if num > 0:
#    if num %2 == 1:
#        result = "Positive odd number"
#    else:
#        result = "Positive even number"
#elif num < 0:
#    result = "Negative number"
#else:
#    result = "It is zero"
#print(result)

#num = int(input("Enter the integer (0 to 100): "))
#sum = 0
#while num > 0:
#    sum += num
#    num -=1
#print(sum)

#message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
#search = "r"
#result = 0
#for symb in message:
#    if symb == search:
#        result += 1
#print(result)

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = int(pool/quantity)
    print(f"The size of mailings is {chunk} ")
except ZeroDivisionError:
    print('Divide by zero forbidden!')