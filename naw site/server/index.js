import express from 'express';
import cors from 'cors';
import crypto from 'crypto';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 4000;
const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;

app.get('/api/health', (_req, res) => {
    return res.json({ ok: true, botToken: Boolean(TELEGRAM_BOT_TOKEN) });
});

function isValidTelegramAuth(authData) {
    if (!TELEGRAM_BOT_TOKEN) return false;
    const { hash, ...data } = authData;
    const dataCheckString = Object.keys(data)
        .sort()
        .map((key) => `${key}=${data[key]}`)
        .join('\n');

    const secretKey = crypto
        .createHash('sha256')
        .update(TELEGRAM_BOT_TOKEN)
        .digest();

    const hmac = crypto
        .createHmac('sha256', secretKey)
        .update(dataCheckString)
        .digest('hex');

    return hmac === hash;
}

app.post('/api/auth/telegram', (req, res) => {
    try {
        const authData = req.body;
        if (!authData || !authData.hash) {
            return res.status(400).json({ ok: false, error: 'Invalid payload' });
        }

        const valid = isValidTelegramAuth(authData);
        if (!valid) {
            return res.status(401).json({ ok: false, error: 'Invalid signature' });
        }

        // Simple session stub (stateless): echo back user basics
        const user = {
            id: authData.id,
            first_name: authData.first_name,
            last_name: authData.last_name,
            username: authData.username,
            photo_url: authData.photo_url,
            auth_date: authData.auth_date,
        };
        return res.json({ ok: true, user });
    } catch (e) {
        return res.status(500).json({ ok: false, error: 'Server error' });
    }
});

app.listen(PORT, () => {
    console.log(`Auth server running on http://localhost:${PORT}`);
});


