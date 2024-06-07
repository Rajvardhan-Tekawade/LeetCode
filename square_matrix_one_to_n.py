#The test case for n=19 isn't working (reason: The LeetCode answerkey switches the expected output between true and false)
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        
        l=0
        t=[]
        for i in matrix[0]:
            l+=1
            t.append(l)
        for i in matrix:
            i.sort()
            if i!=t:
                return False
        return True