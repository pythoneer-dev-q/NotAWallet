from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse
from security import database as db
from typing import Optional

asset_app = APIRouter()

@asset_app.get('/')
async def main_checkMan(call: Optional[str] = Query(None)):
    if not call:
        return HTMLResponse(content=f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Проверка на человека | NotAWallet</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --accent: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --bg: #f8fafc;
            --text: #1e293b;
            --card-bg: rgba(255, 255, 255, 0.9);
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: background 0.3s ease;
            overflow: hidden;
        }}

        .card {{
            background: var(--card-bg);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border: 1px solid rgba(226,232,240,0.8);
            opacity: 0;
            transform: translateY(20px);
            animation: fadeIn 1s forwards 1s;
        }}

        @keyframes fadeIn {{
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .loader {{
            position: absolute;
            width: 60px;
            height: 60px;
            border: 6px solid rgba(102,126,234,0.3);
            border-top-color: #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}

        h2 {{
            background: var(--accent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 12px;
        }}

        p {{
            color: #475569;
            margin-bottom: 20px;
        }}

        .checkbox-container {{
            margin: 15px 0;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }}

        input[type="checkbox"] {{
            width: 18px;
            height: 18px;
            cursor: pointer;
        }}

        button {{
            background: var(--accent);
            border: none;
            color: white;
            padding: 12px 28px;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }}

        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(102, 126, 234, 0.3);
        }}

        button[disabled] {{
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }}

        .honeypot {{
            position: absolute;
            left: -9999px;
        }}
    </style>
</head>
<body>
    <div class="loader" id="loader"></div>
    <div class="card" id="mainCard">
        <h2>Проверка на человека</h2>
        <p>Подтвердите, что вы не робот, чтобы продолжить.</p>

        <div class="checkbox-container">
            <input id="humanCheckbox" type="checkbox">
            <label for="humanCheckbox">Я не робот</label>
        </div>

        <div class="honeypot">
            <label>Телефон (не заполнять)</label>
            <input id="hp" name="phone_hp" autocomplete="off">
        </div>

        <button id="goBtn" disabled>Далее</button>

        <p style="font-size:12px; color:#94a3b8; margin-top:12px;">
            Проверка предотвращает автоматические переходы.
        </p>
    </div>

    <script>
        const loader = document.getElementById('loader');
        const card = document.getElementById('mainCard');
        const cb = document.getElementById('humanCheckbox');
        const btn = document.getElementById('goBtn');
        const hp = document.getElementById('hp');
        const redirectUrl = "https://notawallet.sbs/main";

        window.addEventListener('load', () => {{
            loader.style.display = 'none';
            card.style.display = 'block';
        }});

        cb.addEventListener('change', () => {{
            btn.disabled = !cb.checked;
        }});

        btn.addEventListener('click', () => {{
            if (hp.value.trim() !== "") {{
                alert("Проверка не пройдена.");
                return;
            }}
            btn.innerHTML = '<div class="loader" style="width:20px;height:20px;border-width:3px;"></div> Перенаправление...';
            setTimeout(() => {{
                window.location.href = redirectUrl;
            }}, 1000);
        }});
    </script>
</body>
</html>
""", status_code=200)
    return HTMLResponse(content=f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Проверка на человека | NotAWallet</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --accent: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --bg: #f8fafc;
            --text: #1e293b;
            --card-bg: rgba(255, 255, 255, 0.9);
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: background 0.3s ease;
            overflow: hidden;
        }}

        .card {{
            background: var(--card-bg);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border: 1px solid rgba(226,232,240,0.8);
            opacity: 0;
            transform: translateY(20px);
            animation: fadeIn 1s forwards 1s;
        }}

        @keyframes fadeIn {{
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .loader {{
            position: absolute;
            width: 60px;
            height: 60px;
            border: 6px solid rgba(102,126,234,0.3);
            border-top-color: #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}

        h2 {{
            background: var(--accent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 12px;
        }}

        p {{
            color: #475569;
            margin-bottom: 20px;
        }}

        .checkbox-container {{
            margin: 15px 0;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }}

        input[type="checkbox"] {{
            width: 18px;
            height: 18px;
            cursor: pointer;
        }}

        button {{
            background: var(--accent);
            border: none;
            color: white;
            padding: 12px 28px;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }}

        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(102, 126, 234, 0.3);
        }}

        button[disabled] {{
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }}

        .honeypot {{
            position: absolute;
            left: -9999px;
        }}
    </style>
</head>
<body>
    <div class="loader" id="loader"></div>
    <div class="card" id="mainCard">
        <h2>Проверка на человека</h2>
        <p>Подтвердите, что вы не робот, чтобы продолжить.</p>

        <div class="checkbox-container">
            <input id="humanCheckbox" type="checkbox">
            <label for="humanCheckbox">Я не робот</label>
        </div>

        <div class="honeypot">
            <label>Телефон (не заполнять)</label>
            <input id="hp" name="phone_hp" autocomplete="off">
        </div>

        <button id="goBtn" disabled>Далее</button>

        <p style="font-size:12px; color:#94a3b8; margin-top:12px;">
            Проверка предотвращает автоматические переходы.
        </p>
    </div>

    <script>
        const loader = document.getElementById('loader');
        const card = document.getElementById('mainCard');
        const cb = document.getElementById('humanCheckbox');
        const btn = document.getElementById('goBtn');
        const hp = document.getElementById('hp');
        const redirectUrl = "https://notawallet.sbs{call}";

        window.addEventListener('load', () => {{
            loader.style.display = 'none';
            card.style.display = 'block';
        }});

        cb.addEventListener('change', () => {{
            btn.disabled = !cb.checked;
        }});

        btn.addEventListener('click', () => {{
            if (hp.value.trim() !== "") {{
                alert("Проверка не пройдена.");
                return;
            }}
            btn.innerHTML = '<div class="loader" style="width:20px;height:20px;border-width:3px;"></div> Перенаправление...';
            setTimeout(() => {{
                window.location.href = redirectUrl;
            }}, 1000);
        }});
    </script>
</body>
</html>
""", status_code=200)
    
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
    <title>NotAWallet - Криптовалютный кошелек</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-light: #f8fafc;
            --bg-dark: #0f172a;
            --text-light: #1e293b;
            --text-dark: #f1f5f9;
            --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            --card-bg-light: rgba(255, 255, 255, 0.9);
            --card-bg-dark: rgba(30, 41, 59, 0.9);
            --border-light: rgba(226, 232, 240, 0.8);
            --border-dark: rgba(51, 65, 85, 0.8);
            --shadow-light: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-dark: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-light);
            color: var(--text-light);
            line-height: 1.6;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            overflow-x: hidden;
        }

        body.dark {
            background: var(--bg-dark);
            color: var(--text-dark);
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            padding: 60px 20px 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }

        header h1 {
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 700;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #ffffff, #f0f9ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            position: relative;
            z-index: 1;
            animation: float 3s ease-in-out infinite;
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }

        @keyframes float {

            0%,
            100% {
                transform: translateY(0px);
            }

            50% {
                transform: translateY(-10px);
            }
        }

        .nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border-light);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        body.dark .nav {
            background: rgba(15, 23, 42, 0.95);
            border-bottom-color: var(--border-dark);
        }

        .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 60px;
        }

        .logo {
            font-weight: 700;
            font-size: 1.2rem;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }


        .theme-toggle {
            background: var(--accent-gradient);
            border: none;
            border-radius: 50px;
            padding: 8px 16px;
            color: white;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .theme-toggle:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .card {
            background: var(--card-bg-light);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-light);
            border: 1px solid var(--border-light);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        body.dark .card {
            background: var(--card-bg-dark);
            box-shadow: var(--shadow-dark);
            border-color: var(--border-dark);
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }

        body.dark .card:hover {
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
        }

        .card h2 {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 20px;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .card p {
            font-size: 1.1rem;
            line-height: 1.7;
            margin-bottom: 15px;
            color: var(--text-light);
        }

        body.dark .card p {
            color: var(--text-dark);
        }

        .wallet-features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .feature-card {
            background: var(--card-bg-light);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            border: 1px solid var(--border-light);
            transition: all 0.3s ease;
            position: relative;
        }

        body.dark .feature-card {
            background: var(--card-bg-dark);
            border-color: var(--border-dark);
        }

        .feature-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-light);
        }

        body.dark .feature-card:hover {
            box-shadow: var(--shadow-dark);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .feature-card h3 {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: var(--text-light);
        }

        body.dark .feature-card h3 {
            color: var(--text-dark);
        }

        .feature-card p {
            font-size: 0.95rem;
            opacity: 0.8;
        }



        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            border: none;
            border-radius: 10px;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .btn-primary {
            background: var(--accent-gradient);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: transparent;
            border: 2px solid var(--accent-gradient);
            color: var(--text-light);
        }

        body.dark .btn-secondary {
            color: var(--text-dark);
        }

        .btn-secondary:hover {
            background: var(--accent-gradient);
            color: white;
        }

        .card ul {
            list-style: none;
            padding: 0;
        }

        .card ul li {
            margin: 12px 0;
            padding-left: 25px;
            position: relative;
            font-size: 1rem;
        }

        .card ul li::before {
            content: "🔗";
            position: absolute;
            left: 0;
            top: 0;
        }

        footer {
            background: var(--card-bg-light);
            border-top: 1px solid var(--border-light);
            text-align: center;
            padding: 40px 20px;
            margin-top: 60px;
        }

        body.dark footer {
            background: var(--card-bg-dark);
            border-top-color: var(--border-dark);
        }

        footer p {
            color: var(--text-light);
            opacity: 0.7;
        }

        body.dark footer p {
            color: var(--text-dark);
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px 15px;
            }

            .card {
                padding: 20px;
                margin-bottom: 20px;
            }

            .wallet-features {
                grid-template-columns: 1fr;
            }
        }

        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, .3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--bg-light);
        }

        body.dark ::-webkit-scrollbar-track {
            background: var(--bg-dark);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--accent-gradient);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #5a67d8 0%, #667eea 100%);
        }
    </style>
