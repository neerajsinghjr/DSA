"""
Problem Description:
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
The soldiers are positioned in front of the civilians. 
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:
    Input: mat = 
    [[1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]], 
    k = 3
    Output: [2,0,3]
    Explanation: 
    The number of soldiers in each row is: 
    - Row 0: 2 
    - Row 1: 4 
    - Row 2: 1 
    - Row 3: 2 
    - Row 4: 5 
    The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:
    Input: mat = 
    [[1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]], 
    k = 2
    ~ Output: [0,2]
    ~ Explanation: 
    The number of soldiers in each row is: 
    - Row 0: 1 
    - Row 1: 4 
    - Row 2: 1 
    - Row 3: 1 
    The rows ordered from weakest to strongest are [0,2,3,1].
"""


"""
Approach 1: Binary Search
"""
def getSoldiers(nums):
    start, end = 0, len(nums)
    while(start < end):
        mid = (start + (end-start))//2
        if(nums[mid] == 1):
            start = mid + 1
        else:
            end = mid
    return mid+1        
    

def kWeakestRows(mat, k: int):
    res = {}
    count = 0
    for key,row in enumerate(mat):
        print(row)
        break
    #     count = getSoldiers(row)
    #     print("count:",count, "row:",row)
    #     res[key] = count
    #     print("res:", res)
    # res = sorted(res, key=res.get)
    # return res[:k]
        
"""
Approach 2: Python Based Solution
"""
# def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#     dict1={}
#     tup1 = ()
#     count= 0
#     x =[]
#     for i in range(len(mat)):
#         tup1 = tuple(mat[i])
#         count = tup1.count(1)
#         dict1[i]=count
#     x= sorted(dict1, key=dict1.get)
#     return x[:k]    


def main():
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 
    k = 3
    res = kWeakestRows(mat, k)
    if res:
        for r in res:
            print("Result:",r, end=" ")
    print("")                                 ## Pretty Printing...


if __name__ == "__main__":
    print("#------------------------- Code Starts ----------------------#")
    main()
    print("#------------------------- Code Ends ---------------------#")