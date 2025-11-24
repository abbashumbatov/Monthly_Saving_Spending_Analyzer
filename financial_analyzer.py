# Day 7 - Mini Project for the Weekend


finance={
    'Income':[2500,2600,2550,2700,2800],
    'Expenses':[1300,1400,1200,1500,1600],
    'Name':'Abbas'
}


def monthly_calculation(data):
    incomes=data['Income']
    expenses=data['Expenses']
    name=data['Name']

    for i in range(len(incomes)):
        income=incomes[i]
        expense=expenses[i]
        savings=income-expense
        ratio=savings/income

        print(f'\n--- Month {i+1} report for {name} ---')
        print(f'Income: {income}')
        print(f'Expense: {expense}')
        print(f'Savings: {savings}')
        print(f'Savings ratio: {ratio:.2f}')

        # Classification

        if ratio>0.40:
            print('Status: Excellent')
        elif ratio>0.20:
            print('Status: Good')
        elif ratio>0:
            print('Status: Weak but Positive')
        else:
            print('Status: Negative')

        # Warnings

        if expense>income*0.5:
            print('Warning: Expense is more than 50% of the income')

        if ratio<0.1:
            print('Risk: Low savings rate')


monthly_calculation(finance)


