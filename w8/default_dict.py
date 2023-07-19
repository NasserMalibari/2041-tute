
import collections

d_dict = collections.defaultdict(int)

# normally a key error!
d_dict["a"] += 1
print(d_dict)

