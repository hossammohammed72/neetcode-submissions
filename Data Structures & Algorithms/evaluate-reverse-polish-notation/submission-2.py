class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+','-','*','/']
        for i in range(len(tokens)):
            if tokens[i] in operands:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if tokens[i] =='+':
                    result = operand1+operand2
                elif tokens[i] == '-':
                    result = operand2-operand1
                elif tokens[i] == '*':
                    result = operand1*operand2
                elif tokens[i] == '/':
                    result = operand2/operand1
                stack.append(int(result))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
                


                
        