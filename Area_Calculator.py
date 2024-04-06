import math

print('=================')
print(' Area Calculator ')
print('=================')

while True:
    options = '''
    Select an Option
        1. Triangle
        2. Rectangle
        3. Square
        4. Circle
        5. Quit
    '''
    print(options)

    try:
        shape = int(input('Enter your chosen option: '))

        if shape == 1: 
            base = int(input('Base: '))
            height = int(input('Height: '))
            area = 1/2 * base * height
            print('Area of Triangle:', area)
            break
        elif shape == 2: 
            length = int(input('Length: '))
            width = int(input('Width: '))
            area = length * width
            print('Area of Rectangle:', area)
            break
        elif shape == 3:
            side = int(input('Size: '))
            print('Area of Square:', side * side)
            break
        elif shape == 4:
            radius = int(input('Radius: '))
            print('Area of Circle:', math.pi * (radius * radius))
            break
        elif shape == 5:
            print('Goodbye!')
            break  # Exit the loop and end the program
        else:
            print('Invalid option. Please try again.')

    except ValueError:
        print('Invalid input. Please enter a valid option.')

    # Optionally, you can add a prompt here to continue or quit the program
    # based on user input
    # choice = input('Do you want to continue (yes/no)? ')
    # if choice.lower() != 'yes':
    #     print('Goodbye!')
    #     break  # Exit the loop and end the program
