
# 🎬 Flix API

API RESTful para gerenciamento de filmes, atores, avaliações e gêneros. Construída com Django REST Framework e hospedada no PythonAnywhere.

---

## 🌐 Link da API

- Base URL: [`https://fhao.pythonanywhere.com/api/v1/`](https://fhao.pythonanywhere.com/api/v1/)

---

## 🔐 Autenticação

A autenticação é feita com **JWT (JSON Web Token)**.

### 📤 Obter token:
```http
POST /api/v1/auth/token/
```
**Body:**
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

O token retornado deve ser usado no header das requisições:

```http
Authorization: Bearer <seu_token_aqui>
```

---

## 📚 Endpoints por recurso

### 🎭 Atores

- `GET /api/v1/actors/` – Lista todos os atores
- `POST /api/v1/actors/` – Cria um novo ator (requer token)

#### Exemplo de resposta:
```json
[
  {
    "id": 1,
    "name": "Vin Diesel",
    "birthday": "1967-07-18",
    "nationality": "USA"
  }
]
```

---

### 🎬 Filmes

- `GET /api/v1/movies/` – Lista filmes
- `POST /api/v1/movies/` – Cria filme (token necessário)

### ⭐ Reviews

- `GET /api/v1/reviews/` – Lista avaliações
- `POST /api/v1/reviews/` – Cria avaliação (token)

### 🎞️ Gêneros

- `GET /api/v1/genres/` – Lista gêneros
- `POST /api/v1/genres/` – Cria gênero (token/admin)

---

## 🧪 Testando com Postman

Você pode importar a coleção Postman com os seguintes grupos:

- ✅ `actors`
- ✅ `movies`
- ✅ `genres`
- ✅ `reviews`
- ✅ `authentication`

Cada endpoint já está configurado com:
- Método (`GET`, `POST`, etc)
- Headers com `Bearer Token`
- Corpo da requisição (se necessário)

---

## ⚙️ Tecnologias

- **Python 3.13**
- Django
- Django REST Framework
- **SQLite3** (banco de dados local padrão do Django)
- JWT (djangorestframework-simplejwt)
- Hospedagem: PythonAnywhere

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## ✨ Autor

Desenvolvido por [FHAO-3](https://github.com/FHAO-3)
