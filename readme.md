<h4 align="center">
  ☕ Code and Coffee
</h4>

<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-implementação">Implementação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

<br>

## :rocket: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [JavaScript](#)
- [Html](#)
- [Css](#)
- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://github.com/pennersr/django-allauth)
- [Django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- [Bootstrap](https://facebook.github.io/react-native/)
- [Grid.js](https://gridjs.io/)
- [Cleave.js](https://github.com/nosir/cleave.js)
- [ViaCEP](https://viacep.com.br/)

## Instalação

1. Criar ambiente virtual :
```bash
python -m venv env
```

2. Ativar ambiente virtual (cmd):
```bash
env\Scripts\activate
```

3. Atualizar pip:
```bash
python -m pip install --upgrade pip
```

4. Instalar dependências:
```bash
pip install -r requirements.txt
```

5. Sincronizar database:
```bash
python web\manage.py migrate
```

6. Criar um super usuário:
```bash
python web\manage.py createsuperuser
```

7. Iniciar o servidor:
```bash
python web\manage.py runserver
```

## 🔖 Implementações

- Autenticação (Login/Logout)
- Controle de acesso
- Módulo Agendamento (Create, Read, Update, Delete)
- Módulo Médico (Create, Read, Update, Delete)
- Módulo Paciente (Create, Read, Update, Delete)

## :memo: Licença

Esse projeto está sob a licença MIT.