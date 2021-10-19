import timeit, time
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def fib(n):
    assert n >= 0
    fib_num = None

    if n < 2:
        fib_num = n
    else:
        fib_num = fib(n - 1) + fib(n - 2)

    return fib_num

def memoized_fib(n, state={}):
    assert n >= 0
    fib_num = None

    if n in state.keys():
        return state[n]
    else:
        if n < 2:
            fib_num = n
        else:
            fib_n_2 = memoized_fib(n - 2, state)
            fib_n_1 = memoized_fib(n - 1, state)
            fib_num = fib_n_1 + fib_n_2
        
        state[n] = fib_num

    return fib_num

def plot_performance(times1, times2):
    # using plotly
    # fig = px.line(x=range(len(times1)), y = [times1, times2])
    # fig.show()

    # fig = go.Figure()
    # fig.add_trace(go.Scatter(
    #     x=[i for i in range(len(times1))],
    #     y=times1,
    #     name = 'fib()', # Style name/legend entry with html tags
    #     connectgaps=True # override default to connect the gaps
    # ))
    # fig.add_trace(go.Scatter(
    #     x=[i for i in range(len(times2))],
    #     y=times2,
    #     name='memoized_fib()',
    # ))
    # fig.update_layout(title='Function performance',
    #                xaxis_title='Fibonacci number calculated',
    #                yaxis_title='Seconds')
    # fig.show()

    # using matplotlib
    plt.plot(range(len(times1)), times1, label='fib') 
    plt.plot(range(len(times2)), times2, label='memoized fib')
    plt.xlabel('Calculated fibonacci number')
    plt.ylabel('Time (seconds)')
    leg = plt.legend()
    plt.show()

if __name__ == '__main__':
    # print(memoized_fib(100))

    # num_times = 10
    # t = timeit.timeit(f"fib({num_times})", setup="from __main__ import fib")
    # print(f'{t} microseconds')

    # t = timeit.timeit("memoized_fib(20)", setup="from __main__ import memoized_fib")
    # print(f'{t} microseconds')

    count = 10
    fib_times = []
    for i in range(count):
        fib_times.append(
            timeit.timeit(f"fib({i})", setup="from __main__ import fib")
        )

    memoized_fib_times = []
    for i in range(count):
        memoized_fib_times.append(
            timeit.timeit(f"memoized_fib({i})", 
                setup="from __main__ import memoized_fib")
        )

    plot_performance(fib_times, memoized_fib_times)