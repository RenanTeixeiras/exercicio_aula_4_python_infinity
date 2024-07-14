
def ler_json():
    import json
    with open('banco.json','r') as file:
        banco = json.load(file)
    
    return banco

def solicitar_usuario():
    usuario = input('Digite o nome de usuario: ')
    return usuario

def solicitar_senha():
    senha = input('Digite a senha: ')
    return senha

def cadastrar():
    banco = ler_json()
    usuario = solicitar_usuario()
    senha = solicitar_senha()
    from werkzeug.security import generate_password_hash
    senha = generate_password_hash(senha)

    banco['usuarios'].append(usuario)
    banco['senhas'].append(senha)
    import json
    with open('banco.json','w') as file:
        file.write(json.dumps(banco, indent=4))
    print('Usuário cadastrado com sucesso.')
    ...

def fazer_login():
    banco = ler_json()
    while True:
        usuario = solicitar_usuario()
        if usuario not in banco['usuarios']:
            print('Usuário inválido! ')
        else:
            break
    posicao_usuario = banco['usuarios'].index(usuario)
    from werkzeug.security import check_password_hash

    while True:
        senha = solicitar_senha()
        if check_password_hash(banco['senhas'][posicao_usuario],senha) == False:
            print('Senha inválida!')
        else:
            break

    print('LOGIN EFETUADO COM SUCESSO')

escolhas = {
    '1': cadastrar,
    '2': fazer_login
}

def menu():
    print('DIGITE A OPÇÃO DESEJADA: ')
    print('1 - CADASTRAR-SE')
    print('2 - LOGAR')
    while True:
        opcao = input('-> ')
        if opcao not in ['1','2']:
            print('Opção inválida.')
        else:
            break
        
    escolhas[opcao]()
