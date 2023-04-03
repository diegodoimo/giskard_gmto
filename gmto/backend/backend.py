from .graph import Graph
from collections import defaultdict

class State:
    def __init__(self, path: list, today: int, autonomy: int, k: int):
        """State of the Millennium Falcon.

        Parameters
        ----------
        path : list
            list of planets visited by the Millennium Falcon.
        today : int
            present day.
        autonomy : int
            number of days that can be travelled before stopping for fuel.
        k : int
            number of times the bounty hunters have been in the same location (planet, day) of the Millennium Falcon.
        """
        self.path = path
        self.today = today
        self.autonomy = autonomy
        self.k = k

    @property
    def planet(self):
        return self.path[-1]


class Backend:
    def __init__(self, start: str, end: str, countdown: int, skymap: Graph, hunters_map: list, autonomy: int):
        """Backend class used to compute best optimal path between two planets.

        Parameters
        ----------
        start : str
            name of the starting planet.
        end : str
            name of the destination planet.
        countdown : int
            maximum number of days to reach destination planet.
        skymap : Graph
            adjacency list of the routes between planets.
        hunters_map : list
            list of locations [{"planet": (str), "day": (int)}] where Bounty Hunter will be found. 
        autonomy : int
            autonomy of the Millennium Falcon.
        """
        self.end = end
        self.start = start
        self.skymap = skymap
        self.countdown = countdown
        self.max_autonomy = autonomy
        self.has_hunters = defaultdict(lambda: defaultdict(lambda: 0))
        for hunters in hunters_map:
            self.has_hunters[hunters["planet"]][hunters["day"]] = 1

        self._paths = None

    def get_probas(self) -> float:
        """Computes the probability to arrive to the destination planet.

        Returns
        -------
        float
            Probability to arrive to destination planet alive.
        """

        paths = self._calculate_paths()

        if len(paths) == 0:
            # it is not possible to reach the destination
            return 0

        # minimum number of times bounty hunters are met
        best_k = min([k for _, k, _ in paths])

        # probability of being captured
        pr_hunted = 0.1 * (1 - 0.9**best_k) / (1 - 0.9)

        return 1 - pr_hunted

    def _is_valid_state(self, state: State):
        if state.today > self.countdown:
            return False
        if state.autonomy < 0:
            return False

        return True

    def _calculate_paths(
        self,
    ):
        """Builds the list of possible paths to destination.

        Returns
        -------
        list
            List of possible paths to destination. Each path is a 'State' class containing 
            the sequence of visited planes, the number of times the buounty hunters are met 
            and the duration of the travel.
        """
        paths = []

        initial_state = State(
            path=[self.start],
            today=0,
            autonomy=self.max_autonomy,
            k=self.has_hunters[self.start][0],
        )

        states_to_explore = [initial_state]

        while states_to_explore:
            state = states_to_explore.pop(0)

            if state.planet == self.end:
                paths.append((state.path, state.k, state.today))
                continue

            for neighbor, weight in self.skymap.get_neighbors(state.planet):
                day = state.today + weight
                autonomy = (
                    (state.autonomy - weight)
                    if neighbor != state.planet
                    else self.max_autonomy
                )
                k = state.k + self.has_hunters[neighbor][day]

                next_state = State(
                    path=state.path + [neighbor], today=day, autonomy=autonomy, k=k
                )

                if self._is_valid_state(next_state):
                    states_to_explore.append(next_state)

        return paths

