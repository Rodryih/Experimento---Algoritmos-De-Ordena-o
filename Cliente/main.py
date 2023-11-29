import time
import Arquivos

from Algoritmos.Bubble import BubbleSort
from Algoritmos.Insertion import InsertionSort
from Algoritmos.Selection import SelectionSort
from Algoritmos.Merge import MergeSort
from Algoritmos.Quick import QuickSort
from Algoritmos.Shell import ShellSort
from Algoritmos.Heap import HeapSort


def menu():
    print("\n================MENU================")
    print("       1. Ordenar 100 Mil Nomes")
    print("       2. Ordenar 250 Mil Nomes")
    print("       3. Ordenar 500 Mil Nomes")
    print("       4. SAIR")
    print("====================================\n")


file = Arquivos.Arquivos
nomes = []

# MAIN
while True:
    menu()

    op = int(input("Escolha uma opçao: \n"))

    if op == 1:

        nomes = file.cemk()
        ini = time.time() * 1000
        SelectionSort.sort(nomes, 100000)
        fim = time.time() * 1000
        print("Tempo de Ordenacao em Milissegundos:\n\n")
        print("Selection Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.cemk()
        ini = time.time() * 1000
        InsertionSort.sort(nomes)
        fim = time.time() * 1000
        print("Insertion Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.cemk()
        ini = time.time() * 1000
        BubbleSort.sort(nomes)
        fim = time.time() * 1000
        print("Bubble Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.cemk()
        ini = time.time() * 1000
        ShellSort.sort(nomes, 100000)
        fim = time.time() * 1000
        print("Shell Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.cemk()
        ini = time.time() * 1000
        HeapSort.sort(nomes)
        fim = time.time() * 1000
        print("Heap Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.cemk()
        ini = time.time() * 1000
        MergeSort.sort(nomes)
        fim = time.time() * 1000
        print("Merge Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.cemk()
        ini = time.time() * 1000
        QuickSort.sort(nomes)
        fim = time.time() * 1000
        print("Quick Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

    elif op == 2:

        nomes = file.duzentosk()
        ini = time.time() * 1000
        SelectionSort.sort(nomes, 100000)
        fim = time.time() * 1000
        print("Tempo de Ordenacao em Milissegundos:\n\n")
        print("Selection Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.duzentosk()
        ini = time.time() * 1000
        InsertionSort.sort(nomes)
        fim = time.time() * 1000
        print("Insertion Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.duzentosk()
        ini = time.time() * 1000
        BubbleSort.sort(nomes)
        fim = time.time() * 1000
        print("Bubble Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.duzentosk()
        ini = time.time() * 1000
        ShellSort.sort(nomes, 100000)
        fim = time.time() * 1000
        print("Shell Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.duzentosk()
        ini = time.time() * 1000
        HeapSort.sort(nomes)
        fim = time.time() * 1000
        print("Heap Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.duzentosk()
        ini = time.time() * 1000
        MergeSort.sort(nomes)
        fim = time.time() * 1000
        print("Merge Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.duzentosk()
        ini = time.time() * 1000
        QuickSort.sort(nomes)
        fim = time.time() * 1000
        print("Quick Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

    elif op == 3:

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        SelectionSort.sort(nomes, 100000)
        fim = time.time() * 1000
        print("Tempo de Ordenacao em Milissegundos:\n\n")
        print("Selection Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        InsertionSort.sort(nomes)
        fim = time.time() * 1000
        print("Insertion Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        BubbleSort.sort(nomes)
        fim = time.time() * 1000
        print("Bubble Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        ShellSort.sort(nomes, 100000)
        fim = time.time() * 1000
        print("Shell Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        HeapSort.sort(nomes)
        fim = time.time() * 1000
        print("Heap Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        MergeSort.sort(nomes)
        fim = time.time() * 1000
        print("Merge Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

        nomes = file.quinhetosk()
        ini = time.time() * 1000
        QuickSort.sort(nomes)
        fim = time.time() * 1000
        print("Quick Sort:\n")
        print(f"{fim - ini} Milissegundos\n\n")

    elif op == 4:
        break
    else:
        print("\n>>> Opçao invalida, consute o menu para ver as opçoes validas.\n")
