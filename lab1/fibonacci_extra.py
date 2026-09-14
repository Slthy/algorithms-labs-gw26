
def fibonacci(n):               # using golden ratio
    sqrt_5 = 5 ** 0.5           # ept to the power of 1/2
    phi = (1 + sqrt_5) / 2      # Golden ratio (~1.618)
    psi = (1 - sqrt_5) / 2      # Conjugate (~-0.618)
    
    return round((phi**n - psi**n) / sqrt_5) # round to the nearest integer because int
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
