class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infors(self):
        print(f"Disciplina: {self.nome}, Professor: {self.professor}")

# Temporário
#python = Disciplina("Python", "Russi")
#print(python.professor)
#python.exibir_infors()