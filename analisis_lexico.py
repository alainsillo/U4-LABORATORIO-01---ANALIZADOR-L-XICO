import re

class Token:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1

        # Especificación de tokens (el orden importa)
        self.patrones = [
            ('KEYWORD', r'\b(if|else|while|for|return|int|float|char|void)\b'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('NUMBER', r'\d+(\.\d+)?'),
            ('STRING', r'\".*?\"'),
            ('OPERATOR', r'==|!=|<=|>=|[+\-*/=<>]'),
            ('DELIMITER', r'[;,\(\)\{\}]'),
            ('WHITESPACE', r'[ \t]+'),
            ('NEWLINE', r'\n'),
            ('ERROR', r'.')
        ]

    def tokenizar(self):
        tokens = []
        while self.pos < len(self.codigo):
            encontrado = False
            for tipo, patron in self.patrones:
                regex = re.compile(patron)
                match = regex.match(self.codigo, self.pos)
                if match:
                    valor = match.group(0)
                    if tipo == 'NEWLINE':
                        self.linea += 1
                    elif tipo not in ['WHITESPACE', 'NEWLINE']:
                        tokens.append(Token(tipo, valor, self.linea))
                    self.pos = match.end()
                    encontrado = True
                    break
            if not encontrado:
                self.pos += 1
        return tokens


# ================================
#   PRUEBAS DE FUNCIONAMIENTO
# ================================
ejemplos = [
    "int x = 10;",
    "float total = 3.5 + 4.2;",
    "if (x > 5) { x = x + 1; }",
    """int a = 1;
int b = 2;
int c = a + b;"""
]

for i, codigo in enumerate(ejemplos, 1):
    print("=" * 50)
    print(f"EJEMPLO {i}")
    print("=" * 50)
    lexer = AnalizadorLexico(codigo)
    tokens = lexer.tokenizar()
    for token in tokens:
        print(f"{token.tipo:<12} → {token.valor}")