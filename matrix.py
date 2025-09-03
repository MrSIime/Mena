matrix = [
    [
        ['0','1','2','3','4'],
        ['5','6','7','8','9'],
        ['a','b','c','d','e'],
        ['f','g','h','i','j'],
        ['k','l','m','n','o']
    ],
    [
        ['p','q','r','s','t'],
        ['u','v','w','x','y'],
        ['z','а','б','в','г'],
        ['ґ','д','е','є','ж'],
        ['з','и','і','ї','й']
    ],
    [
        ['к','л','м','н','о'],
        ['п','р','с','т','у'],
        ['ф','х','ц','ч','ш'],
        ['щ','ь','ю','я','A'],
        ['B','C','D','E','F']
    ],
    [
        ['G','H','I','J','K'],
        ['L','M','N','O','P'],
        ['Q','R','S','T','U'],
        ['V','W','X','Y','Z'],
        ['!','@','#','$','%']
    ],
    [
        ['^','&','*','(',')'],
        ['-','_','=','+','['],
        [']','{','}',';',':'],
        ["'",'"',',','.','<'],
        ['>','/','?','\\','end']
    ]
]

def get_coords(target: str):
    if not target in matrix:
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                if matrix[i][j][k] == target:
                    coords = (i, j, k)
                    return coords


def post_coords(target):
    try:
        i, j, k = target
        sym = matrix[i][j][k]
        return sym
    except:
        return None