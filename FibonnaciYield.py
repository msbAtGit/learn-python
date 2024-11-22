# Interating over a list of items in Fibonnaci sequence using yield

def fibonnaci(n):
  term2 = 0
  term1 = 1


  for i in range(1,n + 1):
    term = term1 + term2
    yield term
    term2 = term1
    term1 = term

#using yield we get single item every time we call the fibonnaci function
for i in fibonnaci(8):
  print(i)
