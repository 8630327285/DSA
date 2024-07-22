def isvalid(s);
  st = []
  for i range(len(s)):
    if s[i] == '(' or s[i]) == '{' or s[i] == '[':
        st.append(s[i])
    elif s[i] == ')' and st[-1] !='(': return False
    elif s[i] == '}' and st[-1] != '{' : return False
    elif s[i] == ']' and st[-1] != '[' : return False