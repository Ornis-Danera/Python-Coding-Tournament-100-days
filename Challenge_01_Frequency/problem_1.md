#  Challenge #1: The Frequency Counter
**Tier I: Novice (Day 1)**

In data science, we often start by understanding the distribution of our data.

---

###  The Task
Write a Python function `get_frequency(data)` that takes a list of items and returns a dictionary where the keys are the items and the values are their counts.

### ⚙️ Constraints
* **Manual Logic:** Do not use the built-in `collections.Counter`.
* **Scalability:** Your solution should handle a list of at least **1,000 items** efficiently.

###  Example
**Input:**
```python
data = ["apple", "banana", "apple", "cherry", "banana", "apple"]
```

**Output:**
```python
{"apple": 3, "banana": 2, "cherry": 1}
```

Note: Remember: Clean code is not written; it is refined.
