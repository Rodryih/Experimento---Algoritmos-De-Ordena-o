# Esse Algoritmo foi retirado do site Programiz, link: https://www.programiz.com
# Pagina especifica do Algoritimo: https://www.programiz.com/dsa/shell-sort
# Programiz é uma plataforma de aprendizado de programação em várias linguagens.
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

class ShellSort:

    @staticmethod
    def sort(my_list, size):
        lista = my_list

        # Rearrange elements at each size/2, size/4, size/8, ... intervals
        interval = size // 2
        while interval > 0:
            for i in range(interval, size):
                temp = lista[i]
                j = i
                while j >= interval and lista[j - interval] > temp:
                    lista[j] = lista[j - interval]
                    j -= interval

                lista[j] = temp
            interval //= 2
