class Solution:
    def isValid(self, s):
        stack = []
        matching_pairs = {")" : "(", "}" : "{", "]" : "[", }

        for char in s:
            if char in matching_pairs:
                if not stack or stack[-1] == matching_pairs[char]:
                    stack.append(char)
                else:
                    return False
            elif char not in matching_pairs:
                if not stack:
                    return False
                stack.pop()
        
        return not stack