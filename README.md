# Automação de Cobrança por E-mail Integrada ao Google Sheets

Este sistema automatiza o processo de cobrança, lendo dados de uma planilha do **Google Sheets**, identificando pagamentos pendentes e disparando **e-mails personalizados** para os destinatários. A solução elimina tarefas repetitivas, tornando o fluxo de cobrança mais **simples, rápido e organizado**.

-----

## Funcionalidades

  * Carrega automaticamente os dados de uma planilha Google Sheets, utilizando o formato CSV para acesso rápido.
  * Converte datas e aplica lógica para identificar com precisão quais cobranças estão pendentes e prontas para o envio do lembrete.
  * Envia e-mails personalizados em formato HTML via protocolo SMTP.
  * Realiza a contagem dos e-mails disparados para fins de *logging* e auditoria.
  * Estrutura simples, limpa e modular, fácil de adaptar a diferentes necessidades.
  * Permite a customização completa do corpo e do *layout* visual do e-mail.

-----

## Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes ferramentas e bibliotecas:

  * **Python:** Linguagem principal de desenvolvimento.
  * **Pandas:** Utilizado para manipulação eficiente dos dados carregados do CSV da planilha.
  * **Google Sheets:** Serve como a base de dados central do sistema.

-----

## Estrutura do Projeto

Abaixo está a organização principal dos arquivos do repositório:

```
automacao_cobranca_email/
├── main.py             # Código principal: responsável por ler a planilha e disparar os e-mails
├── enviaremail.py      # Módulo com a função dedicada ao envio via SMTP
└── .env                # Arquivo de configuração que armazena credenciais (e-mail e senha)
```

-----

## Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1\. Clonagem e Acesso

```bash
git clone https://github.com/MtsQueiroz/automacao_cobranca_email.git
cd automacao_cobranca_email
```

### 2\. Instalação de Dependências

Instale as bibliotecas Python necessárias (`pandas` para dados e `python-dotenv` para variáveis de ambiente):

```bash
pip install pandas python-dotenv
```

### 3\. Configuração do Arquivo `.env`

Crie um arquivo chamado **`.env`** na raiz do projeto com suas credenciais de e-mail:

```bash
EMAIL=seuemail@gmail.com
PASSWORD=sua_senha_de_app
```

> **Importante:** Para serviços como o **Gmail**, é obrigatório utilizar uma **Senha de App** (Gerada nas configurações de segurança da sua conta), e não a senha principal da sua conta.

-----

## Configuração da Planilha Google Sheets


### 1\. Estrutura Mínima da Planilha

A sua página deve conter estas colunas:

| Coluna | Descrição | Formato Recomendado |
| :--- | :--- | :--- |
| **nome** | Nome do cliente/destinatário | Texto |
| **email** | E-mail para envio do lembrete | E-mail |
| **valor** | Valor total da fatura | Número |
| **data\_vencimento** | Data limite para o pagamento | Data (`DD/MM/AAAA`) |
| **data\_lembrete** | Data para o disparo do lembrete | Data (`DD/MM/AAAA`) |
| **pagou** | Status do pagamento | **`sim`** ou **`nao`** |
| **num\_fatura** | Número ou código de identificação da fatura | Texto/Número |

### 2\. Lógica de Funcionamento

O arquivo `main.py` executa a seguinte lógica para determinar o envio:

1.  Baixa o conteúdo da planilha em formato CSV.
2.  Verifica as condições de envio linha por linha, utilizando o seguinte critério:
    ```python
    date.today() >= data_lembrete and pagou == "nao"
    ```
3.  Para cada linha que atende a essas condições um e-mail personalizado é enviado.

### Observação

> A **página** dentro do arquivo do Google Sheets **deve ter o mesmo nome** que será utilizado na **URL do CSV**.
>
> **Exemplo:** Se a URL de acesso remoto aponta para a página chamada `dados_faturas`, a página na planilha deve ser nomeada **`dados_faturas`**.

-----
