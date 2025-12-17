from data_loader import load_expenses
from report_generator import generate_summary, plot_summary

def main():
    df = load_expenses("data/sample_expenses.csv")
    summary = generate_summary(df)
    print(summary)
    plot_summary(summary)

if __name__ == "__main__":
    main()
