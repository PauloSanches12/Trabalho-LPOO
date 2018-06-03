class pessoa:
    def __init__(self,nome):
        self.nome=nome

class Inscricao:
    def __init__(self):
        self.valor=0

class InscricaoDeAluno(Inscricao):
    def __init__(self):
        super().__init__()
        self.valor=50

class InscricaoDeProfessor(Inscricao):
    def __init__(self):
        super().__init__()
        self.valor = 80

class InscricaoDeProfissional(Inscricao):
    def __init__(self):
        super().__init__()
        self.valor = 120
        
class EncoInfo:
    def __init__(self,inscritos):
        self.inscritos=[]

class Inscrito:
    def __init__(self,pessoa,inscricao):
        self.pessoa=pessoa
        self.inscricao=inscricao

class atendente(pessoa):
    def __init__(self,nome,encoinfo):
        super().__init__(nome)
        self.encoinfo=encoinfo

    def atender(self,pessoa, inscricao):
        if len(self.encoinfo.inscritos) < 100:
            a=self.encoinfo.inscritos
            a.append(Inscrito(pessoa,inscricao))
        else:
           print("Impossivel atender")
           self.emitir_realtorio()
    def emitir_realtorio(self):
        ca=0
        cprofe=0
        cprofi=0
        for i in self.encoinfo.inscritos:
            if type(i.inscricao)==InscricaoDeAluno:
                ca+=1
            elif type(i.inscricao)==InscricaoDeProfessor:
                cprofe+=1
            else:
                cprofi+=1
        print('Relatorio:')
        print('Alunos:',ca)
        print('Professor:',cprofe)
        
def chance(x,a,b,c):
    r=random.random()*100
    if x < r:
        return a
    elif x < r:
        return b
    else:
        return c
    
import random
E=EncoInfo([])
A=atendente("Crisley",E)
B=atendente("João",E)
C=atendente("Samuel",E)
if __name__ == '__main__':
    atendentes=chance(33,A,B,C)
    for n in range(102):
        p=pessoa("Enzo"+str(n))
        atendentes.atender(p,random.choice([InscricaoDeAluno(),InscricaoDeProfessor(),InscricaoDeProfissional()]))
