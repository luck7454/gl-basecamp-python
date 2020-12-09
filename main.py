def count_holes(values):  # основная функция
    one_hole_in_num = ["4", "6", "0", "9"]
    two_hole_in_num = ["8"]
    hole_sum = 0
    for i in values:  # цикл проверяющий элементы при вводе пользователя
        if i in one_hole_in_num:  # цикл проверяющий элементы в 1м списке
            hole_sum += 1
        if i in two_hole_in_num:  # цикл проверяющий элементы в 2м списке
            hole_sum += 2
    return hole_sum


while True:
    value = input(str("Please, enter an integer numbers: "))
    if value.isnumeric():  # проверка строки на наличие сиволов кроме цифр
        value = str(value)
    else:
        print("Error")
        continue
    if value[0] == '0':  # проверка первого символа строки
        print("Quantity of holes: ", count_holes(value) - 1)
    else:
        print("Quantity of holes: ", count_holes(value))
