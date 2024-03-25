# Resultado - Desafio CoorLab

O objetivo deste desafio é construir uma aplicação sólida e funcional que atenda aos objetivos do usuário, que são realizar a consulta da viagem mais rápida/confortável e a viagem mais econômica para uma determinada cidade. 

## Tecnologias Utilizadas

#### Backend

- Python
- Flask 

O <Strong>Flask</Strong> foi utilizado no backend, já que o projeto se trata de uma aplicação simples, com poucas rotas e sem muitos requisitos, como autenticação e sessões de usuários. O microframework Flask atendeu perfeitamente a todas as necessidades deste projeto.

#### Frontend

- Javascript, HTML e CSS
- Vue 3
- Vite
- Vuetify
- Vuedatepicker
- Heroicons

O <Strong>Vuetify</Strong> é um framework para construção de interfaces de usuário baseado em Vue.js.

Utilizei este framework para facilitar a construção e integração dos componentes da aplicação, como os botões e o combobox de seleção.

As bibliotecas <Strong>Vuedatepicker</Strong> e <Strong>Heroicons</Strong> foram utilizadas para dar suporte na implementação de componentes relacionados a datas e ícones.

## Funcionamento da aplicação

Com a aplicação em execução, acessando o endereço `localhost:3000/transport`, a API escrita em python retorna o conjunto de dados do arquivo `data.json`.
Com isso, a aplicação <Strong>Vuetify</Strong> consome esses dados, carregando-os na página principal para que o usuário possa realizar as consultas de viagens.

Neste projeto, o <Strong>frontend</Strong> ficou encarregado da lógica para encontrar a viagem mais rápida/confortável e a viagem mais econômica, além de exibi-las na tela. Por ser uma lógica bastante simples e um conjunto de dados relativamente pequeno, o <Strong>frontend</Strong> realiza essa tarefa com muita eficiência.

É importante ressaltar que, com o aumento da complexidade/tamanho do conjunto de dados, é mais recomendável tratar esse tipo de lógica/regra de negócio no <Strong>backend</Strong> da aplicação.

## Como rodar localmente

Executando o <Strong>script</Strong> presente no caminho `/app/run.sh` (este script executará o backend e o frontend da aplicação ao mesmo tempo, além de instalar as dependências necessárias), basta acessar o link:

- http://localhost:8080




