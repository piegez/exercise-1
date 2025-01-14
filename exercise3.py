import json
from statistics import mean

def income_analysis(data):
  valid_income = [day['valor'] for day in data if day['valor'] > 0]

  min_income = min(valid_income)
  max_income = max(valid_income)

  avg_income = mean(valid_income)

  days_above_average = sum(1 for value in valid_income if value > avg_income)

  return min_income, max_income, days_above_average

with open('dados.json', 'r') as file:
  income_data = json.load(file)

min_value, max_value, days_above_avg = analyze_income(income_data)

print(f"Menor faturamento: R$ {min_value: .2f}")
print(f"Maior faturamento: R$ {max_value: .2f}")
print(f"Número de dias com faturamento acima da média determinada: {days_above_?avg}")
