def rotLeft(a, d):
    '''
    In this challenge we have to "rotate" an array a to the left, given d rotations.

    My solution is not clever, once it uses way more memory than it's really needed.

    The new position of the elementss are only a translation given by d, so basically we'd write "x_translated = x_original - d"

    '''
    new = [0 for i in range(0,len(a))]
    nova_posicao = 0

    for i in range(len(a)):
        nova_posicao =  i - d
        new[nova_posicao] = a[i]
        
    return new