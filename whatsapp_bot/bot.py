from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
    
        lista_amigos = ["Roberth", "Keslly", 'Amadeus', "Fátima", "Luciene", "Bruno", "Dani", "Letícia Santos", "Rafaela", "Silmara"]
        

        self.execute(r'C:\Users\Public\Desktop\Google Chrome.lnk')
        self.wait(8000)
        self.click_at(244, 63) # barra de navegação
        self.paste("web.whatsapp.com")
        self.enter()
        if not self.find( "ponteiro", matching=0.97, waiting_time=1000000):
            self.not_found("ponteiro")
        for amigo  in lista_amigos:
            self.click_at(201, 197)
            self.paste(amigo)
            self.wait(3000)
            self.click_at(178, 343)
            self.wait(2000)
            self.click_at(756, 970)
            self.paste('Oii ' + amigo + ', estou mandando essa mensagem através de um código em Python que desenvolvi. Ele personaliza e envia mensagens em massa para as pessoas, caso queira ver o código em si e como ele funciona poderá encontrar um vídeo que acabei de postar no meu canal do YouTube, o link é: https://youtu.be/BzTTjo864ho')
            self.wait(2000)
            self.enter()
            self.wait(2000)
            self.click_at(529, 198)
            self.wait(2000)
        
        

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()



