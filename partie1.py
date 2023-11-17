def display_map (m,d):
    for i in range (len(m)):
        for j in range (len(m[0])):
            for k in d:
                if m[i][j]==k:
                    m[i][j]=d[k]
        
    return m

def affichage(M,d):
        m=display_map(M,d)
        for a in range(len(m)):
            for b in range (len (m[0])):
                print (m[a][b],end="")
                if b==len(m[0])-1:
                     print(end="\n")
        return""
                


map = [[0,0,0,1,1],
[0,0,0,0,1],
[1,1,0,0,0],
[0,0,0,0,0]]

dico = {0:' ',1:'#'}

print(affichage(map,dico))
