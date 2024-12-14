def calculate_love_score(name1, name2):
    full_name = name1 + name2

    letter_true = 'true'
    letter_love = 'love'

    true_count = 0
    love_count = 0

    for i in letter_true:
        true_count += full_name.count(i)

    for i in letter_love:
        love_count += full_name.count(i)

    love_score = str(true_count) + str(love_count)

    return print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")