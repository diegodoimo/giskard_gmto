from .backend import Backend
from .graph import build_graph


def get_proba(empire_data: dict, falcon_data: dict):
    """Computes the probility to arrive at the destination planet.

    Parameters
    ----------
    empire_data : dict
        The Empire state.
            "countdown" (int): maximum number of days to reach destination;
            "bounty_hunters" list[dict]: list of locations [{"planet": (str), "day": (int)}]
            where Bounty Hunter will be found.
    falcon_data : dict
        The Millennium Flacon state. 
            "departure" (str): planet where the Millennium Falcon is on day 0;
            "arrival" (str): planet where the Millennium Falcon must be at or before countdown;
            "autonomy" (int): the autonomy of the Millennium Falcon in days;
            "routes_db (str): the path to a database containing the routes between the planets.

    Returns
    -------
    float
        Probability to arrive at destination.
    """
    countdown = empire_data["countdown"]
    hunter_map = empire_data["bounty_hunters"]

    autonomy = falcon_data["autonomy"]
    departure = falcon_data["departure"]
    arrival = falcon_data["arrival"]
    path_db = falcon_data["routes_db"]

    # load the routes_db in an adjaency list
    skymap = build_graph(path_db)

    # backend class used to compute the success probability
    bk = Backend(
        start=departure,
        end=arrival,
        skymap=skymap,
        autonomy=autonomy,
        countdown=countdown,
        hunters_map=hunter_map,
    )

    return bk.get_probas()
