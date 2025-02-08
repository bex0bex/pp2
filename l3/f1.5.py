def string_permutations(s):
    def permute(s, step=0):
        if step == len(s):
            print("".join(s))
        for i in range(step, len(s)):
            s_copy = list(s)
            s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
            permute(s_copy, step + 1)

    permute(list(s))
