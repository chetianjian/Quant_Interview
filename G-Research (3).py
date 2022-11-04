# We quite like prime numbers at G-Research. We also often face requirements
# that are unknown at the start of software engineering and have to evolve to
# follow where the research leads. We'd now like FizzBuzz but with the added
# complexity of prime numbers being preferentially emitted as "Prime".


def fizzbuzz(num):
    def addd(x):
        if x < 10:
            return  x
        return addd(sum(map(int, str(x))))

    def three_multiple(x):
        return "fizz" if addd(x) in [0, 3, 6, 9] else ""

    def five_multiple(x):
        return "buzz" if str(x)[-1] in ["0", "5"] else ""

    def judge(x):
        result = three_multiple(x) + five_multiple(x)
        if result:
            return result
        else:
            if (x % 2 == 0 and x != 2) or x == 1:
                return x
            for i in range(7, x//2, 2):
                if x % i == 0:
                    return x
            return "prime"


    return list(map(judge, range(num)))


print(fizzbuzz(20))
print(fizzbuzz(100))