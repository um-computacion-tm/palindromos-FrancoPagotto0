import unittest
from palindrome import is_palindrome



class testpalindrome(unittest.TestCase):
    def test_A (self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_B(self):
        resultado = is_palindrome("aca")
        self.assertEqual(resultado, True)   
    
    def test_C(self):
        resultado = is_palindrome("ABCBA")
        self.assertEqual(resultado, True)

    def test_D(self):
        resultado = is_palindrome("NEUQ UEN")
        self.assertEqual(resultado, True)  

    def test_E(self):
        resultado = is_palindrome("ab")
        self.assertEqual(resultado,False)

    def test_F (self):
        resultado = is_palindrome("hola")
        self.assertEqual(resultado,False) 
   
    def test_G (self):
        resultado = is_palindrome("Franco")
        self.assertEqual(resultado,False) 
   



unittest.main()