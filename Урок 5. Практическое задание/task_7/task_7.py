"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

earnings = {}
firms_earning = {}
data = [firms_earning, earnings]
sum_margin = 0
count_firm_avg = 0

with open("task7.txt", encoding='utf-8') as f:
    for line in f:
        name, form, salary, cost = line.split()
        margin = float(salary) - float(cost)
        if margin > 0:
            count_firm_avg = count_firm_avg + 1
            sum_margin = sum_margin + margin
            firms_earning[name] = margin
if count_firm_avg > 0:
    earnings["average_earning"] = sum_margin / count_firm_avg

with open("task_7.json", "w", encoding='utf-8') as write_f:
    json.dump(data, write_f)
print(f"{firms_earning} {earnings}")