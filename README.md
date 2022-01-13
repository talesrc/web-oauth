# WEBII-Sistema-CRUD

Instituto Federal de Pernambuco
Diciplina: Desenvolvimento Web II

Projeto: Criação de um sistema de gerenciamento de biblioteca 

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
