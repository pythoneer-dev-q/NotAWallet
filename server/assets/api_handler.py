from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from security import database as db

asset_app = APIRouter()

@asset_app.get('/errs')
async def main_responseWriter():
    return HTMLResponse(
        content="""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Ошибки транзакций</title>
    <style>
        :root {
            --bg-light: #f4f7f9;
            --bg-dark: #121212;
            --text-light: #333;
            --text-dark: #eee;
            --accent-gradient: linear-gradient(90deg, #9b5de5, #f15bb5, #00bbf9, #00f5d4);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-light);
            color: var(--text-light);
            margin: 0;
            padding: 20px;
            transition: all 0.3s ease;
        }

        body.dark {
            background-color: var(--bg-dark);
            color: var(--text-dark);
        }

        h1 {
            text-align: center;
            font-size: 2em;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 3s ease infinite;
        }

        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        table {
            width: 90%;
            margin: 20px auto;
            border-collapse: collapse;
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        body.dark table {
            box-shadow: 0 2px 12px rgba(255,255,255,0.1);
        }

        th, td {
            padding: 12px 20px;
            text-align: left;
        }

        th {
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        tr:nth-child(even) {
            background-color: #f6f8fa;
        }

        body.dark tr:nth-child(even) {
            background-color: #1e1e1e;
        }

        tr:hover {
            background-color: rgba(155, 93, 229, 0.1);
        }

        .description {
            max-width: 500px;
        }

        caption {
            caption-side: top;
            font-size: 1.3em;
            margin-bottom: 10px;
            font-weight: bold;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            color: #888;
        }

        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background: var(--accent-gradient);
            border: none;
            border-radius: 8px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s ease;
        }

        .theme-toggle:hover {
            opacity: 0.85;
        }
    </style>
</head>
<body>
    <button class="theme-toggle" onclick="toggleTheme()">Переключить тему</button>
    <h1>Ошибки транзакций API</h1>
    <table>
        <caption>Список возможных ошибок</caption>
        <thead>
            <tr>
                <th>Код ошибки</th>
                <th>Описание</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>SUM_ERR</td>
                <td class="description">Ошибка суммы: сумма транзакции некорректна или превышает допустимый лимит.</td>
            </tr>
            <tr>
                <td>SRVR_ERR</td>
                <td class="description">Ошибка сервера: внутренняя ошибка на сервере API, повторите запрос позже.</td>
            </tr>
            <tr>
                <td>WLT_NT_EXST</td>
                <td class="description">Кошелек не существует: указанный кошелек отправителя не найден.</td>
            </tr>
            <tr>
                <td>INV_NT_EXST</td>
                <td class="description">Кошелек получателя не существует: указанный кошелек получателя отсутствует.</td>
            </tr>
            <tr>
                <td>ACTIVATED</td>
                <td class="description">Уже активирован: транзакция или функционал уже был использован/активирован ранее.</td>
            </tr>
            <tr>
                <td>USER_ERR</td>
                <td class="description">Ошибка пользователя: введены неверные данные, отсутствует авторизация или неправильно заполнены параметры.</td>
            </tr>
            <tr>
                <td>RESCTRICTED</td>
                <td class="description">Ограничено: доступ к операции заблокирован для данного пользователя или кошелька.</td>
            </tr>
        </tbody>
    </table>
    <footer>
        &copy; 2025 Все права защищены. Объяснения ошибок API для разработчиков.
    </footer>

    <script>
        function toggleTheme() {
            document.body.classList.toggle("dark");
        }
    </script>
</body>
</html>
"""
    )

