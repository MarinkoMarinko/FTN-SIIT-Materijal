import os


def all_paths(file_path):                           # O(n)
    if not os.path.exists(file_path):
        print("Path does not exist!")
        return
    if os.path.isfile(file_path):
        print(os.path.abspath(file_path))
        return
    elif os.path.isdir(file_path):
        for dir_name in os.listdir(file_path):
            new_path = os.path.join(file_path, dir_name)
            all_paths(new_path)


if __name__ == "__main__":
    path = "/home/marinko/Desktop/Faks"
    all_paths(path)