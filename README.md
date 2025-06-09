📄 Relatório Final
📝 Descrição da Aplicação
A aplicação desenvolvida simula o sistema de controle de medicamentos de uma farmácia. As principais funcionalidades incluem:

Cadastro de medicamentos com campos: ID, nome, quantidade e preço.

Venda de medicamentos, controlando a quantidade disponível.

Exibição do estoque atualizado.

Visualização do histórico de vendas.

Alertas automáticos para confirmação de cadastro e venda.

A interface foi construída com HTML, CSS e JavaScript puro. O foco do sistema é ser funcional e de fácil uso para o operador da farmácia.

🧠 Tabelas de Decisão e Justificativas
Tabela 1 – Cadastro de Medicamentos
Condição	Ação esperada
Todos os campos preenchidos	Cadastrar medicamento e exibir alerta
Campo vazio	Não cadastrar e exibir alerta de erro
Medicamento com ID já existente	Atualizar dados do medicamento

Justificativa: Garante que o cadastro não seja duplicado e os dados estejam completos.

Tabela 2 – Venda de Medicamentos
Condição	Ação esperada
ID válido e quantidade disponível	Realizar venda e atualizar estoque
ID inválido	Exibir alerta de erro
Quantidade maior que o estoque	Bloquear venda e exibir alerta de erro

Justificativa: Garante consistência no estoque e integridade da operação de venda.

✅ Relatório de Testes Automatizados
Ferramenta utilizada: Selenium WebDriver + Pytest
Navegador: Firefox
Testes realizados:
Cadastro de Medicamento

Dados usados: ID = 1, Nome = dipirona, Quantidade = 1, Preço = 3

Resultado esperado: Alerta de sucesso

Resultado obtido: ✅ Alerta "Medicamento dipirona cadastrado com sucesso!"

Venda de Medicamento

Dados usados: ID = 1, Quantidade = 1

Resultado esperado: Alerta de venda

Resultado obtido: ✅ Alerta "Venda de 1 unidades de dipirona realizada com sucesso!"

Visualização de Estoque

Verificação do estoque restante após a venda

Visualização de Vendas

Verificação se a venda aparece no histórico
