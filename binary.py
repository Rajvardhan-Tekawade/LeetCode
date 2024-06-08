class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        s1=s2=c=0
        for i in a:
            s1=s1+int(i)*(2**c)
            c+=1
        c=0
        for i in b:
            s2=s2+int(i)*(2**c)
            c+=1
        s3=s1+s2
        s3=bin(s3)
        s3=str(s3)
        return (s3[2:])