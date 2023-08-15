class Aluno():
    def __init__(self, aNome, aIdade, aNota1, aNota2, aMedia):
        self.nome = aNome
        self.idade = aIdade
        self.nota1 = aNota1
        self.nota2 = aNota2
        self.media = aMedia
        
    def calculaMedia(self, aluno):
        aluno.media= (aluno.nota1 + aluno.nota2) / 2
        return self.media
    
    def imprimiDados(self, aluno):
        print(f"O aluno {aluno.nome} tem {aluno.idade} anos de idade, suas notas foram {aluno.nota1} e {aluno.nota2}, com uma média de {aluno.media}")

    def validacao(self, aluno):
        if aluno.media >= 6.0:
            print(f"Aluno {aluno.nome} foi aprovado!")
        elif aluno.media < 6.0:
            print(f"Aluno {aluno.nome} está de recuperação!")
        else:
            print("Algo deu errado!")

aluno1 = Aluno("Matheus", 19, 10, 9, 0)
aluno2 = Aluno("Lucas", 18, 9, 8, 0)

aluno1.calculaMedia(aluno1)
aluno2.calculaMedia(aluno2)

aluno1.imprimiDados(aluno1)
aluno2.imprimiDados(aluno2)

aluno1.validacao(aluno1)
aluno2.validacao(aluno2)