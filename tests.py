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
  def test_type(self):
    c=Fraction()
    with self.assertRaises(TypeError,msg="add method should raise a type error with incorrect argument type"):
      c.__add__(0)
      c.__add__("a")
    #should raise type error when passed a non-fraction
  def test_return(self):
    c=Fraction()
    b=Fraction(1,2)
    a=c.__add__(b)
    self.assertTrue(isinstance(a,Fraction),"add method should return a Fraction")
    #should return a fraction
  def test_fact(self):
    c=Fraction(1,2)
    b=Fraction(1,2)
    a=c.__add__(b)
    self.assertEqual(1,a.numerator,"Numerator is not factored")
    self.assertEqual(1,a.denominator,"Denominator is not factored")
  #returned faction should be in the lowest common form

class TestSub(unittest.TestCase):
  pass
  #should raise type error when passed a non-fraction
  #should return a fraction
  #returned faction should be in the lowest common form

class TestMul(unittest.TestCase):
  pass
  #should raise type error when passed a non-fraction
  #should return a fraction
  #returned faction should be in the lowest common form
  #negative guest negative result

class TestDiv(unittest.TestCase):
  pass
  #should raise type error when passed a non-fraction
  #should return a fraction
  #returned faction should be in the lowest common form
  #negative guest negative result