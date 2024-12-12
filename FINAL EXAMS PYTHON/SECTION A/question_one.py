#1.(i)
def circle_area(radius):
    pie = 3.14
    area = pie*radius*2
    return area
radius = 4
area = circle_area(radius)
print(f"The area of the circle with radius:{radius} is: {area}")


#i.(ii)
#Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.

integers = [4, 7, 2, 9, 12, 15]
odd_sum = 0

for odd_numbers in integers:
    if odd_numbers %2 != 0:
        odd_sum += odd_numbers

print(f"The sum of odd number in the list of integers is: {odd_sum}")


#1(iii)
sum= 5
sum+=6
difference= 8
difference-=5
product=4
product*=3
quotient= 9
quotient/=3
print(f"sum {sum},difference{difference},product{product}and quotient{quotient}is:.")


#1.(v)

dict = {
    'age':26,
    'city':'Kampala' 
    }
print(dict)
