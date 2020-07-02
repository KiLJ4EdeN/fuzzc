# operations module
# from fuzzc import operations
def s_norm(x, y, norm_method=None, l=1):
  """
  Compute S norm for two fuzzy sets.
  :param x: a Fuzzy_Set instance.
  :param y: a Fuzzy_Set instance.
  :param norm_method: s_norm method.
  :param l: l parameter for dombi method.
  :return: S normed Fuzzy_Set instance.
  """
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  assert all(x.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
  assert len(x.membership_fn) == len(y.membership_fn)
  if not norm_method:
    s_fn = []
    for a, b in zip(x.membership_fn, y.membership_fn):
      s_fn.append(max(a, b))
    return Fuzzy_Set(x.fuzzy_set, np.array(s_fn))
  elif norm_method == 'dombi':
    # higher lambdas equal in maximum.
    assert l > 0, ' l must be greater than 0.'
    d_fn = []
    for a, b in zip(x.membership_fn, y.membership_fn):
      d_fn.append(1 / ((1 + (((1/a)-1) ** -l + ((1/b)-1) ** -l ) ** (-1 / l))))
    return Fuzzy_Set(x.fuzzy_set, np.array(d_fn))
  else:
    print('Wrong Method.')
    return None

def t_norm(x, y, norm_method=None, l=1):
  """
  Compute T norm for two fuzzy sets.
  :param x: a Fuzzy_Set instance.
  :param y: a Fuzzy_Set instance.
  :param norm_method: s_norm method.
  :param l: l parameter for dombi method.
  :return: T normed Fuzzy_Set instance.
  """
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  assert all(x.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
  assert len(x.membership_fn) == len(y.membership_fn)
  if not norm_method:  
    s_fn = []
    for a, b in zip(x.membership_fn, y.membership_fn):
      s_fn.append(min(a, b))
    return Fuzzy_Set(x.fuzzy_set, np.array(s_fn))
  elif norm_method == 'dombi':
    # higher lambdas equal in minimum.
    assert l > 0, ' l must be greater than 0.'
    d_fn = []
    for a, b in zip(x.membership_fn, y.membership_fn):
      d_fn.append(1 / ((1 + (((1/a)-1) ** l + ((1/b)-1) ** l ) ** (1 / l))))
    return Fuzzy_Set(x.fuzzy_set, np.array(d_fn))
  else:
     print('Wrong Method.')
     return None

def algebraic_sum(x, y):
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  assert all(x.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
  assert len(x.membership_fn) == len(y.membership_fn)
  a_fn = []
  for a, b in zip(x.membership_fn, y.membership_fn):
    a_fn.append((a+b) - (a*b))
  return Fuzzy_Set(x.fuzzy_set, np.array(a_fn))

def algebraic_diff(x, y):
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  assert all(x.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
  assert len(x.membership_fn) == len(y.membership_fn)
  a_fn = []
  comp = 1 - y.membership_fn
  for a, b in zip(x.membership_fn, comp):
    a_fn.append(min(a, b))
  return Fuzzy_Set(x.fuzzy_set, np.array(a_fn))

def min_max_avg(x, y, l=0.5):
  # l=1 gives max, and l=0 gives out zero.
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  assert all(x.fuzzy_set == y.fuzzy_set), ' sets must use the same reference.'
  assert len(x.membership_fn) == len(y.membership_fn)
  m_fn = []
  for a,b in zip(x.membership_fn, y.membership_fn):
    m_fn.append((l*max(a,b))+((1-l)*min(a,b)))
  return Fuzzy_Set(x.fuzzy_set, np.array(m_fn))

def cartesian_prod(x, y):
  assert str(type(x)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'x must be a Fuzzy_Set instance.'
  assert str(type(y)) == '''<class 'fuzzc.core.Fuzzy_Set'>''', 'y must be a Fuzzy_Set instance.'
  r = len(x.membership_fn)
  c = len(y.membership_fn)
  c_fn = np.zeros((r, c))
  for i, _ in enumerate(x.membership_fn):  
    for j, _ in enumerate(y.membership_fn):
      c_fn[i, j] = min(x.membership_fn[i], y.membership_fn[j])
  return c_fn

# add AE and ML

def enhance(membership_fn, d):
  # enhance by an integer factor.
  membership_fn = membership_fn * d
  membership_fn[membership_fn>=1]=1
  return membership_fn

def weaken(membership_fn, d):
  # weaken by an integer factor.
  membership_fn = membership_fn / d
  return membership_fn

def projection(membership_fn, axis=0):
  if axis==0:
    count = membership_fn.shape[axis]
    fn = np.zeros((count, 1))
    for i in range(count):
      fn[i, 0] = np.amax(membership_fn[i, :])
    return fn
  elif axis==1:
    count = membership_fn.shape[axis]
    fn = np.zeros((1, count))
    for i in range(count):
      fn[0, i] = np.amax(membership_fn[:, i])
    return fn
  else: 
    print('Unsupported axes.')
    return None

def cylindrical_extension():
  return None
