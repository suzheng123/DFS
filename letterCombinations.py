"""
425. Letter Combinations of a Phone Number
Given a digit string excluded '0' and '1', return all possible letter combinations that the number could represent.

Example 1:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation: 
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'
"""

d = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        result = []
        
        if digits:
            if len(digits) == 1:
                return d[digits]
                
            self.dfs(digits,0,'',result)
        return result
    
    def dfs(self,digits,index,string,results):
        if index == len(digits):
            results.append(string)
            return
    
        for letter in d[digits[index]]:
            self.dfs(digits,index+1,string+letter,results)
        