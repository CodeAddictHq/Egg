digits = [
  '0',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
]
chars = [
  '0',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  'a',
  'b',
  'c',
]
def genOTP_4digit():
  combs = []
  for a in digits:
    for b in digits:
      for c in digits:
        for d in digits:
          combs.append(a+b+c+d)
  return combs[0:100:]
  
def genOTP_6digit():
  combs = []
  for a in digits:
    for b in digits:
      for c in digits:
        for d in digits:
          for e in digits:
            for f in digits:
              combs.append(a+b+c+d+e+f)
  return combs


def genPASS_wifi():
  combs = []
  for a in digits:
    for b in digits:
      for c in digits:
        for d in digits:
          for e in digits:
            for f in digits:
              combs.append(a+b+c+d+e+f)
  return combs
  
  
  
def genNum(last_num,):
  nums = []
  n = 0
  if last_num<0 or last_num == 0:
    return []
  while last_num >= n:
    nums.append(n)
    n += 1
  return nums
    
  
  
a = (genOTP_6digit())
