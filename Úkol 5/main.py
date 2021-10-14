def main():
    user_in = abs(int(input("FACTORIAL OF WHICH NUMBER DO YOU WANT: ")))
    print("FACTORIAL OF {} IS {}".format(user_in, factorial_loop(user_in)))
    print("FACTORIAL OF {} IS {}".format(user_in, factorial_recursion(user_in)))


def factorial_loop(user_in):
    out = 1
    if user_in > 1:
        for i in range(2, user_in + 1):
            out *= i
    return out


def factorial_recursion(user_in):
    if user_in < 2:
        return 1
    return user_in * factorial_recursion(user_in - 1)


if __name__ == '__main__':
    main()
