from flask import Flask, url_for, request

app = Flask(__name__)


# Колонизация Марса
@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


# Рекламная кампания
@app.route('/promotion')
def promotion():
    a_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(a_list)


# Изображение Марса
@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}">
                        <p>Вот она какая, красная планета.</p>
                    </body>
                </html>"""


# Реклама с картинкой
@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <div class="alert alert-danger" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-info" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


# Отбор астронавтов
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <p>Просим заполнить все поля</p>
                                    <p></p>
                                    <input type="lastname" class="form-control" id="lastname" placeholder="Введите фамилию" name="lastname">
                                    <p></p>
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Бакалавриат</option>
                                          <option>Магистратура</option>
                                          <option>Специалитет</option>
                                          <option>Подготовка кадров высшей квалификации</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Выбор основной профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="isled" value="isled" checked>
                                          <label class="form-check-label" for="isled">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="terra" value="terra">
                                          <label class="form-check-label" for="terra">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="eczo" value="eczo">
                                          <label class="form-check-label" for="eczo">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="clim" value="clim">
                                          <label class="form-check-label" for="clim">
                                            климатолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Какова ваша мотивация?</label>
                                        <textarea class="form-control" id="motiv" rows="3" name="motiv"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['lastname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['motiv'])
        print(request.form['accept'])
        return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Форма отправлена</title>
                  </head>
                  <body>
                    <div class="alert alert-success" role="alert">
                      Форма отправлена
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
