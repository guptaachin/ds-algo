## Details for question

Link: [here](https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150) <br>
Python  
    - [Code file](lc20.py)  
    - [Test file](lc20_test.py)

Tags: easy, stack

Description:

- Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Questions:

- What happens with ? `({)}` < is invalid - here correct order is important
- Why is this invalid `{{)` ?

Observations:

- The question does not make clear if `({)}` is valid or invalid ?
- There can be a question where `({)}` can be valid. In this case we can maintain a freq count dict of open brackets.

Complexity:

- Space - Stack creation = len(s) = O(n)
- Time - Iterate once through string - O(n)
