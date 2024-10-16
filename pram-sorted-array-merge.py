import concurrent.futures
import bisect
 
def find_position_A(A, B, i):
    rankB = bisect.bisect_right(B, A[i])
    return i + rankB
 
def find_position_B(A, B, j):
    rankA = bisect.bisect_right(A, B[j])
    return j + rankA
 
def merge_sorted_arrays(A, B):
    n = len(A)
    m = len(B)
    C = [0] * (n + m)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures_A = [executor.submit(find_position_A, A, B, i) for i in range(n)]
        futures_B = [executor.submit(find_position_B, A, B, j) for j in range(m)]
        for i, future in enumerate(futures_A):
            pos = future.result()
            C[pos] = A[i]  
        for j, future in enumerate(futures_B):
            pos = future.result()
            C[pos] = B[j]   
    return C
 
if __name__ == "__main__":
    A = [1, 3, 5]
    B = [2, 4, 6]
    merged_array = merge_sorted_arrays(A, B)
    print("Merged Array:", merged_array)