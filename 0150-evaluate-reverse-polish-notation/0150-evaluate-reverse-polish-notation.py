class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_valid_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        stk = []
        for t in tokens:
            if is_valid_number(t):
                stk.append(t)
                continue
            y = int(stk.pop()) 
            x = int(stk.pop())
            ans = 0
            if t == "+":
                ans = x + y
            elif t == "-":
                ans = x - y
            elif t == "*":
                ans = x * y
            elif t == "/":
                ans = int(x / y)
            stk.append(str(ans))
        return int(stk[0])
