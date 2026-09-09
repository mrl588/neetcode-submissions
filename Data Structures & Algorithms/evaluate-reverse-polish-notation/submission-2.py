class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stack = []
        for token in tokens:
            if token in ops:
                oper2 = int(stack.pop())
                oper1 = int(stack.pop())
                res = 0 
                if token == "+":
                    res = oper1 + oper2
                if token == "-":
                    res = oper1 - oper2
                if token == "*":
                    res = oper1 * oper2
                if token == "/":
                    res = int(oper1 / oper2)   
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]