class Orders:
    
    def combine_orders(self, requests, n_max):
        '''Return an integer indicating the minimum number of travels'''
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