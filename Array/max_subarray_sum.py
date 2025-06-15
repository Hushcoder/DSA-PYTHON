## Mine Solution was O(N^2) TC, so failed for Large N.

## Sliding window + HashMap/FreqMap Technique
def max_arr_sum(A, N, k):
    from collections import defaultdict

    left = 0
    freq = defaultdict(int)
    max_sum = 0
    curr_sum = 0

    for right in range(N):
        freq[A[right]] += 1
        curr_sum += A[right]

        while len(freq) > k:
            freq[A[left]] -= 1
            curr_sum -= A[left]

            if freq[A[left]] == 0:
                del freq[A[left]]
            
            left += 1
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    
    # custom input
    result = max_arr_sum([1,2,2,3,2,3,5,1,2,1,1], 11, 2)
    print(result)