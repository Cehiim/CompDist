def quebra_num(num_string): # Número vem no formato: a + bi
  lista = num_string.split(" ")
  num_a, sinal, num_b = lista[0],lista[1], lista[2]
  num_b = num_b[:-1]
  num_a = float(num_a)
  num_b = float(num_b)
  
  if(sinal == "-"):
    num_b *= -1
    
  return num_a, num_b  #Obtém os números reais a e b

def junta_nuns(a, b): #Converte os números para o formato a + bi
  if(b > 0):
    return f"{a} + {b}i"
  else:
    b *= -1
    return f"{a} - {b}i"

def soma(num_string1, num_string2):
  num_a1, num_b1 = quebra_num(num_string1) # Divide os números
  num_a2, num_b2 = quebra_num(num_string2)

  num_a_soma = num_a1 + num_a2 # Soma
  num_b_soma = num_b1 + num_b2

  return junta_nuns(num_a_soma, num_b_soma)


def subtracao(num_string1, num_string2):
  num_a1, num_b1 = quebra_num(num_string1)
  num_a2, num_b2 = quebra_num(num_string2)

  num_a_sub = num_a1 - num_a2
  num_b_sub = num_b1 - num_b2

  return junta_nuns(num_a_sub, num_b_sub)


def mult(num_string1, num_string2):
  num_a1, num_b1 = quebra_num(num_string1)
  num_a2, num_b2 = quebra_num(num_string2)

  num_a_mul = (num_a1 * num_a2) - (num_b1 * num_b2)
  num_b_mul = (num_b1 * num_a2) + (num_a1 * num_b2)

  return junta_nuns(num_a_mul, num_b_mul)

def div(num_string1, num_string2):
  a, b = quebra_num(num_string1)
  c, d = quebra_num(num_string2)

  num_a_div = (a * c + b * d) / (c**2 + d**2)
  num_b_div = (b * c - a * d) / (c**2 + d**2)

  return junta_nuns(num_a_div, num_b_div)