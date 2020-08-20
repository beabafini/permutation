# chamada inicial para começar o processamento
def allPermutations(string, outputLength):
    return permutations(list(string), '', outputLength)

# chamada principal da função para separação e junção das possibilidades
def permutations(charArray, permutation, outputLength):
    if len(permutation) < outputLength:
        for i in range(0, len(charArray)): #percorre a lista de caracteres para formular as combinações
            tempList = list(charArray)
            tempList.pop(i) #retira o caractere em questão para não repetí-lo
            newString = permutation + charArray[i] #forma uma nova combinação
            permutations(tempList, newString, outputLength) #faz uma chamada recursiva para continuar o processo com outras combinações
    elif permutation not in permuts:
        permuts.append(permutation) #adiciona a combinação na lista caso ela ainda não exista
    
    return permuts

def toString(permuts):
    return '\n'.join(permuts) #converte os caracteres da lista em strings

word = input("Enter a word: ")

result = []

for i in range(1, len(list(word))+1): #percorre os tamanhos da string para obter todos os tamanhos de combinações
    permuts = []
    permuts = allPermutations(word, i)
    permuts.sort()
    print(toString(permuts))
