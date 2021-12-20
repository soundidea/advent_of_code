from functools import reduce

factors = {
  'forward': 1+0j,
  'up': 0-1j,
  'down': 0+1j
}

parsed_input = [factors[direction] * int(distance) for (direction, distance) in [
    command.split() for command in open('02_input.txt').readlines()]]

final_pos = sum(parsed_input)
print('part 1:', int(final_pos.real * final_pos.imag))

final_aim, final_pos = reduce(
    lambda aim_pos, cmd: (aim_pos[0] + cmd.imag,
                          aim_pos[1] + complex(cmd.real, aim_pos[0] * cmd.real)),
    parsed_input,
    (0+0j, 0+0j))
print('part 2:', int(final_pos.real * final_pos.imag))

