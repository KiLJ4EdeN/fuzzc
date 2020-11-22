import numpy as np

# fuzzc.entropy
def fuzziness(x):
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  entropy = 0
  summation = []
  err = 0
  for member in x.membership_fn:
    # do not count NANS
    if member == 0:
      err = err+1
      pass
    else:
      summation.append(member*np.log(member) + (1-member)*np.log(1-member))
  entropy = (-1/(len(x.membership_fn)-err)) * (sum(summation))
  return entropy


def inaccuracy(x, y):
  # x with respect to y.
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  assert all(x.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
  assert len(x.membership_fn) == len(y.membership_fn)
  entropy = 0
  summation = []
  err = 0
  for m1, m2 in zip(x.membership_fn, y.membership_fn):
    if (m1 != 0) and (m2 != 0):
      summation.append(m1*np.log(m2) + (1-m1)*np.log(1-m2))
    else:
      err += 1
  summation = np.array(summation)
  entropy = (-1/(len(x.membership_fn) - err)) * (summation.sum())
  return entropy  
