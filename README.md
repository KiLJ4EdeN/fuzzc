# fuzzc
A simple python module to Use fuzzy logic. All the methods return the Fuzzy_Set class. Which is easy to use compared to using traditional numpy arrays.

Hint that the module is still in proggress.
Any contribution is welcome.
The idea is to provide a utility, with the ability to compete with matlab. 



[![License](https://img.shields.io/github/license/KiLJ4EdeN/fuzzc)](https://img.shields.io/github/license/KiLJ4EdeN/fuzzc) [![Version](https://img.shields.io/github/v/tag/KiLJ4EdeN/fuzzc)](https://img.shields.io/github/v/tag/KiLJ4EdeN/fuzzc) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/fuzzc)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/fuzzc) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/fuzzc)](https://img.shields.io/github/repo-size/KiLJ4EdeN/fuzzc) [![Issue open](https://img.shields.io/github/issues/KiLJ4EdeN/fuzzcfuzzc)](https://img.shields.io/github/issues/KiLJ4EdeN/fuzzc)
![Issue closed](https://img.shields.io/github/issues-closed/KiLJ4EdeN/fuzzc)

## Available Functions Up to now.

add, substract, multiplication, comparative operatiors ( >, <, etc), show, support, crossover, is_fuzzy_singleton,
center, plot_membership, height, alpha_cut, core, is_normal, is_convex.
## Prerequisites:

1 - Python

2 - Numpy

3 - Matplotlib


### To see an example usage:

1 - Clone the repo and put the module in the cwd.
```bash
git clone https://github.com/KiLJ4EdeN/fuzzc/
cd fuzzc
python3
```
2 - Import the module and try some functionalities:
```python
import fuzzc.core as fuzzc
# create a set of points in the set.
fuzzy_set = np.linspace(0, 100, 1, dtype=np.int32)
print(fuzzy_set)
# create a random membership function.
membership_fn = np.around(np.random.rand(len(fuzzy_set)), decimals=1)
# create the Fuzzy_Set instance.
myset = fuzzc.Fuzzy_Set(fuzzy_set=fuzzy_set, membership_fn=membership_fn)
# Use the utilities.
myset.show()
myset.is_fuzzy_singleton()
```

3 - A more generilized example.
```python
import fuzzc.core as fuzzc
# height fuzzy example with plot.
# define height ranges
fuzzy_set = np.array([130, 140, 150, 160, 170, 180, 190, 200, 210])
# create a custom membership function for average height (avg = 170).
membership_fn = np.array([0., 0.1, 0.25, 0.5, 1.0, 0.5, 0.25, 0.1, 0])
myset = fuzzc.Fuzzy_Set(fuzzy_set=fuzzy_set, membership_fn=membership_fn)
# show the members and their respective membership.
myset.show()
# plot the membership function.
myset.plot_membership()
# find the height.
myset.height()
# extract the cross over points and the support.
supp_set, supp_fn = myset.support()
print(supp_set)
print(supp_fn)
cross_set, cross_fn = myset.crossover()
print(cross_set)
print(cross_fn)
# find the center of the set.
myset.center()
# Alpha cuts are also available.
alpha_cut, fn = myset.alpha_cut(0.5)
print(alpha_cut)
print(fn)
# The core of a fuzzy set is where the memberships are maximized( ==1 ).
core, core_fn = myset.core()
print(core)
print(core_fn)
```

 

