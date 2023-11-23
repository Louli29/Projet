def creat_perso(depart): #depart couple (x depart, y depart)
    d={}
    d["char"]="o"
    d["x"]=depart[0]
    d["y"]=depart[1]
    return d
#print(creat_perso((0,0)))
p=creat_perso((0,0))
def update_p(letter,p,m):#p position personnage et m matrice map
    if letter=="d" :
        if p["y"]+1<=len(m) and m[p["x"]][p["y"]+1]==0:
            p["y"]+=1       
    if letter=="q":
        if m[p["x"]][p["y"]-1]==0:
            p["y"]-=1
    if letter=="z":
        if m[p["x"]-1][p["y"]]==0:
            p["x"]-=1
    if letter=="s" :
        if p["x"]+1<len(m[0]) and m[p["x"]+1][p["y"]]==0:
            p["x"]+=1
    if p["x"] <0:
        p["x"]=0
    if p["y"]<0:
        p["y"]=0
        
    return p



def display_map_and_char (m,d,p,letter):# m matrice map, dico des murs, p position personnage, letter le déplacement 
    L=[[None for a in range (len(m[0]))] for b in range(len(m))]
    for i in range (len(m)):
        for j in range (len(m[0])):
            for k in d:
                if m[i][j]==k:
                    L[i][j]=d[k]

    
   
    L[p["x"]][p["y"]]="o"
    

    return L

def affichage(M,d,p,letter):
            m=display_map_and_char(M,d,p,letter)
            for a in range(len(m)):
                for b in range (len (m[0])):
                    print (m[a][b],end="")
                print(end="\n")
            return""
                
map = [[0,0,0,1,1],
       [0,0,0,0,1],
       [1,1,0,0,0],
       [0,0,0,0,0]]

dico = {0:' ',1:'#'}

#print(affichage(map,dico,(0,0),letter))

l="q"
print(affichage (map,dico,p,l))
    
while True:

    letter=input("on avance vers où ? ")
    p=update_p(letter,p,map)
    print(affichage(map,dico,p,letter))
    
    



