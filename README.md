# WEBII-Sistema-CRUD

Instituto Federal de Pernambuco
Diciplina: Desenvolvimento Web II

Projeto: Criação de um sistema de gerenciamento de biblioteca

Senha
admin
ifpepaulista

#Executar no terminal\
python -m venv venv\
venv\Scripts\activate\
pip install -r requirements.txt\
pip freeze > requirements.txt\
python manage.py runserver\

#Executar projeto no Putty - AWS
cd ~\
python3.8 -m venv venv\
source venv/bin/activate\
pip3.8 install -r requirements.txt\
Adicionar DNS a setting em ALLOWED_HOSTS = ['']\
python3.8 manage.py runserver 0.0.0.0:8000\

#Enviar atualizações para o github\
git status\
git add .\
git status\
git commit -m "mensagem"\
git push origin main\

## Atividade 
https://developers.facebook.com/apps/?show_reminder=true
![image](https://user-images.githubusercontent.com/276077/166114761-e9b09073-3cee-4c5c-800a-619e694e98c3.png)



![image](https://user-images.githubusercontent.com/276077/166114779-922c9385-fb37-425c-af4b-c0382aae707e.png)


![image](https://user-images.githubusercontent.com/276077/166114797-7e0b04fb-9476-4eb4-b434-561777f9fa82.png)


![image](https://user-images.githubusercontent.com/276077/166114881-b14ecca7-bf1a-4a0d-b0bf-6fd5f721516c.png)


![image](https://user-images.githubusercontent.com/276077/166114898-02ab2f4c-a8ef-4cee-8ad5-d2ce1b19fe5d.png)

![image](https://user-images.githubusercontent.com/276077/166114960-0678afee-bdf3-4dc9-904e-c7e851a20f65.png)


![image](https://user-images.githubusercontent.com/276077/166114998-d8a9a060-1e2a-401d-a050-a06435ba40f1.png)

![image](https://user-images.githubusercontent.com/276077/166115090-aeff0b29-68c5-4ee0-b5e6-1bfd5cbd6734.png)


![image](https://user-images.githubusercontent.com/276077/166115122-a72d3178-c387-4599-8854-2355060611ef.png)


![image](https://user-images.githubusercontent.com/276077/166115185-33b4f10a-baaf-48d6-bea4-6f6f771b857e.png)

![image](https://user-images.githubusercontent.com/276077/166115224-01fd1e44-784c-423e-81ff-93b6b40f4213.png)

![image](https://user-images.githubusercontent.com/276077/166115407-c76baebf-4900-4de7-9801-1f67f27332be.png)

![image](https://user-images.githubusercontent.com/276077/166115472-bb732061-8590-408a-b3bd-f27a6693d2ee.png)


![image](https://user-images.githubusercontent.com/276077/166115567-de99dd91-2024-4b5a-aa7e-cc3a343ddb86.png)





Adicionar o backend abaixo: 

```
social_core.backends.facebook.FacebookOAuth2
```

Adicionar as seguintes variáveis com os dados obtidos no Facebook: 

```
SOCIAL_AUTH_FACEBOOK_KEY = "393994085924520"
SOCIAL_AUTH_FACEBOOK_SECRET = "a33421356da79e98ac94805a7dae53
```

Link para a página de login 

```
<li class="facebook">
                <a href="{% url 'social:begin' 'facebook' %}">Login com o Facebook </a>
</li>

```

![image](https://user-images.githubusercontent.com/276077/166115991-ce422980-86dc-4c56-826c-439f4a292974.png)
