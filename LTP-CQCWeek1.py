def is_palindrome(s):
    """ (str) -> bool

    Return true only if s i a palindrome
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    >>> is_palindrome('dented')
    False
    """
    return reverse(s) == s

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.
    
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''

    #for each character in s, add that char to the beginning to rev
    for ch in s:
        rev = ch + rev

    return rev

def is_palindrome_v2(s):
    """ (str) -> bool

    Return true only if s i a palindrome
    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    >>> is_palindrome_v2('dented')
    False
    """
    #the number of chars in s.
    n = len(s)
    #comapre the first half of s to the reverse of second part of s
    #omit the middle character
    return s[:n // 2] == reverse(s[n - n // 2:])
    

def is_palindrome_v3(s):
    """ (str) -> bool

    Return true only if s i a palindrome
    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    >>> is_palindrome_v3('dented')
    False
    """

    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1
    return j <= i
        
    
