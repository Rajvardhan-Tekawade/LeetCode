class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        m=0
        for i in range(1,len(salary)-1):
            m+=salary[i]
        m=m/(len(salary)-2)
        return m