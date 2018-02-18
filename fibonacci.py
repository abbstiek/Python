###     Abygail Stiekman        ##
##           aes15d             ##
##          6/20/2017           ##

from __future__ import print_function

class Fibonacci(object):

    numseq = 0
    nums = [0,1]

    def __init__(self, n):
        self.numseq = n
        self.fill_list()

    def __iter__(self):
        self.a, self.b, self.index = 0, 1, 0
        return self

    def __next__(self):
        return self.next()

    def next(self):
        fib = self.a
        if self.index == self.numseq:
            raise StopIteration
        else:
            self.index += 1
            self.a, self.b = self.b, self.a + self.b
            return fib

    def fill_list(self):
        fib1, fib2 = 0, 1

        while fib2 < self.numseq:
            self.nums.append(fib2)
            fib1, fib2 = fib2, fib1+fib2

    def get_nums(self):
        return self.nums

    def __str__(self):
        fiblist = "The first " + str(self.numseq) \
        + " Fibonacci numbers are " + str(self.nums)
        return fiblist

def fibonacci_gen(N=10):
    if N == 0:
        yield 0
    for i in Fibonacci(N):
        yield i

def fun():
    for i in fibonacci_gen(10):
        print(i)

if __name__ == "__main__":
    fun()