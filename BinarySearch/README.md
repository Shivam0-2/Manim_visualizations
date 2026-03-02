# Binary Search Visualization (Manim)

This project visualizes the **Binary Search algorithm** step by step using the Manim animation engine.

The animation demonstrates how the search space is reduced iteratively using the `low`, `mid`, and `high` pointers.

---

## Demo Video

Watch the full animation on YouTube:  
https://youtu.be/9Kt17G7Ie1s

---

## What This Visualization Shows

- Movement of `Low`, `Mid`, and `High` pointers
- Step-by-step comparisons
- Range shrinking logic
- Found / Not Found conditions
- Visual intuition behind **O(log n)** time complexity

---

## Algorithm Overview

Binary Search works on **sorted arrays**.

At each step:
1. Compute `mid = (low + high) // 2`
2. Compare target with `arr[mid]`
3. Narrow the search space:
   - If target > mid → move `low`
   - If target < mid → move `high`
   - If equal → element found

### Time Complexity
- Best Case: **O(1)**
- Worst Case: **O(log n)**

---

## How to Run Locally

Install Manim:
pip install manim

Render the animation:
manim -pql binary_search.py BinarySearch
