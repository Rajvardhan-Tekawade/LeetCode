class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence=sentence.split(" ")
        goat=""
        index=0
        for i in sentence:
            index+=1
            if i[0] in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
                goat=goat+i+"ma"
            else:
                goat=goat+i[1:]+i[0]+"ma"
            for j in range(index):
                    goat=goat+"a"
            goat=goat+" "
        goat=goat.strip()
        return goat