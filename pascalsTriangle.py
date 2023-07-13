class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(numRows):
            temp_list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    temp_list.append(l[i-1][j-1]+ l[i-1][j])
            l.append(temp_list)
        return l
            

            
