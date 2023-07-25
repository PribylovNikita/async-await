import aiofiles
import asyncio
import os
import argparse
import timeit
import time


async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            await asyncio.sleep(0.001)
            data = await f.read(1024)
            if not data:
                break


async def main(directory):
    files = [os.path.join(directory, file) for file in os.listdir(directory)]
    for coro in asyncio.as_completed([read_file(file) for file in files]):
        await coro


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read all binary files from a directory.")
    parser.add_argument("directory", type=str, help="The directory containing the binary files.")
    args = parser.parse_args()

    number_of_calls = 1
    elapsed_time = timeit.timeit("asyncio.run(main(args.directory))", globals=globals(), number=number_of_calls)
    print(f"async_reader: average runtime across {number_of_calls} trial(s) is "
          f"{elapsed_time / number_of_calls:.4f} seconds")
