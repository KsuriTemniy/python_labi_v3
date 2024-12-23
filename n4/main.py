import math
import numpy as np
import matplotlib.pyplot as plt

import logging
import seaborn as sns

logging.basicConfig(level=logging.WARNING)


def f(x: float) -> float:
    return 2 * x


def func_c(x: float, y: float) -> float | None:
    if x - y == 0:
        return f(x) ** 2 + y ** 2 + math.sin(y)
    elif x - y > 0:
        return (f(x) - y) ** 2 + math.cos(y)
    else:
        if y == math.pi / 2:
            logging.warning("Tan isn't defined in point pi/2")
            return None
        return (y - f(x)) ** 2 + math.tan(y)


def func_g(x: float, b: float) -> float | None:
    if 0.5 < x * b < 10:
        return math.exp(f(x) - abs(b))
    elif 0.1 < x * b < 0.5:
        return math.sqrt(abs(f(x) + b))
    else:
        return 2 * f(x) ** 2


def create_array(name_of_variable: str) -> np.array(float):
    print(f"Enter start, end, number of points for {name_of_variable}")
    try:
        start, end, n = map(int, input().split())
    except ValueError:
        logging.warning("Invalid input. Please enter three integers.")
        return

    return np.linspace(start, end, n)


def plot_func_c_g(x: np.array(float),
                  y: np.array(float),
                  b: np.array(float),
                  c: np.array(float),
                  g: np.array(float)) -> None:
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, c, label="c (x, y)", color='blue')
    ax.plot(x, b, g, label="g (x, b)", color='red')

    ax.set_xlabel("x")
    ax.set_ylabel("y / b")
    ax.set_zlabel("z (c / g)")

    ax.legend()
    plt.show()

    plt.savefig("plots/task_1_plot.png", format="png")
    plt.savefig("plots/task_1_plot.pdf", format="pdf")

    plt.close()


def task_1() -> None:
    x = create_array("x")
    y = create_array("y")
    b = create_array("b")

    c = np.array([func_c(x=xi, y=yi) for xi, yi in zip(x, y)])
    g = np.array([func_g(x=xi, b=bi) for xi, bi in zip(x, b)])

    plot_func_c_g(x=x, y=y, b=b, c=c, g=g)


def task_2(sdv: float = 0.5, size: int = 50) -> None:
    if sdv < 0:
        logging.warning("Standard deviation must be non-negative")
        sdv = 0.5

    means = np.random.randint(0, 10, 6)

    x1 = np.random.normal(loc=means[0], scale=sdv, size=size)
    y1 = np.random.normal(loc=means[1], scale=sdv, size=size)

    x2 = np.random.normal(loc=means[2], scale=sdv, size=size)
    y2 = np.random.normal(loc=means[3], scale=sdv, size=size)

    x3 = np.random.normal(loc=means[4], scale=sdv, size=size)
    y3 = np.random.normal(loc=means[5], scale=sdv, size=size)

    plt.figure(figsize=(10, 7))

    plt.scatter(x1, y1, color='red', label='Cluster 1')
    plt.scatter(x2, y2, color='blue', label='Cluster 2')
    plt.scatter(x3, y3, color='green', label='Cluster 3')

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.title("Scatter Plot with 3 Clusters")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.savefig("plots/task_2_scatter.png", format="png")
    plt.savefig("plots/task_2_scatter.pdf", format="pdf")

    plt.close()


def task_3() -> None:
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    preferences = [20, 30, 15, 25, 10]

    plt.figure(figsize=(6, 6))
    plt.pie(preferences, labels=categories, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title("User Preferences")
    plt.show()

    plt.savefig("plots/task_3_piechart.png", format="png")
    plt.savefig("plots/task_3_piechart.pdf", format="pdf")

    plt.close()


def task_4() -> None:
    matrix = np.random.rand(10, 10)

    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=False, cmap='coolwarm', cbar=True)
    plt.title("Heatmap of Random Matrix")
    plt.show()

    plt.savefig("plots/task_4_heatmap.png", format="png")
    plt.savefig("plots/task_4_heatmap.pdf", format="pdf")

    plt.close()


def task_5() -> None:
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']

    values = [50, 30, 70, 40, 60]

    plt.figure(figsize=(8, 6))
    plt.barh(categories, values, color=sns.color_palette("muted"))
    plt.xlabel("Values")
    plt.ylabel("Categories")
    plt.title("Horizontal Bar Chart")
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

    plt.savefig("plots/task_5_barchart.png", format="png")
    plt.savefig("plots/task_5_barchart.pdf", format="pdf")

    plt.close()


def task_7() -> None:
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

    ax.set_title("Surface Plot of z = sin(sqrt(x^2 + y^2))")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    fig.colorbar(surf, shrink=0.5, aspect=10)

    plt.show()

    plt.savefig("plots/task_7_surfaceplot.png", format="png")
    plt.savefig("plots/task_7_surfaceplot.pdf", format="pdf")

    plt.close()


def main() -> None:
    np.random.seed(42)

    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_7()


if __name__ == "__main__":
    main()
