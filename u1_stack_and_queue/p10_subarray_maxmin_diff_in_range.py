from collections import deque


def count_subarray_maxmin_diff(arr, k):
    """
    Sliding window + monotonous deque to get min/max in window
    [i, j] fix i increase j, if max(i, j)-min(i, j) > k,
    then no need to check [i, j+1 j+2 ...], the diff will > k;
    and no need to check any partial array of [i, j-1], the diff will <= k;
    So we can just count the i-started array: +(j-i), then i += 1 for next window.
    """
    min_dq = deque([0])
    max_dq = deque([0])
    cnt = 0

    # sliding window [j, i]
    j, i = 0, 0
    while i < len(arr):
        if max_dq and min_dq and arr[max_dq[0]] - arr[min_dq[0]] > k:
            # means pairs between max_dq[0], min_dq[0] (e.g. p, q) exclusively all satisfy <= k.
            # We only count [j, j...q-1] which are q-j pairs, in this round, then we move j (slide window) until j=p+1, for next i round.
            p, q = min(max_dq[0], min_dq[0]), max(max_dq[0], min_dq[0])
            cnt += q - j

            # Now sliding window [j, i] -> [p+1, i]. diff should be smaller than k.
            while j <= p:
                if arr[j] == arr[min_dq[0]]:
                    min_dq.popleft()
                if arr[j] == arr[max_dq[0]]:
                    max_dq.popleft()
                j += 1
        else:
            i += 1
            if i == len(arr):
                break
            while min_dq and arr[min_dq[-1]] > arr[i]:
                min_dq.pop()
            min_dq.append(i)

            while max_dq and arr[max_dq[-1]] < arr[i]:
                max_dq.pop()
            max_dq.append(i)

    # Now [j, j j+1 ... len(arr)-1] all satisfy the condition. C(len(arr)-j, 2) + one ele array
    cnt += int((len(arr) - j) * (len(arr) - j - 1) / 2) + len(arr) - j

    return cnt


if __name__ == "__main__":
    print(count_subarray_maxmin_diff([1, 2, 1, 2], 3))
    print(count_subarray_maxmin_diff([1, 3, 1, 3], 1))
