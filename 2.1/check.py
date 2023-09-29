product_name = input()
product_cost_per_kilo = int(input())
product_weight = int(input())
customer_money = int(input())
total_cost = product_weight * product_cost_per_kilo
change = customer_money - total_cost

print('Чек')
print(f'{product_name} - {product_weight}кг - {product_cost_per_kilo}руб/кг')
print(f'Итого: {total_cost}руб')
print(f'Внесено: {customer_money}руб')
print(f'Сдача: {change}руб')
