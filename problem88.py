nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3
k = m + n

i, j, k = m-1, n-1, k-1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k = k - 1

while j > 0:
    nums1[k] = nums2[j]
    j = j - 1
    k = k - 1

print(nums1)