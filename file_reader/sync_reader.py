import datetime
import os
import argparse
import timeit
import time


def read_file(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            time.sleep(0.001)
            data = f.read(1024)
            if not data:
                break


def main(directory):
    begin = datetime.datetime.now()
    files = [os.path.join(directory, file) for file in os.listdir(directory)]
    for f in files:
        if os.path.isfile(f):
            read_file(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read all binary files from a directory.")
    parser.add_argument("directory", type=str, help="The directory containing the binary files.")
    args = parser.parse_args()

    number_of_calls = 1
    elapsed_time = timeit.timeit("main(args.directory)", globals=globals(), number=number_of_calls)
    print(f"sync_reader: average runtime across {number_of_calls} trial(s) is "
          f"{elapsed_time / number_of_calls:.4f} seconds")
