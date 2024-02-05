## Details for question

Links  
[Question](https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150) <br>
Python  
 - [Code file](lc101.py)  
 - [Test file](lc101_test.py)

Tags: stack, medium

Questions:

- How do you create a stack where push, pop and getMin are all O(1) ?

Observations:

- The trick here is to keep the minimum in each stack entry.
- We create a stack with tuples (val, min_until_now)

Complexity:

- Time: O(1) - for each stated method
- Space: O(n) where n is length of stack
