# RESPONSÁVEL APENAS PELA EXECUÇÃO DO SERVIDOR

from src.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()