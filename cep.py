import requests



# Editar input do usuario
def cep_usuario(cep):
    # cep_edit tirar do os caractere não numeros
    cep_edit = "".join(c for c in cep if c.isdigit())
    # confirma tamanho string  
    if len(cep_edit) == 8:
       return f"https://viacep.com.br/ws/{cep_edit}/json/"
    else: 
        # Cep  e inválido
        return None
    
"""headers"""



def local_user():
    try:
        cep_input = input("Digite seu cep:")
        url_cep  = cep_usuario(cep_input)
        if url_cep:
            r = requests.get(url_cep)
            r.raise_for_status()
            return r.json()
        
    except requests.exceptions.HTTPError as  e:
        print(f"An error HTTP: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexão: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Tempo limete de conexão excedido: {e}")

