from functools import reduce

algorithm, image = open('20_input.txt').read().split('\n\n')
algorithm = {idx for idx,c in enumerate(''.join(map(str.strip, algorithm)))
                 if c == '#'}
image = {(x,y) for y,row in enumerate(image.split('\n'))
               for x,c in enumerate(row)
               if c == '#'}

def enhance(image, algorithm, outside):
  def pixel_value(image, xrng, yrng, outside, x,y):
    return int(''.join('1' if (xn,yn) in image
                           else '0' if xn in xrng and yn in yrng
                           else outside
                       for yn in [y-1, y, y+1] for xn in [x-1, x, x+1]),
               2)
  xrng, yrng = (range(min(x for x,_ in image),
                      max(x for x,_ in image) + 1),
                range(min(y for y,_ in image),
                      max(y for y,_ in image) + 1))
  return {(x,y) for x in range(xrng.start - 1, xrng.stop + 1)
                for y in range(yrng.start - 1, yrng.stop + 1)
                if pixel_value(image,xrng, yrng, outside, x, y) in algorithm}

print('part 1:', len(reduce(lambda i,step: enhance(i, algorithm, str(step%2)), range(2), image)))
print('part 2:', len(reduce(lambda i,step: enhance(i, algorithm, str(step%2)), range(50), image)))
