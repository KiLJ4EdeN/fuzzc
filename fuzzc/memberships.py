# fuzzc.memberships
def triangular(a, b, c, x, plot=False):
  # Creates membership fn for a set.
  fuzzy_set = x
  for i, _ in enumerate(x):
    left = ((x[i]-a)/(b-a))
    right = ((c-x[i])/(c-b))
    x[i] = max(min(left, right), 0)
  if plot:
    import matplotlib.pyplot as plt
    plt.plot(x)
  return Fuzzy_Set(fuzzy_set, x)

def bell_shaped(a, b, c, x, plot=False):
  # Creates membership fn for a set.
  fuzzy_set = x
  for i, _ in enumerate(x):
    x[i] = 1 / (1 + (abs((x[i]-c)/a)) ** (2*b))
  if plot:
    import matplotlib.pyplot as plt
    plt.plot(x, 'r')
  return Fuzzy_Set(fuzzy_set, x) 
