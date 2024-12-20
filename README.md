## Introducao
O projeto BitJoin e um site de criptoativos e moedas em geral,O principal objetivo com o site Bitjoin e fornecer as principais cotacoes e noticias sobre as principais criptomoedas, informando dentro do site e por email
Todos os dias as 6 e 25 e enviado a todos os emails cadastrados um resumo da cotacao do bitcoin


## Pagina de cotacoes 
![image](https://github.com/user-attachments/assets/95978b9c-b052-4ff1-a2ff-8ec2121c2582) 
- /
**Servidor**
- Todas as cotacoes de moedas atualizam a cada 3 minutos
- Os dados da cotacao sao armazenados em cache e substituidos a cada 3 minutos, servindo o usuario final com maior velocidade de resposta
- Tempo de resposta da pagina ( cache ): 0.40 ms
- Tempo de resposta da pagina ( sem cache ) : 0.65 ms

**Layout**
- Todos os botoes possuem um metodo hover que aumenta 0.5% o tamanho do botao quando o usuario passa o mouse por cima e deixa a cor do botao escura
- Os blocos de cotacao tambem sao responsivos e aumentam 0.5% quando o usuario passa o mouse por cima
- A pagina possui adaptacao para dispositivos menores
- Ao clicar no botao o usuario sera levado para ```/cadastro```.

  
**Pagina Para Dispositivos menores**.


  ![image](https://github.com/user-attachments/assets/0df86306-2436-4a3c-9ae1-8b082e197453)


## Pagina de noticias 
![image](https://github.com/user-attachments/assets/69dc51c2-3ff6-45ce-8b5c-dbbecbb8937f)
- /news

**Servidor**
- Todas as noticias Sao armazenadas em cache, aumentando a velocidade de resposta da pagina
- As noticias Sao atualizadas a cada 1 dia
- A descricao de noticias e limitada a 300 caracteres, para melhorar a visibilidade no front end 
- Todas as noticias devem possuir keywords relacionadas as moedas
- Todos os titulos, links e descricoes devem ser obrigatoriamente validos, caso algum desses sao invalidos o servidor passa pra proxima noticia
- Caso Nenhuma noticia valida seja encontrada, Os dados em cache ja salvos serao retornados evitando erros
- Eu implementei uma funcao para todos os dias as 1 e 25 da manha ele executar a atualizacao das noticias, evitando assim que o acesso do site fique lento para algum usuario
- Tempo de resposta ( cache ) : 0.40 ms
- Tempo de resposta ( sem cache ) : 2.0 segundos

**Layout**
- Todos as imagens e icones possui um modo hover que aumenta o tamanho em 1.05 ao passar o mouse por cima
- O width do box onde as noticias estao se adapta ao tamanho do texto
- Os titulos e descricoes tambem possuem um metodo hover que aumenta o tamanho em 1.05 para quando o usuario passar o mouse
- O campo onde esta o link usa o metodo target = blank,Isso significa que ao clicar no link abrira uma aba adicional e o usuario ficara no site
- A pagina possui adaptacao para dispositivos menores.
  

**Pagina para dispositivos menores**



![image](https://github.com/user-attachments/assets/6b061a21-c11e-4a28-bc93-0b56e6d49318)

## Pagina de Cadastro ( / )
![image](https://github.com/user-attachments/assets/1f7cf412-6560-433d-82f3-0cbfc15e89c0)
- /cadastro

**Servidor**
- Quando o Servidor recebe os dados enviados ele trata e verifica se os dados sao validos, caso seja invalido ele retornara um erro que sera retornado como popup
- O servidor verifica se o email do usuario ja esta cadastrado , se estiver ele retorna um erro
- Quando os dados Sao validos o Servidor retorna o codigo 200 e inicia uma Threading para salvar o usuario na db e enviar o email de boas vindas
- Quando o Usuario e salvo ele recebe um Email de boas vindas automaticamente
- Ao receber os dados o servidor verifica se o email possui @ e .com
- Ele tambem verifica se os dados possuem caracteres especiais como ( % * / (  # ` ) se possuirem os dados serao rejeitados
- Tempo de Resposta 0.39 ms

  **Layout**
  - Adicionei um Script em js que verifica se os dados sao validos antes de enviar para o backend, caso os dados sejam invalidos sera retornado um erro pelo proprio navegador
  - Apos o Usuario se cadastrar, e a resposta do backend for de sucesso, Um pop up de Sucesso sera levantado
  - Caso o Usuario ja esteja cadastrado,O backend informara o erro e sera levantado um pop up de erro
  - Quando o usuario Passa o mouse no botao o botao aumentara a scala em 1.05
  - Foi colocado Placeholders nos campos para maior visibilidade
  - Apos o pop up de sucesso ser levantado o usuario e redirecionado para a pagina / e os inputs sao reiniciados
  - A pagina possui adaptacao para dispositivos menores.
 
    **Pagina para dispositivos menores**


  ![image](https://github.com/user-attachments/assets/b27ab07d-c229-492f-92d1-873fa892a1d8)


  **Pop Ups**
| ![image](https://github.com/user-attachments/assets/b40f301f-20fc-4c73-ad71-1c2a86438162) | ![image](https://github.com/user-attachments/assets/710ad91f-5884-49b0-8637-80506af83881) | 
|----------------------------------------------------------|----------------------------------------------------------|
| Sucesso                                    | Usuario ja cadastrado                                    |

