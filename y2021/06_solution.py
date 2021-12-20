def spawn_schedule(first_spawn_day, num_days, num_fish):
  '''For num_fish who will first spawn on first_spawn_day, generate the
     list of days, with how many fish will be spawned on each day.'''
  spawn_days = range(first_spawn_day, num_days, 7)
  return [num_fish if d in spawn_days else 0 for d in range(num_days)]

feesh = list(map(int, open('06_input.txt').read().strip().split(',')))
num_days = 256
spawning_schedule = list(map(sum, zip(*[spawn_schedule(f, num_days, 1) for f in feesh])))
for day in range(num_days):
  spawning_schedule = list(map(sum, zip(spawning_schedule,
                                        spawn_schedule(day + 9,
                                                       num_days,
                                                       spawning_schedule[day]))))
print('part 1:', len(feesh) + sum(spawning_schedule[:80]))
print('part 2:', len(feesh) + sum(spawning_schedule))
