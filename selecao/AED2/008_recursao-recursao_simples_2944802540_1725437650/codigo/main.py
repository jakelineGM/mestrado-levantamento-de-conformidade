def prop(n):
  eh = False;
  if(n<5 or n%17==0):
    eh = True;
  elif(n%5==0):
    eh = prop(n/5);
  elif(n%2!=0):
    eh = prop(n-3);
  
  return eh;
  

entrada = input();
i, fim = (int(num) for num in entrada.split());

while(i<=fim):
  if(prop(i)):
    print(i);
  i+=1;