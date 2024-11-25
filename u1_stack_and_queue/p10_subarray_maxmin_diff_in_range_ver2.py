from collections import deque


def count_subarray_maxmin_diff(arr, k):
    cnt = 0

    i, j = 0, 0
    min_dq = deque([0])
    max_dq = deque([0])

    while i < len(arr):
        while j < len(arr):
            # if [i j] doesn't satisfy, means [i i+1...j-1] satisfy, count out of j loop
            if arr[max_dq[0]] - arr[min_dq[0]] > k:
                break

            # Extend j -> j+1;
            # Note that we need j to be len(arr) if all the [i j] satisfy, because we will count as cnt += j-i
            j += 1
            if j == len(arr):
                break
            while min_dq and arr[min_dq[-1]] > arr[j]:
                min_dq.pop()
            min_dq.append(j)
            while max_dq and arr[max_dq[-1]] < arr[j]:
                max_dq.pop()
            max_dq.append(j)

        # Count [i, i i+1 ... j-1]
        cnt += j - i

        # Move i -> i+1
        if arr[min_dq[0]] == arr[i]:
            min_dq.popleft()
        if arr[max_dq[0]] == arr[i]:
            max_dq.popleft()
        i += 1

    return cnt


if __name__ == "__main__":
    print(count_subarray_maxmin_diff([1, 2, 1, 2], 3))
    print(count_subarray_maxmin_diff([1, 3, 1, 3], 1))
