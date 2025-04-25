from pathlib import Path
from algos import naive_search, boyer_moore_horspool, kmp_search
from utils import measure_algorithm, print_results

BENCHMARKS_PATH = Path().resolve() / 'benchmarks'

N = 100

if __name__ == "__main__":
    filenames, avg_times, avg_comparisons = measure_algorithm(
        naive_search, BENCHMARKS_PATH, N
    )
    print_results("Naive algorithm", filenames, avg_times, avg_comparisons)

    filenames, avg_times, avg_comparisons = measure_algorithm(
        boyer_moore_horspool, BENCHMARKS_PATH, N
    )
    print_results(
        "Boyer-Moore-Horspool algorithm", filenames, avg_times, avg_comparisons
    )

    filenames, avg_times, avg_comparisons = measure_algorithm(
        kmp_search, BENCHMARKS_PATH, N
    )
    print_results("Knuth-Morris-Pratt algorithm", filenames, avg_times, avg_comparisons)
