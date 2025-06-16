# Sistema de Eventos em Python

Este repositório contém uma implementação inicial de um sistema para gerenciamento de eventos escrito em Python. A aplicação ainda está em fase de desenvolvimento, contendo diferentes módulos responsáveis por lidar com usuários, eventos, ingressos e transações.

## Estrutura do projeto

- **evento/** – classes base para eventos, além das versões *online* e *presencial*;
- **ingresso/** – define a classe `Ingresso`, responsável pelo controle de vendas;
- **pessoa/** – módulo de usuários contendo `PessoaBase` e subclasses como produtores e vendedores;
- **transacao/** – registra as transações de compra de ingressos;
- **sistemaVendasBeto.py** – implementação de um sistema em linha de comando para testes;
- **DIAGRAMAS/** – diagramas `.drawio` do planejamento do projeto.

## Requisitos

- Python 3.10 ou superior.
- Não há dependências externas listadas no projeto no momento.

## Observação

Este projeto faz parte de um trabalho acadêmico e várias partes do código ainda estão em desenvolvimento.

## Licença

Este repositório não possui uma licença específica e é fornecido apenas para fins de estudo.