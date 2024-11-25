"""

Given String S and W. Return the 1st position (or all positions) t in S where S[t..] matches with W

KMP:
Ref: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

1. Construct a partial match table T based on the pattern string W,
so that for each position i in W, T[i] is the largest position that not equal to i and W[..T[i]-1] matches with W[..i-1].
(which in practice means, if we try to match a string with w, when it doesn't match at W[i], then it should continue checking W[T[i]]).
To construct this table, basically it's like compare 2 W (W, W'), keep the prefix matched and current positions mismatched,
reusing the known results before to keep moving W' to achieve that state.

2. With T known, move 2 pointers in S and W and compare, if mismatch at S[p], W[q],
then move W so that S[p] corresponds to W[T[q]] then keep comparing at these 2 positions.
"""


def gen_partial_match(w: str):
    """
    construct a partial match table t for given string w
    :param w:
    :return:
    """
    t = [0] * (len(w) + 1)
    t[0] = -1
    q = 0
    for p in range(1, len(w)):
        if w[p] == w[q]:
            t[p] = t[q]
        else:
            t[p] = q
            # Move q to achieve the state that prefix match w[..p] and w[..q]
            while q >= 0 and w[p] != w[q]:
                q = t[q]
        # Now w[..p] and w[..q] match, move both cursor the next
        q += 1
    # Only needed when we want to find all matched w in s
    t[len(w)] = q
    return t


def kmp_match(s: str, w: str):
    """
    find w in s, return the matched starting positions in s
    :param s:
    :param w: pattern str
    :return:
    """
    t = gen_partial_match(w)
    p = q = 0
    res = []
    while p < len(s) and p + len(w) - q <= len(s):
        if s[p] == w[q]:
            p += 1
            q += 1
            if q == len(w):
                # if only 1st matched position is needed, then return p-len(w) directly
                res.append(p-len(w))
                q = t[q]
        else:
            q = t[q]
            if q == -1:
                p += 1
                q = 0
    return res


if __name__ == "__main__":
    s = "acdbcdcdabcdcdcdaa"
    w = "cdcda"
    print(kmp_match(s, w))
