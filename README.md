## Introdução  
O projeto BitJoin é um site de criptoativos e moedas em geral. O principal objetivo do site BitJoin é fornecer as principais cotações e notícias sobre as principais criptomoedas, informando dentro do site e por e-mail.  
Todos os dias, às 6h25, é enviado a todos os e-mails cadastrados um resumo da cotação do Bitcoin.

## Página de Cotações  

![image](https://github.com/user-attachments/assets/95978b9c-b052-4ff1-a2ff-8ec2121c2582)  
GET ```/```
Esta página exibe as cotações mais recentes das moedas.

---

### **Servidor**
- As cotações de moedas são atualizadas a cada **3 minutos**.
- Os dados são armazenados em **cache** e substituídos a cada 3 minutos, garantindo maior velocidade de resposta para o usuário.
- **Tempo de resposta da página**:
  - Com cache: **0.40 ms**.
  - Sem cache: **0.65 ms**.

### **Layout**
- **Interatividade visual:**
  - Todos os botões possuem um efeito hover que:
    - Aumenta o tamanho em **0.5%**.
    - Escurece a cor do botão.
  - Os blocos de cotação também aumentam **0.5%** quando o mouse passa por cima.
- **Responsividade:**
  - A página é adaptada para dispositivos menores, garantindo uma boa experiência para todos os usuários.
- **Redirecionamento:**
  - Ao clicar no botão, o usuário será levado para a página ```/cadastro```.

<div align="center">
  
### **Página para dispositivos Menores**

</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/0df86306-2436-4a3c-9ae1-8b082e197453" alt="Página menor" />
</div>

## Página de Notícias  
![image](https://github.com/user-attachments/assets/69dc51c2-3ff6-45ce-8b5c-dbbecbb8937f)  
GET ```/news```
Esta página exibe e disponibiliza as notícias mais recentes relacionadas ao mercado.

---

### **Servidor**
- Todas as notícias são armazenadas em **cache**,e atualizadas 1 vez ao dia automaticamente,melhorando o tempo de resposta.
- As notícias são atualizadas diariamente, às **1h25 da manhã**, para evitar lentidão durante o acesso.
- Nao precisa de interacao dos usuarios para atualizar as noticias
- **Descrição das notícias**:
  - Limitada a **300 caracteres** para melhor exibição no front-end.
  - Todas as notícias devem conter keywords relacionadas às moedas.
- **Validação de dados**:
  - Títulos, links e descrições são obrigatoriamente válidos. Caso alguma notícia tenha dados inválidos, ela será ignorada e sera buscada a proxima.
- **Fallback em caso de erro**:
  - Se nenhuma notícia válida for encontrada, os dados armazenados em cache são retornados, evitando erros para o usuário.
- **Tempo de resposta**:
  - Com cache: **0.40 ms**.
  - Sem cache: **2.0 segundos**.


### **Layout**
- **Interatividade visual:**
  - Todas as imagens e ícones possuem um efeito hover que aumenta o tamanho em **1.05** quando o mouse passa sobre eles.
  - Títulos e descrições também utilizam o efeito hover, ampliando o texto em **1.05**.
- **Links:**
  - Os links para as notícias abrem em uma nova aba (`target="_blank"`), mantendo o usuário no site.
- **Responsividade:**
  - A largura dos boxes das notícias se adapta automaticamente ao tamanho do texto.
  - A página foi projetada para se ajustar perfeitamente a dispositivos menores.

---
<div align="center">
  
### **Página para dispositivos Menores**

</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/6b061a21-c11e-4a28-bc93-0b56e6d49318" alt="Página menor" />
</div>


## Página de Cadastro  

![image](https://github.com/user-attachments/assets/1f7cf412-6560-433d-82f3-0cbfc15e89c0)  
GET, POST ```/cadastro```
Esta página permite que o usuário cadastre seu email para receber resumos sobre o Bitcoin.

---

### **Servidor**
- Quando o servidor recebe os dados enviados, ele:
  - Trata e verifica se os dados são válidos. Caso sejam inválidos, retorna um erro exibido como popup.
  - Verifica se o email do usuário já está cadastrado. Se estiver, retorna um erro.
  - Caso os dados sejam válidos, retorna o código **200** e inicia uma **Thread** para salvar o usuário na base de dados e enviar o email de boas-vindas.
  - Envia automaticamente o email de boas-vindas após salvar o usuário.
- **Tempo de resposta**: 0.39 ms.


### **Proteções**
- O servidor realiza as seguintes verificações:
  - O email deve conter ```@``` e ```.com```.
  - Dados com caracteres especiais como ```% * / ( # ` ``` são rejeitados.
  - Todos os inputs passam por tratamento para prevenir injeção de código, evitando falhas como **SQL Injection** e **XSS**.
- Os erros nao são retornados diretamente, mas sim com mensagens personalizadas, evitando vazamento de informações sensíveis.


### **Layout**
- Adicionado um script em JavaScript para validar os dados antes de enviá-los ao backend. Caso sejam inválidos, o próprio navegador exibe um erro.
- **Após o cadastro:**
  - Se o backend retornar sucesso, um popup de sucesso é exibido.
  - Se o usuário já estiver cadastrado, o backend informará o erro, que será exibido em um popup.
- **Interações visuais:**
  - O botão aumenta a escala em **1.05** quando o mouse passa sobre ele.
  - Placeholders foram adicionados aos campos para melhorar a experiência do usuário.
- **Redirecionamento:**
  - Após o popup de sucesso, o usuário é redirecionado para a página ```/``` e os inputs são reiniciados.
- A página foi otimizada para adaptação em dispositivos menores.

---
<div align="center">
  
### **Página para dispositivos Menores**

</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/25045262-260f-4dea-ab80-626d424a6d21" alt="Página menor" />
</div>

**Pop-Ups**  

| **Sucesso**                                                                                     | **Usuário já cadastrado**                                                                      | **Dados Inválidos**  
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------|  
| <img src="https://github.com/user-attachments/assets/b40f301f-20fc-4c73-ad71-1c2a86438162" alt="Popup Sucesso" width="300" /> | <img src="https://github.com/user-attachments/assets/710ad91f-5884-49b0-8637-80506af83881" alt="Popup Usuário já cadastrado" width="300" /> | <img src="https://github.com/user-attachments/assets/d5e0db0a-e5d1-4039-b8d2-5928ef40c2bb" alt="Pop up dados inválidos" width="300" />  

## Pagina Desinscrever

![image](https://github.com/user-attachments/assets/711bbaf0-9f00-4d6e-bcc9-130172636cfa)

Esta página permite que o usuário remova seu email do banco de dados.

### **Servidor**
- Quando o usuário clica em "Continuar", o email é enviado para outra página via JavaScript usando `fetch` (```/EnviarCodigo```), e o codigo para o Email e enviado atraves de uma Thread.
- O BackEnd verifica se o email existe no banco de dados e se é válido antes de realizar o envio.
- Essa página envia um email e gera um código aleatório de 6 dígitos.
- O código é salvo em uma lista de dicionários, onde o email é usado como chave.
- O código gerado possui um timeout de **30 minutos**.
- Quando o usuário insere o código de verificação, o código e o email são enviados para outra página via `fetch` em JavaScript (```/VerificarCodigo```) e verificados, caso tudo esteja correto ele retorna codigo de sucesso 200.
- Caso o Timeout do codigo solicitado esteja expirado, ele e apagado automaticamente
- Verificações realizadas:
  - As verificacoes Ocorrem no FrontEnd e no Backend
  - Se o email solicitado possui um código gerado. Caso contrário, retorna um erro: ```Código ou Email inválido```.
  - Se o timeout do código é válido e o código está correto. Caso contrário, retorna um erro: ```Código Incorreto```.
  - Se o email existe no banco de dados.
  - Se o código tem exatamente 6 dígitos e contém apenas números inteiros.


### **Proteções**
- **Prevenção contra vulnerabilidades:**
  - Nenhum dado é passado diretamente, evitando vulnerabilidades como **SQL Injection** e **XSS**.
- **Validações realizadas:**
  - Todos os campos são tratados e verificados.
  - O email só é considerado válido se possuir ```@```, ```.``` e ```.com``` e tiver mais de 5 caracteres.
  - O código só é válido se possuir exatamente 6 caracteres numéricos.
- **Tratamento de erros:**
  - Todos os erros são retornados em mensagens amigáveis, sem vazamento de informações sensíveis.

### **Layout**
- **Botões**:
  - Possuem um efeito **hover** que aumenta a escala em **1.05** quando o mouse passa sobre eles e a cor ficam mais escura.
- **Popup de Inserir o Código**:
  - Tem um place Holder ( ```Insira seu codigo numerico aqui```) 
  - Aparece apenas após o backend confirmar que o email é válido e o código foi enviado.
  - É responsivo e ajusta seu tamanho de acordo com o conteúdo.
  - Botões do popup possuem um efeito **hover** que aumenta a escala em **1.05**.
- **Validações**:
  - O sistema verifica se o email e o código são válidos.
  - O input do código é validado diretamente com **JavaScript**.
- **Mensagens de Erro**:
  - Possuem um efeito **hover** que as oculta quando o usuário clica no input correspondente.
  - As mensagens de erro do backend são exibidas de forma clara no frontend.
- **Função Cancelar**:
  - Ao clicar no botão "Cancelar", todos os inputs são limpos e a página é reiniciada.
- **Popup Final de Sucesso**:
  - Indica sucesso na operação.
  - Quando clicado, o usuário é redirecionado para a página padrão e a página é reiniciada automaticamente.


**Pop-Ups**  

| **Email invalido**                                                                                     | **Usuário nao esta cadastrado**                                                                      | **Insira o codigo de verificacao** 
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------|
| <img src="https://github.com/user-attachments/assets/a9cb6668-cd57-44c7-9c52-bfe51e44bc5e" alt="Email Invalido" width="300" /> | <img src="https://github.com/user-attachments/assets/e0fb2763-b7f8-490c-b11b-2bc4bfc98619" alt="Popup Usuário já cadastrado" width="300" /> | <img src="https://github.com/user-attachments/assets/fda11ccd-f95a-42da-b6b6-72f0638885d2" alt="Insira o codigo de verificacao" width="300" /> 


| **Codigo invalido**                                                                                     | **Codigo incorreto**                                                                      | **Sucesso** 
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------|
| <img src="https://github.com/user-attachments/assets/c0200f30-bed4-4b74-8ded-525966aa8015" alt="Codigo Invalido" width="300" /> | <img src="https://github.com/user-attachments/assets/7c5fb64e-2f3b-4a0b-81ae-b39ccc96222e" alt="Codigo incorreto" width="300" /> | <img src="https://github.com/user-attachments/assets/13edca4a-624d-4ed3-a282-76c82d3e7dfd" alt="Sucesso" width="300" /> 

<div align="center">
  
### **Página para dispositivos Menores**

</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/87878610-f1df-43c9-b84f-a522435ec8f7" alt="Página menor" />
</div>
