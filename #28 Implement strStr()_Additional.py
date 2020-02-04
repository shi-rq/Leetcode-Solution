def strStr(self, haystack: str, needle: str) -> int:
    len_needle = len(needle)
    len_haystack = len(haystack)
    needle_hash = hash(needle)
    haystack_hash = []
    result = []
    for n in range(len_haystack - len_needle + 1):
        haystack_hash.append(hash(haystack[n: n + len_needle]))
    for n in range(len(haystack_hash)):
        if needle_hash == haystack_hash[n]: result.append(n)
    return result