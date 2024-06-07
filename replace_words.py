class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        sentence=sentence.split(" ")
        for i in dictionary:
            for j in range(len(sentence)):
                if i == sentence[j][0:len(i)]:
                    sentence[j]=i
        r=""
        for i in sentence:
           r=r+i+" "
        return (r[:-1])
