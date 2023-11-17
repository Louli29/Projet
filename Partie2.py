def creat_perso(depart):
    d={}
    d["char"]="o"
    d["x"]=depart[0]
    d["y"]=depart[1]
    return d
#print(creat_perso((0,0)))

def display_map_and_char (m,d,p):
    Perso=creat_perso(p)
    L=[[None for a in range (len(m[0]))] for b in range(len(m))]
    for i in range (len(m)):
        for j in range (len(m[0])):
            for k in d:
                if m[i][j]==k:
                    L[i][j]=d[k]


    L[Perso["x"]][Perso["y"]]="o"
    

        
    return L

def affichage(M,d,p):
        m=display_map_and_char(M,d,p)
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

print(affichage(map,dico,(0,0)))


