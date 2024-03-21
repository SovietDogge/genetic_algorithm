import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(12)


def func(x, y):  # main
    return abs(x) + y

# def func(x, y):
#     # x, y = individual
#     return x ** 2 - y ** 2


# def func(x, y):
#     return x ** 2 - y ** 2


def to_xlsx(**kwargs):
    df = pd.DataFrame({arg: value for arg, value in kwargs.items()})
    # with pd.ExcelWriter('test.xlsx') as file:
    #     df.to_excel(file)
    # plt.plot = df.loc[:53, 'x'].plot()
    # plt.ylabel('x value')
    # plt.plot = df.loc[:53, 'fit_value'].plot()
    # plt.ylabel('fitness value')
    # plt.plot(df['adapt_value'][:53])
    # plt.plot = df.loc[:53, 'adapt_value'].plot()
    # plt.ylabel('adaptation value')
    plt.plot(df['y'])
    plt.plot = df.loc[:53, 'y'].plot()
    plt.ylabel('y')
    plt.xlabel('Iteration')
    plt.show()
