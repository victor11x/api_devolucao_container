# Meu MVP

Este projeto faz parte do MVP do curso de pós-graduação em Desenvolvimento de Full Stack do ano 2023, pela PUC - Rio.

A ideia do MVP é elaborar uma ideia que atenda um problema do mundo real, depois estrutura as ideias e criar um protótipo da entrega final.

O meu projeto de MVP atende uma necessidade de segmento logistico, Super Portal que consolidade departamentos e atividades de Gestão Estoque, Aquisição Produtos e Gerenciamento Operacional de todo Galpão Logistico, centralizando tudo unico portal que pode Administrador (Gestor) realizar solicitações de compra produtos direto com fornecedores parceiros, listagem de pedidos para ser enviado para cliente final e monitoramento do estoque se existe necessidade compra produtos faltantes.

# Arquitetura da Aplicação

Projeto foi construido uma arquitura de Microserviço. Este repositorio faz parte do BLOCO C que está em microserviço de Api Devolução que consta todos produtos devolvidos pelo cliente. Imagem abaixo apresenta desenho da arquitetura do projeto .

<div align="center">
<h4>Diagrama da Arquitetura Microserviço</h4>
<img src="https://github.com/victor11x/images/blob/master/Diagrama.jpg?raw=true" width="700px"/>
</div>
<br>
O repositorio esta toda aplicação do Backend que consta todas as regras de negocios e API que aponta uma rota do metodo POST e GET.

Para armazenamento desde dados utilizei banco de dados SQLite que atende demanda inicial do prototipo.

Na parte de documentação utilizado API em Swagger.

--

## Como executar em FLASK

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5004
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5004 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t api_produto_devolvido .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ sudo docker run --rm -p 5004:5004 api_produto_devolvido
```

Uma vez executando, para acessar o front-end, basta abrir o [http://localhost:5004/#/](http://localhost:5004/#/) no navegador.
