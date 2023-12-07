import glob
import importlib.util
import sys
import time

filenames = sorted(glob.glob('day_*.py'))
overall_load_time, overall_init_time, overall_runtime = (0,0,0)
for filename in filenames:
  modulename = filename[:-3]
  print('Day', int(modulename[-2:]))

  start_time = time.perf_counter()
  spec = importlib.util.spec_from_file_location(modulename, filename)
  module = importlib.util.module_from_spec(spec)
  sys.modules[modulename] = module
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_load_time += elapsed
  print(f'Module load: {elapsed:.3f} ms')

  start_time = time.perf_counter()
  spec.loader.exec_module(module)
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_init_time += elapsed
  print(f'Static init: {elapsed:.3f} ms')

  start_time = time.perf_counter()
  module.part1()
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_runtime += elapsed
  print(f'Part 1: {elapsed:.3f} ms')

  start_time = time.perf_counter()
  module.part2()
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_runtime += elapsed
  print(f'Part 2: {elapsed:.3f} ms\n')

print(f'Overall module load: {overall_load_time:.3f} ms')
print(f'Overall static init: {overall_init_time:.3f} ms')
print(f'Overall runtime: {overall_runtime:.3f} ms')
print(f'Overall time: {overall_load_time + overall_init_time + overall_runtime:.3f} ms')

