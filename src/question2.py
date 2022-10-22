class Orders:
    
    def combine_orders(self, requests, n_max):
        '''Calcula o menor número de viagens necessarias para recolher os valores de todos as agencias, Possui complexidade O(n).
        
        Parametros: 
           1. requests: é uma lista de inteiros, representando o valor monetário requisitado por uma agência.
           2. n_max:  é um inteiro contendo o valor máximo que pode ser levado em uma única viagem.
        
        
        Retorno:
             um valor inteiro, contendo o número mínimo de viagens que deve ser feita para atender todas as requisições.
        '''
        n_orders = 0
  
        for i in range(len(requests)-1):
                if(requests[i] != -1):
                    if requests[i] + requests[i+1] <= n_max:
                        n_orders +=1
                        requests[i+1] = -1
                        
                    else:
                        n_orders +=1
        if requests[-1] != -1:
                n_orders += 1
        return n_orders