import unittest
from random import randint
from recursive_sorts import insertion_sort, merge_sort, quicksort, hybrid_sort
from time import perf_counter_ns

class TestRecursiveSorts(unittest.TestCase):
    def test_merge_sort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        merge_sort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_quicksort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        quicksort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_insertion_sort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        insertion_sort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_large_random_array_merge_sort(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        merge_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_large_random_array_quicksort(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        quicksort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_large_random_array_insertion_sort(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        insertion_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_merge_sort_strings(self):
        lst = ["banana", "apple", "orange", "kiwi"]
        merge_sort(lst)
        self.assertEqual(lst, ["apple", "banana", "kiwi", "orange"])

    def test_quicksort_strings(self):
        lst = ["banana", "apple", "orange", "kiwi"]
        quicksort(lst)
        self.assertEqual(lst, ["apple", "banana", "kiwi", "orange"])

    def test_insertion_sort_strings(self):
        lst = ["banana", "apple", "orange", "kiwi"]
        insertion_sort(lst)
        self.assertEqual(lst, ["apple", "banana", "kiwi", "orange"])

    def test_hybrid_sort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        hybrid_sort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_hybrid_sort_large_random_array(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        hybrid_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_merge_sort_vs_quicksort_performance(self):
        lst1 = [randint(0, 10000) for _ in range(10000)]
        lst2 = lst1.copy()
        start_time = perf_counter_ns()
        merge_sort(lst1)
        merge_time = perf_counter_ns() - start_time
        start_time = perf_counter_ns()
        quicksort(lst2)
        quicksort_time = perf_counter_ns() - start_time
        # Both should produce the same sorted result
        self.assertEqual(lst1, lst2)
        # Both times should be reasonable (less than 10 seconds each)
        self.assertLess(merge_time, 10_000_000_000)
        self.assertLess(quicksort_time, 10_000_000_000)
        # quicksort should generally be faster than merge sort for large random arrays
        self.assertLess(quicksort_time, merge_time)

if __name__ == '__main__':
    unittest.main()