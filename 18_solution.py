from string import maketrans
import re

class I(int):
  def __sub__(self, i): return I(int(self) * i)
  def __mul__(self, i): return I(int(self) + i)
  def __add__(self, i): return I(int(self) + i)

inputs = re.sub(r'(\d+)', r'I(\1)', open('18_input.txt').read()).splitlines()
print 'part 1:', sum(eval(expr.translate(maketrans('*', '-'))) for expr in inputs)
print 'part 2:', sum(eval(expr.translate(maketrans('*+', '-*'))) for expr in inputs)
