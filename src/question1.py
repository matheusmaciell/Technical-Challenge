class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_open_contract (open_contracts, renegotiated_contracts):
        '''Get the ID from the biggest debt from the open contracts.'''
        bigger = 0
        actual_contratc = None
        index = -1
        for i in range(len(open_contracts)):
            if(open_contracts[i].debt > bigger and open_contracts[i].id not in renegotiated_contracts):
                actual_contratc = open_contracts[i]
                bigger = open_contracts[i].debt
                index = i
        return actual_contratc,index

    def get_top_N_open_contracts(self,open_contracts, renegotiated_contracts, top_n):  
        '''Get the top n ID's from the open contracts.'''
        top_n_open_contracts = []
        for i in range(top_n):
            top,index = Contracts.get_top_open_contract(open_contracts, renegotiated_contracts)
            open_contracts[index].debt = -1
            if(index != -1):
                top_n_open_contracts.append(top.id)
        return top_n_open_contracts

    


