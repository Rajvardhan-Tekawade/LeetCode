class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split(" ")
        index=0
        for i in title:
            c=len(i)
            if c>2:
                title[index]=title[index].capitalize()
            else:
                title[index]=title[index].lower()
            index+=1
        s=""
        for i in title:
            s=s+i+" "
        return s.strip()