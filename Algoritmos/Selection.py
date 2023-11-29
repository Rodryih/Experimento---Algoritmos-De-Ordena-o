# Esse Algoritmo foi retirado do site Programiz, link: https://www.programiz.com
# Pagina especifica do Algoritimo: https://www.programiz.com/dsa/selection-sort
# Programiz é uma plataforma de aprendizado de programação em várias linguagens.
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

class SelectionSort:

    @staticmethod
    def sort(my_list, size):
        lista = my_list

        for step in range(size):
            min_idx = step

            for i in range(step + 1, size):

                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if lista[i] < lista[min_idx]:
                    min_idx = i

            # put min at the correct position
            (lista[step], lista[min_idx]) = (lista[min_idx], lista[step])
