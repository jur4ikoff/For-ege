
def f_second_task_homework_16_03_2022(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f_second_task_homework_16_03_2022(n - 1) + g_second_task_homework_16_03_2022(n - 1) - 2


def g_second_task_homework_16_03_2022(n):
    if n == 1:
        return 1
    if n > 1:
        return f_second_task_homework_16_03_2022(n - 1) + 2 * g_second_task_homework_16_03_2022(n - 1)


print(f_second_task_homework_16_03_2022(14) + g_second_task_homework_16_03_2022(14)) # 1594324
count = 0


def third_task_homework_16_03_2022(n):
    global count
    count += 1
    if n >= 1:
        count += 1
        third_task_homework_16_03_2022(n - 1)
        third_task_homework_16_03_2022(n - 3)
        count += 1
    return count


print(third_task_homework_16_03_2022(40))  # 22947841
