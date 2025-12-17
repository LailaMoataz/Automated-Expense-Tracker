import matplotlib.pyplot as plt

def generate_summary(df):
    summary = df.groupby("category")["amount"].sum()
    return summary

def plot_summary(summary):
    summary.plot(kind="bar", figsize=(8,5), title="Total Expenses by Category")
    plt.ylabel("Amount")
    plt.show()
