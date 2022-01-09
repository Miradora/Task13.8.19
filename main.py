# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


ticket = int(input('Сколько билетов хотите купить?\n'))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Возраст учаcтника {i}\n"))
    if age < 18:
        price.append(0)
    if 18 <= age < 25:
        price.append(990)
    if age >= 25:
        price.append(1390)
print(price)
print('Сумма билетов:', sum(price))
if ticket > 3:
    print('Сумма с учетом скидки:', sum(price) - sum(price)/100 * 10)

















