def inimeste_ja_palgade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uendatud loedid, kuhu lisati inimest ja pala
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :param inr n: Inimeste arv
    :rtype: list, list
    """
    if n>0:
        for j in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p

def andmed_veerudes(i:list,p:list)->any:
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    """
    for j in range(len(i)):
        print(i[j], "-",p[j])


def andmete_eemaldamine_nimi_jargi(i,list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    """
    nimi=input("Keda kustutada ära(nimi): ")
    for j in range(0,len(i)-1):
        if nimi in i:
            i.rove(nimi)
            p.pop(j)
    return i,p

def kellel_on_suurim_palk(i:list,p:list)->any:
    """
    """
    nimed=[]
    max_palk=max(p)
    for palk in p:
        if palk==max_palk:
            ind+1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def kellel_on_väiksem_palk(i:list,p:list)->any:
    """
    """
    nimed=[]
    min_palk=min(p)
    for palk in p:
        if palk==min_palk:
            ind+1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed 



def sorteerimine(i:list,p:list):
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p