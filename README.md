# 📝 ToDo List Desktop — by Jessé

Um aplicativo desktop moderno de lista de tarefas (To-Do) desenvolvido com **PySide6 (Qt)**, focado em produtividade, organização e experiência visual inspirada em ferramentas como Todoist.

---

## 🚀 ✨ Funcionalidades

### 📋 Gerenciamento de tarefas

* ➕ Adicionar tarefas com título e data
* ✅ Marcar tarefas como concluídas
* 🗑 Remover tarefas
* ✏️ Estrutura pronta para edição (CRUD completo)

---

### 📅 Organização por tempo (estilo Todoist)

* 📅 **Today** → tarefas de hoje
* ⏭ **Tomorrow** → tarefas de amanhã
* 📆 **Upcoming** → tarefas futuras
* ✅ **Completed** → tarefas finalizadas

---

### 🏷 Sistema de Tags

* Criação e uso de tags como:

  * Trabalho
  * Pessoal
  * Lazer
  * Estudo
  * Dia a dia
* Filtro por tag
* Contador automático por categoria

---

### 🔎 Filtros inteligentes

* Filtrar tarefas por:

  * Data (Today, Tomorrow, etc.)
  * Status (Completed)
  * Tags personalizadas
* Interface atualiza dinamicamente

---

### 🔢 Contadores dinâmicos

* Quantidade de tarefas por categoria no menu lateral
* Atualização automática em tempo real

---

### 🔃 Ordenação

* Botão de ordenação por data
* Tarefas sem data vão para o final

---

### 🎨 Interface moderna

* Sidebar estilo VS Code
* Layout com splitter (redimensionável)
* Scroll customizado
* Tema escuro elegante
* Topbar customizada (sem moldura do Windows)

---

### 💾 Persistência de dados (nível profissional)

* Dados salvos automaticamente em:

```
C:\Users\SEU_USUARIO\AppData\Local\TDList\tasks.json
```

✔ Não perde dados ao reinstalar
✔ Não depende da pasta do programa
✔ Padrão de softwares profissionais

---

## 🖥 Instalação

Baixe o instalador:

👉 https://drive.google.com/drive/folders/1WL7nTFKgIBtziSDGANU8G6u7xwv-NdyT?usp=sharing

---

### 🧩 O instalador inclui:

* Escolha de diretório
* Criação de atalho na área de trabalho
* Instalação simples e rápida

---

## 🛠 Tecnologias utilizadas

* Python
* PySide6 (Qt for Python)
* JSON (armazenamento de dados)
* PyInstaller (empacotamento)
* Inno Setup (instalador)

---

## 📁 Estrutura do projeto (simplificada)

```
to-do_list_app/
│
├── ui/
│   └── app.py
│
├── utils/
│   └── utilities.py
│
├── styles/
│   └── styles.py
│
└── main.py
```

---

## 🧠 Arquitetura

O projeto segue uma separação inspirada em **MVC (Model-View-Controller)**:

* **UI (View)** → interface com PySide6
* **Lógica (Controller)** → manipulação de eventos e regras
* **Dados (Model)** → JSON persistente no AppData

---

## 📌 Próximas melhorias (roadmap)

* 🔄 Auto-update
* ☁️ Sincronização com nuvem
* 🔔 Notificações
* 🔍 Busca funcional
* 📱 Versão mobile
* 👥 Multiusuário

---

## 👨‍💻 Autor

Desenvolvido por **Jessé** 🚀

---

## 💬 Observação final

Este projeto começou como prática e evoluiu para um **aplicativo desktop completo**, com arquitetura organizada, persistência profissional e experiência moderna.

---
