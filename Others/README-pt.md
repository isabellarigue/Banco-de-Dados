# Banco de Dados Aerodinâmica 

## O que é?

Um Banco de Dados é basicamente um lugar onde centralizamos os dados, dentro de tabelas. Com isso, é bem mais fácil e rápido acessar informações. 

Assim, esse projeto propõe a criação de um banco de dados para a divisão de Aerodinâmica da equipe Unicamp E-Racing, a fim de armazenar dados de simulações e testes de maneira efetiva e centralizada. Buscando facilitar a interação com o MySQL (banco de dados escolhido) também foi feita uma interface gráfica em Python, a qual atua como um intermédio entre o usuário e o servidor do banco, para que seja mais intuitivo adicionar e alterar dados no software, exportar planilhas e ver histogramas.

## Como usar?

Pode-se utilizar no formato de aplicativo, baixando o executável. Nesse caso não será preciso MySQL, Python ou qualquer outra biblioteca. Se estiver utilizando um sistema Windows, você pode usar o [instalador](https://drive.google.com/file/d/1Cr7XbCGEswlSXTWD1gX-Qcu0XpieaJBs/view?usp=sharing) para obter o app. Outra opção é baixar a [pasta build](../build), disponível aqui neste repositório, note que esse modo tende a demorar um pouco mais. Após baixado, altere o arquivo password.txt (localizado na pasta Others) digitando a senha no espaço indicado, feito isso basta abrir o app_script.exe e se divertir! A interface tende a ser intuitiva, não é preciso nenhum conhecimento prévio, logo apenas vá lendo os comandos e avisos mostrados na tela. Outrossim, fiz também esse mini [tutorial](https://drive.google.com/file/d/1kGWFlAdHZInAjpxgRfVd06st-oeM_kBL/view?usp=sharing) em forma de vídeo para ajudar com a instalação e uso do app.

Ademais, cabe mencionar que é possível rodar diretamente o código para acessar a aplicação. Nesse caso, é preciso ter Python instalado, além de algumas bibliotecas, são elas:

### Bibliotecas necessárias 

- tkinter
- mysql-connector
- sys
- os
- pandas
- matplotlib
- numpy
- datetime

## Quais as tabelas disponíveis?

No momento as tabelas disponíveis para armazenar dados são:

- Simulações do STAR-CCM+
- Simulações do Ansys
- Testes túnel de vento Denso
- Testes Coastdown

Há algumas outras tabelas criadas referentes a outros possíveis testes, mas estas não estão completamente implementadas.

## Valores padrão

No arquivo [values.csv](../Others/values.csv) há alguns valores padrão para facilitar a inserção de novos dados. Esses aparecem automaticamente na interface, nos lugares correspondentes. Caso deseje alterar alguns desses valores, basta modificar no próprio csv e salvar, mas lembre-se de tomar cuidado com a formatação.

## Código do Ansys

Quando rodamos uma simulação no Ansys são gerados arquivos .txt com o report e os pontos do aerofólio. Para facilitar a inserção desses dados no banco, foi criado o código [ansys.py](../ansys.py) que automatiza esse processo. Note que é necessário indicar os diretórios corretos no código para que ele funcione. Para maiores detalhes, veja o [tutorial](https://drive.google.com/file/d/1W2CqZVEdpp9yeLHV9P8-uMh3kKZzkUWp/view?usp=sharing).

## Observações

- O servidor utilizado é o PlanetScale;
- É feito um backup diariamente do banco de dados, mas ainda assim é preciso cuidado quando for mexer no mesmo, principalmente ao deletar arquivos!;
- É necessário internet para conectar-se ao servidor, dessa forma há também o modo offline que funciona apenas localmente;
- Para a tabela de testes no túnel de vento são feitas contas de correção para o valor dos coeficientes medidos, uma vez que ocorre uma deformção das linhas de fluxo confinadas dentro de um túnel;
- A pasta [Spreadsheet](../Spreadsheet) contém arquivos excel com os dados de simulações cadastrados no banco até o dia de hoje. São apenas para registro e exemplificação, os dados mais atuais devem ser exportados diretamente pela interface da aplicação;
- Cuidado com unidade de medida e formatação;
- Cuidado com a senha, não a deixe exposta, pois ela dá acesso total ao banco de dados.

## Erros comuns 

Tome cuidado ao digitar a senha no arquivo password.txt, atente-se para que não haja nenhum espaço em branco invisível após ou antes do texto, caso contrário poderá dar erro. Outro ponto importante é que caso esteja rodando diretamente o código .py é necessário instalar a biblioteca mysql-connector com o comando "pip install mysql-connector-python", escrito dessa forma. Por fim, lembre-se de abrir o executável como administrador, para evitar quaisquer problemas de permisão nos diretórios! 

## Contato

Qualquer problema, dúvida, comentário podem entrar em contato comigo! 
> email da equipe: isabella.rigue@unicamperacing.com.br

> email pessoal: bellarigue@gmail.com