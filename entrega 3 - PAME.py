from uuid import uuid4


class Sistema:
    projetos=()
    tipo_projeto=()
 
    usuarios = ()
    tipo_usuarios=()
    senhas= ()
    IDs=[]
    def login(self,usuario,senha):
        
        usuario= input("digite seu usuario: ")
        print("/n")

        if usuario in usuarios:

            local_usuario= usuarios.index(usuario,0,len(usuarios)-1)

            senha =input("digite a senha: ")
            print("/n")
            if senha == senhas[local_usuario]:

                tipo_usuario = tipo_usuarios[local_usuario]

                print("Bem vindo %s /n"%(usuario))

                if tipo_usuario[usuario] == 0:
                    printf

                
            
            
        else:
            print("usuario nao encontrado")


    

class Consultor:
    def ()



class Gerente:




class Projetos:

