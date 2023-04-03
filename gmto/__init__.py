import argparse
from .backend import get_proba
from .web.helpers import read_empire_data, read_falcon_data

def cli():
    """
    A wrapper function used to create the give-me-the-odds script.
    """
    parser = argparse.ArgumentParser(description="""A command line interface to compute the probability that 
                                     the Millennium Falcon will reach the destination planet.""")
    parser.add_argument("falcon_path", help = "Path to Millennium Falcon JSON file")
    parser.add_argument("empire_path", help="Path Empire JSON file")
    args = parser.parse_args()

    #load dictionaries containing empire and millennium falcon data.
    empire_data = read_empire_data(args.empire_path)
    falcon_data = read_falcon_data(args.falcon_path)

    # compute the probability of success.
    proba = get_proba(empire_data, falcon_data)

    print(f"{proba * 100:.1f}")