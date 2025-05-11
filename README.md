

## 📌 Task: I want a binary search program in java

### 🧠 Explanation
This Java program implements a binary search algorithm. It defines a `binarySearch` method that takes a sorted array and a target value as inputs. The method initializes two pointers, `left` and `right`, to represent the current search bounds. It then enters a loop that continues until the `left` pointer exceeds the `right` pointer. Within the loop, it calculates the middle index and checks if the middle element is the target. If it is, the index is returned. If the target is greater than the middle element, the search continues in the right half of the array; otherwise, it continues in the left half. If the target is not found, the method returns -1. The `main` method demonstrates how to use the `binarySearch` method and prints the result.

### 📄 Code File: `binary_search.java`
