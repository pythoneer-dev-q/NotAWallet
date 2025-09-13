import { useState } from 'react';
import {
  Menu,
  X,
  Shield,
  Zap,
  Globe,
  ArrowRight,
  Check,
  Star,
  Smartphone,
  Lock,
  TrendingUp,
  Users,
  Eye
} from 'lucide-react';

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [activeFeature, setActiveFeature] = useState(0);

  const features = [
    {
      icon: Shield,
      title: "Максимальная безопасность",
      description: "Многоуровневая защита с аппаратным шифрованием и биометрической аутентификацией"
    },
    {
      icon: Zap,
      title: "Быстрые переводы",
      description: "Мгновенные транзакции с минимальными комиссиями по всему миру"
    },
    {
      icon: Globe,
      title: "Поддержка 100+ криптовалют",
      description: "Управляйте всеми вашими цифровыми активами в одном месте"
    },
    {
      icon: TrendingUp,
      title: "Аналитика портфеля",
      description: "Отслеживайте доходность и получайте инсайты для инвестиций"
    }
  ];

  const cryptocurrencies = [
    { name: "Bitcoin", symbol: "BTC", color: "from-orange-400 to-orange-600" },
    { name: "Ethereum", symbol: "ETH", color: "from-blue-400 to-purple-600" },
    { name: "Solana", symbol: "SOL", color: "from-purple-400 to-pink-600" },
    { name: "Cardano", symbol: "ADA", color: "from-blue-500 to-blue-700" },
    { name: "Polygon", symbol: "MATIC", color: "from-purple-500 to-indigo-600" },
    { name: "Chainlink", symbol: "LINK", color: "from-blue-400 to-blue-600" }
  ];

  return (
    <div className="min-h-screen bg-white">
      <header className="fixed w-full top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <img
                src="/naw.png"
                alt="NAW Logo"
                className="h-10 w-10"
              />
              <span className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-blue-500 bg-clip-text text-transparent">
                NAW Wallet
              </span>
            </div>

            <nav className="hidden md:flex space-x-8">
              <a href="#features" className="text-gray-700 hover:text-purple-600 transition-colors">Возможности</a>
              <a href="#security" className="text-gray-700 hover:text-purple-600 transition-colors">Безопасность</a>
              <a href="#supported" className="text-gray-700 hover:text-purple-600 transition-colors">Криптовалюты</a>
              <a href="#download" className="text-gray-700 hover:text-purple-600 transition-colors">Скачать</a>
            </nav>

            <div className="hidden md:flex space-x-4">
              <button className="px-4 py-2 text-purple-600 hover:bg-purple-50 rounded-lg transition-colors">
                Создать кошелек
              </button>
            </div>

            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden p-2"
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {isMenuOpen && (
          <div className="md:hidden absolute top-16 left-0 right-0 bg-white border-b border-gray-200 shadow-lg">
            <nav className="px-4 py-4 space-y-4">
              <a href="#features" className="block text-gray-700 hover:text-purple-600">Возможности</a>
              <a href="#security" className="block text-gray-700 hover:text-purple-600">Безопасность</a>
              <a href="#supported" className="block text-gray-700 hover:text-purple-600">Криптовалюты</a>
              <a href="#download" className="block text-gray-700 hover:text-purple-600">Скачать</a>
              <div className="flex flex-col space-y-2 pt-4 border-t">
                <button className="px-4 py-2 text-purple-600 border border-purple-200 rounded-lg">
                  Создать кошелек
                </button>
              </div>
            </nav>
          </div>
        )}
      </header>

      <section className="pt-24 pb-16 bg-gradient-to-br from-purple-50 via-blue-50 to-cyan-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="text-center lg:text-left">
              <h1 className="text-5xl lg:text-6xl font-bold leading-tight mb-6">
                <span className="bg-gradient-to-r from-purple-600 to-blue-500 bg-clip-text text-transparent">
                  Будущее
                </span>
                <br />
                криптовалют
                <br />
                <span className="bg-gradient-to-r from-blue-500 to-cyan-400 bg-clip-text text-transparent">
                  в ваших руках
                </span>
              </h1>
              <p className="text-xl text-gray-600 mb-8 leading-relaxed">
                Безопасный, удобный и функциональный кошелек для управления всеми вашими
                цифровыми активами. Более 1 миллиона пользователей уже доверяют нам.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
                <a href="https://t.me/nawcryptotextbot"><button className="group px-8 py-4 bg-gradient-to-r from-purple-600 to-blue-500 text-white rounded-lg hover:shadow-xl transform hover:-translate-y-1 transition-all text-lg font-semibold">
                  Создать кошелек бесплатно
                  <ArrowRight className="inline ml-2 group-hover:translate-x-1 transition-transform" size={20} />
                </button></a>
              </div>
              <div className="flex items-center justify-center lg:justify-start mt-8 space-x-6 text-sm text-gray-500">
                <div className="flex items-center space-x-2">
                  <Users size={16} />
                  <span>1M+ пользователей</span>
                </div>
                <div className="flex items-center space-x-2">
                  <Shield size={16} />
                  <span>100% безопасно</span>
                </div>
                <div className="flex items-center space-x-2">
                  <Star size={16} />
                  <span>4.8/5 рейтинг</span>
                </div>
              </div>
            </div>

            <div className="relative">
              <div className="relative mx-auto w-80 h-96">
                <div className="absolute inset-0 bg-gradient-to-br from-purple-600 to-blue-500 rounded-3xl p-1 shadow-2xl">
                  <div className="bg-white rounded-3xl p-6 h-full relative overflow-hidden">
                    <div className="text-center mb-6">
                      <img
                        src="/photo_2025-09-07_01-32-44-no-bg-preview (carve.photos).png"
                        alt="NAW Logo"
                        className="h-12 w-12 mx-auto mb-2"
                      />
                      <h3 className="font-bold text-gray-800">Ваш портфель</h3>
                    </div>

                    <div className="bg-gradient-to-r from-purple-100 to-blue-100 rounded-2xl p-4 mb-4">
                      <div className="text-center">
                        <p className="text-sm text-gray-600">Общий баланс</p>
                        <p className="text-2xl font-bold text-gray-800">$24,567.89</p>
                        <p className="text-sm text-green-600">+12.5% за день</p>
                      </div>
                    </div>

                    <div className="space-y-3">
                      {cryptocurrencies.slice(0, 3).map((crypto) => (
                        <div key={crypto.symbol} className="flex items-center justify-between bg-gray-50 rounded-xl p-3">
                          <div className="flex items-center space-x-3">
                            <div className={`w-8 h-8 rounded-full bg-gradient-to-r ${crypto.color}`}></div>
                            <div>
                              <p className="font-medium text-sm">{crypto.name}</p>
                              <p className="text-xs text-gray-500">{crypto.symbol}</p>
                            </div>
                          </div>
                          <div className="text-right">
                            <p className="font-medium text-sm">${(Math.random() * 1000 + 100).toFixed(2)}</p>
                            <p className="text-xs text-green-600">+{(Math.random() * 10 + 1).toFixed(1)}%</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="absolute -top-4 -right-4 w-16 h-16 bg-gradient-to-r from-yellow-400 to-orange-500 rounded-full flex items-center justify-center shadow-lg animate-pulse">
                  <Lock className="text-white" size={24} />
                </div>
                <div className="absolute -bottom-4 -left-4 w-14 h-14 bg-gradient-to-r from-green-400 to-blue-500 rounded-full flex items-center justify-center shadow-lg animate-bounce">
                  <TrendingUp className="text-white" size={20} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="features" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Почему выбирают NAW Wallet?
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Мы объединили лучшие технологии блокчейна с интуитивным дизайном,
              чтобы создать идеальный инструмент для управления криптовалютами
            </p>
          </div>

          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-6">
              {features.map((feature, index) => (
                <div
                  key={index}
                  className={`p-6 rounded-2xl cursor-pointer transition-all ${activeFeature === index
                    ? 'bg-gradient-to-r from-purple-50 to-blue-50 border-2 border-purple-200'
                    : 'bg-gray-50 hover:bg-gray-100'
                    }`}
                  onMouseEnter={() => setActiveFeature(index)}
                >
                  <div className="flex items-start space-x-4">
                    <div className={`p-3 rounded-xl ${activeFeature === index
                      ? 'bg-gradient-to-r from-purple-600 to-blue-500 text-white'
                      : 'bg-white text-gray-600'
                      } transition-all`}>
                      <feature.icon size={24} />
                    </div>
                    <div>
                      <h3 className="text-xl font-semibold text-gray-900 mb-2">
                        {feature.title}
                      </h3>
                      <p className="text-gray-600 leading-relaxed">
                        {feature.description}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            <div className="relative">
              <div className="bg-gradient-to-br from-purple-600 to-blue-500 rounded-3xl p-8 text-white">
                <div className="text-center mb-8">
                  <h3 className="text-2xl font-bold mb-4">Управляйте активами просто</h3>
                  <p className="text-purple-100">
                    Все функции доступны в несколько касаний
                  </p>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-white/10 backdrop-blur rounded-xl p-4 text-center">
                    <div className="text-2xl font-bold">100+</div>
                    <div className="text-sm text-purple-100">Криптовалют</div>
                  </div>
                  <div className="bg-white/10 backdrop-blur rounded-xl p-4 text-center">
                    <div className="text-2xl font-bold">24/7</div>
                    <div className="text-sm text-purple-100">Поддержка</div>
                  </div>
                  <div className="bg-white/10 backdrop-blur rounded-xl p-4 text-center">
                    <div className="text-2xl font-bold">0.1%</div>
                    <div className="text-sm text-purple-100">Комиссия</div>
                  </div>
                  <div className="bg-white/10 backdrop-blur rounded-xl p-4 text-center">
                    <div className="text-2xl font-bold">1M+</div>
                    <div className="text-sm text-purple-100">Пользователей</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="security" className="py-20 bg-gradient-to-br from-gray-50 to-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Безопасность мирового уровня
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Ваши средства защищены современными методами шифрования и многоуровневой системой безопасности
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-green-400 to-blue-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <Shield className="text-white" size={32} />
              </div>
              <h3 className="text-xl font-semibold mb-3">Аппаратное шифрование</h3>
              <p className="text-gray-600">
                Приватные ключи хранятся в защищенном чипе вашего устройства
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-purple-400 to-pink-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <Eye className="text-white" size={32} />
              </div>
              <h3 className="text-xl font-semibold mb-3">Биометрическая защита</h3>
              <p className="text-gray-600">
                Отпечаток пальца или Face ID для доступа к кошельку
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-orange-400 to-red-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <Lock className="text-white" size={32} />
              </div>
              <h3 className="text-xl font-semibold mb-3">Мульти-подпись</h3>
              <p className="text-gray-600">
                Дополнительный уровень защиты для крупных транзакций
              </p>
            </div>
          </div>

          <div className="mt-16 bg-white rounded-3xl p-8 shadow-lg">
            <div className="grid lg:grid-cols-2 gap-8 items-center">
              <div>
                <h3 className="text-2xl font-bold text-gray-900 mb-4">
                  Полный контроль ваших средств
                </h3>
                <div className="space-y-4">
                  <div className="flex items-center space-x-3">
                    <Check className="text-green-500 flex-shrink-0" size={20} />
                    <span className="text-gray-700">Вы владеете приватными ключами</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Check className="text-green-500 flex-shrink-0" size={20} />
                    <span className="text-gray-700">Децентрализованное хранение</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Check className="text-green-500 flex-shrink-0" size={20} />
                    <span className="text-gray-700">Открытый исходный код</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Check className="text-green-500 flex-shrink-0" size={20} />
                    <span className="text-gray-700">Регулярный аудит безопасности</span>
                  </div>
                </div>
              </div>
              <div className="text-center">
                <div className="inline-block p-8 bg-gradient-to-br from-purple-100 to-blue-100 rounded-full">
                  <Shield className="text-purple-600" size={64} />
                </div>
                <p className="mt-4 text-gray-600 text-lg">
                  Сертификат SOC 2 Type II
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="supported" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Поддерживаемые криптовалюты
            </h2>
            <p className="text-xl text-gray-600">
              Управляйте всеми популярными цифровыми активами в одном приложении
            </p>
          </div>

          <div className="grid md:grid-cols-3 lg:grid-cols-6 gap-6">
            {cryptocurrencies.map((crypto) => (
              <div
                key={crypto.symbol}
                className="group p-6 bg-gray-50 rounded-2xl hover:bg-white hover:shadow-lg transition-all cursor-pointer"
              >
                <div className={`w-12 h-12 rounded-full bg-gradient-to-r ${crypto.color} mx-auto mb-4 group-hover:scale-110 transition-transform`}></div>
                <div className="text-center">
                  <h4 className="font-semibold text-gray-900">{crypto.symbol}</h4>
                  <p className="text-sm text-gray-600">{crypto.name}</p>
                </div>
              </div>
            ))}
          </div>

          <div className="text-center mt-12">
            <p className="text-gray-600 text-lg mb-6">
              И еще более 100 криптовалют и токенов
            </p>
            <button className="px-8 py-3 bg-gradient-to-r from-purple-600 to-blue-500 text-white rounded-lg hover:shadow-lg transform hover:-translate-y-0.5 transition-all">
              Посмотреть полный список
            </button>
          </div>
        </div>
      </section>

      <section id="download" className="py-20 bg-gradient-to-br from-purple-600 via-blue-600 to-cyan-500">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center text-white">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6">
              Начните управлять криптовалютами уже сегодня
            </h2>
            <p className="text-xl text-purple-100 mb-12 max-w-3xl mx-auto">
              Скачайте приложение и начните управлять криптовалютами уже сегодня
            </p>

            <div className="flex flex-col sm:flex-row gap-6 justify-center items-center mb-12">
              <button className="group flex items-center space-x-3 bg-black text-white px-8 py-4 rounded-2xl hover:bg-gray-800 transition-colors">
                <Smartphone size={24} />
                <div className="text-left">
                  <div className="text-xs text-gray-300">Скачать приложение</div>
                  <div className="text-lg font-semibold">NAW Wallet</div>
                </div>
              </button>
            </div>

            <div className="grid md:grid-cols-3 gap-8 text-center">
              <div>
                <div className="text-3xl font-bold mb-2">1M+</div>
                <div className="text-purple-100">Активных пользователей</div>
              </div>
              <div>
              </div>
              <div>
                <div className="text-3xl font-bold mb-2">24/7</div>
                <div className="text-purple-100">Техподдержка</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <footer className="bg-gray-900 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-3 mb-6">
                <img
                  src="/photo_2025-09-07_01-32-44-no-bg-preview (carve.photos).png"
                  alt="NAW Logo"
                  className="h-8 w-8"
                />
                <span className="text-xl font-bold">NAW Wallet</span>
              </div>
              <p className="text-gray-400 mb-6">
                Безопасный и удобный кошелек для управления криптовалютами нового поколения.
              </p>
              <div className="flex space-x-4">
                <div className="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-500 rounded-full flex items-center justify-center cursor-pointer hover:scale-110 transition-transform">
                  <span className="text-sm font-bold">T</span>
                </div>
                <div className="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-500 rounded-full flex items-center justify-center cursor-pointer hover:scale-110 transition-transform">
                  <span className="text-sm font-bold">X</span>
                </div>
                <div className="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-500 rounded-full flex items-center justify-center cursor-pointer hover:scale-110 transition-transform">
                  <span className="text-sm font-bold">D</span>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-lg font-semibold mb-6">Продукт</h4>
              <div className="space-y-3">
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Возможности</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Безопасность</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Цены</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">API</a>
              </div>
            </div>

            <div>
              <h4 className="text-lg font-semibold mb-6">Поддержка</h4>
              <div className="space-y-3">
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Центр помощи</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Связаться с нами</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Статус сервиса</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Сообщество</a>
              </div>
            </div>

            <div>
              <h4 className="text-lg font-semibold mb-6">Компания</h4>
              <div className="space-y-3">
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">О нас</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Блог</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Карьера</a>
                <a href="#" className="block text-gray-400 hover:text-white transition-colors">Пресса</a>
              </div>
            </div>
          </div>

          <div className="border-t border-gray-800 pt-8 mt-12">
            <div className="flex flex-col md:flex-row justify-between items-center">
              <div className="text-gray-400 text-sm">
                © 2024 NAW Wallet. Все права защищены.
              </div>
              <div className="flex space-x-6 text-sm text-gray-400 mt-4 md:mt-0">
                <a href="#" className="hover:text-white transition-colors">Политика конфиденциальности</a>
                <a href="#" className="hover:text-white transition-colors">Условия использования</a>
                <a href="#" className="hover:text-white transition-colors">Cookies</a>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;