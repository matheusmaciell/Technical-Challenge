class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:   
    def filter_renegotieted_contracts(open_contracts,renegotiated_contracts):
        ''' Filtra a lista de contratos abertos utilizando a lista dos contratos renegociados'''
        dict = {}
        for contract in renegotiated_contracts:
            dict[contract] = True
        
        open = []
        for open_contract in open_contracts:
            if(not  dict.get(open_contract.id)):
                open.append(open_contract)
        return open        

    def get_top_open_contract (open_contracts):
        '''Busca o contrato com maior debito nao renegociado'''

        bigger = 0
        actual_contratc = None
        index = -1
        for i in range(len(open_contracts)):
            if(open_contracts[i].debt > bigger):
                actual_contratc = open_contracts[i]
                bigger = open_contracts[i].debt
                index = i
        return actual_contratc,index

    def get_top_N_open_contracts(self,open_contracts, renegotiated_contracts, top_n):  
        ''' Encontra o top_N de maiores debito de contratos nao renegociados
        
        Parametros: 
            1. open_contracts: Uma lista em que cada elemento é uma instância de Contract,
            2. renegotiated_contracts: Uma lista de numeros inteiros representando os identificadores dos associados que já renegociaram seus débitos
            3. top_n: Um inteiro com a quantidade de devedores que devem ser retornados pelo método.
        
        Retorno: 
             uma lista contendo top_n inteiros referentes aos identificadores dos devedores,
            ordenada do maior devedor para o menor, isto é, a posição 0 terá o maior devedor e a posição top_n -1 o menor.
        
        '''
        top_n_open_contracts = []

        # Filtra os contratos já renegociados para evitar aumento na complexidade
        contracts = Contracts.filter_renegotieted_contracts(open_contracts,renegotiated_contracts)
        
        # Caso não haja nenhum contrato aberto retorna uma lista vazia
        if len(contracts) <= 0:
            return top_n_open_contracts 

        # Encontra o maior elemento da lista para o top N, depois o maior para o segundo maior até completar a lista
        for i in range(top_n):
            top,index = Contracts.get_top_open_contract(contracts)
  
            contracts[index].debt = -1
            if(index != -1):
                top_n_open_contracts.append(top.id)
        return top_n_open_contracts

    

