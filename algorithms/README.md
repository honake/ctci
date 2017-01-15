# Editorial

## Sorting: Comparator

### functools.cmp_to_key(func)
Transform an old-style comparison function to a key function. Used with tools that accept key functions (such as sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby()).

A comparison function is any callable that accept two arguments, compares them, and returns a negative number for less-than, zero for equality, or a positive number for greater-than.
A key function is a callable that accepts one argument and returns another value to be used as the sort key.

#### Example:

```python3
sorted(iterable, key=cmp_to_key(locale.strcoll))
```
