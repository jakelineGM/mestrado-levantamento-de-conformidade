import sys 

def main():
  tokens = sys.stdin.read().split()
  pilha = []
  out = []

  def push(v):
    pilha.append(v)
    out.append(f"push {v}")

  def pop():
    v = pilha.pop()
    out.append(f"pop {v}")
    return v

  i = 0
  parar = False

  while i < len(tokens) and not parar:
    x = int(tokens[i])
    i += 1

    push(x)

    if pilha[-1] == 0:
      break 

    while pilha and pilha[-1] < 0:
      if len(pilha) < 2:
        parar = True
        break 

      a = pop()
      b = pop()
      s = a + b
      push(s)

      if pilha[-1] == 0:
        parar = True
        break 
  sys.stdout.write("\n".join(out))

if __name__ == "__main__":
  main()