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


### What did I learn?

- Getting better at thinking more abstract instead of brute force. Maybe?
- Use `strip()` when pulling in text data!
- Use `range(a, b)` to iterate over things without storing every instance!
- Use `sort()` to sort in place, and `sorted()` to return sorted list.
- `sorted()` can be made more elaborate (like pandas) through the use of a `lambda`.
