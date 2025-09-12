declare global {
    interface Window {
        Telegram?: {
            Login?: {
                auth: (options: any, callback: (data: any) => void) => void;
            };
        };
    }
}

export { };


