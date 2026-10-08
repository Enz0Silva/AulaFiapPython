from aluno import Aluno # PascalCase
from disciplina import Disciplina

# Criar / Instanciar 1 aluno
aluno1 = Aluno("João", "123456" ,"Ciências Da Computação")
# print(aluno1.notas_por_disciplina)

# Criar / Instanciar 2 aluno
model_mat = Disciplina( "Modelagem Matemática.","Roberto ")
model_lin = Disciplina( "Modelagem Linear.","Rodolfo ")


# Quero matrícular o aluno nas disciplinas
aluno1.matricular(model_mat)
aluno1.matricular(model_lin)
# print(aluno1.disciplinas[0].professor)
# print(aluno1.disciplinas[0].exibir_infos()

# Adicionar notas referente as diciplinas
aluno1.adicionar_nota(model_mat,10)
aluno1.adicionar_nota(model_mat,20)
aluno1.adicionar_nota(model_lin,30)
#print(aluno1.notas_por_disciplinas)

print(aluno1.calcular_media_d(model_lin))