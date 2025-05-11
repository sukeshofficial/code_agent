

## 📌 Task: I want a program to find numbers using binary search in java

### 🧠 Explanation
This Java program implements a binary search algorithm to find a specific number in a sorted array. The `binarySearch` method takes an array and a target number as input. It initializes two pointers, `left` and `right`, to the start and end of the array. It then enters a loop where it calculates the middle index and compares the middle element with the target. If they match, it returns the index. If the target is greater than the middle element, it narrows the search to the right half; if smaller, it narrows to the left half. If the target is not found after the loop, it returns -1. The `main` method demonstrates how to use this function and prints the result.

### 📄 Code File: `binary_search.java`
