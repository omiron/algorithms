def solution(A):
    """
    Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become
    a2blc5a3. If the "compressed" string would not become smaller than the
    original string, your method should return the original string.
    >>> solution("aaab")
    'a3b'
    >>> solution('aabbac')
    'aabbac'
    >>> solution('abcde')
    'abcde'
    >>> solution('abcccccde')
    'abc5de'
    """
#   intervals will be like [(start_position, number_char_repeated), ....]
    intervals = []
    start = end = -1
    prev = ''
    deserve = False

#   calculate intervals
    for idx, ch in enumerate(A):
        if ch == prev:
            if start != -1:
                end = idx
            else:
                start = idx - 1
                end = idx
        else:
            prev = ch
            if start != -1:
                if (start + 1 < end):
                    deserve = True
                intervals.append((start, end))
            start = end = -1

    if deserve:
#       the compressed string is less than the original string
        the_string = list(A)
        for interval in intervals:
            number_chars = str(interval[1] - interval[0] + 1)
            the_string.insert(interval[0] + 1, number_chars)
            start_to_del = interval[0] + len(number_chars) + 1
            how_many_to_del = interval[1] - interval[0]
            del the_string[start_to_del: start_to_del + how_many_to_del]
        return ''.join(the_string)
    else:
        return A
