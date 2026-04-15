from .styles import menu, topbar, janela, btn_style,btn_style2, splitter_style, scroll_style, titulo_lista, conteudo_style, background, btn_style3,texto_conteudo, calendar_style, btn_sort_sty, tag_colors, btns_tags_styles, tag_label_style

from typing import List

from controller.task_controller import TaskController

from PySide6.QtWidgets import QCheckBox, QLineEdit, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QSizePolicy, QSplitter, QScrollArea, QDateEdit
from PySide6.QtCore import QTimer, Qt, QPoint, QDate

class ToDoListApp(QMainWindow):
    
    def __init__(self):
        super().__init__()       
        
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 980, 600)
        self.setWindowFlags(Qt.FramelessWindowHint) #type: ignore
        self.setStyleSheet(janela)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout_principal = QVBoxLayout(self.central_widget)
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.layout_principal.setSpacing(0)
        
        self.filtro_atual = "all"
        self.controller = TaskController()
        
        # ── Barra do topo ──────────────────────────────
        self.topbar = QWidget()
        self.topbar.setFixedHeight(50)
        self.topbar.setStyleSheet(topbar)
        
        topbar_layout = QHBoxLayout(self.topbar)
        topbar_layout.setContentsMargins(10, 0, 10, 0)
        
        self.titulo = QLabel("Para Lembrar - TO-DO")
        self.titulo.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        
        self.btn_minimizar = QPushButton("─")
        self.btn_maximizar = QPushButton("□")
        self.btn_fechar    = QPushButton("✕")
        
        for btn in [self.btn_minimizar, self.btn_maximizar, self.btn_fechar]:
            btn.setStyleSheet(btn_style)
            btn.setFixedSize(40, 40)
        
        self.btn_fechar.setStyleSheet(btn_style + "QPushButton:hover { background-color: #e04040; }")
        
        topbar_layout.addWidget(self.titulo)
        topbar_layout.addStretch()
        topbar_layout.addWidget(self.btn_minimizar)
        topbar_layout.addWidget(self.btn_maximizar)
        topbar_layout.addWidget(self.btn_fechar)
        
        # ── Conexões ───────────────────────────────────
        self.btn_fechar.clicked.connect(self.close)
        self.btn_minimizar.clicked.connect(self.showMinimized)
        self.btn_maximizar.clicked.connect(self.alternar_maximizar)
        
        # ── Arrastar janela ────────────────────────────
        self._drag_pos = QPoint()
        self.topbar.mousePressEvent   = self.drag_inicio
        self.topbar.mouseMoveEvent    = self.drag_mover
        
        # ── Conteúdo ───────────────────────────────────
        self.area_conteudo = QWidget()
        conteudo_layout = QGridLayout(self.area_conteudo)
        conteudo_layout.setContentsMargins(0, 0, 0, 0)
        
        self.menu_lateral = QWidget()
        self.menu_lateral.setMinimumWidth(180)
        self.menu_lateral.setStyleSheet(menu)
        
        self.menu_layout = QVBoxLayout(self.menu_lateral)
        self.menu_layout.setContentsMargins(10, 10, 10, 10)
        self.menu_layout.setSpacing(4)
        
        #-------------QScrollArea <---------------
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.menu_lateral)
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #type: ignore
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)   #type: ignore
        self.scroll_area.setStyleSheet(scroll_style)
        
        #-------------QScrollArea
        
        self.search = QPushButton("🔎  Buscar") #TODO: fazer a busca
        self.search.setFixedHeight(36)
        self.search.setStyleSheet(btn_style2)
        self.menu_layout.addWidget(self.search)
        
        self.botoes_menu = {
            "Inbox": QPushButton("📥  Inbox"),
            "Today": QPushButton("📅  Today"),
            "Tomorrow": QPushButton("📅  Tomorrow"),
            "Upcoming": QPushButton("🗓  Upcoming"),
            "Completed": QPushButton("✅  Completed"),
        }
        
        self.botoes_menu["Today"].clicked.connect(lambda: self.filtrar("today"))
        self.botoes_menu["Tomorrow"].clicked.connect(lambda: self.filtrar("tomorrow"))
        self.botoes_menu["Upcoming"].clicked.connect(lambda: self.filtrar("upcoming"))
        self.botoes_menu["Completed"].clicked.connect(lambda: self.filtrar("completed"))
        self.botoes_menu["Inbox"].clicked.connect(lambda: self.filtrar("all"))
        
        
        for nome, btn in self.botoes_menu.items():
            btn.setStyleSheet(btn_style2)
            btn.setCursor(Qt.PointingHandCursor) #type: ignore
            self.menu_layout.addWidget(btn)


        label_projects = QLabel("TAGS")
        label_projects.setStyleSheet("color: #888; font-size: 17px; margin-top:10px;")

        self.menu_layout.addWidget(label_projects)

        self.botoes_tags = {
            "Trabalho": QPushButton("● Trabalho"),
            "Pessoal": QPushButton("● Pessoal"),
            "Lazer": QPushButton("● Lazer"),
            "Estudo": QPushButton("● Estudo"),
            "Dia A Dia": QPushButton("● Dia A Dia"),
        }
        
        # No __init__, onde cria os botoes_tags
        for tag, btn in self.botoes_tags.items():
            btn.setStyleSheet(btn_style2)
            btn.setCursor(Qt.PointingHandCursor) #type: ignore
            btn.clicked.connect(lambda _, t=tag: self.filtrar_por_tag(t))
            self.menu_layout.addWidget(btn)
        
        for btn in self.botoes_tags.values():
            btn.setStyleSheet(btn_style2)
            btn.setCursor(Qt.PointingHandCursor) #type: ignore

        for btns in self.botoes_tags.values():
            self.menu_layout.addWidget(btns)
        
        self.menu_layout.addStretch()
        
        # --------------------- CONTEUDO ---------------
        self.conteudo = QWidget()
        self.conteudo_lyout = QVBoxLayout(self.conteudo)
        self.conteudo_lyout.setContentsMargins(20, 20, 20, 20)
        self.conteudo_lyout.setSpacing(10)
        self.conteudo.setStyleSheet(background)
        
        self.tags_selecionadas = set() # <- lista de tags
        
        self.tag_buttons = {}
        tags_layout = QHBoxLayout()
        
        for tag, cor in tag_colors.items():
            btn = QPushButton(tag)
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor) #type: ignore
            btn.setStyleSheet(btns_tags_styles(cor))
            btn.toggled.connect(lambda checked, t=tag: self.tags_selecionadas.add(t) if checked else self.tags_selecionadas.discard(t))
            self.tag_buttons[tag] = btn
            tags_layout.addWidget(btn)
        
        tags_layout.addStretch()
        
        self.title_list = QLabel("Personal TO-DO")
        self.title_list.setStyleSheet(titulo_lista)
        self.conteudo_lyout.addWidget(self.title_list)
        
        self.add_layout = QHBoxLayout()
        self.input_task = QLineEdit()
        self.input_task.setPlaceholderText("Adicionar tarefa...")
        self.input_task.setStyleSheet(btn_style2)
        
        self.input_date = QDateEdit()
        self.input_date.setDate(QDate.currentDate())
        self.input_date.setCalendarPopup(True) 
        self.input_date.setCursor(Qt.PointingHandCursor) #type: ignore
        self.input_date.setStyleSheet(calendar_style)
        
        self.btn_sort = QPushButton("Sort")
        self.btn_sort.setStyleSheet(btn_sort_sty)
        self.btn_sort.clicked.connect(self.sort_by_date)
    
    
        self.btn_add_task = QPushButton("+")
        self.btn_add_task.setFixedWidth(30)
        self.btn_add_task.setCursor(Qt.PointingHandCursor) #type: ignore
        self.btn_add_task.setStyleSheet(titulo_lista)
        
        
        self.btn_add_task.clicked.connect(self.add_task)
        self.input_task.returnPressed.connect(self.add_task)
        
        
        self.add_layout.addWidget(self.input_task)
        self.add_layout.addWidget(self.btn_add_task)
        self.add_layout.addWidget(self.input_date)
        self.add_layout.addWidget(self.btn_sort)
        
        self.task_list = QVBoxLayout()
        self.task_list.setSpacing(8)
        
        self.conteudo_lyout.addLayout(self.task_list)
        self.conteudo_lyout.insertLayout(1, self.add_layout)
        self.conteudo_lyout.insertLayout(2, tags_layout)
        self.conteudo_lyout.addStretch()
        
        self.conteudo_scroll = QScrollArea()
        self.conteudo_scroll.setWidgetResizable(True)
        self.conteudo_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #type: ignore
        self.conteudo_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  #type: ignore
        self.conteudo_scroll.setWidget(self.conteudo)
        self.conteudo_scroll.setStyleSheet(scroll_style)
        
        
        #dados load dados em json ---------------------------
        
        self.tasks = []
        self.load_tasks()
        
        # --------------------- CONTEUDO ---------------
        
        self.splitter = QSplitter(Qt.Horizontal) #type: ignore
        self.splitter.addWidget(self.scroll_area)
        self.splitter.addWidget(self.conteudo_scroll)
        self.splitter.setSizes([200, 760])
        self.splitter.setStretchFactor(0, 1)  # menu lateral
        self.splitter.setStretchFactor(1, 3)  # conteúdo principal
        
        self.splitter.setStyleSheet(splitter_style)
        
        conteudo_layout.addWidget(self.splitter, 0, 0)
        conteudo_layout.setColumnStretch(0, 1)
        
        self.layout_principal.addWidget(self.topbar)
        self.layout_principal.addWidget(self.area_conteudo)
    
    def alternar_maximizar(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    def filtrar(self, tipo):
        self.filtro_atual = tipo
        self.render_tasks()
        self.update_menu_style()
        
    def filtrar_por_tag(self, tag):
        self.filtro_atual = f"tag_{tag}"
        self.render_tasks()
    
    def drag_inicio(self, event):
        if event.button() == Qt.LeftButton: #type: ignore
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def drag_mover(self, event):
        if event.buttons() == Qt.LeftButton: #type: ignore
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            
    def update_counters(self):
        today, tomorrow, upcoming, completed = self.separate_tasks()
        
        self.botoes_menu["Today"].setText(f"📅 Today ({len(today)})")
        self.botoes_menu["Tomorrow"].setText(f"📅 Tomorrow ({len(tomorrow)})")
        self.botoes_menu["Upcoming"].setText(f"🗓  Upcoming ({len(upcoming)})")
        self.botoes_menu["Completed"].setText(f"✅  Completed ({len(completed)})")
        
    def update_counters_tags(self):
        work, personal, leisure, study, day_by_day = self.separate_task_tag()
        
        self.botoes_tags["Trabalho"].setText(f"● Trabalho ({len(work)})")
        self.botoes_tags["Pessoal"].setText(f"● Pessoal ({len(personal)})")
        self.botoes_tags["Lazer"].setText(f"● Lazer ({len(leisure)})")
        self.botoes_tags["Estudo"].setText(f"● Estudo ({len(study)})")
        self.botoes_tags["Dia A Dia"].setText(f"● Dia A Dia ({len(day_by_day)})")
        

    def separate_task_tag(self):
        return self.controller.separate_task_tag()

    def separate_tasks(self):
        return self.controller.separate_tasks()
    
    
    def render_section(self, titulo, tarefas):
        if not tarefas:
            return

        label = QLabel(titulo)
        label.setStyleSheet("font-size: 14px; color: #4FC3F7; margin-top: 10px;")

        self.task_list.addWidget(label)

        for task in tarefas:
            self.create_task(
                task["title"],
                task.get("date"),
                task["done"],
                task["id"]
            )
                
            
    def clear_tasks_ui(self):
        while self.task_list.count():
            item = self.task_list.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
    def render_tasks(self):
        self.clear_tasks_ui()
        
        today, tomorrow, upcoming, completed = self.separate_tasks()
        
        # ← filtro por tag
        if self.filtro_atual.startswith("tag_"):
            tag = self.filtro_atual.replace("tag_", "")
            tarefas_tag = [t for t in self.tasks if tag in t.get("tags", []) and not t.get("done")]
            self.render_section(tag, tarefas_tag)
            self.title_list.setText("Personal TO-DO")
            return
        
        if self.filtro_atual == "today":
            self.title_list.setText("Today")
            self.render_section("Today", today)
            
        elif self.filtro_atual == "tomorrow":
            self.title_list.setText("Tomorrow")
            self.render_section("Tomorrow", tomorrow)
            
        elif self.filtro_atual == "upcoming":
            self.title_list.setText("Upcoming")
            self.render_section("Upcoming", upcoming)
        
        elif self.filtro_atual == "completed":
            self.title_list.setText("Completed")
            self.render_section("Completed", completed)
        
        else:  # Inbox / All
            self.title_list.setText("Personal TO-DO")
            self.render_section("Today", today)
            self.render_section("Tomorrow", tomorrow)
            self.render_section("Upcoming", upcoming)
            
    def sort_by_date(self):
        self.controller.sort_by_date()
        self.tasks = self.controller.get_tasks()
        self.render_tasks()
        
    def update_menu_style(self):
        for nome, btn in self.botoes_menu.items():
            if nome.lower() == self.filtro_atual:
                btn.setStyleSheet(btn_style2 + "background-color: #2a2d33;")
            else:
                btn.setStyleSheet(btn_style2)
            
    def load_tasks(self):
        self.tasks = self.controller.load_tasks()
        
        self.update_counters()
        self.update_counters_tags()
        
        for task in self.tasks:
    
            self.create_task(
                task["title"],
                task.get("date"),
                task["done"],
                task["id"],
                task.get("tags", [])
            )
    
    def add_task(self):
        print("executando add_task")
        
        texto = self.input_task.text().strip()
        if texto:
            data = self.input_date.date().toString("yyyy-MM-dd")
            tags = list(self.tags_selecionadas)
            self.controller.add_task(texto, data, tags)
            self.tasks = self.controller.get_tasks()
            
            self.update_counters()
            self.update_counters_tags()
            self.render_tasks()
            
            self.input_task.clear()
            
            for btn in self.tag_buttons.values():
                btn.setChecked(False)
            
            self.conteudo.adjustSize()
            self.conteudo.update()
            
            QTimer.singleShot(50, lambda: 
                self.conteudo_scroll.verticalScrollBar().setValue(
                    self.conteudo_scroll.verticalScrollBar().maximum()
                )
            )
            
    
    def toggle_task(self, task_id, state):
        print("executando toggle_task")
        self.controller.toggle_task(task_id, state)
        self.tasks = self.controller.get_tasks()
        self.update_counters()
        self.update_counters_tags()
        self.render_tasks()
        
        
    def delete_task(self, task_id, widget):
        print("executando delete_task")
        self.controller.delete_task(task_id)
        self.tasks = self.controller.get_tasks()
        
        self.update_counters()
        self.update_counters_tags()
        
        widget.deleteLater()
    
    def create_task(self, title, date=None, done=False, task_id=None, tags=None):
        
        print("executando create_task")
        task_widget = QWidget()
        task_widget.setStyleSheet(conteudo_style)
        task_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) #type: ignore
        task_layout = QHBoxLayout(task_widget)
        task_layout.setContentsMargins(10, 12, 10, 12)
        
        tags = tags or []
        
        btn_delete = QPushButton("🗑")
        btn_delete.setFixedWidth(30)
        btn_delete.clicked.connect(lambda _, tid=task_id, w=task_widget: self.delete_task(tid, w))
        
        checkbox = QCheckBox()
        checkbox.setChecked(done)
        checkbox.setFixedWidth(24)
        checkbox.stateChanged.connect(
            lambda state, tid=task_id: self.toggle_task(tid, state)
        )
        checkbox.setCursor(Qt.PointingHandCursor) #type: ignore
        checkbox.setStyleSheet(btn_style3)
        
        if task_id is None:
            task_id = len(self.tasks) + 1
        
        text_container = QVBoxLayout()
        
        label = QLabel(title)
        label.setWordWrap(True)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred) #type: ignore
        label.setStyleSheet(texto_conteudo)
        
        if done:
            label.setStyleSheet("color: #888; text-decoration: line-through;")
        
        text_container.addWidget(label)
        
        if date:
            data_label = QLabel(str(date))
            data_label.setStyleSheet("color: #4FC3F7; font-size: 11px;")
            text_container.addWidget(data_label)
            
        if tags:
            tags_layout = QHBoxLayout()
            
            for tag in tags:
                cor = tag_colors.get(tag, "#aaaaaa")
                tag_label = QLabel(tag)
                tag_label.setStyleSheet(tag_label_style(cor))
                tags_layout.addWidget(tag_label)
            
            tags_layout.addStretch()
            text_container.addLayout(tags_layout)
        
        task_layout.addWidget(checkbox)
        task_layout.addWidget(btn_delete)
        task_layout.addLayout(text_container)
        task_layout.addStretch()
        
        self.task_list.addWidget(task_widget)
            
# pyinstaller --noconfirm --onefile --windowed --icon=icon.png main.py
# pyinstaller --noconfirm --onefile --windowed --icon=icon.png --distpath "./appcopiler/app" main.py

# TODOAPP_final