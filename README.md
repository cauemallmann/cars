# 🚗 Sistema de Gestão de Revenda de Automóveis

## 📖 Descrição
Este projeto é um sistema SaaS desenvolvido em Django para a gestão de revendas de automóveis. Ele permite que usuários finais e administradores gerenciem carros, vendas e a área financeira de forma eficiente. O sistema foi projetado para ser intuitivo e fácil de usar, com foco em automação e gerenciamento de processos.

## 🌟 Funcionalidades Principais

### 1. **Cadastro de Carros**
- Permite que os usuários cadastrarem novos carros para venda.
- Inclui campos detalhados como marca, modelo, ano, fotos e informações de preço.
- Os carros cadastrados ficam em status "pendente" até aprovação pelo administrador.

### 2. **Envio de Propostas**
- Os usuários podem enviar propostas de compra para carros disponíveis.
- Sistema de notificação que informa ao administrador sobre novas propostas recebidas.

### 3. **Gerenciamento de Vendas**
- Vendedores podem agendar avaliações de carros.
- Sistema de confirmação de vendas, onde os vendedores podem marcar as vendas como concluídas.
- Registro histórico de todas as vendas realizadas.

### 4. **Agendamentos**
- Permite que usuários e vendedores agendem avaliações de carros de forma prática.
- Gestão eficiente de horários disponíveis e acompanhamento dos agendamentos.

### 5. **Área Financeira**
- Controle de fluxo de caixa, permitindo que administradores monitorem entradas e saídas.
- Relatórios financeiros detalhados, com métricas de desempenho da revenda.
- Gerenciamento de contas de cada revenda, com acesso para administradores e usuários.

### 6. **Administração de Usuários**
- Múltiplos níveis de acesso para administradores e vendedores.
- Permite ao administrador gerenciar e aprovar usuários na plataforma.
- Recursos para desativar usuários sem exclusão permanente.

### 7. **Sistema de Aprovação de Cadastro**
- O administrador pode revisar e aprovar ou rejeitar novos carros cadastrados.
- Notificações por e-mail para os usuários sobre o status de aprovação.

### 8. **Desativação de Carros**
- Em vez de excluir, o sistema permite a desativação de carros, alterando o status `active` para `False`.
- Mantém o histórico dos carros, mesmo após desativação, para fins de consulta e relatórios.

## 🔮 Futuras Funcionalidades
- **Cotação de Juros Automatizada**: Implementação de um sistema que calcula e apresenta automaticamente as taxas de juros para financiamentos de veículos.
- **Exibição de Comissões**: Sistema que calcula e exibe as comissões de vendas para vendedores, proporcionando maior transparência e motivação.
- **Integração com Sistemas de Pagamento**: Facilitar o processo de pagamento para vendas realizadas, com opções para diferentes métodos de pagamento.
- **Relatórios Avançados**: Criação de relatórios detalhados sobre o desempenho das vendas, preferências dos clientes e tendências de mercado.

## 👥 Contribuições
Sinta-se à vontade para contribuir! Sugestões, relatórios de bugs e pull requests são sempre bem-vindos.

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
