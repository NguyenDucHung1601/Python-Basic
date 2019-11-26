import random as ra
import datetime as dt
import os as o

print(ra.randint(1,100))

t = dt.datetime.now()
print(t)
print(t.date())

print(o.getcwd())
print(o.getenv('PATH'))


