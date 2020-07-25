import simpleplot

coords = [ (n, n) for n in range(10)]

def f(n):
    return 1000 * 1.15 ** (n - 1)

def g(n):
    return 1000 * n

def make_plot(fun1, fun2, plot_length):
    points = []
    fun1_points = [(x, fun1(x)) for x in range(1, plot_length)]
    fun2_points = [(x, fun2(x)) for x in range(1, plot_length)]
    for x in range(1, plot_length):
        points.append((x, float(fun1(x)) / fun2(x)))
    simpleplot.plot_lines("Growth rate comparison", 400, 600,
                      "x", "f(x) / g(x)", [points, fun1_points, fun2_points], True,
                         ["f(x) / g(x)", "f(x)", "g(x)"])
    
make_plot(f, g, 30)