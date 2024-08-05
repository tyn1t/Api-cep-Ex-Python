from cep import local_user 


if __name__=="__main__":
    response = local_user()
    print(f"""
    Cep:{response.get("cep")}
    Logradouro:{response.get( "logradouro")}
    bairro: {response.get( "bairro")}
    uf:{response.get( "uf")}
    localidade:{response.get( "localidade")}
    """)

    

