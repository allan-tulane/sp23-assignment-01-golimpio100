"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra, rb = foo(x-1), foo(x-2)
        return ra + rb
    pass

def longest_run(mylist, key):
    ### TODO
    maxrun = 0
    curr = 0
    for i in mylist:
      if i == key:
        curr += 1
      else:
        maxrun = max(maxrun, curr)
        curr = 0
    return max(maxrun, curr)
    pass
  
print(longest_run([1,2,4,2,6,2,4,4,4,5,7],4))

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    n = len(mylist)
    if n == 0:
      return Result(0, 0, 0, False)
    elif n == 1:
        return Result(1 if mylist[0] == key else 0, 1 if mylist[0] == key else 0, 1 if mylist[0] == key else 0, mylist[0] == key)
    else:
        mid = n // 2
        leftr = longest_run_recursive(mylist[:mid], key)
        rightr = longest_run_recursive(mylist[mid:], key)
        is_entire_range = leftr.is_entire_range and rightr.is_entire_range and mylist[mid-1] == mylist[mid] == key
        longest_size = max(leftr.longest_size, rightr.longest_size, leftr.right_size + rightr.left_size if is_entire_range else 0)
        left_size = leftr.left_size + (rightr.left_size if leftr.is_entire_range else 0)
        right_size = rightr.right_size + (leftr.right_size if rightr.is_entire_range else 0)
        return Result(left_size, right_size, longest_size, is_entire_range)
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


print(longest_run_recursive([1,2,4,2,6,2,4,4,4,5,7],4))