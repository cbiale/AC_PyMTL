from pymtl3 import *

def incrementar_8bit( x ):
  return b8(x) + b8(1)

def test_incrementar_8bit_simple():
  assert incrementar_8bit( b8(2) ) == b8(3)

def test_incrementar_8bit_overflow():
  assert incrementar_8bit( b8(0xff) ) == b8(0)
