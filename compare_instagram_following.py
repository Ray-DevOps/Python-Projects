brand_names = []

for profiles in data:
  names = profiles.get('name')
  brand_names.append(names)

game_over = False

score = [ ]

answer = ""

# if answer == "correct":
#     name_a = name_b
#     brand_names.remove(name_a)
#     name_b = random.choice(brand_names)

while game_over == False:

    name_a = random.choice(brand_names)
    brand_names.remove(name_a)
    name_b = random.choice(brand_names)

    follower_count_a = 1
    description_a = ""
    country_a = ""

    for profile in data:
        if profile.get('name') == name_a:
            file_a = profile
            follower_count_a = file_a.get("follower_count")
            description_a = file_a.get("description")
            country_a = file_a.get("country")

    follower_count_b = 1
    description_b = ""
    country_b = ""

    for profile in data:
        if profile.get('name') == name_b:
            file_b = profile
            follower_count_b = file_b.get("follower_count")
            description_b = file_b.get("description")
            country_b = file_b.get("country")

    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(logo2)
    answer = input(
        f"Against B: {name_b}, a {description_b}, from {country_b}. Who has more followers? Type 'A' or 'B': ").upper()

    if answer == 'B' and follower_count_b > follower_count_a:
        score.append(1)
        print(f"You're right! Current score: {sum(score)}")

    elif answer == 'A' and follower_count_a > follower_count_b:
        score.append(1)
        print(f"You're right! Current score: {sum(score)}")

    elif (answer == 'B' and follower_count_a > follower_count_b) or (answer == 'A' and follower_count_b > follower_count_a):
        score.append(0)
        print(f"Sorry, that's wrong. Game over. Final score: {sum(score)}")
        break
        game_over = True

    else:
        print(f"Sorry, that's wrong. Game over. Final score: {sum(score)}")
        break
        game_over = True

