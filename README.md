# franco-bot
Chatbot para aprender sobre Chatbots.

# Descrição
Proposta de trabalho final para a disciplina de chatbots da Pós Graduação em Ciência de Dados da FURB.

Membros: @mauroschramm e Barbara Sabrina.

Professor: Cristiano Roberto Franco.

# Arquitetura base

A plataforma escolhida para estudo e trabalho foi o [Rasa](https://rasa.com/docs/) e o [RasaX](https://rasa.com/docs/rasa-x/) para entregar as UIs de desenho + bot, bem como histórico das conversasões.

Encontramos um exemplo em https://github.com/RasaHQ/financial-demo que cria o cluster do rasa com todos os seus componentes e, de quebra, ajuda com alguns exemplos desse domínio financeiro.

Visão geral sobre os arquivos:
- `/rasa-infra` - informações gerais para executar a plataforma;
- `/rasa-infra/docker-compose.yml` - informações para subida dos containers localmente - explicado mais pra frente o passo a passo;
- `/rasa-data` - dados para rodar.

Boa parte da configuração é possível pela UI do RasaX.

O docker-compose sobre 10 componentes para rodar o RasaX:
1. Nginx
1. Rasa Worker
1. Rasa Production
1. Rasa X
1. Rasa App
1. Rasa Db Migration
1. Rasa Db - PostGres
1. Rasa Cache - Redis
1. Rasa Broker - RabbitMQ
1. Rasa Text Extractor - Duckling

# Executando

1. Pré-requisitos:
    - (Docker Desktop For Windows)[https://www.docker.com/products/docker-desktop];

1. Comandos para subir a infra (pode usar um "pouquinho" de memória :-P):
    - Usando seu terminal de preferência, entre na pasta rasa-infra deste projeto e digite `docker-compose up`. 
        Isso irá baixar todas as imagens necessários para subir os 10 containers no pacote para rodar o RasaX.
        > Info 1: Usando o argumento -d roda tudo em segundo plano;
        > Info 2: Ctrl+C no terminal interrompe todas as instâncias;
    
1. Após tudo no ar, acessar http://localhost:80 no navegador;
    > Se a porta 80 estiver ocupada, é possível alterar a porta exposta no #rasa-infra/docker-compose.yml.

1. A senha de acesso é `12345`;

1. Conectar à conta git...