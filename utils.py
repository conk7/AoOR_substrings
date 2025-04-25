import time
from pathlib import Path
from typing import Callable, List


def measure_algorithm(algorithm: Callable, benchmarks_path: Path, n: int = 100):
    text_files = [
        "bad_t_1.txt",
        "bad_t_2.txt",
        "bad_t_3.txt",
        "bad_t_4.txt",
        "good_t_1.txt",
        "good_t_2.txt",
        "good_t_3.txt",
        "good_t_4.txt",
    ]
    pattern_files = [
        "bad_w_1.txt",
        "bad_w_2.txt",
        "bad_w_3.txt",
        "bad_w_4.txt",
        "good_w_1.txt",
        "good_w_2.txt",
        "good_w_3.txt",
        "good_w_4.txt",
    ]

    texts = []
    patterns = []

    for filename in text_files:
        texts.append((benchmarks_path / filename).read_text())

    for filename in pattern_files:
        patterns.append((benchmarks_path / filename).read_text())

    avg_times = []
    avg_comparisons = []
    for text, pattern in zip(texts, patterns):
        total_time = 0
        comparisons = 0
        for _ in range(n):
            start = time.time()
            _, comparisons = algorithm(text, pattern)
            end = time.time()

            total_time += end - start

        avg_time = total_time / n
        avg_time *= 1000

        avg_times.append(avg_time)
        avg_comparisons.append(comparisons)

    return text_files, avg_times, avg_comparisons


def print_results(
    algorithm: str,
    filenames: List[str],
    avg_times: List[float],
    avg_comparisons: List[int],
):
    print(f"\n\n{algorithm}")
    print(f"{'Benchmark':<20}{'Average time(ms)':<20}{'Average num of comparisons':<15}")
    print("-" * 60)
    for f, t, c in zip(filenames, avg_times, avg_comparisons):
        print(f"{f:<20}{t:<20.4f}{c}")
