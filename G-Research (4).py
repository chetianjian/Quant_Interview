# Q4：G-Research also has an inexplicable penchant for pi. The requirements are now
# such that if the number being tested, represented as a decimal's present in the
# first p digits of pi, also represented as a decimal and ignoring any decimal point,
# then "Pi" is emitted preferentially to Fizzes Buzzes or Prime. e.g. if p is 3 then
# we test against 314 and so 3,1,4,14,31 and 314 would all return "Pi".


def fizzbuzz(n, p):
    def addd(x):
        if x < 10:
            return x
        return addd(sum(map(int, str(x))))

    def three_multiple(x):
        return "fizz" if addd(x) in [0, 3, 6, 9] else ""

    def five_multiple(x):
        return "buzz" if str(x)[-1] in ["0", "5"] else ""

    def judge(x):
        merge = three_multiple(x) + five_multiple(x)
        if merge:
            return merge
        else:
            if (x % 2 == 0 and x != 2) or x == 1:
                return x
            for i in range(7, x // 2, 2):
                if x % i == 0:
                    return x
            return "prime"

    def remove_dot(x):
        return "".join(str(x).split("."))

    def getpi(x=p):
        i, approx, pos = (0, 0, 0)
        while pos < x:
            last, approx = approx, approx + 4 * (-1) ** i / (2 * i + 1)
            if remove_dot(last)[pos] == remove_dot(approx)[pos]:
                pos += 1
            i += 1
        return remove_dot(approx)[: p]

    def get_all_pi():
        s, index_set = getpi(x=p), set()
        for digits in range(1, min(len(str(n)) + 2, p)):
            for i in range(p):
                if int(s[i: i + digits]) <= n:
                    index_set = index_set | {int(s[i: i + digits])}
        return index_set

    indices, result = get_all_pi(), list(map(judge, range(n)))

    for _ in indices:
        result[_] = "pi"
    return result


print(fizzbuzz(15, 3))
print(fizzbuzz(20, 8))