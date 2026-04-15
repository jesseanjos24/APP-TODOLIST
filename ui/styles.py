
menu =  '''
    background: #f3f0f0; 
'''

topbar = '''
    background: #53c2e4;
'''

background = '''
    background-color: #ffffff;
'''

janela = """
    QMainWindow {
        background-color: #ffffff;
        font-size: 35px;
    }
    
    QMenuBar {
        background-color: #ffffff;
        color: #202020;
        font-size: 15px;
        font-weight: bold;
        padding: 5px;
    }

    QMenuBar::item {
        padding: 5px 15px;
        background: transparent;
    }

    QMenuBar::item:selected {
        background-color: #3a90c0;
        border-radius: 4px;
    }
"""

btn_style = """
    QPushButton {
        background: transparent;
        color: white;
        font-size: 17px;
        font-weight: bolder;
        border: none;
        width: 40px;
        height: 40px;
        border-radius: 20px;
        padding: 0px;
        text-align: center;
    }
    
    QPushButton:hover { background-color: rgba(255, 255, 255, 0.445); }
"""

btn_style2 = """
    QPushButton {
            background: transparent;
            color: #202020;
            font-size: 14px;
            border: none;
            height: 30px;
            border-radius: 15px;
            padding: 10px;
            text-align: left;
        }
        
    QPushButton:hover { background-color: rgba(78, 220, 255, 0.445); }
    
    QLineEdit {
        background: transparent;
        border-radius: 15px;
        padding: 5px 15px;
        font-size: 16px;
        color: #202020;
    }
    
    QLineEdit:focus {
        border-bottom: 1px solid #cf0acf;
    }
"""

btn_style3 = """

    QCheckBox::indicator {
        width: 13px;
        height: 13px;
        border: 1px solid #aaaaaa;
        border-radius: 9px;
        padding: 2px;
    }
    
    QCheckBox::indicator:checked {
        background-color: #4EABDF;
        border: 2px solid #4EABDF;
    }
    
"""

splitter_style = """
    QSplitter::handle {
        background-color: transparent;
        width: 1px;
    }
"""

scroll_style = """
    QScrollArea { border: none; background: transparent; }
    QScrollBar:vertical {
        width: 6px;
        background: transparent;
    }
    QScrollBar::handle:vertical {
        background: #aaaaaa;
        border-radius: 3px;
    }
"""
titulo_lista = """
    font-size: 22px;
    font-weight: bold;
    color: #202020;
"""

texto_conteudo = """
    background: transparent;
    font-size: 16px;
    color: #202020;
    border: none;
"""

conteudo_style = '''
    background-color: #ffffff;
    border: none;
    border-bottom: 1px solid #ebebeb;
    color: #202020;
    padding: 4px 8px 4px 0px;
'''

calendar_style = '''
    QDateEdit {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 4px 10px;
        font-size: 14px;
        color: #202020;
    }
    
    QDateEdit:focus {
        border: 1px solid #4EABDF;
    }
    
    QDateEdit::drop-down {
        border: none;
        width: 24px;
    }
    
    QDateEdit::down-arrow {
        image: none;
        width: 0;
        height: 0;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 5px solid #4EABDF;
    }

    QCalendarWidget {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
    }

    QCalendarWidget QToolButton {
        background-color: transparent;
        color: #202020;
        font-size: 14px;
        font-weight: bold;
        border: none;
        padding: 6px;
        border-radius: 6px;
    }

    QCalendarWidget QToolButton:hover {
        background-color: #e8f4fb;
        color: #4EABDF;
    }

    QCalendarWidget QMenu {
        background-color: #ffffff;
        color: #202020;
        font-size: 13px;
    }

    QCalendarWidget QSpinBox {
        background-color: #ffffff;
        color: #202020;
        font-size: 13px;
        border: none;
    }

    QCalendarWidget QAbstractItemView {
        background-color: #ffffff;
        color: #202020;
        selection-background-color: #4EABDF;
        selection-color: #ffffff;
        font-size: 13px;
        gridline-color: transparent;
        outline: none;
    }

    QCalendarWidget QAbstractItemView:enabled {
        color: #202020;
    }

    QCalendarWidget QAbstractItemView:disabled {
        color: #cccccc;
    }

    QCalendarWidget #qt_calendar_navigationbar {
        background-color: #4EABDF;
        border-radius: 8px;
        padding: 4px;
    }

    QCalendarWidget #qt_calendar_navigationbar QToolButton {
        color: #202020;
    }
'''

btn_sort_sty = """
    QPushButton {
        background-color: #2b2d31;
        color: #e8eaed;
        border: 1px solid #3c4043;
        border-radius: 6px;
        padding: 6px 12px;
        font-size: 13px;
    }

    QPushButton:hover {
        background-color: #3c4043;
    }

    QPushButton:pressed {
        background-color: #1e1f22;
    }

    QPushButton:focus {
        border: 1px solid #4FC3F7;
}
"""

def btns_tags_styles(cor):
    
    return f"""
        QPushButton {{
            background: transparent;
            border: 1px solid {cor};
            border-radius: 10px;
            color: {cor};
            padding: 2px 10px;
            font-size: 12px;
        }}
        QPushButton:checked {{
            background-color: {cor};
            color: white;
        }}
    """

def tag_label_style(cor):
    return f"""
        background-color: {cor};
        color: white;
        border-radius: 8px;
        padding: 1px 8px;
        font-size: 11px;
    """

tag_colors = {
    "Trabalho": "#FF7043",
    "Pessoal":  "#4EABDF",
    "Lazer":    "#66BB6A",
    "Estudo":   "#f72ea3",
    "Dia A Dia": "#ff000d",
}