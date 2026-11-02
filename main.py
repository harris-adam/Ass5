# main.py
# Compare merge sort, quicksort, hybrid sort, and Python's built-in sort
# on large random arrays of integers

from recursive_sorts import merge_sort, quicksort, hybrid_sort
from random import randint
from time import perf_counter_ns

def draw_sort_speed_charts(sort_times, list_lengths):
    import matplotlib.pyplot as plt

    ms_sort_times = []
    qs_sort_times = []
    hs_sort_times = []
    py_sort_times = []
    for sort_triplet in sort_times:
        ms_sort_times.append(sort_triplet[0] / 1_000_000_000)
        qs_sort_times.append(sort_triplet[1] / 1_000_000_000)
        hs_sort_times.append(sort_triplet[2] / 1_000_000_000)
        py_sort_times.append(sort_triplet[3] / 1_000_000_000)
    plt.plot(list_lengths, ms_sort_times, marker='o', label='Merge Sort')
    plt.plot(list_lengths, qs_sort_times, marker='o', label='Quick Sort')
    plt.plot(list_lengths, hs_sort_times, marker='o', label='Hybrid Sort')
    plt.plot(list_lengths, py_sort_times, marker='o', label='Python Sort')
    plt.title("Merge Sort vs Quick Sort vs Hybrid Sort vs Python Sort")
    plt.xlabel("Items")
    plt.ylabel("Seconds per Sort")
    plt.legend()
    plt.grid()
    plt.show()


def experiment(num_trials, list_size, min_value, max_value):
    ms_total_time = 0
    qs_total_time = 0
    hs_total_time = 0
    py_total_time = 0

    for _ in range(num_trials):
        lst1 = [randint(min_value, max_value) for _ in range(list_size)]
        lst2 = lst1.copy()
        lst3 = lst1.copy()
        lst4 = lst1.copy()

        start_time = perf_counter_ns()
        merge_sort(lst1)
        end_time = perf_counter_ns()
        ms_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        quicksort(lst2)
        end_time = perf_counter_ns()
        qs_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        hybrid_sort(lst3)
        end_time = perf_counter_ns()
        hs_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        lst4.sort()
        end_time = perf_counter_ns()
        py_total_time += (end_time - start_time)

    avg_ms_time = ms_total_time / num_trials
    avg_qs_time = qs_total_time / num_trials
    avg_hs_time = hs_total_time / num_trials
    avg_py_time = py_total_time / num_trials
    return (avg_ms_time, avg_qs_time, avg_hs_time, avg_py_time)

def main():
    print("Running sort time trials...")
    experiment_sizes = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    sort_times = []
    num_trials = 5
    min_value = 1
    max_value = 1000000
    for size in experiment_sizes:
        sort_pair = experiment(num_trials, size, min_value, max_value)
        sort_times.append(sort_pair)
    print("Sort Times (ns):")
    print("Items\tMerge Sort\tQuick Sort\tHybrid Sort\tPython Sort")
    for i in range(len(experiment_sizes)):
        print(f"{experiment_sizes[i]}\t{sort_times[i][0]:.2f}\t{sort_times[i][1]:.2f}\t{sort_times[i][2]:.2f}")
    draw_sort_speed_charts(sort_times, experiment_sizes)

if __name__ == '__main__':
    main()