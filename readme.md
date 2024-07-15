# Repositório: Integração Google Sheets e MySQL
Este repositório está em **desenvolvimento**. O objetivo é utilizar a API do Google para acessar uma planilha de Vendedores no Google Drive, tratar os dados e inseri-los em um banco de dados MySQL.

# Modelagem do Banco de Dados
O banco de dados contém três tabelas:

Vendedores:

- idVendedores (chave primária): Identificador único para cada vendedor.
- Nome (texto): Nome do vendedor.
- Email (texto): Endereço de email do vendedor.
- CPF (texto): Número do CPF do vendedor.
- data_nascimento (data): Data de nascimento do vendedor.

Produtos:

- Produto_idProduto (chave primária): Identificador único para cada produto.
- nome_produto (texto): Nome do produto.
- Quantidade (inteiro): Quantidade em estoque do produto.
- Unidade_Local (texto): Unidade de medida do produto (ex: unidade, kg, litro).
- Valor unitário (moeda): Preço unitário do produto.

Venda:

- id_venda (chave primária): Identificador único para cada venda.
- id_vendedor (chave estrangeira): Referência ao idVendedores na tabela "Vendedores".
- id_produto (chave estrangeira): Referência ao Produto_idProduto na tabela "Produtos".
- quantidade_vendida (inteiro): Quantidade do produto vendida naquela venda.
- data_venda (data): Data da venda.

### Explicação do Relacionamento N

Um vendedor pode vender vários produtos: Um vendedor pode estar associado a múltiplas vendas, cada uma com diferentes produtos.
Um produto pode ser vendido por vários vendedores: Um produto pode ser vendido em múltiplas transações realizadas por diferentes vendedores.
Esta relação muitos-para-muitos (N) é gerenciada através da tabela "Venda", que conecta vendedores e produtos com informações adicionais sobre cada transação.

