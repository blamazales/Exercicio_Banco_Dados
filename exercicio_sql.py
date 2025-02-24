import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade int(100), curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(1,"Barbara",29,"Data Science")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(2,"Leonardo",22,"Biologia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(3,"Jose",19,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(4,"Murilo",35,"Filosofia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(5,"Maria",30,"Engenharia")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

#dados = cursor.execute('SELECT * FROM alunos')
#for usuario in dados:
#	print(usuario)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for usuario in dados:
#	print(usuario)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
##dados = cursor.execute('SELECT * FROM alunos WHERE curso ="Engenharia" ORDER BY curso ASC')
#for usuario in dados:
#	print(usuario)

#d) Contar o número total de alunos na tabela
#dados = cursor.execute('SELECT COUNT(*) FROM alunos').fetchall()
#quantidade = dados[0][0]  # Pega o primeiro resultado da consulta
#print(f"Quantidade de registros na tabela alunos: {quantidade}")


#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET nome="José" WHERE nome="Jose"')  


#b) Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos WHERE id=4')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade int(100), saldo FLOAT);')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(2,"Maria",50,2000.50)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(3,"João",35,5500)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(4,"Alessandra",23,3000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(5,"David",30,3350.50)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(6,"Teo",19,350.50)')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.



conexao.commit()
conexao.close()