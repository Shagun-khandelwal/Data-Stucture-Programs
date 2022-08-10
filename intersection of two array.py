# Leetcode 350. Intersection of two array
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    mylist=[]
    d={}
    for x in nums1:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    for x in nums2:
        if x in d:
            if d[x]>0:
                mylist.append(x)
                d[x]-=1
    return mylist

nums1=[1,2,2,1]
nums2=[2,2]
print(intersect(nums1,nums2))