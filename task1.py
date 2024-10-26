money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital
counter = 0

while True:
    budget += salary
    budget -= spend
    spend *= 1 + increase
    if budget >= 0:
        counter += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", counter)
