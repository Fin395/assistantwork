import pandas as pd


df = pd.read_excel(r'C:\Users\Sergei\OneDrive\Рабочий стол\расходы.xlsx', header=None)

dates_column = df.iloc[:, 0]
cost_column = df.iloc[:, 1]
companies_column = df.iloc[:, 2]

dates = dates_column.dt.date.tolist()
costs = cost_column.tolist()
companies = companies_column.tolist()

for index, row in df.iterrows():
    print(f"{row[0].strftime('%d.%m.%Y')} провести переговоры с представителями компании {row[2]}, бюджет: {row[1]}")
