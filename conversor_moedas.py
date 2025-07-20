import requests

def obter_taxa_cambio(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem.upper()}"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        taxas = dados.get('rates', {})
        if moeda_destino.upper() not in taxas:
            raise ValueError(f"Moeda de destino '{moeda_destino}' inválida.")
        return taxas[moeda_destino.upper()]
    except requests.RequestException as e:
        raise ConnectionError(f"Erro de conexão: {e}")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Erro inesperado: {e}")

def main():
    print("=== Conversor de Moedas ===")
    moeda_origem = input("Moeda de origem (ex: EUR): ").strip()
    moeda_destino = input("Moeda de destino (ex: USD): ").strip()
    try:
        valor = float(input("Valor a converter: ").replace(",", "."))
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um número.")
        return
    try:
        taxa = obter_taxa_cambio(moeda_origem, moeda_destino)
        valor_convertido = valor * taxa
        print(f"\n{valor:.2f} {moeda_origem.upper()} = {valor_convertido:.2f} {moeda_destino.upper()}")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except ConnectionError as ce:
        print(f"Erro: {ce}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main() 