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

Solution = Solution()
print(Solution.isValid("([])")) 