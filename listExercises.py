import sys
import random
#Problem 1:
#You are given a list of integers. Your task is to find the second largest number in the list.
#Write a Python function called find_second_largest(numbers) that takes a list of integers as input and returns the second largest number in the list.

#Method 1 sorting the list desceding and taking the second element 
def find_second_largest_1(numbers):
    
    '''
    The list is sorted in desceding order and it is token the second element of it representing the second largest number in the list
    '''
    
    numbers.sort(reverse=True)
    second_maximum = numbers[1]
    return second_maximum

#Method 2 sorting the list asceding and taking the second element 
def find_second_largest_2(numbers):
    
    '''
    The list is sorted in asceding order and it is token the last but one element of it representing the second largest number in the list using negative index
    '''
    
    numbers.sort()
    second_maximum = numbers[-2]
    return second_maximum

#Method 3 finding the first maxim element and remove from list and again using maz function
def find_second_largest_3(numbers):
    
    first_maximum = max(numbers)
    numbers.remove(first_maximum)
    second_maximum = max(numbers)
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

#Problem 3 
#You are given a list of integers. Your task is to find the maximum difference between any two numbers in the list.
#Write a Python function called max_difference(numbers) that takes a list of integers as input and returns the maximum difference between any two numbers in the list.

#Method 1 using sort
def max_difference_1(numbers):
    
    '''
    The list is sorted descending and after that we return the defference between first and last element
    '''
    
    numbers.sort(reverse=True)
    maximum_diff = 0 
    maximum_diff = numbers[0] - numbers[-1]
    return maximum_diff

#Method 2 using min and max
def max_difference_2(numbers):
    
    '''
    With find the maximum and minimum elements in list and then we make difference betwen them
    '''
    
    max_element = max(numbers)
    min_element = min(numbers)
    difference = max_element - min_element
    return difference

#Method 3 using simple iteration
def max_difference_3(numbers):
    
    '''
    It is made diferrence betweeneach element and try to find the maximum
    '''
    maximum_dif = -sys.maxsize - 1
    for i in numbers:
        for j in numbers:
            if abs(i-j) > maximum_dif:
                maximum_dif = abs(i-j) 
    
    return maximum_dif


#Challenge
#Given a list of distinct integers between 1 and 100 with length 99, how do you find out the number not present in the array as efficiently as possible (array is not sorted)
def generate_list():
    elements = []
    for i in range(1, 101):
        elements.append(i)
    random.shuffle(elements)
    elements.remove(9)
    return elements

def find_missing_element(numbers):
    sum_of_elements = 0
    gauss_sum = 100*(100 + 1)/2
    sum_of_elements = sum(number for number in numbers)
    missing_element = gauss_sum - sum_of_elements
    return missing_element
    


if __name__ == "__main__":
    #Testing functions for problem 1
    numbers_test = [5, 2, 7, 3, 9, 1]
    result = find_second_largest_1(numbers_test)
    print("The second largest number in the list using descending sort is:" + str(result))
    
    result = find_second_largest_2(numbers_test)
    print("The second largest number in the list using ascending sort is:" + str(result))
    
    result = find_second_largest_3(numbers_test)
    print("The second largest number in the list using max() and remove() is:" + str(result))
    
    print("\n")
    #Testing functions for problem 2
    number_test_1 = [5, 8, 10, 9, 1, 0, 2, 3]
    total_sum_even_1 = sum_even_numbers_1(number_test_1)
    print("The sum of even elements using sum() is: "+ str(total_sum_even_1))
    
    total_sum_even_2 = sum_even_numbers_2(number_test_1)
    print("The sum of even elements using filter() is: "+ str(total_sum_even_2))
    
    total_sum_even_3 = sum_even_numbers_3(number_test_1)
    print("The sum of even elements using simple iteration is: "+ str(total_sum_even_3))
    
    print("\n")
    #Testing functions for problem 3
    numbers_test_2 = [1, 3, 6, 7, 11, 9, 23]
    difference_1 = max_difference_1(numbers_test_2)
    print("Maximum difference between any two elements using sort is : "+str(difference_1))
    
    difference_2 = max_difference_2(numbers_test_2)
    print("Maximum difference between any two elements using min and max is : "+str(difference_2))
    
    difference_3 = max_difference_3(numbers_test_2)
    print("Maximum difference between any two elements using min and max is : "+str(difference_3))
    
    
    print("\n")
    #Testing functions for challenge
    numbers_test_3 = generate_list()
    print("The list of 99 elements :")
    print(numbers_test_3)
    
    element_missed = find_missing_element(numbers_test_3)
    element_missed = int(element_missed)
    print("The missing element is :" + str(element_missed))