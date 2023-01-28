def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0: #(1)
        return str(r)
    else:
        return dec_to_bin(q) + str(r) #(2)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1': #(3)
        return 1
    else:
        if nb_bin[-1] == '0': 
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

