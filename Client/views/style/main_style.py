# Styling constants
PRIMARY_COLOR = '#2C3E50'  # Dark blue-gray
SECONDARY_COLOR = '#34495E'  # Slightly lighter blue-gray
ACCENT_COLOR = '#3498DB'  # Bright blue
BACKGROUND_COLOR = '#ECF0F1'  # Light gray-white
TEXT_COLOR = '#2C3E50'  # Dark text color
HOVER_COLOR = '#BDC3C7'  # Light gray for hover effects

def apply_global_style(app):
    """
    Apply a professional, clean style to the entire application.
    
    Args:
        app (QApplication): The main application instance
    """
    global_style = f'''
    /* Global Application Style */
    QWidget {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
        font-family: 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
        font-size: 14px;
    }}
    
    /* Main Window Styling */
    QMainWindow {{
        background-color: {BACKGROUND_COLOR};
    }}
    
    /* Sidebar Styling */
    QListWidget {{
        background-color: {SECONDARY_COLOR};
        color: white;
        border: none;
        padding: 10px;
        border-right: 1px solid {PRIMARY_COLOR};
    }}
    
    QListWidget::item {{
        background-color: {SECONDARY_COLOR};
        color: white;
        padding: 8px;
        margin: 2px;
        border-radius: 4px;
    }}
    
    QListWidget::item:selected {{
        background-color: {ACCENT_COLOR};
        color: white;
    }}
    
    QListWidget::item:hover {{
        background-color: {HOVER_COLOR};
        color: {TEXT_COLOR};
    }}
    
    /* Status Bar Styling */
    QLabel {{
        background-color: {PRIMARY_COLOR};
        color: white;
        padding: 8px;
        border-top: 1px solid {SECONDARY_COLOR};
        font-weight: bold;
        border-radius: 20px;
        margin: 5px;
    }}
    
    /* Buttons Styling */
    QPushButton {{
        background-color: {ACCENT_COLOR};
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
    }}
    
    QPushButton:hover {{
        background-color: {SECONDARY_COLOR};
    }}
    
    /* Input Fields Styling */
    QLineEdit, QTextEdit, QComboBox {{
        background-color: white;
        border: 1px solid {HOVER_COLOR};
        border-radius: 4px;
        padding: 6px;
    }}
    
    QLineEdit:focus, QTextEdit:focus, QComboBox:focus {{
        border-color: {ACCENT_COLOR};
        outline: none;
    }}
    '''
    
    # Apply the style to the application
    app.setStyleSheet(global_style)

def configure_main_window(main_window):
    """
    Additional configuration for the main window.
    
    Args:
        main_window (MainWindow): The main application window
    """
    # Set window icon (you'll need to replace 'path/to/icon.png' with your actual icon path)
    # main_window.setWindowIcon(QIcon('path/to/icon.png'))
    
    # Add some additional styling properties
    main_window.setStyleSheet('''
        QMainWindow {
            background-color: #ECF0F1;
        }
    ''')