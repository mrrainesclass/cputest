import random
import time
import math
import sys
import tracemalloc

def stress_test():
    """Stress test memory and CPU by generating and processing large data."""
    print("Starting stress test...")

    start_time = time.time()
    tracemalloc.start()

    data = [random.randint(1, 100) for _ in range(10_000_000)]

    total = sum(x * x for x in data)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    end_time = time.time()

    print(f"Total sum of squares: {total}")
    print(f"Memory used: {current / 1024**2:.2f} MB; Peak: {peak / 1024**2:.2f} MB")
    print(f"Execution time: {end_time - start_time:.2f} seconds\n")


def floating_point_test():
    """Test floating-point precision and performance with heavy computation."""
    print("Starting floating-point test...")

    start_time = time.time()
    errors = 0

    results = []
    for _ in range(1_000_000):
        a = random.uniform(0.000001, 5.0)
        b = random.uniform(0.000001, 5.0)
        c = a * b / (a + b + 1e-10)
        if math.isnan(c) or math.isinf(c):
            errors += 1
        results.append(c)

    end_time = time.time()

    print(f"Generated {len(results)} floating-point computations.")
    print(f"Invalid results: {errors}")
    print(f"Execution time: {end_time - start_time:.2f} seconds\n")


if __name__ == "__main__":
    stress_test()
    floating_point_test()