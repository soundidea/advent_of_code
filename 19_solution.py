from itertools import chain

def parse_rule(rule_text):
  i, rule = rule_text.split(': ')
  return (i, [branch.split() for branch in rule.split(' | ')])

def consumer(rules, message, i):
  for branch in rules[i]:
    if branch[0].startswith('"'):
      if message.startswith(branch[0][1]):
        yield message[1:]
    else:
      remainders = [message]
      for child in branch:
        remainders = [r for rem in remainders for r in consumer(rules, rem, child)]
      for remainder in remainders:
        yield remainder

rules, messages = open('19_input.txt').read().split('\n\n')
rules = dict(map(parse_rule, rules.splitlines()))
messages = messages.splitlines()

print 'part 1:', sum('' in consumer(rules, msg, "0") for msg in messages)
rules.update({'8': [['42'],['42','8']], '11': [['42','31'],['42','11','31']]})
print 'part 2:', sum('' in consumer(rules, msg, "0") for msg in messages)
