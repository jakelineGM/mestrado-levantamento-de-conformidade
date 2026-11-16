class ponto:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.distancia = (x ** 2 + y ** 2) ** 0.5  

    def __lt__(self, outro):
       
        
        if self.distancia != outro.distancia:
            return self.distancia < outro.distancia
        
        if self.x != outro.x:
            return self.x < outro.x
        
        return self.y < outro.y


entrada = eval(input())


pontos = []
for item in entrada:
    pontos.append(ponto(item[0], item[1]))


pontos_ordenados = sorted(pontos)


for ponto in pontos_ordenados:
    print(f"{ponto.x} {ponto.y}")