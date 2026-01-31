#  Challenge #4: The Unique Identifier Check
**Tier I: Novice (Day 4)**

In data management, we often need to ensure that IDs (like social security numbers or product codes) are unique. If there are duplicates, our data is "dirty."

---

###  The Task
Write a Python function `has_duplicates(id_list)` that returns `True` if any ID appears more than once, and `False` if every ID is unique.

### ⚙️ Constraints
* **The Twist:** To think like a Grandmaster, try to solve this without using a loop.
* **Logic:** Utilize Python's built-in data structures—specifically one that does not allow duplicate elements.

### 💻 Example
**Input A:**
```python
ids = [101, 102, 103, 101] # Returns True
```

**Input B:**
```python
ids = [1, 2, 3, 4, 5] # Returns False
```

Note: Compare the length of the original list to the length of a set() version of that list.
