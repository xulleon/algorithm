# https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''
        The logic is simple. other than the last char, any
        other char of the index need to find any char which
        is less than current char lexicographically. The
        last measure is to find any char available at the
        last char of the string.
        '''
        if len(palindrome) == 1:
            return ''
        n = len(palindrome)
        palindrome = list(palindrome)
        modified = []
        index = 0
        end = ord('z')
        while index < n:
            modified = palindrome[:]
            base = ord('a')

            while base < end:
                modified = palindrome[:]
                if index == n - 1:
                    modified[index] = chr(base)
                else:
                    if base >= ord(modified[index]):
                        # if any char below current char
                        # can not be found, then move to
                        # next index
                        break

                    modified[index] = chr(base)
                if modified != modified[::-1]:
                    return ''.join(modified)
                base += 1
            index += 1
        return ''
            
