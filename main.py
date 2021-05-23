# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse

# Press the green button in the gutter to run the script.
import csv

if __name__ == '__main__':
    # Configuring arg parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_path', metavar='N', type=str, nargs='+')

    # Get the values
    args = arg_parser.parse_args()
    print(args.file_path)
    files = args.file_path

    file_pointer = 0

    with open(files[0], 'r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            if file_pointer == 0:
                print(line)
            print(line)
            file_pointer = file_pointer + 1
