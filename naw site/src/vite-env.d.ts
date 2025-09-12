/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_TELEGRAM_BOT_ID: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}
