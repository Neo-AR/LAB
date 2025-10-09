import time
import random
import numpy as np

from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def fill_mas(mas, var):
    if var == 1:  # Возрастающий
        return list(range(len(mas)))
    if var == 2:  # Убывающий
        return list(range(len(mas), 0, -1))
    if var == 3:  # Возрастающе-убывающий
        half = len(mas) // 2
        return list(range(half)) + list(range(len(mas) - half, 0, -1))
    if var == 4:  # Случайный
        return [random.randint(-100, 100) for _ in range(len(mas))]

def shell(nums):
    arr = nums.copy()  # Работаем с копией
    inc = len(arr) // 2
    while inc:
        for i in range(inc, len(arr)):
            temp = arr[i]
            j = i
            while j >= inc and arr[j - inc] > temp:
                arr[j] = arr[j - inc]
                j -= inc
            arr[j] = temp
        inc = inc // 2
    return arr

def built_in_sort(nums):
    return sorted(nums.copy())  # Работаем с копией

def quicksort(nums):
    if len(nums) <= 1:
        return nums.copy()  # Возвращаем копию
    q = random.choice(nums)
    s_nums = [n for n in nums if n < q]
    e_nums = [n for n in nums if n == q]
    m_nums = [n for n in nums if n > q]
    return quicksort(s_nums) + e_nums + quicksort(m_nums)

def fill_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            matr[i][j] = random.randint(-100, 100)

def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Невозможно умножить матрицы")
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def test(razm):
    # ПРАВИЛЬНОЕ создание матриц
    matrix_1 = [[0] * razm for _ in range(razm)]
    matrix_2 = [[0] * razm for _ in range(razm)]

    fill_matr(matrix_1)
    fill_matr(matrix_2)

    start = time.perf_counter()
    multiply = matrix_multiply(matrix_1, matrix_2)
    end = time.perf_counter()

    time_of_work = end - start
    print(f"Время умножения матриц {razm}X{razm}: {time_of_work:.6f} секунд")
    return time_of_work

def sortir(mas, var):
    arr = mas.copy()  # Всегда работаем с копией
    if var == 1:
        return shell(arr)
    if var == 2:
        return built_in_sort(arr)
    if var == 3:
        return quicksort(arr)

def process_array(arr, fill_idx, result_list, time_list):
    original_arr = fill_mas(arr, fill_idx)
    
    for sort_type in [1, 2, 3]:
        # Создаем копию для каждой сортировки
        arr_copy = original_arr.copy()
        
        start = time.perf_counter()
        sorted_arr = sortir(arr_copy, sort_type)
        end = time.perf_counter()
        
        result_list.append(sorted_arr)
        time_list.append(end - start)

def sortirovki():
    # Уменьшим размеры для тестирования
    c = [[0] * 10000 for _ in range(4)]  # было 100000
    d = [[0] * 30000 for _ in range(4)]  # было 300000

    result_1, time_1 = [], []
    result_2, time_2 = [], []

    for i in range(4):
        process_array(c[i], i + 1, result_1, time_1)

    for i in range(4):
        process_array(d[i], i + 1, result_2, time_2)
        
    return result_1, result_2, time_1, time_2

def draw(X, Y):
    plt.figure(figsize=(10, 6))
    plt.plot(X, Y, 'bo-', label='Исходные данные')  # Добавляем метку для легенды
    

    plt.plot([i for i in range(10000)], [i**2+i**3 for i in range(10000)])
    # Аппроксимируем данные полиномом
    p2 = Polynomial.fit(X, Y, deg=3)

    
    X2_fit = np.linspace(min(X), max(X), 100)
    Y2_fit = p2(X2_fit)
    # Рисуем аппроксимированную кривую
    plt.plot(X2_fit, Y2_fit, 'g', label='Аппроксимированная прямая deg=3')
    # Добавляем подписи и заголовок
    plt.xlabel("Размерность матриц (N x N)")
    plt.ylabel("Время работы (секунды)")
    plt.title("Зависимость времени умножения матриц от их размера")
    
    # Добавляем легенду
    plt.legend()
    
    # Выводим формулу кривой
    formula2 = f"y = {p2.coef[0]:.2f} + {p2.coef[1]:.2f}x + {p2.coef[2]:.2f}x^2 + {p2.coef[3]:.2f}x^3"
    #plt.text(0.02, 0.9, formula1, transform=plt.gca().transAxes, fontsize=12,
             #verticalalignment='top')
    
    plt.text(0.02, 0.9, formula2, transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top')
    
    plt.show()


def main():
    choose = meet()
    if choose == 1:
        print("Запуск тестирования сортировок...")
        res_1, res_2, tim_1, tim_2 = sortirovki()
        
        print("\n" + "="*80)
        print("10000 чисел")
        print("Вид\\Набор данных       Возрастающий   Убывающий   Возраст-убыв   Случайный")
        print("-"*80)
        
        print(f"Сортировка Шелла      {tim_1[0]:.6f}    {tim_1[1]:.6f}    {tim_1[2]:.6f}    {tim_1[3]:.6f}")
        print(f"Встроенная сортировка {tim_1[4]:.6f}    {tim_1[5]:.6f}    {tim_1[6]:.6f}    {tim_1[7]:.6f}")
        print(f"Быстрая сортировка    {tim_1[8]:.6f}    {tim_1[9]:.6f}    {tim_1[10]:.6f}    {tim_1[11]:.6f}")
        
        print("\n" + "="*80)
        print("30000 чисел")
        print("Вид\\Набор данных       Возрастающий   Убывающий   Возраст-убыв   Случайный")
        print("-"*80)
        
        print(f"Сортировка Шелла      {tim_2[0]:.6f}    {tim_2[1]:.6f}    {tim_2[2]:.6f}    {tim_2[3]:.6f}")
        print(f"Встроенная сортировка {tim_2[4]:.6f}    {tim_2[5]:.6f}    {tim_2[6]:.6f}    {tim_2[7]:.6f}")
        print(f"Быстрая сортировка    {tim_2[8]:.6f}    {tim_2[9]:.6f}    {tim_2[10]:.6f}    {tim_2[11]:.6f}")
        
    elif choose == 2:
        print("Запуск тестирования умножения матриц...")
        
        # Создаем размерности матриц
        rows_cols = [100, 200, 400, 800, 1000]
        # current = 100
        # while len(rows_cols) < 10:  # Ограничим до 10 размеров для теста
        #     rows_cols.append(current)
        #     if current < 1000:
        #         current += 100
        #     else:break
        #         #current += 1000  # Для больших размеров увеличиваем шаг
        times = []
        
        for size in rows_cols:
            try:
                time_taken = test(size)
                times.append(time_taken)
            except MemoryError:
                print(f"Пропускаем размер {size} - недостаточно памяти")
                break
            except Exception as e:
                print(f"Ошибка при размере {size}: {e}")
                break
        
        print(f"\nРазмеры матриц: {rows_cols}")
        print(f"Время выполнения: {times}")
        
        if len(rows_cols) == len(times):
            draw(rows_cols, times)
            #draw()
        else:
            # Если какие-то размеры были пропущены, обрезаем lists
            min_len = min(len(rows_cols), len(times))
            draw(rows_cols[:min_len], times[:min_len])


def meet():
    while True:
        try:
            print("\nВыберите операцию:")
            print("1 - Сравнение сортировок")
            print("2 - Перемножение матриц")
            choose = int(input("Введите 1 или 2: "))
            if choose in [1, 2]:
                return choose
            else:
                print("Пожалуйста, введите 1 или 2")
        except ValueError:
            print("Пожалуйста, введите число")

if __name__ == "__main__":
    main()