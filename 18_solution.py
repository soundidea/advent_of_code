import ast, string

inputs = open('18_input.txt').read()

def fixup(node, part):
  if isinstance(node, ast.BinOp):
    if isinstance(node.op, ast.Sub):
      node.op = ast.Mult()
    elif isinstance(node.op, ast.Mult):
      node.op = ast.Add()
    elif part==2 and isinstance(node.op, ast.Add):
      node.op = ast.Mult()

translations = {
  1: ('*', '-'),
  2: ('*+', '+*')
}

for part in (1,2):
  module = ast.parse(inputs.translate(string.maketrans(*translations[part])))
  for node in ast.walk(module):
    fixup(node, part)
  print 'part %d: %d' % (part, reduce(lambda a, expr: a + eval(compile(ast.Expression(expr.value), 'N/A', 'eval')), module.body, 0))