@asset_app.get('/main')
async def main_Mainget():
    return HTMLResponse(content="""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NotAWallet - Макет кошелька</title>
    <style>
        :root {
            --bg-light: #f4f7f9;
            --bg-dark: #121212;
            --text-light: #333;
            --text-dark: #eee;
            --accent-gradient: linear-gradient(90deg, #9b5de5, #f15bb5, #00bbf9, #00f5d4);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-light);
            color: var(--text-light);
            margin: 0;
            padding: 0;
            transition: all 0.3s ease;
        }

        body.dark {
            background-color: var(--bg-dark);
            color: var(--text-dark);
        }

        header {
            text-align: center;
            padding: 50px 20px 30px;
            background: radial-gradient(circle at top, #9b5de5, #f15bb5);
            color: white;
        }

        header h1 {
            font-size: 3em;
            margin: 0;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 3s ease infinite;
        }

        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        body.dark .card {
            background: rgba(20, 20, 20, 0.95);
            box-shadow: 0 8px 20px rgba(255,255,255,0.05);
        }

        .card h2 {
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.8em;
            margin-bottom: 20px;
        }

        .card p {
            font-size: 1.1em;
            line-height: 1.6em;
        }

        .github-link {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: var(--accent-gradient);
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .github-link:hover {
            opacity: 0.85;
        }

        footer {
            text-align: center;
            padding: 30px 20px;
            color: #888;
        }

        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background: var(--accent-gradient);
            border: none;
            border-radius: 8px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s ease;
        }

        .theme-toggle:hover {
            opacity: 0.85;
        }

        /* Дополнительные детали */
        .blockchain-icon {
            width: 40px;
            height: 40px;
            margin-right: 10px;
            vertical-align: middle;
        }

        .card ul {
            list-style: none;
            padding-left: 0;
        }

        .card ul li {
            margin: 8px 0;
            padding-left: 20px;
            position: relative;
        }

        .card ul li::before {
            content: "⛓️";
            position: absolute;
            left: 0;
        }
    </style>
</head>
<body>
    <button class="theme-toggle" onclick="toggleTheme()">Переключить тему</button>
    <header>
        <h1>NotAWallet</h1>
        <p>Макет кошелька с элементами блокчейна</p>
    </header>
    <div class="container">
        <div class="card">
            <h2>О проекте</h2>
            <p>NotAWallet — это демонстрационный макет криптовалютного кошелька, который показывает базовые элементы блокчейна и работу с транзакциями. 
            Проект не хранит реальные средства и предназначен для обучения и тестирования.</p>
            <p>Особенности проекта:</p>
            <ul>
                <li>Визуализация транзакций</li>
                <li>Эмуляция кошелька пользователя</li>
                <li>Отслеживание статусов транзакций</li>
                <li>Интеграция элементов блокчейна для обучения</li>
            </ul>
            <a class="github-link" href="https://github.com/pythoneer-dev-q/notawallet" target="_blank">GitHub репозиторий</a>
        </div>

        <div class="card">
            <h2>Детали интерфейса</h2>
            <p>Интерфейс демонстрирует:</p>
            <ul>
                <li>Красивый градиент заголовков и кнопок</li>
                <li>Поддержку светлой и тёмной темы</li>
                <li>Анимацию элементов для плавного визуального восприятия</li>
                <li>Иконки и элементы, напоминающие блокчейн-сети</li>
            </ul>
        </div>
    </div>
    <footer>
        &copy; 2025 NotAWallet. Все права защищены. Макет кошелька с элементами блокчейна.
    </footer>

    <script>
        function toggleTheme() {
            document.body.classList.toggle("dark");
        }
    </script>
</body>
</html>
""")



from fastapi.responses import HTMLResponse

