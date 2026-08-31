def fibonacci(n):
    for _ in range(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):   # we start from 2 because we already know the first two Fibonacci numbers
            a, b = b, a + b         # a becomes the previous Fibonacci number, b becomes the current Fibonacci number
        return b
def is_positive_integer(text):
    try:
        return int(text) > 0
    except:
        pass
    return False

if __name__ == "__main__":
    import time
    while True:
        text = input("Please enter a positive integer: ")
        if not is_positive_integer(text):
            continue
        start = time.perf_counter()
        result = fibonacci(int(text))
        end = time.perf_counter()
        print(f"fibonacci({int(text)}) = {result}, calculating this took {end - start:.4e} seconds.")
