# Define a expressão lógica a ser calculada
expressao = "A^~BvCvA^DvC"
# Transforma a expressão em uma lista para manipulação mais fácil
expressao = [i for i in expressao]
# Define os símbolos lógicos e as variáveis
simbolos = ["~","^","v","->","<>"]
variables = ["A","B","C","D"]

# Loop para que o usuário insira os valores das variáveis da proposição
for var in variables:
    if var in expressao:
        # Solicita ao usuário o valor da variável e converte para booleano
        value = bool(int(input(f"Valor da variável {var}: ")))
        # Substitui todas as ocorrências da variável na expressão pelo valor informado
        for i in range(len(expressao)):
            if expressao[i] == var:
                expressao[i] = value

# Define a função para calcular o resultado de uma operação lógica
def result(a, sym, b):
    if sym == "~":
        return not b
    elif sym == "^":
        return a and b
    elif sym == "v":
        return a or b
    elif sym == "<>":
        if a == b:
            return True
        return False
    elif sym == "->":
        if a and not b:
            return False
        return True

# Define a função para resolver a expressão lógica
def solve(exp):
    # Itera sobre os símbolos lógicos presentes na expressão
    for sym in simbolos:
        if sym in exp:
            # Encontra o índice do símbolo
            i = exp.index(sym)
            if exp[i] == sym:
                # Obtém os operandos e o símbolo
                a, b, sym = exp[i-1], exp[i+1], exp[i]
                # Calcula o resultado da operação
                res = result(a, sym, b)
                # Atualiza a expressão com o resultado da operação
                if sym == "~":
                    exp[i] = res
                    exp.pop(i+1)
                else:
                    exp[i-1] = res
                    exp.pop(i+1)
                    exp.pop(i)
                # Verifica se a expressão foi reduzida a um único valor
                if len(exp) == 1:
                    return exp[0]
                # Chama recursivamente a função para resolver a expressão restante
                return solve(exp)

# Define a função para resolver expressões com parênteses
def full_solve(exp):
    # Se não houver parênteses na expressão, resolve-a diretamente
    if "(" not in exp:
        return solve(exp)
    
    # Se houver parênteses na expressão
    inside_exp = []
    for i in range(len(exp)):
        if exp[i] == ")":
            # Encontra a expressão dentro dos parênteses
            removal_size = len(inside_exp) + 2
            break
        inside_exp.append(exp[i])
        if exp[i] == "(":
            remove_index = i
            inside_exp = []
    # Resolve a expressão dentro dos parênteses
    exp[remove_index-1] = solve(inside_exp)
    # Remove a expressão dentro dos parênteses e os próprios parênteses da expressão original
    for i in range(removal_size):
        exp.pop(remove_index)
    # Verifica se a expressão foi reduzida a um único valor
    if len(exp) == 1:
        return exp[0]
    # Chama recursivamente a função para resolver a expressão restante
    return full_solve(exp)

# Imprime o resultado da expressão lógica
print(full_solve(expressao))