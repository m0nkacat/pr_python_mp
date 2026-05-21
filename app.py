from PIL import Image
from multiprocessing import Pool
import os
import time


# 2012 - 6, 2013 - 27, 2014 - 210
INPUT_DIR = "Очень_ЗаБаВнЫе_фотокарточки_2014"


def process_image(image_name):
    input_path = os.path.join(INPUT_DIR, image_name)
    image = Image.open(input_path)
    image = image.rotate(-90)
    image.resize((800, 600), Image.LANCZOS)
    image = image.convert('L')
    output_name = f"processed/out_{image_name}"
    image.save(output_name)


def sequential_processing(files):
    start = time.perf_counter()
    for file in files:
        process_image(file)
    end = time.perf_counter()
    print("Последовательно: ", end - start)


def parallel_processing(files):
    start = time.perf_counter()
    with Pool() as pool:
        pool.map(process_image, files)
    end = time.perf_counter()

    print("Параллельно: ", end - start)


def main():

    files = [
        file for file in os.listdir(INPUT_DIR)
        if file.endswith(".jpg")
    ]
    sequential_processing(files)
    parallel_processing(files)


if __name__ == '__main__':
    main()