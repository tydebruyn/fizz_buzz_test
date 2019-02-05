for x in range(100):
    y = x + 1

    #check if multiple of both three and five
    if y % 3 == 0 and y % 5 == 0:
        print("FizzBuzz")

    #check if multiple of three
    elif y % 3 == 0:
        print("Fizz")

    #check if multiple of five
    elif y % 5 == 0:
        print("Buzz")

    else:
        print(y)
