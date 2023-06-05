import unittest
import SE_Sample_File as se


class TestAdd(unittest.TestCase):
    def test_list_int(self):
        result = se.add(1, 2)
        self.assertEqual(result, 3)


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        data = [90, 110, 2, 10]
        results = [True, True, False, False]
        obj = se.temp()
        for i in range(len(data)):
            new_res = obj.hello_world(data[i])
            self.assertEqual(new_res, results[i])


class TestMinus(unittest.TestCase):
    def test_minus(self):
        result = se.minus(12, 5)
        self.assertEqual(result, 7)
    
    def test_minus_minus(self):
        result = se.minus(3, 7)
        self.assertEqual(result, -4)


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        result = se.multiply(12, 5)
        self.assertEqual(result, 60)
    
    def test_multiply_minus(self):
        result = se.multiply(-3, 7)
        self.assertEqual(result, -21)


if __name__ == '__main__':
    unittest.main()
