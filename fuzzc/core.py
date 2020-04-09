# package name = fuzzc
import numpy as np
import matplotlib.pyplot as plt

class Fuzzy_Set():
  # built ins
  def __init__(self, fuzzy_set, membership_fn):
    # initialize
    self.fuzzy_set = fuzzy_set
    self.membership_fn = membership_fn
  
  def __str__(self):
    return f'Fuzzy_Control Fuzzy_Set instance with a length of {len(self.fuzzy_set)}'

  def __add__(self, y):
    try:
      assert all(self.fuzzy_set == y.fuzzy_set)
      assert len(self.membership_fn) == len(y.membership_fn)
      fn = self.membership_fn+y.membership_fn
      fn[fn>=1] = 1
      return self.fuzzy_set, fn
    except AssertionError:
      print('sets must use the same reference.')
    except:
      print('Wrong input!')
      return None

  def __sub__(self, y):
    try:
      assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
      assert len(self.membership_fn) == len(y.membership_fn)
      fn = self.membership_fn-y.membership_fn
      fn[fn<=0] = 0
      return self.fuzzy_set, fn
    except:
      print('Wrong input!')
      return None

  def __mul__(self, y):
      try:
        assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
        assert len(self.membership_fn) == len(y.membership_fn)
        fn = self.membership_fn*y.membership_fn
        return self.fuzzy_set, fn
      except:
        print('Wrong input!')
        return None

  def __gt__(self, y):
    assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
    assert len(self.membership_fn) == len(y.membership_fn)
    if all(self.membership_fn > y.membership_fn):
      return True
    else:
      return False

  def __lt__(self, y):
    assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
    assert len(self.membership_fn) == len(y.membership_fn)
    if all(self.membership_fn < y.membership_fn):
      return False
    else:
      return True

  def __ge__(self, y):
    assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
    assert len(self.membership_fn) == len(y.membership_fn)
    if all(self.membership_fn >= y.membership_fn):
      return True
    else:
      return False

  def __eq__(self, y):
    assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
    assert len(self.membership_fn) == len(y.membership_fn)
    if all(self.membership_fn == y.membership_fn):
      return True
    else:
      return False

  def __ne__(self, y):
    assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
    assert len(self.membership_fn) == len(y.membership_fn)
    if all(self.membership_fn == y.membership_fn):
      return False
    else:
      return True

  def __le__(self, y):
    assert all(self.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
    assert len(self.membership_fn) == len(y.membership_fn)
    if all(self.membership_fn <= y.membership_fn):
      return False
    else:
      return True
  # class methods.
  def show(self):
    out = []
    assert len(self.fuzzy_set) == len(self.membership_fn)   
    if len(self.fuzzy_set) >= 1:
      for item, fn in zip(self.fuzzy_set, self.membership_fn):
        out.append(tuple((item, fn)))
    print(out)
    del out
    return None
  
  def support(self):
    fuzzy_set = self.fuzzy_set[self.membership_fn > 0.0]
    membership_fn = self.membership_fn[self.membership_fn > 0.0]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def crossover(self):
    fuzzy_set = self.fuzzy_set[self.membership_fn == 0.5]
    membership_fn = self.membership_fn[self.membership_fn == 0.5]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def is_fuzzy_singleton(self):
    if len(self.fuzzy_set[self.membership_fn >= 0.0]) == 1:
      return True
    else:
      return False
        
  def center(self):
    # rewrite for a bigger center
    fuzzy_set = self.fuzzy_set[self.membership_fn >= np.amax(self.membership_fn)]
    membership_fn = self.membership_fn[self.membership_fn >= np.amax(self.membership_fn)]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def plot_membership(self):
    try:
      import matplotlib.pyplot as plt
      plt.plot(self.fuzzy_set, self.membership_fn, 'b')
    except:
      print('Could not import matplotlib. Make sure to install.')

  def height(self):
    return np.amax(self.membership_fn)

  def alpha_cut(self, alpha=0.5):
    fuzzy_set = self.fuzzy_set[self.membership_fn >= alpha]
    membership_fn = np.ones(fuzzy_set.shape)
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def core(self):
    fuzzy_set = self.fuzzy_set[self.membership_fn == 1]
    membership_fn = self.membership_fn[self.membership_fn == 1]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def is_normal(self):
    if np.amax(self.membership_fn) == 1:
      return True
    else:
      return False

  def is_convex(self):
    # Incomplete
    return True

  def complement(self, method=None, l=0, w=1):
    # The l parameter is for the sugeno method.
    # l = 0, equates method=None.
    # as l goes higher the memberships are shrinked.
    # The w parameter is for the yager method.
    # with w = 1, memberships equals methds=None.
    # as w goes higher the memberships are empowered.
    if not method:
      return Fuzzy_Set(self.fuzzy_set, 1 - self.membership_fn)
    elif method == 'sugeno':
      assert l > -1, ' l must be greater than -1.'
      sug_fn = []
      for a in self.membership_fn:
        # a fuzzy value of zero is always changed to 1.
        # which is a condition for creating complement classes.
        sug_fn.append((1-a)/(1+l*a))
      return Fuzzy_Set(self.fuzzy_set, np.array(sug_fn))
    elif method == 'yager':
      assert w > 0, 'w must be greater than 0'
      yag_fn = []
      for a in self.membership_fn:
        yag_fn.append((1-a**w)**(1/w))
      return Fuzzy_Set(self.fuzzy_set, np.array(yag_fn))
    else:
      return 'Bad Method.'
