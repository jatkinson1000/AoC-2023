# AoC-2023
Repository for [Advent of Code 2023](https://adventofcode.com/2023)

### Log

- Day 1 :sparkles: :sparkles:
  - Extracting numbers from strings
- Day 2 :sparkles: :sparkles:
  - Extracting numbers from more mangled strings and processing
- Day 3 :sparkles: :sparkles:
  - Extracting numbers based on adjacent symbols.  
    This one was hard. The approach and code is disgusting and could be significantly improved.
- Day 4 :sparkles: :sparkles:
  - Recursion.  
    This could probably be done more efficiently with fewer repeated checks with a little thought.
- Day 5 :sparkles: :sparkles:
  - Mappings.  
    p1 easy, wrote p2, tried to brute force, didn't work.  
    Stepping back and trying to be clever was really difficult.  
    Extending a list whilst actively iterating over it doesn't feel right at all!  
    Given up on perfect docstrings.
- Day 6 :sparkles: :sparkles:
  - Calculations.  
    This one even has tests! :O Nice in comparison to yesterday.  
    Could probably have used bisection or quadratic formula if wanting to be clever.
- Day 7 :sparkles: :sparkles:
  - Calculations.  
    String processing and complex (well more than most basic) sorting.
- Day 8 :sparkles: :sparkles:
  - Calculating path lengths through nodes and overlapping cycles.  
    Solution can be found from making more general asumption than problem states >:(.  
    Wasn't obvious to me I feel.
- Day 9 :sparkles: :sparkles:
  - Sequences.
- Day 10 :sparkles: :sparkles:
  - Maps. Slow on part 1 but set me up well for part 2. 4th overall in RSE.  
    Lost a lot of time in part 2 debugging code that was 'correct' before realising I need to replace `S`. Then did manually for solution before adding general function later.
- Day 11 :sparkles: :sparkles:
  - Maps with 'expanding' distance. Part 2 required refactor after part 1 leads on a red herring. t ~ 1h. 5th overall in RSE.  
- Day 12 :sparkles: :sparkles:
  - Part 2 was really hard. Had to get a hint to implement the dynamic programming aspect. A useful learning opportunity.
- Day 13 :sparkles: :sparkles:
  - Bad/lazy variable naming caused bug that I missed leading me to seek more and more elaborate interpretations to the problem. Would likely have been avoided with more care/testing. As a result the end product is somewhat Frankencode.
- Day 14 :sparkles: :sparkles:
  - Fun one. Spotted part 2 trick quickly. t ~ 1.5h. 4th overall in RSE.  
    Possibly a more concise way of coding tilts rather than 4 functions, one for each direction?
- Day 15 :sparkles: :sparkles:
  - Creating a hash map and sorting items in boxes. Dictionaries (ordered by default in py now) made it easy! t ~ 1h. 4th overall in RSE.
- Day 16 :sparkles: :sparkles:
  - Tracing map round a board. Set myself up well for part 2 by writing for general starting location and direction!
  t ~ 1.5h. 3rd overall in RSE.  
- Day 17 :sparkles: :sparkles:
  - Path finding. Goodness this one was hard! Started with Dijkstra but hard to figure out extra conditions. Moved to a variant of A* based on hint but that ran unbelievably slowly until learning that sets are _significantly_ faster to search than lists in python. also some speed gain from using `continue` in loops to avoid extra computation.  
  t ~ 7h. 3rd overall in RSE!?
- Day 18 :sparkles: :sparkles:
  - Tracing and filling a polygon. Didn't fall for the troll move using the colours! Learnt flood fill for part 1, but total re-write for part 2 using shoelace algorithm.  
  t ~ 1.5-2h. 4rd overall in RSE
- Day 18 :sparkles: :sparkles:
  - More mappings through rules.  
    Pretty pleased with this one! Leveraged the power of dicts and lesson learnt from day 5 using ranges.  
  t ~ 2h. 2nd overall in RSE

### What did I learn?

- Getting better at thinking more abstract instead of brute force. Maybe?
- List comprehensions are king.
- But sets are MUCH faster to search than lists. (d17)
- Use `strip()` when pulling in text data!
- Use `range(a, b)` to iterate over things without storing every instance! (d5, d19)
- Use `sort()` to sort in place, and `sorted()` to return sorted list.
- `sorted()` can be made more elaborate (like pandas) through the use of a `lambda`.
- Double and nested list comprehensions can be useful `[[i for i in j] for j in k]` or `[i for j in k for i in j]`.
- 2D nested lists are indexed `[j][i]`, not `[i][j]` (same as numpy?) which caused me some bugs/loss of time and made me sad.
- As problems get harder doing part one 'properly'/'completely'/'verbosely' sets you up well for part two.
- Dynamic programming: store function inputs and returns in a hash table for quick lookup.  
  Can be done in python using `@cache` decorator from `functools`
- Strings can be accessed like lists but don't suffer from out of bounds errors - just return `''` if longer than string! Can be exploited to avoid termination due to OoB.
- `[{}] * n` does NOT create a list of n empty dicts, instead it creates a list of n copies of a single dict! Use `[{} for _ in range(n+1)]` instead!
- Instead of giant multi-condition if statements consider single clauses with `continue` to avoid unnecessary computation. (d17)
- Learnt about [heapq](https://docs.python.org/3/library/heapq.html) from python library for priority queue sorting. (d17)
- A* algorithm for path finding (alternative to Dijkstra). (d17)
- Flood filling a polygon (d18)
- [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) for area of a polygon based on coordinates. (d18)
- `range`s are powerful, small, and you can index them! (d19)
