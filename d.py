def bubble_sort(arr):
    n = len(arr)
    print(f"Initial Array: {arr}\n" + "-"*40)
    
    for i in range(n):
        swapped = False
        print(f"--- Pass {i + 1} Begins ---")
        
        for j in range(0, n - i - 1):
            left, right = arr[j], arr[j + 1]
            
            if left > right:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                action = "Swap"
            else:
                action = "Keep"
                
            print(f"  j={j} | Compare: {left} > {right} -> {action} | Array: {arr}")
            
        if not swapped:
            print(f"-> No swaps occurred in Pass {i + 1}. Array is sorted.")
            break
            
    return arr

def insertion_sort(arr):
    print(f"Initial Array: {arr}\n" + "-"*50)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comparisons = []
        shifted = []
        
        print(f"--- Step i={i} | Picking Key: {key} ---")
        
        # Check the condition for the first loop comparison or termination
        while j >= 0:
            comp_expr = f"{arr[j]} > {key}"
            if arr[j] > key:
                comparisons.append(f"{comp_expr} (True)")
                shifted.append(arr[j])
                arr[j + 1] = arr[j]
                j -= 1
            else:
                comparisons.append(f"{comp_expr} (False)")
                break
        else:
            if j < 0:
                comparisons.append(f"j reaches out of bounds (< 0)")

        # Insert the key into its correct slotted position
        arr[j + 1] = key
        
        print(f"  Comparisons: {', '.join(comparisons)}")
        print(f"  Shifted elements: {shifted if shifted else 'None'}")
        print(f"  Inserted {key} at index: {j + 1}")
        print(f"  Array afterward: {arr}\n")
        
    return arr

insertion_sort([7, 3, 5, 8, 2])


