import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

if not os.path.exists("expenses.csv"):
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: "))

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!")


def view_expenses():
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def visualize_expenses():
    df = pd.read_csv("expenses.csv")
    if df.empty:
        print("❌ No expenses to show!")
        return
    category_sum = df.groupby("Category")["Amount"].sum()

    category_sum.plot(kind="bar", color="skyblue")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.show()
while True:
    print("\n---- Personal Expense Tracker ----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Visualize Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        visualize_expenses()
    elif choice == "4":
        break
    else:
        print("Exiting... Goodbye!")

