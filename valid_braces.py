import unittest

def validBraces(cadena):
    posible = True
    cadena = list(cadena)
    if len(cadena) % 2 == 1:
        return False

    while posible and len(cadena) > 1:
        for i in range(len(cadena) - 1):
            dif = (ord(cadena[i + 1]) - ord(cadena[i]))

            if ord(cadena[i + 1]) - ord(cadena[i]) == 1 or ord(cadena[i + 1]) - ord(cadena[i]) == 2:
                del cadena[i + 1]
                del cadena[i]
                break
            if cadena[i] == cadena[-2]:
                posible = False
    if len(cadena) == 0:
        return True
    else:
        return False
class Test(unittest.TestCase):
    def test(self):
        cadena1 = "([{}])"
        resultado = validBraces(cadena1)
        self.assertEquals(resultado, True)
    def test2(self):
        cadena2 = "[(])"
        resultado = validBraces(cadena2)
        self.assertEquals(resultado, False)

if __name__ == "__main__":
    unittest.main()