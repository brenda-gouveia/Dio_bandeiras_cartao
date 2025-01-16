# Validador de Cartão de Crédito

Este programa recebe um número de cartão de crédito como entrada e retorna se o número é válido ou não. Além disso, verifica de qual bandeira o cartão faz parte.

Esse trabalho foi feito para o curso sobre Github Copilot da DIO;

## Bandeiras Suportadas

- **Visa**: Bins começam com 4. Comprimento do número do cartão: 13 ou 16 dígitos.
- **MasterCard**: Bins começam com 51-55 ou 2221–2720. Comprimento do número do cartão: 16 dígitos.
- **American Express**: Bins começam com 34 ou 37. Comprimento do número do cartão: 15 dígitos.
- **Discover**: Bins começam com 6011, 622126–622925, 644–649, 65. Comprimento do número do cartão: 16 dígitos.
- **Diners Club**: Bins começam com 300–305, 36, 38 ou 39. Comprimento do número do cartão: 14 ou 16 dígitos.
- **JCB**: Bins começam com 3528-3589. Comprimento do número do cartão: 16 dígitos.
- **HiperCard**: Bins começam com 6062. Comprimento do número do cartão: 16 dígitos.
- **UnionPay**: Bins começam com 62. Comprimento do número do cartão: 16-19 dígitos.
- **enRoute**: Bins começam com 2014 ou 2149. Comprimento do número do cartão: 15 dígitos.
- **Voyager**: Bins começam com 8699. Comprimento do número do cartão: 15 dígitos.
- **Aura**: Bins começam com 50. Comprimento do número do cartão: 16 dígitos.

## Algoritmo de Luhn

O programa utiliza o algoritmo de Luhn para verificar a validade do número do cartão de crédito. O algoritmo de Luhn é um método simples de verificação de soma de verificação usado para validar uma variedade de números de identificação, como números de cartão de crédito.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python instalado.
3. Execute o script `bandeira_cartao.py` e insira o número do cartão de crédito quando solicitado.

## Exemplo de Uso

```python
from bandeira_cartao import validate_credit_card

numero_cartao = "4111111111111111"
resultado = validate_credit_card(numero_cartao)
print(resultado)