# Linear probing
*... is a way of resolving hash collisions*

## General
* there are different strategies for resolving hash collisions, linear probing is one of them
* still pretty good, despite being created in 1954

### Hashing strategies
* `closed addressing` -> all elements with hash collisions are stored in some secondary data structure
```python
if key in hash_map:
    hash_map[key].append(value)
else:
    hash_map[key] = [value]
```
* `perfect hashing` -> no collisions (e.g. `cuckoo hashing`)
* `open addressing` -> elements may *leak out*

### Linear probing (open addressing)
* `on insert`
  * compute h(x)
  * try to insert x at h(x)
  * if h(x) is occupied, try h(x+1), h(x+2), ...
* `on delete`
  * use `tombstones` to mark cell as *empty, but previously occupied*
  * on lookup, we don't stop at tombstones 

### Primary clustering
* main problem, causing linear probing performance to degrade

## References
* [stanford lecture](https://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/12/Small12.pdf)
