import re


# dict of field name => (format RE, validation rule)
rules = {
  'byr': (re.compile(r'^\d{4}$'), lambda val: 1920 <= int(val) <= 2002),
  'iyr': (re.compile(r'^\d{4}$'), lambda val: 2010 <= int(val) <= 2020),
  'eyr': (re.compile(r'^\d{4}$'), lambda val: 2020 <= int(val) <= 2030),
  'hgt': (re.compile(r'^\d+(cm|in)$'), lambda val: 150 <= int(val[:-2]) <= 193 if val[-2:] == 'cm' else 59 <= int(val[:-2]) <= 76),
  'hcl': (re.compile(r'^#[0-9a-f]{6}$'), lambda val: True),
  'ecl': (re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$'), lambda val: True),
  'pid': (re.compile(r'^\d{9}$'), lambda val: True)
}
  

def valid_pt_2(p):
  return all(fmt.match(p[key]) and valid(p[key]) for key, (fmt, valid) in rules.items())


if __name__ == '__main__':
  with open('4_input.txt') as f:
    passports = [dict(re.findall(r'([a-z]{3}):(\S+)', passport)) for passport in f.read().split('\n\n')]

  passports = [p for p in passports if set(rules.keys()).issubset(p.keys())]
  print 'part 1: %d' % len(passports)
  print 'part 2: %d' % sum(1 for p in passports if valid_pt_2(p))
