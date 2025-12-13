class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        control = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in control:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if control[top] != char:
                    return False
        return len(stack) == 0

''' Alternative Implementation
class Solution(object):
    def isValid(self, s):
        control = {'}':'{', ']':'[', ')':'('}
        stack = []

        for char in s:
            if char in control.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != control[char]:
                    return False
                stack.pop()
        return not stack
'''

Solution = Solution()
print(Solution.isValid("([])")) 