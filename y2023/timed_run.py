import glob
import importlib.util
import sys
import time

filenames = ([f for arg in sys.argv[1:] for f in glob.glob(arg)]
             if len(sys.argv) > 1 
             else sorted(glob.glob('day_*.py')))

overall_init_time, overall_p1, overall_p2 = (0,0,0)

for filename in filenames:
  modulename = filename[:-3]
  print('Day', int(modulename[-2:]))

  spec = importlib.util.spec_from_file_location(modulename, filename)
  module = importlib.util.module_from_spec(spec)
  sys.modules[modulename] = module
  spec.loader.exec_module(module)

  start_time = time.perf_counter()
  data = module.parse_data(module.data_files[0])
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_init_time += elapsed
  print(f'Parse data: {elapsed:.3f} ms')

  start_time = time.perf_counter()
  module.part1(data)
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_p1 += elapsed
  print(f'Part 1: {elapsed:.3f} ms')

  start_time = time.perf_counter()
  module.part2(data)
  elapsed = (time.perf_counter() - start_time) * 1000
  overall_p2 += elapsed
  print(f'Part 2: {elapsed:.3f} ms\n')

print(f'Overall data parsing: {overall_init_time:.3f} ms')
print(f'Overall runtime: {overall_p1 + overall_p2:.3f} ms')
print(f'Total: {overall_init_time + overall_p1 + overall_p2:.3f} ms')

