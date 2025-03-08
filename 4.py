import random

# Генерация случайного числа от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Я загадал число от 1 до 100. Попробуйте угадать его!")

while attempts < max_attempts:
    user_guess = input("Введите ваше предположение: ")
    
    # Проверка, является ли ввод числом
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    attempts += 1

    # Проверка на правильность предположения
    if user_guess < secret_number:
        print("Слишком маленькое число.")
    elif user_guess > secret_number:
        print("Слишком большое число.")
    else:
        print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
        break
else:
    print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret_number}.")