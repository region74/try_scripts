from flask import Flask, render_template, request
import os

# Создаем экземпляр приложения
app = Flask(__name__)

# Функция для получения списка файлов и папок по заданному пути
def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # Обрезаем начальную часть пути для каждого элемента списка
            relative_path = os.path.relpath(os.path.join(root, file), path)
            file_list.append(relative_path)
        for dir in dirs:
            relative_path = os.path.relpath(os.path.join(root, dir), path)
            file_list.append(relative_path)
    return file_list

# Определяем маршрут для одной страницы
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    link = 'C:\\Users\\Кирилл\\Documents\\Zoom'
    if request.method == 'POST':
        file_list = get_file_list(link)
        # Преобразуем список в HTML-строку
        file_list_html = "<ul>"
        for item in file_list:
            file_list_html += f"<li>{item}</li>"
        file_list_html += "</ul>"
        return file_list_html
    return render_template('index.html')

# Запускаем приложение, если скрипт запускается напрямую, а не импортируется
if __name__ == '__main__':
    app.run()
