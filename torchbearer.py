"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return (
        "- A single shortest-path run from S finds only the shortest distance from the entrance to one location, but does not give the optimal order to visit multiple relics. You need to know distances from all of the sources to all the relics to determine the optimal solution.\n"
        "- The optimal order to visit the relics, because different orderings give different total costs.\n"
        "- The total torch fuel cost depends on the order in which relics are visited, so the optimal order must be discovered through searching all the orders instead of just a simple greedy algorithm."
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    seen = set()
    sources = []
    for s in [spawn] + list(relics):
        if s not in seen:
            seen.add(s)
            sources.append(s)
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    nodes = set(graph.keys())
    for u in graph:
        for v, _ in graph[u]:
            nodes.add(v)

    dist = {node: float('inf') for node in nodes}
    if source not in dist:
        dist[source] = float('inf')

    dist[source] = 0
    heap = [(0, source)]

    while heap:
        current_dist, current = heapq.heappop(heap)
        if current_dist != dist[current]:
            continue

        for v, w in graph.get(current, []):
            next_dist = current_dist + w
            if next_dist < dist.get(v, float('inf')):
                dist[v] = next_dist
                heapq.heappush(heap, (next_dist, v))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}
    for s in sources:
        dist_table[s] = run_dijkstra(graph, s)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return (
        "- For nodes already finalized (in S): These nodes have had their shortest-path distances confirmed as correct. Once a node is finalized, its distance value will not change and represents the true minimum cost from the source.\n"
        "- For nodes not yet finalized (not in S): These nodes have a tentative distance representing the best path found so far through only finalized nodes, but a better path might still be discovered.\n"
        "- Initialization: At the start, only the source node has distance 0 (finalized), and all other nodes have distance infinity, satisfying the invariant.\n"
        "- Maintenance: When we finalize the node u with minimum dist[u], it must be correct because all nonnegative edge weights mean any path to u through unfinalized nodes would cost at least dist[u]. Updating neighbors preserves the invariant.\n"
        "- Termination: At the end, all reachable nodes are finalized with their true shortest distances, and unreachable nodes remain at infinity.\n"
        "- Correctness matters: The route planner depends on these true distances to compute the actual cost of any relic visit sequence. Wrong distances lead to suboptimal or impossible routing decisions."
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return (
        "- The failure mode: Greedy always picks the nearest unvisited relic from the current location, but nearest-first is locally optimal and ignores how each choice constrains future moves, leading to a globally suboptimal order.\n"
        "- Counter-example setup: Consider a dungeon where relic R1 is close to spawn (cost 1), relic R2 is farther away (cost 5), but from R2 the exit is cheap (cost 1). From R1, reaching R2 is very expensive (cost 100).\n"
        "- What greedy picks: Spawn → R1 (cost 1) → R2 (cost 100) → Exit (cost 1), total 102.\n"
        "- What optimal picks: Spawn → R2 (cost 5) → R1 (cost 10) → Exit (cost 1), total 16.\n"
        "- Why greedy loses: By greedily chasing the nearest relic first, it locks itself into an expensive position for collecting the second relic, wasting far more fuel than a plan that visits R2 first.\n"
        "- What the algorithm must explore: All possible orders of visiting the relics, because the total cost depends entirely on which relic is visited first, second, third, and so on."
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    return (float('inf'), [])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    return (float('inf'), [])


def test_dijkstra_algorithm():
    graph = {
        'S': [('A', 5), ('B', 1)],
        'B': [('A', 1), ('T', 100)],
        'A': [('T', 1)],
        'T': [],
        'U': []
    }
    dist = run_dijkstra(graph, 'S')

    print(dist)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    #_run_tests()
    test_dijkstra_algorithm()
