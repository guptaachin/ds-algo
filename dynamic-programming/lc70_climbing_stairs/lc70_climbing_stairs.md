## Details for question

Links   
[Question](problem-link-here) <br>
Python  
    - [Code file](lc70_climbing_stairs.py)  
    - [Test file](lc70_climbing_stairs_test.py)

Tags: dynamic-programming, easy

Description:

- Given number of stairs and steps you can take, 1 and 2
- Calculate the number of ways you can reach the top

Questions:

- We can easily tackle this with Recursion, why not use it in this case ?
- Can you use Recursion and a data structure to remember the results.

Observations:

- To understand the DP solution, start calculating the ways from the top.
- This will say num_ways(n) = num_ways(n-1) + num_ways(n-2)
- Write it in top down manner now.

Complexity:

- Time: O(n)
- Space: O(1)
