# franco-bot
Chatbot para aprender sobre Chatbots. :dizzy_face:

# Descrição
Proposta de trabalho final para a disciplina de chatbots da Pós Graduação em Ciência de Dados da FURB.

Membros: Mauro Schramm <@mauroschramm> e Barbara Sabrina <@barbararovigo>.

Professor: Cristiano Roberto Franco.

# Arquitetura base

A plataforma escolhida para estudo e trabalho foi o [Rasa](https://rasa.com/docs/) e o [RasaX](https://rasa.com/docs/rasa-x/) para entregar as UIs de desenho + bot, bem como histórico das conversações.

Encontramos um exemplo em https://github.com/RasaHQ/financial-demo que cria o cluster do rasa com todos os seus componentes e, de quebra, ajuda com alguns exemplos desse domínio financeiro.

Visão geral sobre os arquivos:
- `/rasa-infra` - informações gerais para executar a plataforma;
- `/rasa-infra/docker-compose.yml` - informações para subida dos containers localmente - explicado mais pra frente o passo a passo;
> As informações a seguir podem ser alteradas por dentro da UI do RasaX:
- `/data` - dados para o RasaX;
- `/data/nlu` - NLU - Natural Language Undestanding. Dados para treinamento do Rasa X;
- `/data/rules` - regras utilizadas no treinamento;
- `/data/stories` - estórias utilizadas como simulações de conversação para treinamento;
- `/config.yml` - configurações do RasaX;
- `/domain.yml` - informações do domínio do RasaX.

O docker-compose sobre os seguintes componentes para rodar o RasaX:
1. Rasa Server - Nginx
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

Para chegar até aqui foram feitas várias configurações e ajustes conforme orientações do [tutorial ro Rasa X](https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose). O passo a passo simplificado segue:

1. _(só na 1a vez)_ Pré-requisitos:
    - [Docker Desktop For Windows](https://www.docker.com/products/docker-desktop);
    - Python 3 acessível via linha de comando / terminal.

1. Comandos para subir a infra (pode demorar para baixar e usar uma quantidade razoável de memória :-P):

    `$ docker-compose up`
    - Usando seu terminal de preferência, entre na pasta rasa-infra deste projeto e digite a linha de comando acima. 
        Isso irá baixar todas as imagens necessários para subir os 10 containers no pacote para rodar o RasaX.
        - Info 1: Usando o argumento -d roda tudo em segundo plano;
        - Info 2: Ctrl+C no terminal interrompe todas as instâncias;
    
1. _(só na 1a vez)_ No terminal, na pasta rasa-infra, execute o comando para definir a senha:

    `$ python rasa_x_commands.py create --update admin me 12345`

1. Após tudo no ar, acessar http://localhost:80 no navegador;
    - Se a porta 80 estiver ocupada, é possível alterar a porta exposta no #rasa-infra/docker-compose.yml.

1. A senha de acesso é `12345`;

1. Conectar à conta git (botão no canto esquerdo inferior) seguindo as orientações da tela.
    1. Utilizar a conta `git@github.com:jopapo/franco-bot.git`;
    1. Alterar a target branch para `main`;
    1. Adicionar a chave SSH listada na conta do seu usuário no github;
    1. Clicar em verificar;
        > Em caso de erro, é possível ver detalhes do erro na console dos containers.
    1. Confirmar.