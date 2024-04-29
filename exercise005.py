#Valid Parentheses
#using stack

class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        for i in s:
            if i == "(" or i =="[" or i == "{":
                pilha.append(i)
            elif i == ")" and len(pilha) != 0 and pilha[-1] == "(":
                pilha.pop()
            elif i == "}" and len(pilha) != 0 and pilha[-1] == "{":
                pilha.pop()
            elif i == "]" and len(pilha) != 0 and pilha[-1] == "[":
                pilha.pop()
            else:
                return False
        if len(pilha) == 0:       
            return True
        else:
            False

        