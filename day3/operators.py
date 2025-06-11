age = 19
height = 1.65
complex_number = 3 + 4j

base = float(input())
height_triangle = float(input())
area = 0.5 * base * height_triangle
print("The area of the triangle is", area)

a = float(input())
b = float(input())
c = float(input())
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

length = float(input())
width = float(input())
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area:", area_rectangle)
print("Perimeter:", perimeter_rectangle)

radius = float(input())
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print("Area:", area_circle)
print("Circumference:", circumference)

x_intercept = 1
y_intercept = -2
slope = 2
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope:", slope_2)
print("Euclidean distance:", distance)

print(slope == slope_2)

x_values = [-3, -2, -1, 0, 1, 2, 3]
for x in x_values:
    y = x**2 + 6*x + 9
    print("x:", x, "y:", y)

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in 'dragon' and 'on' not in 'python')

length_python = len('python')
print(float(length_python))
print(str(length_python))

number = int(input())
print(number % 2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(float('9.8')) == 10)

hours = float(input())
rate = float(input())
pay = hours * rate
print("Your weekly earning is", pay)

years = int(input())
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
