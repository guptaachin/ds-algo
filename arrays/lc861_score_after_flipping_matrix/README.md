## Details for question

Link: [here](https://leetcode.com/problems/score-after-flipping-matrix/description/) <br>
Python  
    - [Code file](lc861.py)  
    - [Test file](lc861_test.py)

Tags: arrays, bit-manipulation,medium

Description:

- The question is to maximize the sum of binary numbers in all rows.
- Permitted operations are Flipping Rows and Flipping Columns

Questions:

- How do you be sure of getting to the best solution without trying all possible combos ?
  - How so you divide the problem into seeing MSB and LSBs ?

Observations:

- No matter what left most column is MSB and needs to be maximized.
  0111 = 2^0 + 2^1 + 2^2 = 7 and 1000 = 8 SO flipping makes sense.
- Next we need to maximize the number by keeping the changes we have done.
- Here the beautiful part is each bit can be seen as individual number in itself.

Complexity:

- Time: O(n^2)
- Space: O(1)
