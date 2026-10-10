import csv


def write_csv_data(dest, header, list_data):
    with open(dest, "w", newline="", encoding="utf-8-sig") as f:
        list_data.insert(0, header)
        writer = csv.writer(f)
        writer.writerows(list_data)
