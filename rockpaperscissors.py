## importers
import random as r

user_wins = 0
computer_wins = 0
options = ['камінь','бумага','ножниці']

while True:
    user_input = input('Зроби вибір: Камінь, Ножниці, Бумага або натисни Q для виходу: ').lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_numb = r.randint(0,2)
    computer_pick = options[random_numb]
    print("Комп'ютер вибрав",computer_pick+'.')

    if user_input == 'камінь' and computer_pick == 'ножниці':
        print('Ти виграв!')
        user_wins += 1

    elif user_input == 'бумага' and computer_pick == 'камінь':
        print('Ти виграв!')
        user_wins += 1

    elif user_input == 'ножниці' and computer_pick == 'бумага':
        print('Ти виграв!')
        user_wins += 1

    else:
        print("Ти програв!")
        computer_wins +=1

print("Твоя кількість перемог", user_wins)
print("Кількість перемог комп'ютера",computer_wins)
print("Бувай")