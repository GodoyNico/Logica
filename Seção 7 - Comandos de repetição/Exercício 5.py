#5- Faça um programa que leia um nome de usuário e sua senha e não aceite a senha igual ao nome de usuário, mostrando uma mensagem de erro
#e voltando a pedir as informações.

nome=input('Digite seu nome: ')
senha=input('Digite sua senha: ')

while senha == nome:
    print('Senha não pode ser igual ao seu nome.')
    nome=input('Digite seu nome: ')
    senha=input('Digite sua senha: ')
else:
    print('Login efetuado!')
