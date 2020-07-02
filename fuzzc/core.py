# package name = fuzzc
# python setup.py sdist
# v_01 twine upload dist/*
import numpy as np
import matplotlib.pyplot as plt



class Fuzzy_Set():
  # built ins
  def __init__(self, fuzzy_set, membership_fn):
    """
    Create a fuzzy set, using a set and a membership function.
    :param self: a Fuzzy_Set instance.
    :param fuzzy_set: A set to create the fuzzy set from.
    :param membership_fn: A membership_fn associated with the set.
    :return: a Fuzzy_Set instance.
    """
    self.fuzzy_set = fuzzy_set
    self.membership_fn = membership_fn
  
  def __str__(self):
    # for when the object is printed out.
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

  # Class Methods
  def show(self):
    """
    Show a fuzzy set and memberships is tuple pairs.
    :param self: a Fuzzy_Set instance.
    :return: a list containing the pairs.
    """
    out = []
    assert len(self.fuzzy_set) == len(self.membership_fn)   
    if len(self.fuzzy_set) >= 1:
      for item, fn in zip(self.fuzzy_set, self.membership_fn):
        out.append(tuple((np.around(item, 2), np.around(fn, 2))))
    print(out)
    del out
    return None
  
  def support(self):
    """
    Compute where the fuzzy memberships are bigger than zero.
    :param self: a Fuzzy_Set instance.
    :return: a Fuzzy_Set with memberships greater than zero.
    """
    fuzzy_set = self.fuzzy_set[self.membership_fn > 0.0]
    membership_fn = self.membership_fn[self.membership_fn > 0.0]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def crossover(self):
    """
    Find where in fuzzy set the membership is "0.5"
    :param self: a Fuzzy_Set instance.
    :return: Points in fuzzy set where membership is "0.5"
    """
    fuzzy_set = self.fuzzy_set[self.membership_fn == 0.5]
    membership_fn = self.membership_fn[self.membership_fn == 0.5]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def is_fuzzy_singleton(self):
    """
    A fuzzy set with a support of length one.
    :param self: a Fuzzy_Set instance.
    :return: True if the set is singleton else False.
    """
    if len(self.fuzzy_set[self.membership_fn >= 0.0]) == 1:
      return True
    else:
      return False
        
  def center(self):
    # TODO: rewrite for a bigger center
    """
    Compute the fuzzy set center.
    :param self: a Fuzzy_Set instance.
    :return: Fuzzy_Set with maximum membership.
    """
    fuzzy_set = self.fuzzy_set[self.membership_fn >= np.amax(self.membership_fn)]
    membership_fn = self.membership_fn[self.membership_fn >= np.amax(self.membership_fn)]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def plot_membership(self):
    """
    Plot the fuzzy set membership.
    :param self: a Fuzzy_Set instance.
    :return: membership plot using matplotlib.
    """
    try:
      import matplotlib.pyplot as plt
      plt.plot(self.fuzzy_set, self.membership_fn, 'b')
    except:
      print('Could not import matplotlib. Make sure to install.')

  def height(self):
    """
    Compute the fuzzy set height.
    :param self: a Fuzzy_Set instance.
    :return: Maximum membership.
    """
    return np.amax(self.membership_fn)

  def alpha_cut(self, alpha=0.5):
    """
    Compute the fuzzy set alpha cut.
    :param self: a Fuzzy_Set instance.
    :param alpha: cut value for membership_fn.
    :return: Fuzzy_Set with memberships bigger than selected alpha.
    """
    fuzzy_set = self.fuzzy_set[self.membership_fn >= alpha]
    membership_fn = np.ones(fuzzy_set.shape)
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def core(self):
    """
    Compute the fuzzy set core.
    :param self: a Fuzzy_Set instance.
    :return: Fuzzy_Set with membership equal to "1".
    """
    fuzzy_set = self.fuzzy_set[self.membership_fn == 1]
    membership_fn = self.membership_fn[self.membership_fn == 1]
    return Fuzzy_Set(fuzzy_set, membership_fn)

  def is_normal(self):
    """
    Check if the fuzzy set is normal.
    :param self: a Fuzzy_Set instance.
    :return: True if maximum membership is "1" ow False.
    """
    if np.amax(self.membership_fn) == 1:
      return True
    else:
      return False

  def is_subnormnal(self):
    """
    Check if the fuzzy set is subnormal.
    :param self: a Fuzzy_Set instance.
    :return: False if maximum membership is "1" ow True.
    """
    if np.amax(self.membership_fn) == 1:
      return False
    else:
      return True

  def is_complete(self):
    """
    Find if a fuzzy set is complete.
    :param self: a Fuzzy_Set instance.
    :return: True if the set is complete ow False.
    """
    return True if sum[self.membership_fn == 0.5] == len(self.membership_fn) else False

  def is_convex(self):
    # Incomplete
    return True

  def complement(self, method=None, l=0, w=1):
    """
    Create a complement for a fuzzy set.
    :param self: a Fuzzy_Set instance.
    :param method: Complement method.
    :param l: The l parameter is for the sugeno method.
    :param w: The w parameter is for the yager method.
    :return: A complemented Fuzzy_Set instance.
    """
    methods = ['sugeno', 'yager']
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
      print(f'Bad Method. Available Methods are: {methods[0], methods[1]}')
      return None
