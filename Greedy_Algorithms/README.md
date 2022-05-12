# Greedy Algorithms

Recruiter from Google is actively hiring engineers. He has the following choices each month.
```
Month 1           Month 2           Month 3             
  0                 0                 0    
 /|\               /|\               /|\   
 / \               / \               / \   

 40 L              40 L              41 L

  0                 0                 0    
 /|\               /|\               /|\   
 / \               / \               / \   

 50 L              56 L              36 L

  0                 0                 0    
 /|\               /|\               /|\   
 / \               / \               / \   

 55 L              67 L              38 L

  0                 0                 0    
 /|\               /|\               /|\   
 / \               / \               / \   

 45 L              35 L              35 L
```
Consider all the candidates are of equal quality, the recruiter should choose the first candidate from month1, the fourth candidate from month2, the third candidate from month3.

Knapsack is the name given for a particular variety of problems. There are N items and each item has two associated properties which are the weight of the item and the value of the item. Pick items such that total value is maximised or minimised.


Fractional knapsack

- Sort all items on the basis of per unit cost (value/weight)
- Iterate, pick the best and keep updating the weight

0/1 knapsack

When can we apply Greedy algorithms?

When the choice made in the beginning does not affect the choice to be made towards the end. If it does affect we cannot apply greedy algorithms. For e.g., in 0/1 knapsack problems, optimizing the initial choice will affect the choices available in the end. 

Given an array A of the active sale time and an array B of the beauty of the corresponding car, purchase cars such that we maximize the beauty.
