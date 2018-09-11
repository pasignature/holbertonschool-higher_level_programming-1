def fizzbuzz():
    for n in range(1, 101):
        if not n % 3:
            print("Fizz", end='')
        if not n % 5:
            print("Buzz", end='')
        if n % 3 and n % 5:
            print("{:d}".format(n), end='')
        print(" ", end='')
