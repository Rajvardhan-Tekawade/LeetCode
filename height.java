class Solution {
    public int heightChecker(int[] heights) {
        int t=0;
        int expected[]=new int[heights.length];
        for(int i=0;i<heights.length;i++)
        {
            expected[i]=heights[i];
        }
        for(int i=0;i<heights.length-1;i++)
        {
            for(int j=0;j<heights.length-i-1;j++)
            {
                if(heights[j]>heights[j+1])
                {
                    t=heights[j];
                    heights[j]=heights[j+1];
                    heights[j+1]=t;
                }
            }   
        }
        t=0;
        for(int i=0;i<heights.length;i++)
        {
            if(expected[i]!=heights[i])
            {
                t+=1;
            }
        }
        return t;
    }
}