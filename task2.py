salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

counter = 0
money_capital = 0

while counter < months:
    money_capital -= salary
    money_capital += spend
    spend *= 1 + increase
    counter += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
