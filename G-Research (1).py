# Q1：Everyone has heard of "FizzBuzz". If you haven't: Google it. You are allowed
# to use the internet during this test. We'd like you to implement "FizzBuzz" please.
# Except at G-Research we often see the Pareto principle (or "80/20 rule") and
# generally believe in agile incremental delivery, so to make it easier we actually
# just want the Fizzes and not any Buzzes, please.


def fizzbuzz(num):
    def addd(x):
        if x < 10:
            return x
        return addd(sum(map(int, str(x))))


    def three_multiple(x):
        return "fizz" if addd(x) in [3, 6, 9] else x


    return list(map(three_multiple, range(num)))


print(fizzbuzz(20))
print(fizzbuzz(100))