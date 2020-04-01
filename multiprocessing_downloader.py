from multiprocessing import Pool
import os
import requests


main_folder = 'Download/'
folder = 'example/'


urls = []


def read(file):
  with open(file, "r") as f:
    for line in f:
      yield line.strip()


def load(url):

    find_name = url.rfind("/") + 1
    get_name = url[find_name:]
    if os.path.exists(main_folder + folder + get_name):
        pass

    else:
        print("Downloaded: ", url)
        r = requests.get(url, stream=True)
        if r.status_code == requests.codes.ok:
            with open(os.path.join(main_folder + folder, get_name), 'wb') as f:
                for data in r:
                    f.write(data)
    return url


def main():
    urls = read("list.txt")
    with Pool(20) as p:
        p.map(load, urls)


if __name__ == '__main__':
    if os.path.exists(main_folder + folder):
        main()
    else:
        os.makedirs(main_folder + folder)
        main()
