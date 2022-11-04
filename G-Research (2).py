# It was hopefully obvious this was coming. FizzBuzz, please.

def fizzbuzz(num):
    def addd(x):
        if x < 10:
            return x
        return addd(sum(map(int, str(x))))

    def three_multiple(x):
        return "fizz" if addd(x) in [0, 3, 6, 9] else ""

    def five_multiple(x):
        return "buzz" if str(x)[-1] in ["0", "5"] else ""

    def judge(x):
        result = three_multiple(x) + five_multiple(x)
        return x if not result else result


    return list(map(judge, range(num)))


print(fizzbuzz(20))
print(fizzbuzz(100))
