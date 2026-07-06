# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files.


# Функция для вычисления статистики и возврата в виде кортежа
def find_common_elements(list1, list2):
    return sorted(set(list1) & set(list2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__': 
    numbers = list(map(int, input().split()))
    result = 1

    for i in numbers:
        result = i * result

    print(result)