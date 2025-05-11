public class BinarySearch {
    // Method to perform binary search on a sorted array
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Calculate mid index

            // Check if target is present at mid
            if (arr[mid] == target) {
                return mid; // Target found
            }
            // If target is greater, ignore left half
            else if (arr[mid] < target) {
                left = mid + 1;
            }
            // If target is smaller, ignore right half
            else {
                right = mid - 1;
            }
        }
        return -1; // Target not found
    }

    public static void main(String[] args) {
        int[] sortedArray = {2, 3, 4, 10, 40}; // Example sorted array
        int target = 10; // Target value to search for

        int result = binarySearch(sortedArray, target); // Perform binary search

        if (result == -1) {
            System.out.println("Element not found in the array.");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }
}