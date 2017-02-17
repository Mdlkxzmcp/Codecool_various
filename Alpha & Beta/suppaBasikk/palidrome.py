def is_palindrome(s):
    """
    Input: s, a string
    Returns True if s is a palindrome, False otherwise
    """

    def to_chars(s):
        s = s.lower()
        ans = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + char
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))
