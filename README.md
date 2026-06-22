# 🎸 Grupo Pede Pagode

> Aplicação web desenvolvida para a disciplina de **Programação Orientada a Objetos**, simulando o site oficial de um grupo musical de pagode. O sistema possui área pública para visitantes e área restrita para os integrantes do grupo gerenciarem o repertório e os pedidos de música.

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura e Estrutura de Pastas](#arquitetura-e-estrutura-de-pastas)
- [Modelagem Orientada a Objetos](#modelagem-orientada-a-objetos)
- [Banco de Dados](#banco-de-dados)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Fluxo da Aplicação](#fluxo-da-aplicação)
- [Equipe](#equipe)

---

## Sobre o Projeto

O **Grupo Pede Pagode** é um projeto acadêmico que aplica os conceitos de **Programação Orientada a Objetos (POO)** em uma aplicação web real, construída com Python e Flask.

A proposta é representar o site de um grupo musical, onde qualquer visitante pode conhecer o grupo, consultar o repertório de músicas, curtir ou não curtir faixas e fazer pedidos de músicas. Os integrantes do grupo, por sua vez, acessam uma área restrita para gerenciar tudo isso.

O projeto foi desenvolvido em **3 sprints semanais** ao longo de 20 dias, seguindo metodologia ágil adaptada para equipes acadêmicas.

### Conceitos de POO aplicados

| Conceito | Onde é aplicado |
|----------|----------------|
| **Classes e Objetos** | Models `Usuario`, `Musica` e `Pedido` |
| **Encapsulamento** | Atributos privados com métodos de acesso nos models |
| **Métodos** | `adicionar_like()`, `aprovar()`, `autenticar()` e outros |
| **Separação de Responsabilidades** | Camadas distintas de Model, Service e Controller |
| **Reutilização** | `base.html` herdado por todos os templates via Jinja2 |

---

## Funcionalidades

### 🌐 Área Pública — acessível por qualquer visitante

#### Home (Landing Page)
- Banner com nome e slogan do grupo
- Seção "Sobre Nós" com história e estilo musical
- Lista de integrantes com foto, instrumento e descrição
- Informações de contato (WhatsApp, Instagram, e-mail)
- Botões de acesso rápido ao Repertório e ao Pedido de Música

#### Repertório
- Lista completa das músicas disponíveis
- Cada música exibe: nome, artista, gênero, número de likes e dislikes
- Visitante pode curtir (❤️) ou não curtir (👎) qualquer música
- Interação sem recarregar a página (JavaScript + Fetch API)
- Não exige autenticação — qualquer pessoa pode reagir

#### Pedido de Música
- Formulário com três campos: nome do visitante, música desejada e observação (opcional)
- Pedido salvo automaticamente no banco com status **Pendente**
- Confirmação exibida na tela após o envio

---

### 🔒 Área Restrita — acessível apenas após login

#### Login
- Autenticação por e-mail e senha
- Senha armazenada com hash seguro (`werkzeug.security`)
- Sessão Flask gerencia o estado do usuário autenticado
- Todas as rotas da área restrita exigem login (decorator `login_required`)

#### Dashboard
Painel inicial com estatísticas em tempo real:
- Total de músicas no repertório
- Total de pedidos recebidos
- Quantidade de pedidos com status **Pendente**
- Música mais curtida pelos visitantes

#### Gerenciar Pedidos
- Lista todos os pedidos enviados pelos visitantes
- Exibe: nome, música solicitada, observação, data e status atual
- Ações disponíveis: **Aprovar** ou **Recusar** cada pedido
- Status possíveis: `Pendente` → `Aceito` ou `Recusado`

#### Gerenciar Repertório
- Adicionar nova música ao repertório
- Editar informações de músicas existentes
- Remover músicas do repertório
- *(Bônus, se houver tempo)* Upload de PDF com cifra e letra

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Uso no projeto |
|-----------|--------|----------------|
| **Python** | 3.10+ | Linguagem principal |
| **Flask** | 3.x | Framework web, rotas e sessões |
| **SQLite** | 3.x | Banco de dados relacional local |
| **Jinja2** | (incluso no Flask) | Templates HTML dinâmicos |
| **HTML5** | — | Estrutura das páginas |
| **CSS3** | — | Estilização e layout |
| **JavaScript** | ES6+ | Interações sem reload (like/dislike) |
| **Werkzeug** | (incluso no Flask) | Hash seguro de senhas |

---

## Arquitetura e Estrutura de Pastas

O projeto segue uma arquitetura em camadas inspirada no padrão **MVC (Model-View-Controller)**, adaptada para Flask:

```
grupo-pede-pagode/
│
├── app.py                        # Ponto de entrada — instância Flask e registro dos blueprints
├── config.py                     # Configurações (SECRET_KEY, caminho do banco, debug)
├── requirements.txt              # Dependências do projeto
├── database.db                   # Banco de dados SQLite (gerado automaticamente)
│
├── database/
│   ├── connection.py             # Função get_connection() — retorna a conexão com o SQLite
│   └── schema.py                 # Criação das tabelas e função init_db()
│
├── models/                       # Camada de Modelo — entidades e suas responsabilidades
│   ├── usuario.py                # Classe Usuario (autenticar, login, logout)
│   ├── musica.py                 # Classe Musica (adicionar, editar, remover, like, dislike)
│   └── pedido.py                 # Classe Pedido (criar, aprovar, recusar)
│
├── services/                     # Camada de Serviço — regras de negócio e acesso ao banco
│   ├── usuario_service.py        # Validação de login, hash de senha
│   ├── musica_service.py         # CRUD de músicas, contagem de likes/dislikes
│   └── pedido_service.py         # Criação e gestão de pedidos
│
├── controllers/                  # Camada de Controle — rotas e lógica das requisições HTTP
│   ├── home_controller.py        # Rota: GET /
│   ├── repertorio_controller.py  # Rotas: GET /repertorio, POST /like, POST /dislike
│   ├── pedido_controller.py      # Rotas: GET /pedido, POST /pedido
│   ├── login_controller.py       # Rotas: GET /login, POST /login, GET /logout
│   └── dashboard_controller.py   # Rotas: /dashboard, /pedidos, /repertorio/admin
│
├── templates/                    # Camada de Visão — HTML com Jinja2
│   ├── base.html                 # Template base herdado por todos (navbar, footer, blocos)
│   ├── index.html                # Home — landing page pública
│   ├── repertorio.html           # Lista de músicas com botões de like/dislike
│   ├── pedido.html               # Formulário de pedido de música
│   ├── login.html                # Formulário de login
│   ├── dashboard.html            # Painel administrativo com estatísticas
│   ├── pedidos.html              # Gerenciamento de pedidos (área restrita)
│   └── editar_repertorio.html    # Formulário de adição/edição de músicas (área restrita)
│
├── static/
│   ├── css/
│   │   └── style.css             # Estilos globais da aplicação
│   ├── js/
│   │   └── main.js               # JavaScript: interações de like/dislike via Fetch API
│   └── images/                   # Imagens estáticas (fotos de integrantes, etc.)
│
└── uploads/                      # Arquivos enviados pelo admin (PDFs de cifras — bônus)
```

### Por que essa separação?

| Camada | Arquivo(s) | Responsabilidade |
|--------|-----------|-----------------|
| **Model** | `models/*.py` | Representa a entidade e seus comportamentos (POO) |
| **Service** | `services/*.py` | Regras de negócio e acesso ao banco de dados |
| **Controller** | `controllers/*.py` | Recebe a requisição HTTP e retorna a resposta |
| **View** | `templates/*.html` | Renderiza os dados em HTML para o usuário |

Essa separação facilita a manutenção e permite que Caio e João trabalhem em áreas diferentes sem conflito de código.


---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.10 ou superior instalado
- `pip` disponível no terminal

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/usuario/grupo-pede-pagode.git
cd grupo-pede-pagode
```

**2. Crie e ative um ambiente virtual** *(recomendado)*
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute a aplicação**
```bash
python app.py
```

O banco de dados (`database.db`) é criado automaticamente na primeira execução.

**5. Popule o banco com dados de teste**
```bash
python database/seed.py
```

Isso insere músicas de exemplo no repertório e cria o usuário administrador.

**6. Acesse no navegador**

| URL | Descrição |
|-----|-----------|
| `http://localhost:5000/` | Home pública |
| `http://localhost:5000/repertorio` | Repertório com likes |
| `http://localhost:5000/pedido` | Formulário de pedido |
| `http://localhost:5000/login` | Login da área restrita |
| `http://localhost:5000/dashboard` | Painel administrativo |

### Credenciais de teste

```
E-mail: admin@pedepagode.com
Senha:  admin123
```

> ⚠️ Essas credenciais são apenas para fins acadêmicos e de demonstração.

---

## Fluxo da Aplicação

```
VISITANTE
    │
    ├── /               → Home (banner, sobre, integrantes, contato)
    │
    ├── /repertorio     → Lista músicas → [❤️ like | 👎 dislike] (sem login)
    │
    └── /pedido         → Preenche form → Pedido salvo como "Pendente"


INTEGRANTE
    │
    └── /login          → Autentica com e-mail e senha
            │
            └── /dashboard      → Estatísticas gerais
                    │
                    ├── /pedidos             → Ver pedidos → [Aprovar | Recusar]
                    │
                    └── /repertorio/admin    → [Adicionar | Editar | Remover] músicas
```

---

## Equipe

| Integrante | Responsabilidades principais |
|-----------|------------------------------|
| **Caio** | Backend (Sprint 1), Frontend (Sprint 2), CSS final (Sprint 3) |
| **João** | Models e Frontend (Sprint 1), Backend/Auth (Sprint 2), Integração (Sprint 3) |

O projeto adota **rotação de responsabilidades** a cada sprint, garantindo que ambos os integrantes desenvolvam experiência em backend, frontend, banco de dados e integração.

---

*Projeto desenvolvido para a disciplina de Programação Orientada a Objetos.*
