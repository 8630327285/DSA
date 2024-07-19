def ispalindrome(s):
  if len(s) <= 1:
    return True
  if s[0]!=s[-1]:
    return False
  
  return ispalindrome(s[1:len(s)-1])
                      
  
##print(ispalindrome("malayalam"))

print(ispalindrome("nitin"))