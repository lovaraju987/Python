import re

with open('index.html','r') as openIndex:
   html = openIndex.read()

reg = r'([a-zA-Z0-9-/.]+(\.js|\.jpg|\.png|\.html|\.gif|.css))'

res = r"{% static '\1' %}"

repl = re.sub(reg,res,html)
print(repl)
with open('htmltxt.html','w') as f:
   f.write(repl)

