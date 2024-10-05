import curses
import time
import os
from machine_animations import *

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_terminal_width(default_width=80):
    try:
        return os.get_terminal_size().columns
    except OSError:

        return default_width

def show_animation(message):
    width = get_terminal_width()
    for _ in range(5):
        for x in range(0, width - len(message)):
            clear_screen()
            print(" " * x + message)
            time.sleep(0.05)

        for x in range(width - len(message), 0, -1):
            clear_screen()
            print(" " * x + message)
            time.sleep(0.05)




def get_command(commands, condition):
    while True:
        command = input(condition)
        if command in commands:
            return command
        else:
            print("Неправильна команда.-_-")




def animate_machine():
    for i in range(10):
        clear_screen()
        print("Пральна машина працює...")
        clothes_in_machine1()
        time.sleep(0.2)
        clothes_in_machine2()
        time.sleep(0.2)
        clothes_in_machine3()
        time.sleep(0.2)

def dry_animation_machine():
    for i in range(10):
        clear_screen()
        print("Сушка сушить:)")
        clothes_in_machine2()
        time.sleep(0.3)
        clothes_in_machine3()
        time.sleep(0.3)
        clothes_in_machine1()
        time.sleep(0.3)


clear_screen()
show_closed_machine()
get_command(['Powder'], "Напишіть команду 'Powder',щоб відкрити відсік для порошку та залити його туди: ")
clear_screen()
show_closed_machine_with_powder()
print("Порошок залитий")

get_command(['Open'], "Напишіть команду 'Open',щоб відкрити пральну машину: ")
clear_screen()
show_open_machine()
print("Пральна машина відкрита!")

get_command(['Слава Україні'], "Напишіть 'Слава Україні',щоб з'явились речі: ")
clear_screen()
clothes_near_open_machine()
print("Які чудеса творить Зеленський!")

get_command(['Pull'], "Напишіть 'Pull',щоб помістити речі до пральної машини: ")
clear_screen()
clothes_in_machine1()
print("Тепер речі у машинці)")

get_command(['Start'], "Напишіть 'Start',щоб почати роботу пральної машини: ")
clear_screen()
animate_machine()
clothes_in_machine4()
print("Речі успішно попрались")

get_command(['Dry'], "Напишіть 'Dry',для початку роботи опції 'Сушка': ")
clear_screen()
dry_animation_machine()
print("Речі успішно посушились")

get_command(['Finish'], "Введіть команду 'Finish',щоб відкрити машинку з сухими речами: ")
clear_screen()
clothes_in_machine_with_open_door()
print("Машинка відкрилась)")

get_command(['Take'], "Введіть команду 'Take',щоб забрати чистенькі та сухі речі: ")
clear_screen()
clothes_near_open_machine()
print("Речі успішно забрані")

get_command(['Goiteens one love!'], "Введіть команду 'Goiteens one love!',щоб побачити сюрприз: ")
clear_screen()
show_animation("Goiteens one love!")
print("Дякую за перегляд!")



