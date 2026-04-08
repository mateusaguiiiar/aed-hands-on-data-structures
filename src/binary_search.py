from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return -1
