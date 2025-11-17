from datetime import date
import pandas as pd
from enviaremail import enviaremail

URL = f"https://docs.google.com/spreadsheets/d/1fTs9YosIm0yqyXoKsnf98xhEzfQgj890TUz3bgq6MhM/gviz/tq?tqx=out:csv&sheet=dadosfatura"

def load_df(url):
    df = pd.read_csv(url, parse_dates=["data_vencimento", "data_lembrete"], dayfirst=True)
    return df


def verificar_e_enviar(df):
    contar_email = 0
    for _, row in df.iterrows():
        if (date.today() >= row["data_lembrete"].date()) and (row["pagou"] == "nao"):
            enviaremail(
                assunto=f'[AutoCobrix] Número da fatura: {row["num_fatura"]}',
                destinatario=row["email"],
                nome=row["nome"],
                data_vencimento=row["data_vencimento"].strftime("%d, %b %Y"),
                num_fatura=row["num_fatura"],
                valor=row["valor"],
            )
            contar_email += 1
    return f"Email enviados: {contar_email}"

df = load_df(URL)

print(verificar_e_enviar(df))