@asset_app.get("/server/check/{check_id}", response_class=HTMLResponse)
async def render_check_page(check_id: str):
    data = await db.main_searchCheck(check_UID=check_id)

    if not data:
        return HTMLResponse("<h1>Чек не найден</h1>", status_code=404)

    wallet_from = data.get("wallet_from", "N/A")
    amount = data.get("amount", "0")
    check_id_val = data.get("CHECK_ID", "N/A")
    status = data.get("status", 1)

    status_html = (
        '<div class="status completed"><span class="icon">✅</span> Завершен</div>'
        if status == 2 else
        '<div class="status processing"><span class="icon">⚠️</span> В процессе</div>'
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>NotAWallet | Чек</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          margin: 0; padding: 0;
          background: linear-gradient(135deg, #0f0f1a, #1a0033, #250047);
          color: #fff;
          display: flex; flex-direction: column;
          align-items: center; justify-content: flex-start;
          min-height: 100vh;
        }}
        header {{
          padding: 1rem;
          text-align: center;
          background: rgba(255, 255, 255, 0.05);
          width: 100%;
        }}
        .container {{
          max-width: 500px;
          width: 90%;
          margin-top: 2rem;
          background: rgba(255, 255, 255, 0.08);
          border-radius: 20px;
          padding: 20px;
          box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }}
        h1 {{
          font-size: 1.6rem;
          margin-bottom: 1rem;
          text-align: center;
          background: linear-gradient(90deg, #b16cea, #ff6cab, #6dffff);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }}
        .row {{
          margin: 12px 0;
          display: flex;
          justify-content: space-between;
          font-size: 1rem;
        }}
        .field-label {{
          font-weight: bold;
          color: #aaa;
        }}
        .field-value {{
          font-family: monospace;
          color: #d4a9ff;
        }}
        .divider {{
          height: 1px;
          background: rgba(255, 255, 255, 0.15);
          margin: 10px 0;
          border-radius: 2px;
        }}
        .status {{
          margin-top: 1rem;
          padding: 10px;
          border-radius: 12px;
          font-weight: bold;
          text-align: center;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
        }}
        .completed {{
          background: rgba(0, 255, 150, 0.15);
          color: #00ff99;
        }}
        .processing {{
          background: rgba(255, 140, 0, 0.2);
          color: orange;
        }}
        .icon {{
          font-size: 1.4rem;
        }}
        footer {{
          margin-top: auto;
          padding: 15px;
          font-size: 0.9rem;
          color: #aaa;
          text-align: center;
        }}
        @media(max-width: 600px) {{
          .container {{ padding: 15px; }}
          h1 {{ font-size: 1.4rem; }}
          .row {{ font-size: 0.9rem; }}
        }}
      </style>
    </head>
    <body>
      <header>
        <h2>NotAWallet Explorer</h2>
      </header>
      <div class="container">
        <h1>Информация о Чеке</h1>

        <div class="row"><span class="field-label">Wallet From:</span> <span class="field-value">{wallet_from}</span></div>
        <div class="divider"></div>
        <div class="row"><span class="field-label">Сумма:</span> <span class="field-value">{amount}</span></div>
        <div class="divider"></div>
        <div class="row"><span class="field-label">CHECK_ID:</span> <span class="field-value">{check_id_val}</span></div>
        <div class="divider"></div>

        {status_html}
      </div>
      <footer>
        © 2025 NotAWallet | Блокчейн-макет
      </footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html)



@asset_app.get("/server/invoice/{uid}", response_class=HTMLResponse)
async def render_invoice_page(uid: str):
    data = await db.main_searchInvouce(invouce_UID=uid)

    if not data:
        return HTMLResponse("<h1>Счет не найден</h1>", status_code=404)

    user_id = data.get("user_id", "N/A")
    amount = data.get("amount", "0")
    uid_val = data.get("UID", "N/A")
    status = data.get("status", 1)

    status_html = (
        '<div class="status completed"><span class="icon">✅</span> Завершен</div>'
        if status == 2 else
        '<div class="status processing"><span class="icon">⚠️</span> В процессе</div>'
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>NotAWallet | Счет</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          margin: 0; padding: 0;
          background: linear-gradient(135deg, #0f0f1a, #1a0033, #250047);
          color: #fff;
          display: flex; flex-direction: column;
          align-items: center; justify-content: flex-start;
          min-height: 100vh;
        }}
        header {{
          padding: 1rem;
          text-align: center;
          background: rgba(255, 255, 255, 0.05);
          width: 100%;
        }}
        .container {{
          max-width: 500px;
          width: 90%;
          margin-top: 2rem;
          background: rgba(255, 255, 255, 0.08);
          border-radius: 20px;
          padding: 20px;
          box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }}
        h1 {{
          font-size: 1.6rem;
          margin-bottom: 1rem;
          text-align: center;
          background: linear-gradient(90deg, #b16cea, #ff6cab, #6dffff);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }}
        .row {{
          margin: 12px 0;
          display: flex;
          justify-content: space-between;
          font-size: 1rem;
        }}
        .field-label {{
          font-weight: bold;
          color: #aaa;
        }}
        .field-value {{
          font-family: monospace;
          color: #d4a9ff;
        }}
        .divider {{
          height: 1px;
          background: rgba(255, 255, 255, 0.15);
          margin: 10px 0;
          border-radius: 2px;
        }}
        .status {{
          margin-top: 1rem;
          padding: 10px;
          border-radius: 12px;
          font-weight: bold;
          text-align: center;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
        }}
        .completed {{
          background: rgba(0, 255, 150, 0.15);
          color: #00ff99;
        }}
        .processing {{
          background: rgba(255, 140, 0, 0.2);
          color: orange;
        }}
        .icon {{
          font-size: 1.4rem;
        }}
        footer {{
          margin-top: auto;
          padding: 15px;
          font-size: 0.9rem;
          color: #aaa;
          text-align: center;
        }}
        @media(max-width: 600px) {{
          .container {{ padding: 15px; }}
          h1 {{ font-size: 1.4rem; }}
          .row {{ font-size: 0.9rem; }}
        }}
      </style>
    </head>
    <body>
      <header>
        <h2>NotAWallet Explorer</h2>
      </header>
      <div class="container">
        <h1>Информация о Счете</h1>

        <div class="row"><span class="field-label">User ID:</span> <span class="field-value">{user_id}</span></div>
        <div class="divider"></div>
        <div class="row"><span class="field-label">Сумма:</span> <span class="field-value">{amount}</span></div>
        <div class="divider"></div>
        <div class="row"><span class="field-label">UID:</span> <span class="field-value">{uid_val}</span></div>
        <div class="divider"></div>

        {status_html}
      </div>
      <footer>
        © 2025 NotAWallet | Блокчейн-макет
      </footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

