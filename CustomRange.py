# Implementing custom range function using yield
from multipledispatch import dispatch


def customRange (end):
  i = 0
  increment = 1
  while (i < end):
    yield i
    i = i + increment


def customRange(start, end, step = 1):
  i = start
  while(i < end):
    yield i
    i = i + step

for i in customRange(5, 15):
  print(i)
