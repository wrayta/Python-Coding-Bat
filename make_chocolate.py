"""
We want to make a package of goal kilos of chocolate. We have small bars (1 kilo 
each) and big bars (5 kilos each). Return the number of small bars to use, 
assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""
def make_chocolate(small, big, goal):
  while big * 5 > goal and big > 0:
    big -= 1
    
  num_of_small_bars_required = goal - (big * 5)
  
  if(small >= num_of_small_bars_required):
    return num_of_small_bars_required
  else:
    return -1