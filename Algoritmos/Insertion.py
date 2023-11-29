# Esse Algoritmo foi retirado do site Real Python, link: https://realpython.com
# Pagina especifica do Algoritimo: https://realpython.com/sorting-algorithms-python/
# Há uma grande equipe por tras desse site/plataforma que podem ser encontrados aqui https://realpython.com/team/
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

class InsertionSort:

    @staticmethod
    def sort(my_list):
        lista = my_list

        # Loop from the second element of the lista until
        # the last element
        for i in range(1, len(lista)):
            # This is the element we want to position in its
            # correct place
            key_item = lista[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the lista) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if `key_item` is smaller than its adjacent values.
            while j >= 0 and lista[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                lista[j + 1] = lista[j]
                j -= 1

            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            lista[j + 1] = key_item

        return lista
