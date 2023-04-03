import argparse
import json


from gmdo.backend import get_proba
from gmdo.helpers import read_empire_data, read_falcon_data


if __name__ == "__main__":
    # @TODO
    parser = argparse.ArgumentParser(description="My command")
    # parser.add_argument("empire_path", type=argparse.FileType("r"), metavar="PATH_TO_EMPIRE_FILE", help="Bla bla")
    parser.add_argument("empire_path", metavar="PATH_TO_EMPIRE_FILE", help="Bla bla")
    parser.add_argument("falcon_path")
    args = parser.parse_args()

    empire_data = read_empire_data(args.empire_path)
    falcon_data = read_falcon_data(args.falcon_path)

    # compute the probability of success
    proba = get_proba(empire_data, falcon_data)

    print(f"{proba * 100:.2f}%")
