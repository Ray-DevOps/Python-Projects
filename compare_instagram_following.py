# In this program, we get to compare brand names (or celebrities) by their Instagram following.
# we are provided with a data of a number of celebrities (or brands), their occupation (or line of business),
# their countries of citizenship (as a list of dictionaries). 
# The data is available [here] (https://github.com/Ray-DevOps/Python-Projects/blob/main/Instagram_data.txt)
# The program randomly picks two names from the list and ask the user to guess which of the two has higher 
# Instagram following. If the player makes the correct guess, s/he score 1 point and moves on to the next.
# Option 2 of a question becomes option 1 of the following question. For example, suppose the player is 
# asked to pick between A. Christiano Ronaldo and B. Kim Kardashian, and the player correctly picks 
# Christiano Ronaldo, the next question will now present Kim Kardashian as option A and another celebrity 
# say Adidas as option B. If the player correctly picks Adidas, then the next question presents Adidas
# as option A, and another celebrity (or brand) as option B and so on.

brand_names = []

for profiles in data:
  names = profiles.get('name')
  brand_names.append(names)

game_over = False

score = [ ]

name_c = ""
while game_over == False:

    if name_c == "":
        name_a = random.choice(brand_names)
    else:
        name_a = name_c

    brand_names.remove(name_a)
    name_b = random.choice(brand_names)
    name_c = name_b                   # We temporarily store the value of name_b in name_c so that we can 
                                      # later assign it as value of name_a


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


