# Implement a decorator mod_div() which assures that the numerator is always greater
# than the denominator

def divmod(a, b):
  print(a/b)
def mod_div(fun):
  def inner(a, b):
    if a < b:
      a, b = b, a
    fun(a, b)     
  return inner
divmod = mod_div(divmod) 
divmod(2, 4)