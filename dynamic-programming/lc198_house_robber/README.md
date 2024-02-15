## Details for question

Links   
[Question](https://leetcode.com/problems/house-robber/solutions/?envType=study-plan-v2&envId=top-interview-150) <br>
Python  
    - [Code file](lc198_house_robber.py)  
    - [Test file](lc198_house_robber_test.py)

Tags: dynamic-programming, easy

Description:

- Given $ amount in houses
- No adjacent houses can be robbed.
- How much max money can you make ?

Questions / Observations:

- Here how do I tell this is a dp problem ? 
  - I smell recursion, because there is an urge to check all possible combo.
  - Recurson also says top down - If I want to max, should I rob first house or not ?
- Once I know this is a dp problem.
  - Build from bottom, start of array.
  - At 0 - Ask what is the best I can do if I rob this house.
  - At 1 - Ask he same question.
  - At 2 - it will be current + best done at 0.
  - At 3 - Current + max(Best(3-2), Best(3-1))

Complexity:

- Time: O(n)
- Space: O(n)
