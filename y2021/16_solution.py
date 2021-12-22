from functools import reduce
import operator

def parse_packet(bits, pos=0):
  result = {'version': int(bits[pos: pos + 3], 2),
            'type':    int(bits[pos + 3: pos + 6], 2)}
  pos += 6
  if result['type'] == 4:
     value, keep_going = '', 1
     while keep_going:
       keep_going = int(bits[pos])
       value += bits[pos+1:pos+5]
       pos += 5
     value = int(value, 2)
     result['value'] = value
  else:
    len_type = int(bits[pos])
    size_len = 12 if len_type else 16
    subs_remain = int(bits[pos + 1 : pos + size_len], 2)
    pos += size_len
    result['subs'] = []
    while subs_remain > 0:
      old_pos = pos
      sub, pos = parse_packet(bits, pos)
      result['subs'].append(sub)
      subs_remain -= 1 if len_type else (pos - old_pos)
  return result, pos

def sum_versions(packet):
  return packet['version'] + (sum(sum_versions(c) for c in packet['subs'])
                              if 'subs' in packet else 0)

def evaluate(packet):
  t = packet['type']
  if t == 4:
    return packet['value']
  ops = {0: operator.add,
         1: operator.mul,
         2: min,
         3: max,
         5: operator.gt,
         6: operator.lt,
         7: operator.eq}
  sub_values = list(map(evaluate, packet['subs']))
  return reduce(ops[t], sub_values[1:], sub_values[0])

hex_str = open('16_input.txt').read().strip()
bit_str = ''.join('{0:04b}'.format(int(n, 16)) for n in hex_str)
packet, _ = parse_packet(bit_str)
print('part 1:', sum_versions(packet))
print('part 2:', evaluate(packet))
