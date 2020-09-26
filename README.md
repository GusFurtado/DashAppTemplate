# **Dash App Template**

Template para agilizar o início do desenvolvimento de web apps utilizando Dash by Plotly.

## Funções
- Página inicial com atalhos para outras páginas da aplicação;
- Placeholder para autenticação de usuário
- Integração com fonts e ícones;
- Log de erros na aplicação;
- Layout com Dash e gráficos com Plotly;
- Werkzeug para middleware.


## Arquivos

- main.py
- utils.py
- README.md
- assets
  - favicon.ico
  - fonts.py
  - styles.css
- data
  - errorlog.log
- layouts
  - menu.py
  - app1.py
  - app2.py

### main.py
Arquivo principal que unifica todos os arquivos do projeto e realiza os callbacks com o servidor.

### utils.py
Arquivo para dar suporte ao main.py, com o objetivo de organizar o código.

### README.md
Instruções sobre os templates.

### assets
Pasta para os objetos visuais da front-end.

#### assets/favicon.ico
Ícone para o header do HTML.

#### assets/fonts.py
Arquivo com links para integração de fonts.

#### assets/styles.css
Estilos dos objetos HTML do projeto.

### data
Pasta para dados consumidos ou gerados pelo app.

#### data/errorlog.log
Saída para o log de erros da aplicação.

### layouts
Pasta para organizar layouts por aplicação.

#### layouts/menu.py
Página inicial para autenticação de usuário e atalhos para as outras páginas da aplicação.

#### layout/app1.py
Exemplo de página da aplicação.

#### layout/app2.py
Exemplo de página da aplicação.