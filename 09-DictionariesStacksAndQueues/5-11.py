import json

# Read the contents of the json file
with open("voting.json") as file:
    votes = json.load(file)

# Vote for a person
person_name = input("Name of the person you are voting for: ").strip()

votes[person_name] = votes.get(person_name, 0) + 1

# Save voting data to json file
with open("voting.json", "w", encoding="utf-8") as file:
    json.dump(votes, file)

print(f"Vote recorded for {person_name} (total votes: {votes[person_name]}).")