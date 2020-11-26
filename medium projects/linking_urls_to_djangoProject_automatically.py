import re

with open('C:/Users/maila/Development/python_projects/learning python basics/learning concepts and practising/regular expressions/home.html','r') as openIndex:
   html = openIndex.read()

reg = r'([a-zA-Z0-9-/._]+(\.js|\.jpg|\.png|\.html|\.gif|.css))'

res = r"{% static '\1' %}"

repl = re.sub(reg,res,html)
print(repl)
with open('C:/Users/maila/Development/python_projects/learning python basics/learning concepts and practising/regular expressions/home.html','w') as f:
   f.write(repl)
