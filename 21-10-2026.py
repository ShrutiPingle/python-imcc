def longstr(*ss):
  if len(ss)==0:
    return None
  maxs=ss[0]
  for i in ss:
    if len(i)>len(maxs):
      maxs=i
  return maxs

print(longstr("ashwini","yee","na","jaguu"))
