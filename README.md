# The Torchbearer

**Student Name:** Oscar DeHamer
**Student ID:** 130672227
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run from S finds only the shortest distance from the entrance to one location, but does not give the optimal order to visit multiple relics. You need to know distances from all of the sources to all the relics to determine the optimal solution.

- **What decision remains after all inter-location costs are known:**
  The optimal order to visit the relics, because different orderings give different total costs.

- **Why this requires a search over orders (one sentence):**
  The total torch fuel cost depends on the order in which relics are visited, so the optimal order must be discovered through searching all the orders instead of just a simple greedy algorithm.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Spawn node | It is the starting location, so I need distances from it to the relics. |
| Relic chamber node | Each relic can be the current location during the route, so I need distances from every relic to the other relics and the exit. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary: dist_table[source][destination] |
| What the keys represent | The outer key is a source node; the inner key is a destination node. |
| What the values represent | The minimum torch fuel cost from the source to the destination. |
| Lookup time complexity | O(1)|
| Why O(1) lookup is possible | Python dictionaries allow a source/destination pair be found without checking other entries. |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k+1
  Spawn + every relic = k+1
- **Cost per run:** O(n^2 + m)
  Scanning for the next node is O(n^2) plus checking and updating distances across all m edges.
- **Total complexity:** O((k+1) (n^2 + m))
  Multiply number of runs (k+1) by cost per run (n^2 + m).
- **Justification (one line):** Run the Djikstra from the spawn and each of the k relics, then multiply runs by per run cost.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  Their distances are done and the current number is the actual shortest distance from the source.

- **For nodes not yet finalized (not in S):**
  Their distances are only the best ones found so far, based on paths that go through finalized nodes.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Before the loop starts, only the source is finalized with distance 0. Every other node is set to infinity because no path has been found to them yet.

- **Maintenance : why finalizing the min-dist node is always correct:**
  The next node chosen has the smallest distance, so any other path to it would have to go through a node with distance at least the same distance. And since edge weights are nonnegative, the path cannot become cheaper later, so the minimum distance right now is correct.

- **Termination : what the invariant guarantees when the algorithm ends:**
  When there are no nodes left to finalize, every distance in the table is the shortest distance from the source.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

If you know all the shortest distances, you can plan a route that uses the real travel cost between relics.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Picking the closest next relic can make the whole route more expensive.
- **Counter-example setup:** In the spec example, S can go to B, C, or D first and the later travel costs are not the same.
- **What greedy picks:** Greedy picks the closest next relic first, such as S -> B, because it looks cheapest right now.
- **What optimal picks:** The best route may start with a slightly longer first step, like S -> C, if that makes the rest of the route cheaper.
- **Why greedy loses:** A cheap choice can force an expensive one later which leads to a more expensive total cost.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore every order of visiting the relics, because the best total cost depends on th entire sequence.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
