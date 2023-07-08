#Problem 1:
#You are given a list of integers. Your task is to find the second largest number in the list.
#Write a Python function called find_second_largest(numbers) that takes a list of integers as input and returns the second largest number in the list.

def find_second_largest(numbers):
    
    '''
    The list is sorted in desceding order and it is token the second element of it representing the second largest number in the list
    '''
    
    numbers.sort(reverse=True)
    second_maximum = numbers[1]
    return second_maximum

#Problem 2:
#You are given a list of integers. Your task is to find the sum of all the even numbers in the list.
#Write a Python function called sum_even_numbers(numbers) that takes a list of integers as input and returns the sum of all the even numbers in the list.

#Method 1 using sum function 
def sum_even_numbers_1(numbers):
    
    '''
    It is used comprehension in sum function
    '''
    
    sum_even_elements = sum(number for number in numbers if not number%2)
    return sum_even_elements

#Method 2 using filter function 
def sum_even_numbers_2(numbers):
    
    '''
    It is used a filter in sum function with a lambda function
    '''
    
    sum_even_elements = sum(filter(lambda x: not x%2 ,numbers))
    return sum_even_elements

#Method 3 using simple iteration
def sum_even_numbers_3(numbers):
    
    '''
    The list is iterated with a for each element being checked
    '''
    
    sum_even_elements = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even_elements = sum_even_elements + number
    return sum_even_elements

if __name__ == "__main__":
    numbers_test = [5, 2, 7, 3, 9, 1]
    result = find_second_largest(numbers_test)
    print("The second largest number in the list is:" + str(result))
    
    number_test_1 = [5, 8, 10, 9, 1, 0, 2, 3]
    total_sum_even_1 = sum_even_numbers_1(number_test_1)
    print("The sum of even elements using sum() is: "+ str(total_sum_even_1))
    
    total_sum_even_2 = sum_even_numbers_2(number_test_1)
    print("The sum of even elements using filter() is: "+ str(total_sum_even_2))
    
    total_sum_even_3 = sum_even_numbers_3(number_test_1)
    print("The sum of even elements using simple iteration is: "+ str(total_sum_even_3))
    