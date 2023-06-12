# -*- coding: utf-8 -*-
# flag = "YES"
# for i in range(10):
#     a = int(input())
#     if a % 2 != 0:
#         flag = "NO"
# print(flag)
mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

codes_info = [
    "",
    "1 — число цели, которая проявляется в форме агрессивности и амбиций",
    "2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
    "3 — неустойчивость, объединяет талант и веселость, символ приспосабливаемости",
    "4 — означает устойчивость и прочность",
    "5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту. С одной стороны, это самое счастливое число, с другой — самое непредсказуемое",
    "6 — символ надежности. Идеальное число, которое делится как на четное, так и на нечетное, объединяя элементы каждого",
    "7 — символизирует тайну, а также изучение и знание, как путь исследования неизвестного и невидимого",
    "8 — число материального успеха, означает надежность, доведенную до совершенства, символ всеобщего успеха",
    "9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
]
# здесь ничего менять не нужно, это готовый код, который считает "число имени"
def calc_namecode(name):
    letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
               "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

    name = name.upper()
    code = 0
    for letter in name:
        try:
            ltr_code = letters.index(letter) % 9
        except:
            continue
        if ltr_code == 0:
            ltr_code = 9
        code += ltr_code

    while code > 9:
        curr = code // 10 + code % 10
        code = curr

    return code

# добавьте сюда ваш код из Задачи 1
all_list = []
for m in mentors:
    for a in m:
        all_list.append(a)
    # допишите сюда ваш код, который заполнит all_list. можете как складывать списки, так и использовать метод extend

# сделайте список all_names_list, состоящий только из имен, и заполните его
all_names_list = []
for mentor in all_list:
    name = mentor[:mentor.find(' ')]
    all_names_list.append(name)

# сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
unique_names = set(all_names_list)

# теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
# допишите код ниже
all_names_sorted = sorted(unique_names)
# допишите конструкцию вывода результата. можете использовать string.join()
# результат будет в all_names_sorted
a = ', '.join(all_names_sorted)
print(f'Уникальные имена преподавателей: {a}')




# уникальные имена будут в unique_names


# этот код создаст вам уже готовый (пока что пустой) список, в который вы будете добавлять имена
names_codes = [[] for n in range(10)]

# подсказка: в список names_codes дописывайте список имен с группировкой по "числу имени".
# Рекомендуем для простоты список с именами записывать по индексу, который равняется "числу имени"
# например, для имени Владимир код имени 2 и итоговый результат был бы
# names_codes = [[], [], ["Владимир"]] - внутренний список с именем Владимир находится по индексу 2 в списке names_codes
# а самый первый список с индексом 0 будет всегда пустым, т.к. нет числа имени 0

# перебираем все имена и группируем их по "числу имени"
for name in unique_names:
    # команду ниже используйте как есть - она вычисляет "число имени". На входе функция принимает имя (регистр не важен)
    # на выходе возвращает целое число от 1 до 9 - это "число имени". Например, введете "Анна" - получите 5
    code = calc_namecode(name)

    # допишите код, который добавит еще одно имя к нужному "числу имени" в списке names_codes
    names_codes[code].append(name)

# выводим окончательный результат на экран
for id, _ in enumerate(names_codes):
    # допишите вывод расшифровки "числа имени" из codes_info
    # должно выводиться так: 1 — число цели, которая проявляется в форме агрессивности и амбиций
    if id == 0:
        continue
    print(codes_info[id])
    # теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
    # допишите код ниже:
    all_names_sorted = sorted(names_codes[id])

# # допишите код, который выводит сообщение на экран
# # должно выводиться так: Коду 1 соответствуют: Азамат, Денис, Роман, Ринат, Евгений, Адилет, Сергей
    print(f"Коду {id} соответствуют: {', '.join(all_names_sorted)}")