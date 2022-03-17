def first_task_homework_18_03_2022(variable_first_task):
    if variable_first_task > 25:
        return 2 * variable_first_task * variable_first_task * variable_first_task + \
               variable_first_task * variable_first_task
    if variable_first_task <= 25:
        return first_task_homework_18_03_2022(variable_first_task + 2) + 2 * first_task_homework_18_03_2022(
            variable_first_task + 3)


first_task_amount = first_task_homework_18_03_2022(2)
first_task_summ_of_amount = 0
for first_task_iterable_variable in range(len(str(first_task_amount))):
    first_task_summ_of_amount += int(str(first_task_amount)[first_task_iterable_variable])
print(f'Ответ на первую задачу: {first_task_summ_of_amount}')


def second_task(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return second_task(n / 3) + 1
    if n >= 2 and n % 3 != 0:
        return second_task(n - 2) + 5


for second_task_iterable in range(0, 1000000):
    if second_task(second_task_iterable) == 73:
        print(f'Ответ на вторую задачу: {second_task_iterable}')
        break


def third_task_homework_18_03_2022(variable_third_task):
    if variable_third_task == 0:
        return 0
    if variable_third_task % 2 == 0:
        return third_task_homework_18_03_2022(variable_third_task / 2) - 2
    if variable_third_task % 2 != 0:
        return 2 + third_task_homework_18_03_2022(variable_third_task - 1)


count_of_amount_third_task = 0
for third_task_iterable in range(0, 1001):
    if third_task_homework_18_03_2022(third_task_iterable) == -2:
        count_of_amount_third_task += 1
print(f'Ответ на третию задачу: {count_of_amount_third_task}')
