#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import numpy as np
import sys
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html")
print()
print(form)
print("<br><br>")

a=int(form.getvalue("a"))
b=int(form.getvalue("b"))
c=int(form.getvalue("c"))

print(a,b,c)



#def find_roots(a, b, c):
x1 = (-b + np.sqrt(b*b - 4*a*c))/2*a
x2 = (-b - np.sqrt(b*b - 4*a*c))/2*a
#return (x1, x2)


print(x1,x2)

# if __name__ == "__main__":
# 	a, b, c = sys.argv[1:4]
# 	roots = find_roots(int(a), int(b), int(c))
# 	print(roots)