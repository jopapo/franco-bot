# franco-bot
Chatbot para aprender sobre Chatbots. :dizzy_face:

# Descrição
Proposta de trabalho final para a disciplina de chatbots da Pós Graduação em Ciência de Dados da FURB.

Membros: Barbara Sabrina <@barbararovigo>, João Paulo Poffo <@jopapo> e Mauro Schramm <@mauroschramm>

Professor: Cristiano Roberto Franco.

# Requisitos

1. Construir um chatbot em portugues utilizando qualquer uma das tecnologias vistas em sala (rasa, watson, dialog flow, luis...se for usar algo diferente me avisar por email) com pelo menos 10 intenções;
1. O bot deve ser de domínio fechado (menos restaurantes);
   1. O bot deve ter uma UI (aplicativo, web, etc);
   1. O bot deve ter integração com algum tipo de WS (local ou público...pode ser um mock);
   1. O bot deve armazenar as conversas do usuário de alguma forma para usar no item 3;
   1. Explicar arquitetura em um doc;
1. Deverá ser criado um jupyter contendo pelo menos 3 indicadores ou métricas de conversas com o chatbot demonstradas através de gráficos;

# Arquitetura base

Iniciamos um estudo com o [Rasa](https://rasa.com/docs/). Porém, subir a infra do [RasaX](https://rasa.com/docs/rasa-x/) para entregar as UIs de edição e do Bot e histórico de conversações exigia um osquestrador e no mínimo 10 serviços rodando (Nginx, Postgres, Redit, Rabbit, Duckling, Rasa, etc.). Apesar de conseguirmos subir e simular algumas regras, este fator se tornou determinante para desistirmos do modelo e testarmos uma alternativa para entrega do trabalho.

Então, optamos por uma abordagem usando [Watson da IBM](https://www.ibm.com/br-pt/watson) como motor e assistente de modelagem de Chatbots.

## Componentes arquiteturais

* [IBM Watson](https://cloud.ibm.com/developer/watson/): para o gerenciador do ChatBot, com histórico de conversas, assistente de contrução e todos os recursos de IA necessários para um assistente virtual;
* [IBM Cloud Functions](https://cloud.ibm.com/functions/): para o WebService;
   * : [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): Biblioteca do python usada como tecnologia de WebScraping.
* [Gifyu](https://gifyu.com/): Como CDN para as imagens de apoio do Chatbot.

# Entregáveis

* [Link para o chatbot](https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=us-south&integrationID=df8505c9-3abd-4505-8898-eaf4aced5775&serviceInstanceID=702cc5ee-81a9-4536-9e63-4c05c7a35ab0);
* PDF do fluxo de dialogo;
* Fonte do projeto ([webservice backend](functions.py) e json do watson);
* Jupyter notebook com os [indicadores/métricas](#gráficos-extraídos-pelo-jupyter) no github;

Como a persistência é do próprio Watson, criamos um indicador no jupyter usando o histórico de conversas.

## Gráficos extraídos pelo jupyter
### Flow FrancoBot

![image](https://user-images.githubusercontent.com/63163264/119211169-e7aa1700-ba86-11eb-8244-61b84ae9c807.png)

### Gráficos

![image](https://user-images.githubusercontent.com/63163264/119211194-09a39980-ba87-11eb-953d-ee861db10d26.png)   ![image](https://user-images.githubusercontent.com/63163264/119211199-14f6c500-ba87-11eb-930e-41c1c7d3ced4.png)

### Nuvem de Palavras de Textos procurados no FrancoBot

![image](https://user-images.githubusercontent.com/63163264/119211215-322b9380-ba87-11eb-9724-df20a4a2ab1e.png)
