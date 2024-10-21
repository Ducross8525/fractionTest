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
  def test_displayfraction(self):
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
  pass
  #should return a float of numerator/denomenator
  #negative fraction negative float

class TestAdd(unittest.TestCase):
  pass
  #should raise type error when passed a nonfraction
  #should return a fraction
  #returned faction should be in lowest common form

class TestSub(unittest.TestCase):
