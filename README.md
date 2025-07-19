# Conversor de Moedas

Um conversor de moedas simples em Python que utiliza a API gratuita ExchangeRate-API para obter taxas de câmbio em tempo real.

## Requisitos
- Python 3.x
- requests

## Instalação

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o programa:
   ```bash
   python conversor_moedas.py
   ```

## Como usar

1. Informe a moeda de origem (ex: EUR).
2. Informe a moeda de destino (ex: USD).
3. Informe o valor a converter.
4. O valor convertido será exibido na tela.

## Tratamento de erros
- O programa informa se a moeda é inválida ou se houver problemas de conexão com a API.

## Opcional
Para uma interface gráfica, peça para adicionar suporte ao Tkinter ou Streamlit. 