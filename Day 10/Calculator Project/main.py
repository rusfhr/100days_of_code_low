def life_in_weeks(age):
    remain = (90 - age) * 52

    return f"Your have {remain} weeks left.\n"

print(life_in_weeks(20))