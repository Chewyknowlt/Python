print('8-14. Cars')

def car(company, model, ** add):
    #
    info = {}
    info['company'] = company
    info['model'] = model

    for key, value in add.items():
        info[key] = value
    return info
love = car('suzuki', 'corolla',
           color = 'red whine',
           mfg = 'mar')
print(love)
    

 
