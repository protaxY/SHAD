name = input()
cost_per_kilo = int(input())
weight = int(input())
customer_money = int(input())

print('================Чек================')
print(f'Товар:{name:>29}')
cost_suffix = f'{weight}кг * {cost_per_kilo}руб/кг'
print(f'Цена:{cost_suffix:>30}')
print(f'Итого:{weight * cost_per_kilo:>26}руб')
print(f'Внесено:{customer_money:>24}руб')
print(f'Сдача:{(customer_money - weight * cost_per_kilo):>26}руб')
print('===================================')