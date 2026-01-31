#  Challenge #2: The Outlier Filter
**Tier I: Novice (Day 2)**

Data is often messy. Before analyzing it, we must remove "noise."

---

###  The Task
Write a Python function `filter_outliers(numbers, threshold)` that takes a list of integers and a threshold value. The function should return a new list containing only the numbers that are **less than or equal to** the threshold.

### ⚙️ Constraints
* **Pythonic Style:** Use a **List Comprehension** to make the code concise and readable.
* **Immutability:** Ensure the function returns a *new* list rather than modifying the original.

### 💻 Example
Input:
```python
numbers = [10, 55, 2, 100, 4, 75]
threshold = 50

```
**Output:**
```python
[10, 2, 4]
```
