"""
Fibonacci numbers

0, 1, 1, 2, 3, 5, 8, 13, ....

Write a function that gets the nth term in a Fibonnaci sequence:
fib(0) = 0 , 1 calls
fib(3) = fib(2) + fib(1) = fib(1) + fib(0) + fib(1), 3 calls
fib(5)  = fib(4) + fib(3)
        = (fib(3) + fib(2)) + (fib(2) + fib(1))
        = ((fib(2) + fib(1)) + (fib(1) + fib(0)))
            + (fib(1) + fib(0)) + fib(1): 8 calls to fib()
        

"""
import timeit

def fib(n):
    assert n >= 0

    fib_num = None

    # ending conditions
    if n < 2:
        fib_num = n
    else:
        # recursive call
        fib_num = fib(n - 1) + fib(n - 2)

    return fib_num

# rewrite the function using memoization
# use a dictionary to store intermediate results
def memo_fib(n, state={}):
    assert n >= 0

    fib_num = None

    # check if memo_fib(n) is already computed
    if n in state.keys():
        fib_num = state[n]
    else:
        # ending conditions
        if n < 2:
            fib_num = n
        else:
            # recursive call
            fib_num = memo_fib(n - 1) + memo_fib(n - 2)

        # store the result in state
        state[n] = fib_num

    return fib_num


if __name__ == '__main__':

    try:
        # fibs = [fib(i) for i in range(10)]
        # print(fibs)
        # print(fib(35)) # 9227465
        # print(memo_fib(500)) 

        for i in range(10):
            t = timeit.timeit(f'fib({i})', setup="from __main__ import fib")
            print(f'n = {i}: {t} seconds')

        for i in range(10):
            t = timeit.timeit(f'memo_fib({i})', setup="from __main__ import memo_fib")
            print(f'n = {i}: {t} seconds')

        # how to plot performance using matplotlib?


    except AssertionError:
        print('Invalid input to fib()')