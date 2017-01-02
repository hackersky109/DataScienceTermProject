import re
pat = '\'+\''
text = '\[u\'United States Capitol\''
r = re.findall(pat,text)
print(text.translate(None, 'u[\''))
