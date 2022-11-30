for x in range(1, 101):
    if x % 15 == 0:
        print(x, 'FizzBuzz')
    elif x % 3 == 0:
        print(x, 'Fizz')
    elif x % 5 == 0:
        print(x, 'Buzz')