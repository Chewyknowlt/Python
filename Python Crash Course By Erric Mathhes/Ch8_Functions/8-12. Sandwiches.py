print('8-12. Sandwiches')

def order(* sandwitches):
    #
    print('\nWe have these sandwitches: ')
    for sandwitch in sandwitches:
        print('-' + sandwitch)

order('club','fajita','spice')
order('','')
order('hot')
