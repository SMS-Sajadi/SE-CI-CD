def add(x, y):
    my_sum = x + y
    print("The sum is:", my_sum)
    return my_sum


def minus(x, y):
    my_minus = x - y
    print("The minus is:", my_minus)
    return my_minus


def multiply(x, y):
    my_multiply = x * y
    print ("The multiply is:", my_multiply)
    return my_multiply


class temp:
    def __init__(self):
        pass

    def print_loop(self, x):
        for i in range(100):
            if i == x:
                print("I found x!")
                break
        print("I am done!")

    def hello_world(self, x):
        print("This world is amazing!", x)
        if x > 10: return True
        return False


def main():
    x, y = 2, 3
    summ = add(x, y)
    why = temp()
    for i in range(90, 110):
        why.print_loop(i)
    print(why.hello_world(10))
    return


if __name__ == "__main__": main()
