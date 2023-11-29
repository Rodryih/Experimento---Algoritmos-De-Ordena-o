# Esse Algoritmo foi retirado do site Real Python, link: https://realpython.com
# Pagina especifica do Algoritimo: https://realpython.com/sorting-algorithms-python/
# Há uma grande equipe por tras desse site/plataforma que podem ser encontrados aqui https://realpython.com/team/
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

class MergeSort:

    @staticmethod
    def sort(lista):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(lista) < 2:
            return lista

        midpoint = len(lista) // 2

        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result
        return MergeSort.merge(
            left=MergeSort.sort(lista[:midpoint]),
            right=MergeSort.sort(lista[midpoint:]))

    @staticmethod
    def merge(left, right):
        # If the first array is empty, then nothing needs
        # to be merged, and you can return the second array as the result
        if len(left) == 0:
            return right

        # If the second array is empty, then nothing needs
        # to be merged, and you can return the first array as the result
        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0

        # Now go through both arrays until all the elements
        # make it into the resultant array
        while len(result) < len(left) + len(right):
            # The elements need to be sorted to add them to the
            # resultant array, so you need to decide whether to get
            # the next element from the first or the second array
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            # If you reach the end of either array, then you can
            # add the remaining elements from the other array to
            # the result and break the loop
            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break

        return result
