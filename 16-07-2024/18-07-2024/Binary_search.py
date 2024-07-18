def search(arr,target):
  i=0
  j=len(arr)-1
  while i<=j:
    mid=(i+j)//2
    if arr[mid] == target:
      return mid
    elif target<arr[mid]:
      j=mid-1
    elif target>arr[mid]:
      i=mid+1
      return "not found"
    
arr=[1,4,5,7,8,10,12,15,16]
print(search(arr,12))


