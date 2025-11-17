import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

load_dotenv() #O login do email utilizado fica armazenado em um arquivo .env
remetente = os.getenv("email")
senha = os.getenv("senha")

def enviaremail(assunto, destinatario, nome, data_vencimento, num_fatura, valor):
    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = formataddr(("AutoCobrix Ltda.", remetente))  #Nome fictício
    msg["To"] = destinatario

    msg.set_content(
        f"""\
    <html>
    <body>
        <h1>Olá {nome},</h1>
        <p>
            Tudo bem? Estou entrando em contato para lembrá-lo sobre o pagamento
            de <strong>R${valor}</strong> referente à fatura <strong>{num_fatura}</strong>.
        </p>
        <p>
            A data de vencimento é <strong>{data_vencimento}</strong>. 
            Caso já tenha realizado o pagamento, por favor desconsidere esta mensagem.
        </p>
        <p>
            Se possível, me confirme quando estiver tudo certo por aí. 
            Qualquer dúvida, fico à disposição.
        </p>
    </body>
</html>
    """,
        subtype="html",
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
