# 📆 Monthly Financial Dashboard  
**Python Automation | Personal Finance | Data Analytics**

This project analyzes monthly income and expenses over a period of time and produces a simple “dashboard” in the console.  
For each month, it calculates savings and savings ratio, classifies financial status, and prints risk warnings.

It’s a compact example of how Python can be used to automate basic FP&A-style personal finance analysis.

---

## 📌 Features

- Stores multiple months of **income** and **expenses**
- Calculates:
  - Monthly savings (`income - expense`)
  - Savings ratio (`savings / income`)
- Classifies each month as:
  - **Excellent**
  - **Good**
  - **Weak but Positive**
  - **Negative**
- Generates warnings when:
  - Expenses are more than **50%** of income
  - Savings ratio is below **10%** (low savings risk)
- Prints a clear report for each month

---

## 🛠 Tech Stack

- **Python 3**
- Dictionaries
- Lists
- For loops
- Conditional logic
- Basic financial calculations

---

## 🧮 How It Works

### Input structure

```python
finance = {
    'Income':   [2500, 2600, 2550, 2700, 2800],
    'Expenses': [1300, 1400, 1200, 1500, 1600],
    'Name': 'Abbas'
}
```

Each position in `Income` and `Expenses` represents one month.

The function:

```python
def monthly_calculation(data):
    ...
```

loops through each month and prints a report.

---

## 📊 Sample Output

```text
--- Month 1 report for Abbas ---
Income: 2500
Expense: 1300
Savings: 1200
Savings ratio: 0.48
Status: Excellent
Warning: Expense is more than 50% of the income
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/abbashumbatov/Monthly_Financial_Dashboard.git
cd Monthly_Financial_Dashboard
```

2. Run the script:

```bash
python main.py
```

---

## 💡 Why This Project Matters

This project demonstrates:

- Translating financial logic into code  
- Structuring data with dictionaries and lists  
- Applying classification and risk rules  
- Producing readable, structured console reports  

It’s a solid foundation for more advanced FP&A or budgeting tools in Python.

---

## 👤 Author

**Abbas Humbatov**  
Aspiring Financial Data Analyst  
🔗 LinkedIn: *https://www.linkedin.com/in/abbas-humbatov-/*
