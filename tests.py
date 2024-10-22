from fraction import Fraction
import unittest
class TestInit(unittest.TestCase):
  #several of these will need to check to see if an exception is raised
  def test_divZero(self):
    with self.assertRaises(ZeroDivisionError,msg="Denominator of zero fails to raise DivByZero"):
      a = Fraction(1,0)
  def test_default(self):
    b= Fraction()
    self.assertEqual(0,b.numerator,"Default numerator is not zero")
    self.assertEqual(1,b.denominator,"Default denominator is not one")

    #will the 0 argument version of the constructor produce the correct fraction?
  def test_oneArg(self):
    b= Fraction(1)
    self.assertEqual(1,b.numerator,"Numerator is not affected by the 1 argument constructor")
     #will the 1 argument version of the constructor produce the correct fraction?
  def test_twoArg(self):
    b= Fraction(1,2)
    self.assertEqual(2,b.denominator,"Denominator is not affected by the 2 argument constructor")
     #will the 2 argument version of the constructor produce the correct fraction?
  def test_invalidArg(self):
    with self.assertRaises(TypeError,msg="Invalid argument type"):
      b= Fraction("lol",2)
      a= Fraction(1,"Lmao_even")
     #will constructor through an exception if non-numeric data is passed?
  def test_reduced(self):
     b= Fraction(2,2)
     self.assertEqual(1,b.numerator,"Numerator is not reduced for shared factors")
     self.assertEqual(1,b.denominator,"Denominator is not reduced for shared factors")
     #if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2

class TestStr(unittest.TestCase):
  def test_displayFraction(self):
    a = Fraction(1,2)
    self.assertEqual(" 1/2 ",a.__str__(),"fraction not displayed correctly")
  def test_displayInt(self):
    b = Fraction(1,1)
    self.assertEqual(" 1 ",b.__str__(),"fraction must omit a 1 denominator")
     #if the denominator is 1, does display omit the /1?
  def test_displayNeg(self):
    c = Fraction(1, -2)
    self.assertEqual(" -1/2 ",c.__str__(),"fraction must swap the negation to the numerator when displaying")
    #if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
    
class TestFloat(unittest.TestCase):
  def test_defDen(self):
    c = Fraction(2)
    self.assertTrue(isinstance(c.__float__(),float),"float must return a float")
  def test_nonDefDen(self):
    c = Fraction(3,4)
    self.assertEqual(.75,c.__float__(),"float request should return the numerator divided by the denominator")
    #should return a float of numerator/denominator
  def test_negFloat(self):
    c = Fraction(-1,2)
    self.assertLess(c.__float__(),0,"there should be a negative float if the fraction is negative")
    #negative fraction negative float

class TestAdd(unittest.TestCase):
  def setUp(self):
    self.a = Fraction(1,2)
  def test_type(self):
    self.setUp()
    with self.assertRaises(TypeError,msg="add method should raise a type error with incorrect argument type"):
      self.a.__add__(3.2)
      self.a.__add__("a")
    #should raise type error when passed a non-fraction or a non-int
  def test_return(self):
    self.setUp()
    c=self.a.__add__(self.a)
    self.assertTrue(isinstance(c,Fraction),"add method should return a Fraction")
    #should return a fraction
  def test_fact(self):
    self.setUp()
    c=self.a.__add__(self.a)
    self.assertEqual(1,c.numerator,"Numerator is not factored")
    self.assertEqual(1,c.denominator,"Denominator is not factored")
  #returned fraction should be in the lowest common form
  def test_int(self):
    self.setUp()
    c=self.a.__add__(2)
    self.assertEqual(5,c.numerator,"check that factor adds ints correctly")
  #returned fraction should add ints akin to whole numbers in commonly understood math

class TestSub(unittest.TestCase):
  def setUp(self):
    self.a = Fraction(1,2)
  def test_type(self):
    self.setUp()
    with self.assertRaises(TypeError,msg="sub method should raise a type error with incorrect argument type"):
      self.a.__sub__(3.2)
      self.a.__sub__("a")
    #should raise type error when passed a non-fraction or a non-int
  def test_return(self):
    self.setUp()
    c=self.a.__sub__(self.a)
    self.assertTrue(isinstance(c,Fraction),"sub method should return a Fraction")
    #should return a fraction
  def test_fact(self):
    self.setUp()
    c=self.a.__sub__(self.a)
    self.assertEqual(0,c.numerator,"Numerator is not factored")
    self.assertEqual(1,c.denominator,"Denominator is not factored")
  #returned fraction should be in the lowest common form
  def test_int(self):
    self.setUp()
    c=self.a.__sub__(2)
    self.assertEqual(-3,c.numerator,"check that factor subtracts ints correctly")
  #returned fraction should subtract ints akin to whole numbers in commonly understood math

class TestMul(unittest.TestCase):
  def setUp(self):
    self.a = Fraction(1, 2)
    self.b = Fraction(2, 3)

  def test_type(self):
    self.setUp()
    with self.assertRaises(TypeError, msg="mul method should raise a type error with incorrect argument type"):
      self.a.__mul__(3.2)
      self.a.__mul__("a")
    # should raise type error when passed a non-fraction or a non-int

  def test_return(self):
    self.setUp()
    c = self.a.__mul__(self.a)
    self.assertTrue(isinstance(c, Fraction), "mul method should return a Fraction")
    # should return a fraction

  def test_fact(self):
    self.setUp()
    c = self.a.__mul__(self.b)
    self.assertEqual(1, c.numerator, "Numerator is not factored")
    self.assertEqual(3, c.denominator, "Denominator is not factored")

  # returned fraction should be in the lowest common form
  def test_int(self):
    self.setUp()
    c = self.a.__mul__(2)
    self.assertEqual(1, c.numerator, "check that factor multiplies by ints correctly (numerator")
    self.assertEqual(1, c.denominator, "check that factor multiplies by ints correctly (denominator)")
  # returned fraction should subtract ints akin to whole numbers in commonly understood math

  def test_neg(self):
    self.setUp()
    c = self.a.__mul__(-1)
    self.assertEqual(-1, c.numerator, "Numerator is not negated by negative multiplier")
    #negative guest negative result

class TestDiv(unittest.TestCase):
  def setUp(self):
    self.a = Fraction(1, 2)
    self.b = Fraction(2, 3)

  def test_type(self):
    self.setUp()
    with self.assertRaises(TypeError, msg="truediv method should raise a type error with incorrect argument type"):
      self.a.__truediv__(3.2)
      self.a.__truediv__("a")
    # should raise type error when passed a non-fraction or a non-int

  def test_return(self):
    self.setUp()
    c = self.a.__truediv__(self.a)
    self.assertTrue(isinstance(c, Fraction), "truediv method should return a Fraction")
    # should return a fraction

  def test_fact(self):
    self.setUp()
    c = self.a.__truediv__(self.b)
    self.assertEqual(3, c.numerator, "Numerator is not factored")
    self.assertEqual(4, c.denominator, "Denominator is not factored")

  # returned fraction should be in the lowest common form
  def test_int(self):
    self.setUp()
    c = self.a.__truediv__(2)
    self.assertEqual(1, c.numerator, "check that factor divides by ints correctly (numerator")
    self.assertEqual(4, c.denominator, "check that factor divides by ints correctly (denominator)")
  # returned fraction should subtract ints akin to whole numbers in commonly understood math

  def test_neg(self):
    self.setUp()
    c = self.a.__truediv__(-1)
    self.assertEqual(-1, c.numerator, "Numerator is not negated by negative divider")
    #negative guest negative result