# Esse Algoritmo foi retirado do site Real Python, link: https://realpython.com
# Pagina especifica do Algoritimo: https://realpython.com/sorting-algorithms-python/
# Há uma grande equipe por tras desse site/plataforma que podem ser encontrados aqui https://realpython.com/team/
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

from random import randint


class QuickSort:

    @staticmethod
    def sort(my_list):
        lista = my_list
        # If the input lista contains fewer than two elements,
        # then return it as the result of the function
        if len(lista) < 2:
            return lista

        low, same, high = [], [], []

        # Select your `pivot` element randomly
        pivot = lista[randint(0, len(lista) - 1)]

        for item in lista:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
        return QuickSort.sort(low) + same + QuickSort.sort(high)
