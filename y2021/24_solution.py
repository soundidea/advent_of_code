def seek(params, find_largest=True, z=0, idx=0):
  if idx == 14:
    return (z == 0, [])
  i,j,k = params[idx]
  if i == 26:
    magic = z % 26 + j
    if magic > 9 or magic < 1:
      # Backtrack, z will never reach 0 from here.
      return False, []
    success, n = seek(params, find_largest, z // i, idx + 1)
    # No need to search for this digit, just use the one that makes z smaller.
    return success, [magic] + n
  else:
    # Need to search through the 9 possibilities for this digit.
    digits = range(9,0,-1) if find_largest else range(1,10)
    for digit in digits:
      success, n = seek(params, find_largest, z * 26 + digit + k, idx + 1)
      if success:
        return success, [digit] + n
  # Dead end, backtrack.
  return False, []

# Each block of 18 lines is almost identical, it just differs in the params on lines 4,5,15, so just gather those
program = [line.strip().split() for line in open('24_input.txt').readlines()]
params = [list(map(int, [program[i+n][-1] for n in [4,5,15]])) for i in range(0, len(program), 18)]

_,n = seek(params)
print('part 1:', ''.join(map(str, n)))
_,n = seek(params, find_largest=False)
print('part 2:', ''.join(map(str, n)))
