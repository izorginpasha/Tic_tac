from tkinter import *

root = Tk()  # Главное окно
root.title("Крестики нолики")
root.geometry('350x350')

games = Canvas(root, width=300, height=300)  # Новый холст
games.place(x=25, y=25)

for i in range(0, 9):
    x = i // 3 * 100
    y = i % 3 * 100
    games.create_rectangle(x, y, x + 100, y + 100,
                           width=3,
                           outline='#A5A5A5',
                           fill='#CCCCCC',
                           activefill='#FFFAFA')


def add_x(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_line(x, y, x + 80, y + 80, width=7, fill='#0000FF')
    games.create_line(x, y + 80, x + 80, y, width=7, fill='#0000FF')


def add_0(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_oval(x, y, x + 80, y + 80, width=7, outline='#FF0000')


def click(event):
    colum = event.x // 100
    row = event.y // 100
    add_x(colum, row)

games.bind('<Button-1>', click)


root.mainloop()  # Инициализируем окно

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


# Сделать ход в ячейку
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Основная программа
game_over = False
player1 = True
count = 0
while game_over == False:
    if (count > 8):
        break

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
    count += 1

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win or "ничья")
