# 💰 Expense Tracker (Python)

A simple, beginner-friendly **Expense Tracker** built in Python to help users record, track, and manage their daily expenses efficiently.  



## 📌 Features
- ➕ **Add Expenses** — Enter amount, category, and description
- 📜 **View All Expenses** — Displays all recorded expenses in a structured format
- 💾 **Auto-Save Data** — Saves expense history using file handling
- 🗂 **Organized Storage** — Stores data in a text file for later use
- 🖥 **Easy Navigation** — Simple command-line interface



## 🛠️ Technologies Used
- **Python 3**
- **File Handling (Read/Write)**
- **Basic Data Structures** — Lists & Dictionaries

---

## 📂 Project Structure
Expense_Tracker/
│
├── expense_tracker.py # Main program file
├── expenses.txt # Stores expense records
└── README.md # Project documentation


**CODE**
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




**HOW TO RUN 🚀**
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/expense-tracker.git

2.**Navigate to the project folder**
      cd expense-tracker

3.**Run the program**
      python expense_tracker.py

**SCREENSHOTS**
<img width="567" height="339" alt="image" src="https://github.com/user-attachments/assets/e0b4505b-a42a-4586-990f-4200e9d70ebf" />
<img width="641" height="322" alt="Screenshot 2025-08-27 130021" src="https://github.com/user-attachments/assets/cb0e8147-7477-4936-b540-a4be62291cfa" />





