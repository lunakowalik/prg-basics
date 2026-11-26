import csv


def load_provinces():
    letter_to_province = {}
    province_counts = {}

    with open("province.csv", mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            letter = (row.get("Letter") or "").strip().upper()
            name = (row.get("Name") or "").strip()
            if letter and name:
                letter_to_province[letter] = name
                province_counts[name] = 0

    return letter_to_province, province_counts


def count_vehicles_by_province(letter_to_province, province_counts):
    with open("vehicle.txt", mode="r", encoding="utf-8") as txt_file:
        for line in txt_file:
            plate = line.strip().upper()
            if not plate:
                continue
            first_letter = plate[0]
            province_name = letter_to_province.get(first_letter)
            if province_name is not None:
                province_counts[province_name] += 1

    return province_counts


def print_province_summary(province_counts):
    print(f"{'Province':<24} Vehicles")
    print("-" * 34)
    for province_name, count in province_counts.items():
        print(f"{province_name:<24} {count}")


letter_to_province, province_counts = load_provinces()
count_vehicles_by_province(letter_to_province, province_counts)
print_province_summary(province_counts)

