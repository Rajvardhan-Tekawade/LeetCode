class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
            for j in range(len(image)):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image