income = {
  'SP': 67836.43,
  'RJ': 36678.66,
  'MG': 29229.88,
  'ES': 27165.48,
  'Outros': 19849.53
}

total = sum(income.values())

print("Representação por estado (%):")
for estado, value in income.itens():
  percentage = (value / total) * 100
  print(f"{estado}: {percentage:.2f}%")
