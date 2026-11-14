interested_in_cs = (
    input("SURVEY Are you interested in computer science? (y/n): ") == "y"
)
likes_games = input("Do you like playing computer games? (y/n): ") == "y"
has_instagram = input("Do you have an Instagram account? (y/n): ") == "y"

print(
    "SURVEY RESULTS Interested in computer science:",
    "Yes" if interested_in_cs else "No",
)
print("Likes playing computer games:", "Yes" if likes_games else "No")
print("Has an Instagram account:", "Yes" if has_instagram else "No")
