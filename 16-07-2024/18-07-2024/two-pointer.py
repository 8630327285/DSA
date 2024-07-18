def calc(arr,i,j,target):
  while i<=j:
    if arr[i]+arr[j]==target:
      return True
    elif arr[i]+arr[j]<target:
             i=i+1
    elif arr[i]+arr[j]>target:
        j=j-1
  return False
arr=[3,-2,5,6,9,13,5,12,8]
target=14
i=arr[0]
j=arr[8]
print(calc(arr,i,j,target))
