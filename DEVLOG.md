# Development Log – The Torchbearer

**Student Name:** Oscar DeHamer
**Student ID:** 130672227

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [05/12]: Initial Plan

I will start with the written parts, doing part 1 through 4 before I start on the run_dijkstra function. I think that the dijkstra implementation seems pretty difficult, but over the entire project, the _explore function looks really difficult because the pruning especially. I will be sure to test any edge cases I think of while I am writing my code.

---

## Entry 2 – [05/13]: Fixing Dijkstra

I realized my initial Dijkstra implementation was wrong. I was scanning linearly and my time complexity was O(n^2), but if I used a heap I could lower the time complexity and it is probably the intended solution, as this is how we did it in class. I am going to try to implement using a heap for Dijkstra's now. 

---


## Entry 4 – [05/13]: Post-Implementation Reflection

I didn't finish parts 5 and 6 because I ran out of time, but if I had managed my time better, I would have implemented those. I fixed my work for parts 1-4 and am pretty happy with those though.

---

## Final Entry – [05/13]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 |
| Part 2: Precomputation Design | 3 |
| Part 3: Algorithm Correctness | 0.5 |
| Part 4: Search Design | 0.5 |
| Part 5: State and Search Space | 0.25 |
| Part 6: Pruning | 0.25 |
| Part 7: Implementation | |
| README and DEVLOG writing | 1.5 |
| **Total** | 6.5 |
