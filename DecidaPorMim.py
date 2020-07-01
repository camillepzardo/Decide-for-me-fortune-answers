import self as self
import random
import time


class DecidindoPorVoce:
    def __init__(self):
        self.resposta = ["Nem tenta, come um bolo", "Não posso confirmar", "Quem sabe?", "Já bebi demais, não posso opinar",
                         "Isso requer mais avaliação", "Melhor ir ver um filme!", "Acho difícil", "Pode se dizer que sim"];

    def Inicio(self):
        print("Ok, vamos começar! Para sair do programa digite N")
        self.FazerPergunta()

    def FazerPergunta(self):
        self.RespostaUm = input("Digite sua pergunta:")
        self.RespostaUm = self.RespostaUm.upper()

        if self.RespostaUm == "N":
            print("Ok, tchau!")
        else:
            print("Pensando...")
            time.sleep(2)
            print("Resposta: ", random.choice(self.resposta))
            self.respostaNova = input("Você gostaria de perguntar de novo? (S/N)")
            self.respostaNova = self.respostaNova.upper()

            if self.respostaNova == "S":
                self.FazerPergunta()

            elif self.respostaNova == "N":
                print("Tchauzinho! Pode fechar")

            else:
                print("Digite apenas S ou N")
                self.FazerPergunta()


DecidindoPorVoce().Inicio()
