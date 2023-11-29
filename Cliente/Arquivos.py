class Arquivos:
    @staticmethod
    def ler_nomes_arquivo(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            nomes = [linha.strip() for linha in file.readlines()]
        return nomes

    @staticmethod
    def cemk():
        return Arquivos.ler_nomes_arquivo("Dados/nomes100k.txt")

    @staticmethod
    def duzentosk():
        return Arquivos.ler_nomes_arquivo("Dados/nomes250k.txt")

    @staticmethod
    def quinhetosk():
        return Arquivos.ler_nomes_arquivo("Dados/nomes500k.txt")