</head>

<body>
    <nav class="nav">
        <div class="nav-content">
            <div class="logo">NotAWallet</div>
            <button class="theme-toggle" onclick="toggleTheme()">
                <i class="fas fa-moon"></i>
                <span>Тема</span>
            </button>
        </div>
    </nav>

    <header>
        <h1>NotAWallet</h1>
        <p>Современный криптовалютный кошелек с интуитивным интерфейсом</p>
    </header>

    <div class="container">

        <div class="card">
            <h2><i class="fas fa-wallet"></i> Функции кошелька</h2>
            <div class="wallet-features">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-paper-plane"></i>
                    </div>
                    <h3>Отправка</h3>
                    <p>Быстрая и безопасная отправка криптовалют</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-download"></i>
                    </div>
                    <h3>Получение</h3>
                    <p>Получение средств на ваш адрес</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-history"></i>
                    </div>
                    <h3>История</h3>
                    <p>Просмотр всех транзакций</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h3>Безопасность</h3>
                    <p>Защита ваших средств</p>
                </div>
            </div>
        </div>



        <div class="card">
            <h2><i class="fas fa-info-circle"></i> О проекте</h2>
            <p>NotAWallet — это демонстрационный макет криптовалютного кошелька, который показывает базовые элементы
                блокчейна и работу с транзакциями.
                Проект не хранит реальные средства и предназначен для обучения и тестирования.</p>
            <p>Особенности проекта:</p>
            <ul>
                <li>Визуализация транзакций в реальном времени</li>
                <li>Эмуляция кошелька пользователя</li>
                <li>Отслеживание статусов транзакций</li>
                <li>Интеграция элементов блокчейна для обучения</li>
                <li>Современный адаптивный дизайн</li>
                <li>Поддержка светлой и тёмной темы</li>
            </ul>
            <a href="https://github.com/pythoneer-dev-q/notawallet" target="_blank" class="btn btn-primary">
                <i class="fab fa-github"></i>
                GitHub репозиторий
            </a>
        </div>

        <div class="card">
            <h2><i class="fas fa-cogs"></i> Технические детали</h2>
            <p>Интерфейс демонстрирует современные веб-технологии:</p>
            <ul>
                <li>CSS Grid и Flexbox для адаптивной верстки</li>
                <li>CSS Custom Properties для темизации</li>
                <li>Плавные анимации и переходы</li>
                <li>Backdrop-filter для эффекта размытия</li>
                <li>Градиенты и современная типографика</li>
                <li>Интерактивные элементы с hover-эффектами</li>
            </ul>
        </div>
    </div>


    <footer>
        <p>&copy; 2025 NotAWallet. Все права защищены. Демонстрационный макет криптовалютного кошелька.</p>
    </footer>

    <script>
        function toggleTheme() {
            document.body.classList.toggle("dark");
            const themeIcon = document.querySelector('.theme-toggle i');
            const themeText = document.querySelector('.theme-toggle span');

            if (document.body.classList.contains('dark')) {
                themeIcon.className = 'fas fa-sun';
                themeText.textContent = 'Светлая';
            } else {
                themeIcon.className = 'fas fa-moon';
                themeText.textContent = 'Темная';
            }
        }

        window.addEventListener('scroll', function () {
            const nav = document.querySelector('.nav');
            if (window.scrollY > 100) {
                nav.style.background = document.body.classList.contains('dark')
                    ? 'rgba(15, 23, 42, 0.98)'
                    : 'rgba(255, 255, 255, 0.98)';
            } else {
                nav.style.background = document.body.classList.contains('dark')
                    ? 'rgba(15, 23, 42, 0.95)'
                    : 'rgba(255, 255, 255, 0.95)';
            }
        });

        document.querySelectorAll('.feature-card').forEach(card => {
            card.addEventListener('mouseenter', function () {
                this.style.transform = 'translateY(-5px) scale(1.02)';
            });

            card.addEventListener('mouseleave', function () {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });
    </script>
</body>

</html>
""")


@asset_app.get("/server/check/{check_id}", response_class=HTMLResponse)
async def render_check_page(check_id: str):
    data = await db.main_searchCheck(check_UID=check_id)

    if not data or data == 'SRVR_ERR':
        return HTMLResponse("""<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ошибка 404 - NotAWallet</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-light: #f8fafc;
            --bg-dark: #0f172a;
            --text-light: #1e293b;
            --text-dark: #f1f5f9;
            --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --error-gradient: linear-gradient(135deg, #ef4444 0%, #f97316 100%);
            --card-bg-light: rgba(255, 255, 255, 0.9);
            --card-bg-dark: rgba(30, 41, 59, 0.9);
            --border-light: rgba(226, 232, 240, 0.8);
            --border-dark: rgba(51, 65, 85, 0.8);
            --shadow-light: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-dark: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-light);
            color: var(--text-light);
            line-height: 1.6;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            overflow-x: hidden;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        body.dark {
            background: var(--bg-dark);
            color: var(--text-dark);
        }

        .nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border-light);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        body.dark .nav {
            background: rgba(15, 23, 42, 0.95);
            border-bottom-color: var(--border-dark);
        }

        .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 60px;
        }

        .logo {
            font-weight: 700;
            font-size: 1.2rem;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .theme-toggle {
            background: var(--accent-gradient);
            border: none;
            border-radius: 50px;
            padding: 8px 16px;
            color: white;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .theme-toggle:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .main-content {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 100px 20px 40px;
        }

        .error-container {
            max-width: 600px;
            text-align: center;
        }

        .error-icon {
            font-size: 8rem;
            margin-bottom: 30px;
            background: var(--error-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {

            0%,
            100% {
                transform: translateY(0px);
            }

            50% {
                transform: translateY(-10px);
            }
        }

        .error-code {
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 20px;
            background: var(--error-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .error-message {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 15px;
            color: var(--text-light);
        }

        body.dark .error-message {
            color: var(--text-dark);
        }

        .error-description {
            font-size: 1.1rem;
            margin-bottom: 40px;
            opacity: 0.8;
            color: var(--text-light);
        }

        body.dark .error-description {
            color: var(--text-dark);
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            border: none;
            border-radius: 10px;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
            margin: 0 10px;
        }

        .btn-primary {
            background: var(--accent-gradient);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: transparent;
            border: 2px solid var(--accent-gradient);
            color: var(--text-light);
        }

        body.dark .btn-secondary {
            color: var(--text-dark);
        }

        .btn-secondary:hover {
            background: var(--accent-gradient);
            color: white;
        }

        .suggestions {
            margin-top: 50px;
            padding: 30px;
            background: var(--card-bg-light);
            border-radius: 20px;
            box-shadow: var(--shadow-light);
            border: 1px solid var(--border-light);
        }

        body.dark .suggestions {
            background: var(--card-bg-dark);
            box-shadow: var(--shadow-dark);
            border-color: var(--border-dark);
        }

        .suggestions h3 {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 20px;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .suggestions ul {
            list-style: none;
            padding: 0;
            text-align: left;
        }

        .suggestions li {
            margin: 10px 0;
            padding-left: 25px;
            position: relative;
            font-size: 1rem;
        }

        .suggestions li::before {
            content: "💡";
            position: absolute;
            left: 0;
            top: 0;
        }

        footer {
            background: var(--card-bg-light);
            border-top: 1px solid var(--border-light);
            text-align: center;
            padding: 40px 20px;
        }

        body.dark footer {
            background: var(--card-bg-dark);
            border-top-color: var(--border-dark);
        }

        footer p {
            color: var(--text-light);
            opacity: 0.7;
        }

        body.dark footer p {
            color: var(--text-dark);
        }

        @media (max-width: 768px) {
            .error-icon {
                font-size: 6rem;
            }

            .error-code {
                font-size: 3rem;
            }

            .error-message {
                font-size: 1.3rem;
            }

            .btn {
                margin: 5px;
                padding: 10px 20px;
            }

            .suggestions {
                padding: 20px;
            }
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--bg-light);
        }

        body.dark ::-webkit-scrollbar-track {
            background: var(--bg-dark);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--accent-gradient);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #5a67d8 0%, #667eea 100%);
        }
    </style>
</head>

<body>
    <nav class="nav">
        <div class="nav-content">
            <div class="logo">NotAWallet</div>
            <button class="theme-toggle" onclick="toggleTheme()">
                <i class="fas fa-moon"></i>
                <span>Тема</span>
            </button>
        </div>
    </nav>

    <div class="main-content">
        <div class="error-container">
            <div class="error-icon">
                <i class="fas fa-exclamation-triangle"></i>
            </div>

            <div class="error-code">404</div>

            <h1 class="error-message">Страница не найдена</h1>

            <p class="error-description">
                К сожалению, запрашиваемая страница не существует или была перемещена.
            </p>

            <div class="buttons">
                <a href="https://notawallet.sbs/main" class="btn btn-primary">
                    <i class="fas fa-home"></i>
                    На главную
                </a>
                <button class="btn btn-secondary" onclick="goBack()">
                    <i class="fas fa-arrow-left"></i>
                    Назад
                </button>
            </div>

            <div class="suggestions">
                <h3><i class="fas fa-lightbulb"></i> Что можно сделать:</h3>
                <ul>
                    <li>Проверьте правильность URL-адреса</li>
                    <li>Вернитесь на главную страницу</li>
                    <li>Используйте навигационное меню</li>
                    <li>Попробуйте обновить страницу</li>
                </ul>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 NotAWallet. Все права защищены. Демонстрационный макет криптовалютного кошелька.</p>
    </footer>

    <script>
        function toggleTheme() {
            document.body.classList.toggle("dark");
            const themeIcon = document.querySelector('.theme-toggle i');
            const themeText = document.querySelector('.theme-toggle span');

            if (document.body.classList.contains('dark')) {
                themeIcon.className = 'fas fa-sun';
                themeText.textContent = 'Светлая';
            } else {
                themeIcon.className = 'fas fa-moon';
                themeText.textContent = 'Темная';
            }
        }

        function goBack() {
            if (window.history.length > 1) {
                window.history.back();
            } else {
                window.location.href = 'index.html';
            }
        }

        window.addEventListener('scroll', function () {
            const nav = document.querySelector('.nav');
            if (window.scrollY > 100) {
                nav.style.background = document.body.classList.contains('dark')
                    ? 'rgba(15, 23, 42, 0.98)'
                    : 'rgba(255, 255, 255, 0.98)';
            } else {
                nav.style.background = document.body.classList.contains('dark')
                    ? 'rgba(15, 23, 42, 0.95)'
                    : 'rgba(255, 255, 255, 0.95)';
            }
        });

        document.addEventListener('DOMContentLoaded', function () {
            const errorIcon = document.querySelector('.error-icon');
            errorIcon.style.opacity = '0';
            errorIcon.style.transform = 'scale(0.5)';

            setTimeout(() => {
                errorIcon.style.transition = 'all 0.5s ease';
                errorIcon.style.opacity = '1';
                errorIcon.style.transform = 'scale(1)';
            }, 200);

            const errorCode = document.querySelector('.error-code');
            errorCode.style.opacity = '0';
            errorCode.style.transform = 'translateY(20px)';

            setTimeout(() => {
                errorCode.style.transition = 'all 0.5s ease';
                errorCode.style.opacity = '1';
                errorCode.style.transform = 'translateY(0)';
            }, 400);

            const errorMessage = document.querySelector('.error-message');
            errorMessage.style.opacity = '0';
            errorMessage.style.transform = 'translateY(20px)';

            setTimeout(() => {
                errorMessage.style.transition = 'all 0.5s ease';
                errorMessage.style.opacity = '1';
                errorMessage.style.transform = 'translateY(0)';
            }, 600);
        });
    </script>
</body>

</html>""", status_code=404)

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

    if not data or data == 'SRVR_ERR':
        return HTMLResponse("""<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ошибка 404 - NotAWallet</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-light: #f8fafc;
            --bg-dark: #0f172a;
            --text-light: #1e293b;
            --text-dark: #f1f5f9;
            --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --error-gradient: linear-gradient(135deg, #ef4444 0%, #f97316 100%);
            --card-bg-light: rgba(255, 255, 255, 0.9);
            --card-bg-dark: rgba(30, 41, 59, 0.9);
            --border-light: rgba(226, 232, 240, 0.8);
            --border-dark: rgba(51, 65, 85, 0.8);
            --shadow-light: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-dark: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-light);
            color: var(--text-light);
            line-height: 1.6;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            overflow-x: hidden;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        body.dark {
            background: var(--bg-dark);
            color: var(--text-dark);
        }

        .nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border-light);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        body.dark .nav {
            background: rgba(15, 23, 42, 0.95);
            border-bottom-color: var(--border-dark);
        }

        .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 60px;
        }

        .logo {
            font-weight: 700;
            font-size: 1.2rem;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .theme-toggle {
            background: var(--accent-gradient);
            border: none;
            border-radius: 50px;
            padding: 8px 16px;
            color: white;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .theme-toggle:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .main-content {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 100px 20px 40px;
        }

        .error-container {
            max-width: 600px;
            text-align: center;
        }

        .error-icon {
            font-size: 8rem;
            margin-bottom: 30px;
            background: var(--error-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {

            0%,
            100% {
                transform: translateY(0px);
            }

            50% {
                transform: translateY(-10px);
            }
        }

        .error-code {
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 20px;
            background: var(--error-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .error-message {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 15px;
            color: var(--text-light);
        }

        body.dark .error-message {
            color: var(--text-dark);
        }

        .error-description {
            font-size: 1.1rem;
            margin-bottom: 40px;
            opacity: 0.8;
            color: var(--text-light);
        }

        body.dark .error-description {
            color: var(--text-dark);
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            border: none;
            border-radius: 10px;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
            margin: 0 10px;
        }

        .btn-primary {
            background: var(--accent-gradient);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: transparent;
            border: 2px solid var(--accent-gradient);
            color: var(--text-light);
        }

        body.dark .btn-secondary {
            color: var(--text-dark);
        }

        .btn-secondary:hover {
            background: var(--accent-gradient);
            color: white;
        }

        .suggestions {
            margin-top: 50px;
            padding: 30px;
            background: var(--card-bg-light);
            border-radius: 20px;
            box-shadow: var(--shadow-light);
            border: 1px solid var(--border-light);
        }

        body.dark .suggestions {
            background: var(--card-bg-dark);
            box-shadow: var(--shadow-dark);
            border-color: var(--border-dark);
        }

        .suggestions h3 {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 20px;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .suggestions ul {
            list-style: none;
            padding: 0;
            text-align: left;
        }

        .suggestions li {
            margin: 10px 0;
            padding-left: 25px;
            position: relative;
            font-size: 1rem;
        }

        .suggestions li::before {
            content: "💡";
            position: absolute;
            left: 0;
            top: 0;
        }

        footer {
            background: var(--card-bg-light);
            border-top: 1px solid var(--border-light);
            text-align: center;
            padding: 40px 20px;
        }

        body.dark footer {
            background: var(--card-bg-dark);
            border-top-color: var(--border-dark);
        }

        footer p {
            color: var(--text-light);
            opacity: 0.7;
        }

        body.dark footer p {
            color: var(--text-dark);
        }

        @media (max-width: 768px) {
            .error-icon {
                font-size: 6rem;
            }

            .error-code {
                font-size: 3rem;
            }

            .error-message {
                font-size: 1.3rem;
            }

            .btn {
                margin: 5px;
                padding: 10px 20px;
            }

            .suggestions {
                padding: 20px;
            }
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--bg-light);
        }

        body.dark ::-webkit-scrollbar-track {
            background: var(--bg-dark);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--accent-gradient);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #5a67d8 0%, #667eea 100%);
        }
    </style>
</head>

<body>
    <nav class="nav">
        <div class="nav-content">
            <div class="logo">NotAWallet</div>
            <button class="theme-toggle" onclick="toggleTheme()">
                <i class="fas fa-moon"></i>
                <span>Тема</span>
            </button>
        </div>
    </nav>

    <div class="main-content">
        <div class="error-container">
            <div class="error-icon">
                <i class="fas fa-exclamation-triangle"></i>
            </div>

            <div class="error-code">404</div>

            <h1 class="error-message">Страница не найдена</h1>

            <p class="error-description">
                К сожалению, запрашиваемая страница не существует или была перемещена.
            </p>

            <div class="buttons">
                <a href="index.html" class="btn btn-primary">
                    <i class="fas fa-home"></i>
                    На главную
                </a>
                <button class="btn btn-secondary" onclick="goBack()">
                    <i class="fas fa-arrow-left"></i>
                    Назад
                </button>
            </div>

            <div class="suggestions">
                <h3><i class="fas fa-lightbulb"></i> Что можно сделать:</h3>
                <ul>
                    <li>Проверьте правильность URL-адреса</li>
                    <li>Вернитесь на главную страницу</li>
                    <li>Используйте навигационное меню</li>
                    <li>Попробуйте обновить страницу</li>
                </ul>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 NotAWallet. Все права защищены. Демонстрационный макет криптовалютного кошелька.</p>
    </footer>

    <script>
        function toggleTheme() {
            document.body.classList.toggle("dark");
            const themeIcon = document.querySelector('.theme-toggle i');
            const themeText = document.querySelector('.theme-toggle span');

            if (document.body.classList.contains('dark')) {
                themeIcon.className = 'fas fa-sun';
                themeText.textContent = 'Светлая';
            } else {
                themeIcon.className = 'fas fa-moon';
                themeText.textContent = 'Темная';
            }
        }

        function goBack() {
            if (window.history.length > 1) {
                window.history.back();
            } else {
                window.location.href = 'index.html';
            }
        }

        window.addEventListener('scroll', function () {
            const nav = document.querySelector('.nav');
            if (window.scrollY > 100) {
                nav.style.background = document.body.classList.contains('dark')
                    ? 'rgba(15, 23, 42, 0.98)'
                    : 'rgba(255, 255, 255, 0.98)';
            } else {
                nav.style.background = document.body.classList.contains('dark')
                    ? 'rgba(15, 23, 42, 0.95)'
                    : 'rgba(255, 255, 255, 0.95)';
            }
        });

        document.addEventListener('DOMContentLoaded', function () {
            const errorIcon = document.querySelector('.error-icon');
            errorIcon.style.opacity = '0';
            errorIcon.style.transform = 'scale(0.5)';

            setTimeout(() => {
                errorIcon.style.transition = 'all 0.5s ease';
                errorIcon.style.opacity = '1';
                errorIcon.style.transform = 'scale(1)';
            }, 200);

            const errorCode = document.querySelector('.error-code');
            errorCode.style.opacity = '0';
            errorCode.style.transform = 'translateY(20px)';

            setTimeout(() => {
                errorCode.style.transition = 'all 0.5s ease';
                errorCode.style.opacity = '1';
                errorCode.style.transform = 'translateY(0)';
            }, 400);

            const errorMessage = document.querySelector('.error-message');
            errorMessage.style.opacity = '0';
            errorMessage.style.transform = 'translateY(20px)';

            setTimeout(() => {
                errorMessage.style.transition = 'all 0.5s ease';
                errorMessage.style.opacity = '1';
                errorMessage.style.transform = 'translateY(0)';
            }, 600);
        });
    </script>
</body>

</html>""", status_code=404)

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

