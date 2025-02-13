class usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome 
        self.senha = senha
        self.email = email
        self.jogos = []
        self.saldo = 0.0
        self.itens = []
        self.mensagens = []
        self.pontuacao = 0
        self.conquistas = []
        self.preferencias = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)
        print(f"{jogo} adicionado a conta de {self.nome}")

    def adicionar_saldo(valor):
        self.saldo += valor
        
    def adicionar_itens(self, item):
        self.itens.append(item)
        
    #def batepapo(mensagem):
    #    self.mensagens.append = [] 

    def adicionar_pontuacao(self, pontos):
        self.pontuacao += pontos

    def adicionar_conquistas(self, conquisst):
        self.conquistas.append(conquisst)
        
    def adicionar_preferencias(self, preferencia):
        self.preferencias.append(preferencia)

    def mostrar_info(self):
        print(f"email : {self.email}")

class plataforma_game:
    def __init__(self, nome):
        self.nome = nome
        self.usuarios = {}
        self.jogos_disponiveis = []

    def criar_usuario(self, nome, email, senha):
        if email in self.usuarios:
            print("Email ja cadastrado")
        else: 
            novo_usuario = Usuario(nome, email, senha)
            self.usuarios[email] = novo_usuario
            print("Usuario cadastrado")

    def excluir_usuario(self, email, senha):
        if email in self.usuarios:
            usuario_removido = self.usuarios.pop(email)
        else:
            print("Email não encontrado")

    def adicionar_jogo_a_p(self, jogo):
        if jogo in self.jogos_disponiveis:
            print("Jogo já existente")
        else:
            self.jogos_disponiveis.append(jogo)
            print("Jogo adicionado")

    def remover_jogo(self, jogo):
        if jogo in self.jogos_disponiveis:
            self.jogos_disponiveis.remove(jogo)
            print("Jogo removido")
        else: ("O Jogo não está cadastrado")
    
    def adicionar_jogo_usuario(self, email, jogo):
        if email not in self.usuarios:
            printf("Usuario não encontrado")
        elif jogo not in self.jogos_disponiveis:
            print("Jogo não encontrado")
        else:
            self.usuarios[email].adicionar_jogo(jogo)
    
    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuario encontrado")
        else:
            print("\nUsuarios cadastrados:\n")

            for usuario in self.usuarios:
                print(usuario.nome)

    def listar_jogos(self):
        if not self.jogos_disponiveis:
            print("Nenhum jogo cadastrado")
        else:
            print("\nJogos disponiveis:\n")
            for jogo in self.jogos_disponiveis:
                print(jogo)

    def exibir_classificacao(self):
        if not self.usuarios:
            print("Nenhum usuario cadastrado na plataforma")
            return

        classificacao = [
            (usuarios.nome, len(usuario.conquistas))
            for usuario in self.usuarios.values()
        ]

        print("\nClassificacao de conquista dos usuarios:\n")
        for posicao, (nome, num_conquistas) in enumerate(classificacao_ordenada, start = 1):
            print(f"{posicao}º: {nome} - {num_conquistas} conquistas")

class menu:
    def __init__(self, plataforma):
        self.plataforma = plataforma

    def menu(self):
        while True: 
            print("\nMenu principal\n")
            print("1 - Criar Usuario")
            print("2 - Adicionar Jogo a Plataforma")
            print("3 - Adicionar jogo a usuario")
            print("4 - Adicionar conquista a Usuario")
            print("5 - Exibir classificacao")
            print("6 - Listar usuarios")
            print("7 - Listas jogos disponiveis")
            print("8 - Sair ")

            opcao == int(input("Escolha uma opcao"))

            if opcao == 1:
                self.criar_usuario()
            elif opcao == 2:
                self.adicionar_jogo_a_p()
            elif opcao == 3:
                self.adicionar_jogo_usuario
            elif opcao == 4:
                self.adicionar_conquistas
            elif opcao == 5:
                self.plataforma;exibir_classificacao
            elif opcao == 6:
                self.plataforma.listar_usuarios
            elif opcao == 7:
                self.plataforma.listar_usuarios
            else: 
                break

    def criar_usuario(self):
        nome = input("Digite o nome de usuario")
        email = input("Digite o email")
        senha = input("Digite a senha")
        self.plataforma.criar_usuario

    def adicionar_jogo_a_p(self):
        jogo = input("Nome do jogo que deseja adicionar")
        self.plataforma.adicionar_jogo

    def adicionar_jogo_usuario(self):
        email = input("Digite o email do usuario")
        jogo = input("Nome do jogo que deseja adicionar")
        self.plataforma.adicionar_jogo_usuario
    
    def adicionar_conquistas(self):
         email = input("Digite o email do usuario")
         conquista = input("Digite a conquita adquirida")
         if email in self.plataforma_game: 
             print("conquista adicionada")
         else:
             print("Erro ao adicionar conquista")