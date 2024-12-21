## Introdução  
O projeto BitJoin é um site de criptoativos e moedas em geral. O principal objetivo do site BitJoin é fornecer as principais cotações e notícias sobre as principais criptomoedas, informando dentro do site e por e-mail.  
Todos os dias, às 6h25, é enviado a todos os e-mails cadastrados um resumo da cotação do Bitcoin.

## Página de Cotações  
![image](https://github.com/user-attachments/assets/95978b9c-b052-4ff1-a2ff-8ec2121c2582)  

- /  

**Servidor**  
- Todas as cotações de moedas são atualizadas a cada 3 minutos.  
- Os dados da cotação são armazenados em cache e substituídos a cada 3 minutos, servindo o usuário final com maior velocidade de resposta.  
- Tempo de resposta da página (cache): 0.40 ms.  
- Tempo de resposta da página (sem cache): 0.65 ms.  

**Layout**  
- Todos os botões possuem um método hover que aumenta 0.5% o tamanho do botão quando o usuário passa o mouse por cima, além de deixar a cor do botão mais escura.  
- Os blocos de cotação também são responsivos e aumentam 0.5% quando o usuário passa o mouse por cima.  
- A página possui adaptação para dispositivos menores.  
- Ao clicar no botão, o usuário será levado para ```/cadastro```.

**Página para Dispositivos Menores**  

![image](https://github.com/user-attachments/assets/0df86306-2436-4a3c-9ae1-8b082e197453)  

## Página de Notícias  
![image](https://github.com/user-attachments/assets/69dc51c2-3ff6-45ce-8b5c-dbbecbb8937f)  

- /news  

**Servidor**  
- Todas as notícias são armazenadas em cache, aumentando a velocidade de resposta da página.  
- As notícias são atualizadas a cada 1 dia.  
- A descrição das notícias é limitada a 300 caracteres, para melhorar a visibilidade no front-end.  
- Todas as notícias devem possuir keywords relacionadas às moedas.  
- Todos os títulos, links e descrições devem ser obrigatoriamente válidos. Caso algum desses itens seja inválido, o servidor passa para a próxima notícia.  
- Caso nenhuma notícia válida seja encontrada, os dados em cache já salvos serão retornados, evitando erros.  
- Foi implementada uma função para que, todos os dias, às 1h25 da manhã, as notícias sejam atualizadas, evitando que o acesso ao site fique lento para algum usuário.  
- Tempo de resposta (cache): 0.40 ms.  
- Tempo de resposta (sem cache): 2.0 segundos.  

**Layout**  
- Todas as imagens e ícones possuem um modo hover que aumenta o tamanho em 1.05 ao passar o mouse por cima.  
- A largura do box onde as notícias estão se adapta ao tamanho do texto.  
- Os títulos e descrições também possuem um método hover que aumenta o tamanho em 1.05 quando o usuário passa o mouse.  
- O campo onde está o link usa o método ```target="_blank"```. Isso significa que, ao clicar no link, será aberta uma aba adicional, mantendo o usuário no site.  
- A página possui adaptação para dispositivos menores.  

**Página para Dispositivos Menores**  

![image](https://github.com/user-attachments/assets/6b061a21-c11e-4a28-bc93-0b56e6d49318)  

## Página de Cadastro ( / )  
![image](https://github.com/user-attachments/assets/1f7cf412-6560-433d-82f3-0cbfc15e89c0)  

- /cadastro  

**Servidor**  
- Quando o servidor recebe os dados enviados, ele trata e verifica se os dados são válidos. Caso sejam inválidos, ele retorna um erro que será exibido como popup.  
- O servidor verifica se o e-mail do usuário já está cadastrado. Se estiver, ele retorna um erro.  
- Quando os dados são válidos, o servidor retorna o código 200 e inicia uma **Thread** para salvar o usuário na base de dados e enviar o e-mail de boas-vindas.  
- Quando o usuário é salvo, ele recebe um e-mail de boas-vindas automaticamente.  
- Ao receber os dados, o servidor verifica se o e-mail possui ```@``` e ```.com```.  
- Ele também verifica se os dados possuem caracteres especiais como ```% * / ( # ` ```. Se possuírem, os dados serão rejeitados.  
- Tempo de resposta: 0.39 ms.  

**Layout**  
- Adicionado um script em JS que verifica se os dados são válidos antes de enviar para o backend. Caso os dados sejam inválidos, será retornado um erro pelo próprio navegador.  
- Após o usuário se cadastrar, se a resposta do backend for de sucesso, um popup de sucesso será exibido.  
- Caso o usuário já esteja cadastrado, o backend informará o erro e será exibido um popup de erro.  
- Quando o usuário passa o mouse no botão, ele aumenta a escala em 1.05.  
- Foram colocados placeholders nos campos para maior visibilidade.  
- Após o popup de sucesso ser exibido, o usuário é redirecionado para a página ```/``` e os inputs são reiniciados.  
- A página possui adaptação para dispositivos menores.  

**Página para Dispositivos Menores**  

![397858933-b27ab07d-c229-492f-92d1-873fa892a1d8](https://github.com/user-attachments/assets/25045262-260f-4dea-ab80-626d424a6d21)  

**Pop-Ups**  

| **Sucesso**                                                                                     | **Usuário já cadastrado**                                                                      | **Dados Inválidos**  
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------|  
| <img src="https://github.com/user-attachments/assets/b40f301f-20fc-4c73-ad71-1c2a86438162" alt="Popup Sucesso" width="300" /> | <img src="https://github.com/user-attachments/assets/710ad91f-5884-49b0-8637-80506af83881" alt="Popup Usuário já cadastrado" width="300" /> | <img src="https://github.com/user-attachments/assets/d5e0db0a-e5d1-4039-b8d2-5928ef40c2bb" alt="Pop up dados inválidos" width="300" />  
