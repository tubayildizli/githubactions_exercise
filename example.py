
def add(a, b):
  return a + b

def subtract(a, b):
  return a + b  # do not change this line until prompted to do so.


def test_add():
  assert add(3,4)     == 7
  assert add("a","b") == "ab"
  
def test_subtract():
  assert subtract(4,3) == 1
  assert subtract(5,2) == 3