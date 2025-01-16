import re

"""
Construa um programa que recebe uma entrada números de cartão de crédito e retorna se o número é válido ou não. Também verifique de qual bandeira faz parte.

Visa : Bins começam com 4. Comprimento do número do cartão: 13 ou 16 dígitos.
MasterCard : Bins começam com 51-55 ou 2221–2720. Comprimento do número do cartão: 16 dígitos.
American Express : Bins começam com 34 ou 37. Comprimento do número do cartão: 15 dígitos.
Discover : Bins começam com 6011, 622126–622925, 644–649, 65. Comprimento do número do cartão: 16 dígitos.
Diners Club : Bins começam com 300–305, 36, 38 ou 39. Comprimento do número do cartão: 14 ou 16 dígitos.
JCB : Bins começam com 3528-3589. Comprimento do número do cartão: 16 dígitos.
HiperCard : Bins começam com 6062. Comprimento do número do cartão: 16 dígitos.
UnionPay : Bins começam com 62. Comprimento do número do cartão: 16-19 dígitos.
enRoute : Bins começam com 2014 ou 2149. Comprimento do número do cartão: 15 dígitos.
Voyager : Bins começam com 8699. Comprimento do número do cartão: 15 dígitos.
Aura : Bins começam com 50. Comprimento do número do cartão: 16 dígitos.
"""
def luhn_algorithm(card_number):
    """
    Implementa o algoritmo de Luhn para verificar a validade de um número de cartão de crédito.

    Parâmetros:
    card_number (str): O número do cartão de crédito a ser verificado.

    Retorna:
    bool: Retorna True se o número do cartão for válido de acordo com o algoritmo de Luhn, caso contrário, False.
    """
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def validate_credit_card(card_number):
    """
    Valida um número de cartão de crédito verificando seu formato e aplicando o algoritmo de Luhn.

    Parâmetros:
    card_number (str): O número do cartão de crédito a ser validado.

    Retorna:
    str: Retorna "Invalid card number" se o número do cartão for inválido, caso contrário, retorna uma string vazia.
    """
    card_number = card_number.replace(" ", "")
    
    if not card_number.isdigit():
        return "Invalid card number"
    
    if not luhn_algorithm(card_number):
        return "Invalid card number"
    
    card_patterns = {
        "Visa": r"^4\d{12}(\d{3})?$",
        "MasterCard": r"^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$",
        "American Express": r"^3[47]\d{13}$",
        "Discover": r"^6(011\d{12}|22(1[26-9]|[2-8]\d|9[01])\d{10}|4[4-9]\d{13}|5\d{14})$",
        "Diners Club": r"^3(0[0-5]\d{11}|[68]\d{12}|9\d{12})$",
        "JCB": r"^35(2[89]|[3-8]\d)\d{12}$",
        "HiperCard": r"^6062\d{12}$",
        "UnionPay": r"^62\d{14,17}$",
        "enRoute": r"^(2014|2149)\d{11}$",
        "Voyager": r"^8699\d{11}$",
        "Aura": r"^50\d{14}$"
    }
    
    for card_type, pattern in card_patterns.items():
        if re.match(pattern, card_number):
            return f"Valid card number ({card_type})"
    
    return "Invalid card number"

if __name__ == "__main__":
    # Example usage
    card_number = "5065 3535 1314 1014"
    print(validate_credit_card(card_number))