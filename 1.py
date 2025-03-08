import math

def compute_factorial(n):
    """Вычисляет факториал числа n."""
    return math.factorial(n)

def main():
    try:
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)

        # Проверка на положительность
        if number < 0:
            print("Ошибка: Пожалуйста, введите положительное целое число.")
            return

        # Вычисление факториала
        factorial_result = compute_factorial(number)
        print(f"Факториал числа {number} равен {factorial_result}.")
    
    except ValueError:
        print("Ошибка: Ввод должен быть целым положительным числом.")

if __name__ == "__main__":
    main()