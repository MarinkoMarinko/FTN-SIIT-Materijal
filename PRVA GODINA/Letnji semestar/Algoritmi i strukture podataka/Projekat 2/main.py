import os
import sys

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))      # absolute path of current folder
sys.path.insert(0, os.path.join(_BASE_DIR, "src"))          # enables imports from src

from app import SocialNetworkApp   
from menu import Menu

DATASETS = ("small", "medium", "full")


def choose_dataset():
    print("Izaberite skup podataka:")
    for i, name in enumerate(DATASETS, start = 1):
        print(f"  {i}) {name}")
    while True:
        answer = input("> ").strip().lower()
        if answer in DATASETS:
            return answer
        if answer in ("1", "2", "3"):
            return DATASETS[int(answer) - 1]
        print("Unesite 1, 2, 3 ili small/medium/full.")


def main():
    dataset = choose_dataset()
    dataset_dir = os.path.join(_BASE_DIR, "data", dataset)

    print(f"\nUčitavanje skupa '{dataset}' iz: {dataset_dir}")
    app = SocialNetworkApp(dataset_dir).build(verbose = True)

    Menu(app).run()


if __name__ == "__main__":
    main()
