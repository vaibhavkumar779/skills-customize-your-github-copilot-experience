import csv
import matplotlib.pyplot as plt


def load_sales_data(filepath):
    dates = []
    values = []
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row["Month"])
            values.append(float(row["Sales"]))
    return dates, values


def plot_sales_line(dates, values):
    plt.figure(figsize=(8, 4))
    plt.plot(dates, values, marker="o", color="blue", label="Sales")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("sales_line_chart.png")
    plt.show()


def plot_sales_bar(dates, values):
    plt.figure(figsize=(8, 4))
    plt.bar(dates, values, color="orange")
    plt.title("Monthly Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("sales_bar_chart.png")
    plt.show()


if __name__ == "__main__":
    filepath = "sample-data.csv"
    dates, values = load_sales_data(filepath)
    print("Loaded months:", dates)
    print("Sales values:", values)
    plot_sales_line(dates, values)
    plot_sales_bar(dates, values)
