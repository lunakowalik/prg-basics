file_name = input("File name: ").strip()

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    num_lines = len(content.splitlines())
    num_characters = len(content)
    num_words = len(content.split())

    print(f"File name: {file_name}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' was not found.")
except OSError as e:
    print(f"Error reading file '{file_name}': {e}")