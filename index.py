# Create a function that is able to tell us what the area of a triangle will be

def find_area(base, height):
    base = base/2
    height = height
    area = int(base * height)

    return f"The area of your triangle is {area}"

print(find_area(12, 5))