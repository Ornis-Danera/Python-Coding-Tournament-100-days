# Evaluation: Challenge #1

You have completed the first step of the journey. Let’s look at the results.

### 🏆 Scorecard
| Category | Result | Status |
| :--- | :--- | :--- |
| **Accuracy** | Pass | The function produces the correct output. |
| **Logic** | Functional | Demonstrates a "Nested Loop" approach. |
| **Efficiency** | **6/10** | ⚠️ Critical Concern |

---

### 🔍 The Analysis

Your current solution has a **time complexity of $O(n^2)$**. 

Because you have a `while` loop nested inside a `for` loop, if your list had 1,000,000 items, your computer would have to perform up to 1,000,000,000,000 operations. In Data Science, we aim for **$O(n)$**—a single pass through the data.



---

### 💡 Grandmaster's "Pythonic" Tip

> "You can check if a key exists in a dictionary and update it in one pass. This avoids re-scanning the entire list for every new item found. Think about how to use the dictionary itself to remember what you've already seen. Check solution for details"
