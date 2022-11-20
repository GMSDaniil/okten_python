#####
try:
    with open('emails.txt', 'r') as emails:
        lines = []
        for line in emails:
            if line.split('\t\t\t')[1][:-1].endswith('@gmail.com'):
                lines.append(line.split('\t\t\t')[1][:-1])
        # print(lines)
except Exception as err:
    print(err)

############
import uuid
def menu():
    print("1 - Вивід всіх покупок")
    print("2 - Додати покупку в книгу")
    print("3 - Знайти покупку по айді, назві або ціні")
    print("4 - Показати найдорожчу покупку")
    print("5 - Видалити покупку по айді")
    print("6 - Вихід")

x = 0

while x!=6:
    menu()
    x = input()
    match x:
        case '1':
            try:
                with open('purchases.txt', 'r') as file:
                    purchases = []
                    for line in file:
                        l = line.split('\t\t')[1:]
                        l[1] = l[1][:-1]
                        purchases.append(l)
                    for name, price in purchases:
                        print(f'{name} costs {price}')

            except Exception as err:
                print(err)
        case '2':
            try:
                with open('purchases.txt', 'a') as file:
                    name = input('Введіть назву товару: ')
                    id = uuid.uuid1()
                    file.write(f'{id}\t\t')
                    file.write(name+'\t\t')
                    price = input('Введіть ціну товару: ')
                    file.write(price+'\n')
            except Exception as err:
                print(err)
        case '3':
            try:
                with open('purchases.txt', 'r') as file:
                    search = input('Введіть назву, айді або ціну товару: ')
                    if search.isalpha() or search.isalnum():
                        for line in file:
                            if search in line:
                                purchase = line.split('\t\t')
                                purchase[2] = purchase[2][:-1]
                                print(f'Id: {purchase[0]}\nName: {purchase[1]}\nPrice: {purchase[2]}\n')
                    elif search.isnumeric():
                        for line in file:
                            purchase = line.split('\t\t')
                            purchase[2] = purchase[2][:-1]
                            if search in purchase[2]:
                                print(f'Id: {purchase[0]}\nName: {purchase[1]}\nPrice: {purchase[2]}\n')
                    else:
                        print('Товару не існує')
            except Exception as err:
                print(err)
        case '4':
            try:
                with open('purchases.txt', 'r') as file:
                    purchases = []
                    prices = []
                    for line in file:
                        l = line.split('\t\t')
                        l[2] = l[2][:-1]
                        purchases.append(l)
                        prices.append(int(l[2]))
                    for id, name, price in purchases:
                        if int(price) == max(prices):
                            print(f'Id: {id}\nName: {name}\nPrice: {price}\n')
            except Exception as err:
                print(err)
        case '5':
            try:
                with open('purchases.txt', 'r') as file:
                    delete_id = input('Введіть айді: ')
                    new_file = ''
                    for line in file:
                        if delete_id in line:
                            pass
                        else:
                            new_file += line
                with open('purchases.txt', 'w') as file:
                    file.write(new_file)
            except Exception as err:
                print(err)
        case '6':
            pass
        case _:
            print('Error')




