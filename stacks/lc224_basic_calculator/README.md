## Details for question

Links   
[Question](https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150) <br>
Python  
    - [Code file](lc224_basic_calculator.py)  
    - [Test file](lc224_basic_calculator_test.py)

Tags: stacks, hard

Description:

- Given an expresstion with "(", "-1", "+", "-" and "nested ()"
- Evaulate the expression.

Questions:

- How do you deal with nested operation and unary operators "-1"

Observations:

- I tried to tokenize it first but it did not work.

Complexity:

- Time:
- Space:


Dry Run solution:
Test case - "(1+(4+5+2))", 12

num = 0, sign = 1, res = 0, stack = [] 
0 -- '(' -- stack = [0, 1] res = 0, sign =1
1 -- '1' -- num = 1
2 -- '+' -- res = 0 + 1*1 = 1, num = 0, sign = 1
3 -- '(' -- stack = [0,1,1,1] res = 0, sign = 1
4 -- '4' -- num = 0*10+4 = 4
5 -- '+' -- res = 4, sign = 1, num = 0
6 -- '2' -- num = 2
7 -- ')' -- res = 8, res = 8 * 1 = 8, 
