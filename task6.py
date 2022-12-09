"""
*Реализовать структуру данных «Товары». Она должна  представлять собой список 
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже 
должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у 
пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый 
ключ — характеристика товара, например название, а значение — список значений-
характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
number = int(input('Введите количество товаров: '))
i = 1
product_lst = []  # структура данных"Товары"
lst_of_name = []  # список названий
lst_of_price = []  # список цен
lst_of_amt = []  # список количеств
while i <= number:
    goods = {"Название": input(f"Название {i}-го товара: "),
             "Цена": input("Цена: "),
             "Количество": input("Количество: "),
             "ед": input("Единицы измерения: ")}  # второй
    # эл.кортежа-словарь с параметрами
    a = (i, goods)  # кортеж с инф.об отд.товаре
    product_lst.append(a)
    lst_of_name.append(goods['Название'])
    lst_of_price.append(goods['Цена'])
    lst_of_amt.append(goods['Количество'])
    i = i + 1
print(*product_lst, sep='\n')
result_lst = {'Названия': lst_of_name, 'Цены': lst_of_price,
              'Количества': lst_of_amt}
print(f'Аналитика:  {result_lst}')