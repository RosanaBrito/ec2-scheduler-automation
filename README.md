# EC2 Instance Scheduler Automation

Este repositório contém dois scripts AWS Lambda em Python que automatizam o processo de ligar e desligar uma instância EC2 com base em regras de agendamento (cron) definidas no Amazon EventBridge.

## Estrutura

- `start_instance.py`: Script Lambda para iniciar a instância com tag `Servidor = ChipinventorDevel`
- `stop_instance.py`: Script Lambda para parar a mesma instância
- `policies/`: Diretório contendo exemplos de políticas IAM para execução segura das funções
- `eventbridge-cron-expressions.txt`: Exemplos de expressões cron para configurar os agendamentos no EventBridge

## Pré-requisitos

- Permissões no IAM para criar funções Lambda, regras EventBridge e políticas IAM
- A instância EC2 deve ter a tag `Servidor = ChipinventorDevel`
- A função Lambda deve ter as permissões definidas nas políticas

## Fluxo de Funcionamento

1. As funções Lambda fazem `describe_instances` com filtro pela tag `Servidor`
2. Se a instância estiver parada (no caso do `start`) ou em execução (no caso do `stop`), a ação `start_instances` ou `stop_instances` é executada.
3. Os eventos são disparados automaticamente pelo EventBridge, conforme a cron expression definida.

## Segurança

Evite usar `"Resource": "*"` em produção. Prefira restringir o `Resource` ao ARN exato da instância EC2 quando possível.

