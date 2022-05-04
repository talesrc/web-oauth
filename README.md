# Sistema CRUD de Biblioteca

Instituto Federal de Pernambuco  - Campus Paulista 

Diciplina: Desenvolvimento de Sistemas Web II

Desenvolvido por:  [BeatrizFS](https://github.com/BeatrizFS/)

Projeto: Sistema de gerenciamento de biblioteca

## Passos para executar o projeto


> O projeto já possui um banco de dados sqlite na pasta principal com
> com algumas informações salvas. Você pode usar o usuário de administação
> e também visualizar os livros que foram salvos no banco. 

Senha do usuário com permissão de administração:
- Usuário: admin
- Senha: ifpepaulista

1. Crie um ambiente virtual. Na pasta do projeto: 

```
python -m venv venv
```

2. Ative o ambiente virtual
```
source venv/bin/activate
```

3. Instale os requisitos
```
pip install -r requirements.txt
```

4. Entre na pasta do projeto e execute-o
```
python manager.py runserver_plus --cert cert.pem
```

## Atividade 
Nesta atividade você precisa adicionar a autenticação com oauth do Google e do Facebook no projeto da biblioteca. Para isso siga os passos descritos abaixo: 

1. Crie uma entrada para um domínio interno na sua máquina, como indicado no passo 5 do [exemplo de OAUTH](https://github.com/rodrigoclira/devweb2/tree/main/autenticacao-social). Crie o domínio com as iniciais de cada participante do projeto mais a adição do sufixo '**site.com**'. Por exemplo, a dupla formada por **R**enan e **T**om, teriam  que adicionar o domínio '**rtsite.com**' no seu arquivo de hosts. Se tudo estiver configurado corretamente, esses estudantes conseguirão acessar ao  projeto no navegador através do https://rtsite.com/8000. Agora crie o seu domínio (baseado no nome dos participantes), configure localmente e tente acessá-lo. Só avance para a próxima atividade quando o projeto da biblioteca estiver acessível no domínio definido.

> Se o django informar que o domínio não é um 'allowed_hosts', adicione-o no settings.py. (Passo 6 do [exemplo de OAUTH](https://github.com/rodrigoclira/devweb2/tree/main/autenticacao-social)) 

2. Crie um aplicativo no Google Developer Console seguindo os passos descritos [a partir do passo 10](https://github.com/rodrigoclira/devweb2/tree/main/autenticacao-social). Tome cuidado para trocar a indicação de '**mysite.com**' usado no exemplo para o domínio definido no passo anterior. Ao finalizar a criação, pegue o token e o secret e adicione nas suas respectivas variáveis. Teste a autenticação oauth na página de Login e se funcionar, siga para a próxima. 

3. Agora você vai adicionar a autenticação via facebook em uma aplicação. Para fazer isso, siga os passos descritos abaixo:
   - Acesso ao site: https://developers.facebook.com/apps/?show_reminder=true e clique em 'Criar Aplicativo'
![image](https://user-images.githubusercontent.com/276077/166114761-e9b09073-3cee-4c5c-800a-619e694e98c3.png)


   - Em seguida, escolha a opção 'Consumidor'
![image](https://user-images.githubusercontent.com/276077/166114779-922c9385-fb37-425c-af4b-c0382aae707e.png)


   - Dê um novo para a sua aplicação
![image](https://user-images.githubusercontent.com/276077/166114797-7e0b04fb-9476-4eb4-b434-561777f9fa82.png)

   - Na tela de adição de produtos, escolha a opção 'Login do Facebook' (a opção não está sendo exibida na imagem porque o print foi realizado após a escolha)
![image](https://user-images.githubusercontent.com/276077/166114881-b14ecca7-bf1a-4a0d-b0bf-6fd5f721516c.png)

   - Já com o 'Login do Facebook' ativado, escolha a opção 'início rápido' no painel lateral. Clique na opção 'WEB', como indicado na seta.  
![image](https://user-images.githubusercontent.com/276077/166114898-02ab2f4c-a8ef-4cee-8ad5-d2ce1b19fe5d.png)

   - Nela, digite o domínio fictício do seu site. Lembre-se que para isso funcionar, vocẽ precisa ter alterado o arquivo de 'hosts' do seu sistema operacional. Dessa forma, ele encaminhará a requisição para um domínio específico direto para o seu localhost. Adicione o seguinte padrão no campo, onde *dominio_escolhido* é o nome indicado no hostname do seu sistema operacional.

```
https://dominio_escolhido:8000
```

![image](https://user-images.githubusercontent.com/276077/166114960-0678afee-bdf3-4dc9-904e-c7e851a20f65.png)

<!-- ![image](https://user-images.githubusercontent.com/276077/166114998-d8a9a060-1e2a-401d-a050-a06435ba40f1.png) -->

   - Agora clique em configurações, no painel lateral. Nele você vai obter o ID da aplicação e o SECRET. Salve essas informações para serem usadas após a etapa de criação do aplicativo no site do facebook. 

![image](https://user-images.githubusercontent.com/276077/166115090-aeff0b29-68c5-4ee0-b5e6-1bfd5cbd6734.png)


<!-- ![image](https://user-images.githubusercontent.com/276077/166115122-a72d3178-c387-4599-8854-2355060611ef.png) -->


 ![image](https://user-images.githubusercontent.com/276077/166115185-33b4f10a-baaf-48d6-bea4-6f6f771b857e.png)

<!-- ![image](https://user-images.githubusercontent.com/276077/166115224-01fd1e44-784c-423e-81ff-93b6b40f4213.png) -->

<!--  ![image](https://user-images.githubusercontent.com/276077/166115407-c76baebf-4900-4de7-9801-1f67f27332be.png) -->

 <!-- ![image](https://user-images.githubusercontent.com/276077/166115472-bb732061-8590-408a-b3bd-f27a6693d2ee.png)  -->

   - Por fim, após copiar as informações, adicione em configuraçõe do 'Login do Facebook' a url do redirecionamento (destaque na imagem). 
Adicione o seguinte padrão, onde *dominio_definido* é o nome indicado no hostname do seu sistema operacional na etapa 1 da ativididade.

```
https://dominio_definido:8000/social-auth/complete/facebook/
```

![image](https://user-images.githubusercontent.com/276077/166115567-de99dd91-2024-4b5a-aa7e-cc3a343ddb86.png) 

Agora no projeto django faça as seguintes adições: 

   - Adicionar o backend abaixo na lista de **AUTHENTICATION_BACKENDS** do arquivo settings.py: 

```
social_core.backends.facebook.FacebookOAuth2
```

   - Adicionar as variáveis abaixo com os dados obtidos no Facebook. As variáveis devem ficar no settings.py 

```
SOCIAL_AUTH_FACEBOOK_KEY = ""  #Colocar ID obtido no aplicativo do facebook
SOCIAL_AUTH_FACEBOOK_SECRET = "" #Colocar SECRET obtido no aplicativo do facebook
```

   - Por fim, adicone o link para a página de login do facebook usando o redirecionamento url 'social:begin' no template de login (login.html)

```
<li class="facebook">
      <a href="{% url 'social:begin' 'facebook' %}">Login com o Facebook </a>
</li>

```

Por fim, certifique-se de que o urls.py principal da aplicação contém a linha abaixo no urlpatterns

```
    path('social-auth/', include("social_django.urls"), name='social'),
```

_Bonus_: 
Mude os links do login por Facebook e Google por imagens como as apresentadas abaixo. 
![image](https://user-images.githubusercontent.com/276077/166115991-ce422980-86dc-4c56-826c-439f4a292974.png)
