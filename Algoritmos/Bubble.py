# Esse Algoritmo foi retirado do site Real Python, link: https://realpython.com
# Pagina especifica do Algoritimo: https://realpython.com/sorting-algorithms-python/
# Há uma grande equipe por tras desse site/plataforma que podem ser encontrados aqui https://realpython.com/team/
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

class BubbleSort:

    @staticmethod
    def sort(my_list):
        lista = my_list
        size = len(lista)

        for i in range(size):
            # Cria uma bandeira que permitirá à função encerrar antecipadamente
            # caso não haja mais nada para ordenar
            alreadysorted = True

            # Start looking at each item of the list one by one,
            # comparing it with its adjacent value. With each
            # iteration, the portion of the array that you look at
            # shrinks because the remaining items have already been
            # sorted.
            for j in range(size - i - 1):
                if lista[j] > lista[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    alreadysorted = False

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if alreadysorted:
                break

        return lista
