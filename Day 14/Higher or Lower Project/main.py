import game_data
import random

number_list = [i for i in range(0, 50)]
total = 0


while True:
    a = game_data.data[random.choice(number_list)]
    b = game_data.data[random.choice(number_list)]

    a2 = game_data.data[random.choice(number_list)]['name']
    b2 = game_data.data[random.choice(number_list)]['name']

    if a2 != b2:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        answer = input("Who has mor followers? Type 'A' or 'B : " )

        if answer == 'A':
            if a['follower_count'] > b['follower_count']:
                total += 1
                print(f"You're right! Current score : {total}")

            else:
                print(f"Sorry. That's wrong. Final score: {total}")
                break
    else:
        pass
