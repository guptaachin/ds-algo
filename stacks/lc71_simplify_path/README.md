## Details for question

Link: [here](https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150) <br>
Python  
    - [Code file](lc71.py)  
    - [Test file](lc71_test.py)

Tags: stacks, medium

Description:

- Given a unix path with `..` and `.`
- Create a canonical path

Thoughts:

- Here stack is needed to effectively deal with things like `/a/../../../b/../`
- For repetitive `../../` stack’s pop method is useful.

Complexity:

- Time - O(n)
- Space - O(n)
