# Esse Algoritmo foi retirado do site GeeksFotGeeks, link: https://www.geeksforgeeks.org
# Pagina especifica do Algoritimo: https://www.geeksforgeeks.org/python-program-for-heap-sort/
# Esse Codigo foi contribuido por Mohit Kumra
# Obs. O algoritmo teve modificações mínimas, somente para se tornar uma classe.
# Obs. O algoritmo teve algumas variaveis renomeadas por questões de melhor entendimento do aluno.

class HeapSort:

    @staticmethod
    def heapify(lista, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root

        if left < n and lista[i] < lista[left]:
            largest = left

        # See if right child of root exists and is
        # greater than root

        if right < n and lista[largest] < lista[right]:
            largest = right

        # Change root, if needed

        if largest != i:
            (lista[i], lista[largest]) = (lista[largest], lista[i])  # swap

        # Heapify the root.

            HeapSort.heapify(lista, n, largest)

    # The main function to sort an array of given size
    @staticmethod
    def sort(lista):
        n = len(lista)

        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.

        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(lista, n, i)

        # One by one extract elements

        for i in range(n - 1, 0, -1):
            (lista[i], lista[0]) = (lista[0], lista[i])  # swap
            HeapSort.heapify(lista, i, 0)
