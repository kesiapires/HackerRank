#Converting Roman to Int

class Solution:
    def romanToInt(self, s: str) -> int:
        valor = 0
        ultimo = 0
        strInverted = s[::-1]
        for i in strInverted:
            valorAtual = self.convert(i)
            if valorAtual < ultimo:
                valor -= valorAtual
            if valorAtual >= ultimo:
                valor += valorAtual
            ultimo = valorAtual
        return valor
    def convert(self, str):
        if str == "I":
            return 1
        if str == "V":
            return 5
        if str == "X":
            return 10
        if str == "L":
            return 50
        if str == "C":
            return 100
        if str == "D":
            return 500
        if str == "M":
            return 1000
