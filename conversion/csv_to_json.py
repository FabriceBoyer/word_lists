import os
import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        json_data = json.dumps(list(csv_data), indent=2)

    with open(json_file, 'w') as file:
        file.write(json_data)

def convert_csv_to_json(csv_folder, json_folder):
    os.makedirs(json_folder, exist_ok=True)

    for file_name in os.listdir(csv_folder):
        if file_name.endswith('.csv'):
            csv_file = os.path.join(csv_folder, file_name)
            json_file = os.path.join(json_folder, file_name.replace('.csv', '.json'))
            csv_to_json(csv_file, json_file)


def main():
    folders = ["ngsl/1.2"]
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
    for folder in folders:
        csv_folder =  os.path.join(root, folder, "csv") # manually enhanced from src
        json_folder =  os.path.join(root, folder, "json")
        convert_csv_to_json(csv_folder, json_folder)


if __name__ == '__main__':
    main()
