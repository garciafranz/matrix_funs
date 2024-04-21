def det_m(m):
    '''
    >>> det_m([])
    1
    >>> det_m([6.0221023])
    6.0221023
    >>> det_m([[2,1],[5,3]])
    1
    >>> det_m([[0,1,4],[5,8,2],[3,6,9]])
    -15
    '''
    if [] == m:
        return 1
    if hasattr(m, '__iter__'):
        if 1 == len(m):
            return m[0]
        if 2 == len(m) and hasattr(m[0], '__iter__') and 2 == len(m[0]):
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return

def main():
    import doctest
    doctest.testmod()

if '__main__' == __name__:
    main()
