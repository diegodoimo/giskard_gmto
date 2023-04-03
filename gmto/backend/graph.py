import sqlite3
from collections import defaultdict

class Graph:
    """Representation of the sky map as a graph.

    Attributes
    ----------
    adj_list: defaultdict(list)
        Adjacency list representation of the routes to from pairs of planets.
    """

    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u: str, v: str, weight: int):
        """Adds a connection between two planets.

        Parameters
        ----------
        u : str
            Name of the starting planet.
        v : str
            Name destination planet.
        weight : int
            Time (in number of days) to reach v from u.
        """

        if u not in self.adj_list:
            self.adj_list[u].append((u, 1))
        if v not in self.adj_list:
            self.adj_list[v].append((v, 1))

        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def get_neighbors(self, node):
        """Returns the neighbors of `node`.

        Returns
        -------
        neighbors : list[tuple]
            A list of tuples `(neighbor_node, edge_weight)`.
        """
        return self.adj_list[node]

    def __repr__(self):
        string = ""
        for key, val in self.adj_list.items():
            string += f"{key}: {val}\n"
        return string


def build_graph(path_db: str):
    """Given a path to an SQLite database builds a Graph of the routes between planets.

    Parameters
    ----------
    path_db : str
        path to database

    Returns
    -------
    Graph
        Graph representation of the routes between planets.
    """
    conn = sqlite3.connect(path_db)
    c = conn.cursor()
    data = c.execute("SELECT origin, destination,travel_time FROM routes")

    # LOAD SKYMAP ADIANCENCY LIST
    skymap = Graph()

    for row in data:
        skymap.add_edge(u=row[0], v=row[1], weight=row[2])
    return skymap
