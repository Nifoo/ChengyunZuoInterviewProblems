def get_survival_number(n, m):
    """
    f(n, m) = (f(n-1, m) + m -1) %n + 1; f(1, m) = 1
    f(n, m) denotes the index (starting from 1) that survives at last in a n-circle m-out run.
    Note that the n-1 circle will be starting from m+1 from n ring perspective, so there's m offset; also because the index starts from 1 not 0, there's (.. -1) %n + 1 in the calculation.
    :param n: size of the ring (1, 2, ... n)
    :param m: "1, 2... m, 1, 2, ...m ..." who claims m gets out.
    :return: the survival number at last
    """

    # Either use recursion or iteration is fine
    f = 1
    for i in range(2, n):
        f = (f + m - 1) % n + 1
    return f


if __name__ == "__main__":
    print(get_survival_number(41, 3))
