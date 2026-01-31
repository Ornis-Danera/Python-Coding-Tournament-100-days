#  Challenge #3: The Missing Value Imputer
**Tier I: Novice (Day 3)**

In real-world datasets, we often have "None" values or zeros that represent missing information. To keep our data balanced, we sometimes replace these missing values with the average of the rest of the data.

---

###  The Task
Write a Python function `impute_average(data)` that:
1. Calculates the average of all non-zero numbers in a list.
2. Replaces all `0` values in that list with the calculated average.
3. Returns the updated list.

### ⚙️ Constraints
* **Precision:** Round the average to two decimal places using `round(value, 2)`.
* **Data Integrity:** The list will always contain at least one non-zero number.
* **Logic:** You will need to iterate through the list to find non-zero values before performing the replacement.

### 💻 Example
**Input:**
```python
data = [10, 0, 20, 0, 30]
```

**Output:**
```python
# Average of 10, 20, 30 is 20.0
[10, 20.0, 20.0, 20.0, 30]
```

Note: You will need to iterate through the list twice—once to calculate the sum and count of non-zero numbers, and a second time to replace the zeros.
