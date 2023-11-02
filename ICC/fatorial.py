def fatorial (numero):
 fatorial = 1
 for contador in range (numero, 0, -1):
  print(contador, end='')
  if contador > 1:
  print(' × ', end='')
  else:
  print(' = ', end='')
  fatorial = fatorial * contador
 return fatorial