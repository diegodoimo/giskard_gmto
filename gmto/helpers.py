import json
import os.path


def read_empire_data(path: str):
    """Reads the Empire '.json' file.

    Parameters
    ----------
    path : str
        path to the Empire '.json' file.

    Returns
    -------
    dict
        Empire data.
    """

    with open(path, "r") as file:
        empire_data = json.load(file)
    return empire_data


def read_falcon_data(path: str):
    """Reads the Millenium Falcon '.json' file. Makes the path to the routes database absolute.

    Parameters
    ----------
    path : str
        path to the Millenium Falcon '.json' file.

    Returns
    -------
    dict
        Millenium Falcon data.
    """
    with open(path, "r") as file:
        falcon_data = json.load(file)

    if not os.path.isabs(falcon_data["routes_db"]):
        base_path = os.path.dirname(path)
        falcon_data["routes_db"] = os.path.join(base_path, falcon_data["routes_db"])

    return falcon_data
