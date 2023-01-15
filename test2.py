#from f1.py1 import f1fun as f1
#from f1.f2.py2 import f2fun as f2
#f1()
#f2()

#from f1 import py1
#py1.f1fun()

from f1.f2 import py2

c = py2.py2class(10,20,'New')
print(c.p, c.a, c.b, c.s)
py2.f2fun()

from f1.f2.py2 import py2class as p
c1=p(100,200, 'New .....')
print(c1.p, c1.a, c1.b, c1.s)

from f1.f2.py2 import f2fun as p2

p2()

