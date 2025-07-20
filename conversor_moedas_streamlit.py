import streamlit as st
import requests

def obter_lista_moedas(base="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        return sorted(list(dados.get('rates', {}).keys()))
    except Exception:
        # fallback para algumas moedas comuns
        return ["USD", "EUR", "BRL", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "ARS"]

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
    st.title("Conversor de Moedas 💱")
    st.write("Converta valores entre diferentes moedas usando taxas em tempo real.")

    moedas = obter_lista_moedas()
    moeda_origem = st.selectbox("Moeda de origem", moedas, index=moedas.index("USD") if "USD" in moedas else 0)
    moeda_destino = st.selectbox("Moeda de destino", moedas, index=moedas.index("BRL") if "BRL" in moedas else 1)
    valor = st.text_input("Valor a converter", value="1.00")

    if st.button("Converter"):
        try:
            valor_float = float(valor.replace(",", "."))
            taxa = obter_taxa_cambio(moeda_origem, moeda_destino)
            valor_convertido = valor_float * taxa
            st.success(f"{valor_float:.2f} {moeda_origem.upper()} = {valor_convertido:.2f} {moeda_destino.upper()}")
        except ValueError as ve:
            st.error(f"Erro: {ve}")
        except ConnectionError as ce:
            st.error(f"Erro: {ce}")
        except Exception as e:
            st.error(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main() 