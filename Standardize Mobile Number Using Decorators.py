def wrapper(f):

    def fun(l):

        formatted = []

        for i in l:

            num = i[-10:]

            formatted.append("+91 " + num[:5] + " " + num[5:])

        f(formatted)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':

    l = [input() for _ in range(int(input()))]

    sort_phone(l)
