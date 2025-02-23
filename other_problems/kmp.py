"""

Given String S and W. Return the 1st position (or all positions) t in S where S[t..] matches with W

KMP:
Ref: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

(https://blog.csdn.net/qq_43869106/article/details/128753527)

1. longest prefix suffix table 'next[]' :
Construct a next[] table for pattern string W. next[i] indicates the longest identical substring as both prefix and suffix for string W[0:i+1].
So if W[i+1] doesn't match in a comparison, we should move cursor to W[next[i]].
When to derive next[] table, maintain p, q pointing to end of potential prefix, suffix in a loop:
If W[p]!=W[q], keep moving cursor p backwards p=next[p-1] (i.e. scanning prefixes ended with W[p-1])
until W[p]==W[q] or p out of range, then next[q]=p+1 or next[q]=0, respectively.


2. With next[] known, move 2 pointers in S and W and compare, if mismatch at S[p], W[q],
then move W so that S[p] corresponds to W[next[q-1]] then keep comparing at these 2 positions.
"""


def gen_longest_prefix_suffix_next_table(w: str):
    """
    construct a longest_prefix_suffix_next table next for given string w
    :param w:
    :return:
    """
    nxt = [0] * len(w)
    p = 0  # end of prefix
    for q in range(1, len(w)):  # end of suffix
        while w[p] != w[q] and p > 0:
            p = nxt[p-1]
        if w[q] == w[p]:
            nxt[q] = p + 1
            p += 1
        else:
            nxt[q] = 0
    return nxt


def kmp_match(s: str, w: str):
    """
    find w in s, return the matched starting positions in s
    :param s:
    :param w: pattern str
    :return:
    """
    nxt = gen_longest_prefix_suffix_next_table(w)
    print(nxt)
    p = q = 0
    res = []
    while p < len(s) and p + len(w) - q <= len(s):
        if s[p] == w[q]:
            q += 1
            p += 1
            if q == len(w):
                # if only 1st matched position is needed, return p-len(w) directly; otherwise, append in a list
                res.append(p-len(w))
                q = nxt[q-1]
        else:
            if q == 0:
                # move to next p
                p += 1
            else:
                q = nxt[q-1]
    return res


if __name__ == "__main__":
    s = "acdbcdcdabcdcdcdaa"
    w = "cdcda"
    print(kmp_match(s, w))
