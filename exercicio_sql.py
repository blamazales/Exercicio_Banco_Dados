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


#d) Contar o número total de alunos na tabela

conexao.commit()
conexao.close()