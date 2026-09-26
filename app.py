import streamlit as st

!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LAMAVEO Editora | Conectando Conhecimento e Literatura</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        navy: {
                            800: '#1e293b',
                            900: '#0f172a',
                            950: '#090d16'
                        },
                        gold: {
                            500: '#d97706',
                            600: '#b45309',
                            DEFAULT: '#c59b27',
                            light: '#e6c559'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .font-serif { font-family: 'Playfair Display', serif; }
        .glass-nav { background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(10px); }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-gold-500 selection:text-white">

    <header class="fixed top-0 left-0 right-0 z-50 glass-nav border-b border-slate-800 text-white transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <!-- Brand Logo -->
            <a href="#" class="flex items-center space-x-3 group">
                <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-gold to-amber-600 flex items-center justify-center shadow-lg shadow-gold/20 group-hover:scale-105 transition-transform">
                    <i class="fa-solid fa-book-open-reader text-white text-lg"></i>
                </div>
                <div>
                    <span class="text-xl font-serif font-bold tracking-wider text-white">LAMAVEO</span>
                    <span class="block text-[10px] uppercase tracking-widest text-gold-light">Editora & Conhecimento</span>
                </div>
            </a>

            <!-- Desktop Navigation -->
            <nav class="hidden md:flex items-center space-x-8 text-sm font-medium">
                <a href="#inicio" class="hover:text-gold-light transition-colors">Início</a>
                <a href="#catalogo" class="hover:text-gold-light transition-colors">Catálogo</a>
                <a href="#gratuitos" class="hover:text-gold-light transition-colors">Materiais Gratuitos</a>
                <a href="#sobre" class="hover:text-gold-light transition-colors">Sobre</a>
                <a href="#contato" class="hover:text-gold-light transition-colors">Contato</a>
            </nav>

            <!-- Actions (Search, Cart, User) -->
            <div class="flex items-center space-x-4">
                <!-- Search Bar Toggle / Input -->
                <div class="relative hidden lg:block">
                    <input type="text" id="searchInput" placeholder="Buscar livros, autores..." class="bg-slate-800/80 border border-slate-700 text-sm rounded-full pl-10 pr-4 py-2 focus:outline-none focus:border-gold w-60 text-slate-200 placeholder-slate-400 transition-all">
                    <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3 text-slate-400 text-sm"></i>
                </div>

                <!-- Cart Button -->
                <button onclick="toggleCart()" class="relative p-2 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-200 transition-colors" title="Carrinho">
                    <i class="fa-solid fa-cart-shopping text-lg"></i>
                    <span id="cartBadge" class="absolute -top-1 -right-1 bg-gold text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center shadow">0</span>
                </button>

                <!-- User Account Button -->
                <button onclick="openAuthModal()" class="flex items-center space-x-2 bg-gradient-to-r from-gold to-amber-600 hover:from-amber-600 hover:to-gold-700 text-white px-4 py-2 rounded-full text-sm font-medium shadow-md shadow-gold/20 transition-all">
                    <i class="fa-solid fa-user"></i>
                    <span class="hidden sm:inline" id="userAccountBtnText">Entrar</span>
                </button>

                <!-- Mobile Menu Button -->
                <button onclick="toggleMobileMenu()" class="md:hidden p-2 rounded-lg text-slate-300 hover:bg-slate-800">
                    <i class="fa-solid fa-bars text-xl"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Drawer -->
        <div id="mobileMenu" class="hidden md:hidden bg-slate-900 border-b border-slate-800 px-4 pt-2 pb-6 space-y-3">
            <input type="text" id="mobileSearchInput" placeholder="Buscar livros, autores..." class="w-full bg-slate-800 border border-slate-700 text-sm rounded-lg px-4 py-2 text-slate-200 mb-2">
            <a href="#inicio" class="block py-2 text-slate-200 hover:text-gold">Início</a>
            <a href="#catalogo" class="block py-2 text-slate-200 hover:text-gold">Catálogo</a>
            <a href="#gratuitos" class="block py-2 text-slate-200 hover:text-gold">Materiais Gratuitos</a>
            <a href="#sobre" class="block py-2 text-slate-200 hover:text-gold">Sobre</a>
            <a href="#contato" class="block py-2 text-slate-200 hover:text-gold">Contato</a>
        </div>
    </header>

    <section id="inicio" class="relative pt-32 pb-20 lg:pt-40 lg:pb-32 bg-gradient-to-br from-navy-950 via-navy-900 to-slate-900 text-white overflow-hidden">
        <!-- Decorative glowing shapes -->
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-gold/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute bottom-0 left-1/4 w-80 h-80 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
                    <div class="inline-flex items-center space-x-2 bg-gold/10 border border-gold/30 text-gold-light px-3.5 py-1.5 rounded-full text-xs font-semibold tracking-wide uppercase">
                        <i class="fa-solid fa-award"></i>
                        <span>Editora Referência em Ciência & Literatura</span>
                    </div>
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-serif font-bold tracking-tight leading-tight">
                        Conectando Leitores ao <span class="text-transparent bg-clip-text bg-gradient-to-r from-gold-light via-gold to-amber-500">Conhecimento Profundo</span>
                    </h1>
                    <p class="text-slate-300 text-lg max-w-2xl mx-auto lg:mx-0">
                        Explore nossa curadoria exclusiva de livros científicos, literatura contemporânea, obras infanto-juvenis e publicações essenciais nas áreas de saúde, fisioterapia, educação e empreendedorismo.
                    </p>
                    <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start space-y-4 sm:space-y-0 sm:space-x-4 pt-4">
                        <a href="#catalogo" class="w-full sm:w-auto bg-gold hover:bg-gold-600 text-navy-950 font-bold px-8 py-3.5 rounded-xl shadow-lg shadow-gold/25 transition-all transform hover:-translate-y-0.5 text-center">
                            Explorar Catálogo
                        </a>
                        <a href="#gratuitos" class="w-full sm:w-auto bg-slate-800/80 hover:bg-slate-800 border border-slate-700 text-white font-semibold px-8 py-3.5 rounded-xl transition-all text-center flex items-center justify-center space-x-2">
                            <i class="fa-solid fa-download text-gold"></i>
                            <span>Apostilas Gratuitas</span>
                        </a>
                    </div>
                </div>

                <!-- Featured Books Showcase Carousel / Grid -->
                <div class="lg:col-span-5 relative">
                    <div class="relative mx-auto max-w-md bg-gradient-to-b from-slate-800 to-slate-900 p-6 rounded-2xl border border-slate-700 shadow-2xl">
                        <div class="absolute -top-3 -right-3 bg-gold text-navy-950 text-xs font-bold px-3 py-1 rounded-full shadow">
                            Destaque do Mês
                        </div>
                        <div class="aspect-[3/4] rounded-lg overflow-hidden mb-6 shadow-md relative group">
                            <img src="https://placehold.co/400x550/0f172a/c59b27?text=Fisioterapia+Avancada" alt="Livro Destaque" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-navy-950/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4">
                                <span class="text-xs text-gold-light font-medium">Lançamento Científico</span>
                            </div>
                        </div>
                        <h3 class="text-xl font-serif font-bold text-white mb-1">Fundamentos da Fisioterapia Moderna</h3>
                        <p class="text-slate-400 text-sm mb-4">Dra. Beatriz Alvarez & Dr. Carlos Mello</p>
                        <div class="flex items-center justify-between">
                            <span class="text-2xl font-bold text-gold">R$ 149,90</span>
                            <button onclick="quickAdd('Fundamentos da Fisioterapia Moderna', 149.90, 'Livro Físico')" class="bg-gold hover:bg-gold-600 text-navy-950 font-semibold px-4 py-2 rounded-lg text-sm transition-colors">
                                Comprar Agora
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="catalogo" class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <span class="text-gold font-semibold text-sm tracking-wider uppercase">Nossa Curadoria</span>
                <h2 class="text-3xl sm:text-4xl font-serif font-bold text-slate-900 mt-2 mb-4">Catálogo de Livros e Ebooks</h2>
                <p class="text-slate-600">Filtre por categoria para encontrar exatamente o conhecimento que você procura, seja em formato físico, digital (ebook) ou material de estudo gratuito.</p>
            </div>

            <!-- Category Filter Tabs -->
            <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-4 mb-12">
                <button onclick="filterCategory('todos')" class="cat-btn active px-5 py-2.5 rounded-full text-sm font-medium transition-all bg-navy-900 text-white shadow" data-category="todos">
                    Todos os Títulos
                </button>
                <button onclick="filterCategory('literatura-cientificos')" class="cat-btn px-5 py-2.5 rounded-full text-sm font-medium transition-all bg-slate-100 text-slate-700 hover:bg-slate-200" data-category="literatura-cientificos">
                    Literatura e Científicos
                </button>
                <button onclick="filterCategory('infantil-jovem')" class="cat-btn px-5 py-2.5 rounded-full text-sm font-medium transition-all bg-slate-100 text-slate-700 hover:bg-slate-200" data-category="infantil-jovem">
                    Infantil & Literatura Jovem
                </button>
                <button onclick="filterCategory('saude-fisio')" class="cat-btn px-5 py-2.5 rounded-full text-sm font-medium transition-all bg-slate-100 text-slate-700 hover:bg-slate-200" data-category="saude-fisio">
                    Saúde & Fisioterapia
                </button>
                <button onclick="filterCategory('educacao-empreendedorismo')" class="cat-btn px-5 py-2.5 rounded-full text-sm font-medium transition-all bg-slate-100 text-slate-700 hover:bg-slate-200" data-category="educacao-empreendedorismo">
                    Educação & Empreendedorismo
                </button>
                <button onclick="filterCategory('gratuitos')" class="cat-btn px-5 py-2.5 rounded-full text-sm font-medium transition-all bg-amber-50 text-amber-800 border border-amber-200 hover:bg-amber-100" data-category="gratuitos">
                    <i class="fa-solid fa-gift mr-1 text-gold"></i> Gratuitos
                </button>
            </div>

            <!-- Products Grid -->
            <div id="productsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Products will be dynamically populated by JavaScript -->
            </div>
        </div>
    </section>

    <section id="gratuitos" class="py-20 bg-slate-900 text-white relative overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#c59b27_1px,transparent_1px)] [background-size:16px_16px]"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="flex flex-col md:flex-row items-center justify-between mb-12">
                <div>
                    <span class="text-gold font-semibold text-sm tracking-wider uppercase">Iniciativa LAMAVEO</span>
                    <h2 class="text-3xl sm:text-4xl font-serif font-bold mt-2">Materiais de Apoio Gratuitos</h2>
                    <p class="text-slate-400 mt-2 max-w-xl">Baixe apostilas de estudo, e-books introdutórios e guias práticos sem custo algum. Acesso imediato em PDF.</p>
                </div>
                <button onclick="filterCategory('gratuitos')" class="mt-6 md:mt-0 bg-gold hover:bg-gold-600 text-navy-950 font-bold px-6 py-3 rounded-xl transition-all shadow">
                    Ver Todos os Gratuitos
                </button>
            </div>

            <div id="freeGrid" class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Free items injected dynamically -->
            </div>
        </div>
    </section>

    <section id="sobre" class="py-20 bg-slate-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div class="space-y-6">
                    <span class="text-gold font-semibold text-sm tracking-wider uppercase">Sobre a LAMAVEO</span>
                    <h2 class="text-3xl sm:text-4xl font-serif font-bold text-slate-900">Excelência Editorial e Rigor Científico</h2>
                    <p class="text-slate-600 leading-relaxed">
                        Fundada com a missão de transformar o cenário editorial brasileiro, a <strong>LAMAVEO</strong> preza pela qualidade intransigente em suas publicações. Unimos autores renomados nas áreas de ciências da saúde, educação e empreendedorismo a uma literatura infantojuvenil envolvente e formativa.
                    </p>
                    <div class="grid grid-cols-2 gap-6 pt-4">
                        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                            <div class="text-3xl font-bold text-gold mb-1">+250</div>
                            <div class="text-sm text-slate-600 font-medium">Obras Publicadas</div>
                        </div>
                        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                            <div class="text-3xl font-bold text-gold mb-1">100%</div>
                            <div class="text-sm text-slate-600 font-medium">Compromisso com o Leitor</div>
                        </div>
                    </div>
                </div>
                <div class="relative">
                    <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-xl border-4 border-white">
                        <img src="https://placehold.co/600x450/1e293b/c59b27?text=Editora+LAMAVEO+Livros" alt="Editora Lamaveo" class="w-full h-full object-cover">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contato" class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <div class="space-y-6">
                    <span class="text-gold font-semibold text-sm tracking-wider uppercase">Fale Conosco</span>
                    <h2 class="text-3xl font-serif font-bold text-slate-900">Estamos prontos para atendê-lo</h2>
                    <p class="text-slate-600">Tem dúvidas sobre submissão de originais, pedidos em grandes quantidades ou prazos de entrega? Entre em contato com nossa equipe editorial.</p>
                    
                    <div class="space-y-4 pt-2">
                        <div class="flex items-center space-x-4">
                            <div class="w-12 h-12 rounded-full bg-gold/10 text-gold flex items-center justify-center text-lg">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <span class="block text-xs text-slate-500 font-medium uppercase">E-mail de Contato</span>
                                <span class="font-semibold text-slate-800">contato@lamaveoeditora.com.br</span>
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <div class="w-12 h-12 rounded-full bg-gold/10 text-gold flex items-center justify-center text-lg">
                                <i class="fa-solid fa-phone"></i>
                            </div>
                            <div>
                                <span class="block text-xs text-slate-500 font-medium uppercase">Central de Atendimento</span>
                                <span class="font-semibold text-slate-800">(11) 3456-7890 / WhatsApp (11) 98765-4321</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-slate-50 p-8 rounded-2xl border border-slate-200 shadow-sm">
                    <form onsubmit="handleContactSubmit(event)" class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-slate-700 mb-1">Seu Nome</label>
                            <input type="text" required class="w-full bg-white border border-slate-300 rounded-lg px-4 py-2.5 text-slate-800 focus:outline-none focus:border-gold">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-slate-700 mb-1">Seu E-mail</label>
                            <input type="email" required class="w-full bg-white border border-slate-300 rounded-lg px-4 py-2.5 text-slate-800 focus:outline-none focus:border-gold">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-slate-700 mb-1">Mensagem</label>
                            <textarea rows="4" required class="w-full bg-white border border-slate-300 rounded-lg px-4 py-2.5 text-slate-800 focus:outline-none focus:border-gold"></textarea>
                        </div>
                        <button type="submit" class="w-full bg-navy-900 hover:bg-navy-950 text-white font-semibold py-3 rounded-lg transition-all shadow">
                            Enviar Mensagem
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-navy-950 text-slate-400 py-16 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">
                <div class="space-y-4">
                    <div class="flex items-center space-x-3">
                        <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-gold to-amber-600 flex items-center justify-center text-white">
                            <i class="fa-solid fa-book-open-reader"></i>
                        </div>
                        <span class="text-xl font-serif font-bold text-white tracking-wider">LAMAVEO</span>
                    </div>
                    <p class="text-sm text-slate-400">Editora especializada em literatura, obras científicas, saúde, fisioterapia, educação e empreendedorismo.</p>
                </div>
                <div>
                    <h4 class="text-white font-semibold mb-4 text-sm uppercase tracking-wider">Categorias</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="#catalogo" onclick="filterCategory('literatura-cientificos')" class="hover:text-gold transition-colors">Literatura & Científicos</a></li>
                        <li><a href="#catalogo" onclick="filterCategory('infantil-jovem')" class="hover:text-gold transition-colors">Infantil & Jovem</a></li>
                        <li><a href="#catalogo" onclick="filterCategory('saude-fisio')" class="hover:text-gold transition-colors">Saúde & Fisioterapia</a></li>
                        <li><a href="#catalogo" onclick="filterCategory('educacao-empreendedorismo')" class="hover:text-gold transition-colors">Educação & Empreendedorismo</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-semibold mb-4 text-sm uppercase tracking-wider">Links Úteis</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="#inicio" class="hover:text-gold transition-colors">Início</a></li>
                        <li><a href="#catalogo" class="hover:text-gold transition-colors">Catálogo Completo</a></li>
                        <li><a href="#gratuitos" class="hover:text-gold transition-colors">Baixar Apostilas Grátis</a></li>
                        <li><a href="#" onclick="openAuthModal()" class="hover:text-gold transition-colors">Área do Cliente</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-semibold mb-4 text-sm uppercase tracking-wider">Redes Sociais</h4>
                    <div class="flex space-x-3 mb-4">
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-300 hover:text-gold hover:border-gold transition-all"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-300 hover:text-gold hover:border-gold transition-all"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-300 hover:text-gold hover:border-gold transition-all"><i class="fa-brands fa-facebook-f"></i></a>
                    </div>
                    <span class="text-xs text-slate-500">Pagamentos seguros via Cartão, PIX e Boleto. Envio para todo o Brasil.</span>
                </div>
            </div>
            <div class="border-t border-slate-900 pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500">
                <p>&copy; 2026 LAMAVEO Editora Ltda. Todos os direitos reservados.</p>
                <p class="mt-4 sm:mt-0">Desenvolvido com excelência para leitores e pesquisadores.</p>
            </div>
        </div>
    </footer>

    <div id="cartDrawer" class="fixed inset-0 z-50 overflow-hidden hidden">
        <div class="absolute inset-0 bg-navy-950/70 backdrop-blur-sm transition-opacity" onclick="toggleCart()"></div>
        <div class="absolute inset-y-0 right-0 max-w-full flex pl-10">
            <div class="w-screen max-w-md bg-white shadow-2xl flex flex-col">
                <!-- Cart Header -->
                <div class="px-6 py-5 bg-navy-900 text-white flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <i class="fa-solid fa-cart-shopping text-gold"></i>
                        <h3 class="font-serif font-bold text-lg">Seu Carrinho de Compras</h3>
                    </div>
                    <button onclick="toggleCart()" class="text-slate-400 hover:text-white p-1">
                        <i class="fa-solid fa-xmark text-xl"></i>
                    </button>
                </div>

                <!-- Cart Items List -->
                <div id="cartItemsContainer" class="flex-1 overflow-y-auto p-6 space-y-4 divide-y divide-slate-100">
                    <!-- Cart items populated via JS -->
                </div>

                <!-- Cart Footer & Checkout Action -->
                <div class="p-6 bg-slate-50 border-t border-slate-200 space-y-4">
                    <!-- Shipping Calculator for Physical Items -->
                    <div id="shippingSection" class="bg-white p-4 rounded-xl border border-slate-200 space-y-2">
                        <label class="block text-xs font-semibold text-slate-700 uppercase tracking-wide">Cálculo de Frete e Prazo (Correios)</label>
                        <div class="flex space-x-2">
                            <input type="text" id="cepInput" placeholder="Digite seu CEP (ex: 01001-000)" class="flex-1 bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-gold">
                            <button onclick="calculateShipping()" class="bg-navy-900 text-white text-xs font-semibold px-4 py-2 rounded-lg hover:bg-navy-950 transition-colors">Calcular</button>
                        </div>
                        <div id="shippingResult" class="text-xs text-slate-600 pt-1"></div>
                    </div>

                    <div class="flex justify-between text-base font-semibold text-slate-800">
                        <span>Subtotal:</span>
                        <span id="cartSubtotal">R$ 0,00</span>
                    </div>
                    <div class="flex justify-between text-base font-semibold text-slate-800">
                        <span>Frete:</span>
                        <span id="cartShippingCost">R$ 0,00</span>
                    </div>
                    <div class="flex justify-between text-xl font-bold text-navy-900 pt-2 border-t border-slate-200">
                        <span>Total:</span>
                        <span id="cartTotal">R$ 0,00</span>
                    </div>

                    <button onclick="proceedToCheckout()" class="w-full bg-gold hover:bg-gold-600 text-navy-950 font-bold py-3.5 rounded-xl shadow-lg shadow-gold/20 transition-all text-center">
                        Finalizar Pedido / Pagamento
                    </button>
                </div>
            </div>
        </div>
    </div>

    <div id="checkoutModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/80 backdrop-blur-sm hidden">
        <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
            <div class="bg-navy-900 text-white px-6 py-4 flex items-center justify-between">
                <h3 class="font-serif font-bold text-lg">Checkout Seguro - LAMAVEO</h3>
                <button onclick="closeCheckoutModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
            </div>
            <div class="p-6 overflow-y-auto space-y-6">
                <!-- Payment Methods -->
                <div>
                    <label class="block text-sm font-semibold text-slate-700 mb-3">Escolha a Forma de Pagamento</label>
                    <div class="grid grid-cols-3 gap-3">
                        <button onclick="selectPaymentMethod('pix')" id="payPixBtn" class="payment-method-btn p-3 rounded-xl border-2 border-gold bg-gold/5 flex flex-col items-center justify-center text-xs font-semibold text-navy-900">
                            <i class="fa-solid fa-qrcode text-lg text-gold mb-1"></i> PIX (Aprovação imediata)
                        </button>
                        <button onclick="selectPaymentMethod('card')" id="payCardBtn" class="payment-method-btn p-3 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col items-center justify-center text-xs font-semibold text-slate-700">
                            <i class="fa-solid fa-credit-card text-lg text-slate-600 mb-1"></i> Cartão de Crédito
                        </button>
                        <button onclick="selectPaymentMethod('boleto')" id="payBoletoBtn" class="payment-method-btn p-3 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col items-center justify-center text-xs font-semibold text-slate-700">
                            <i class="fa-solid fa-barcode text-lg text-slate-600 mb-1"></i> Boleto Bancário
                        </button>
                    </div>
                </div>

                <!-- Dynamic Payment Form Fields -->
                <div id="paymentFormContainer" class="space-y-4">
                    <!-- Populated by JS based on selection -->
                </div>

                <!-- Customer Details for Digital / Physical delivery -->
                <div class="space-y-3 pt-2 border-t border-slate-200">
                    <h4 class="text-xs font-semibold text-slate-600 uppercase">Dados de Entrega / E-book Digital</h4>
                    <div>
                        <input type="text" id="checkoutName" placeholder="Nome Completo" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-sm">
                    </div>
                    <div>
                        <input type="email" id="checkoutEmail" placeholder="E-mail (para recebimento de E-books)" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-sm">
                    </div>
                </div>
            </div>
            <div class="p-6 bg-slate-50 border-t border-slate-200 flex justify-end space-x-3">
                <button onclick="closeCheckoutModal()" class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 text-sm font-semibold hover:bg-slate-100">Cancelar</button>
                <button onclick="completeOrder()" class="px-6 py-2.5 rounded-xl bg-gold hover:bg-gold-600 text-navy-950 font-bold text-sm shadow">Confirmar Pagamento</button>
            </div>
        </div>
    </div>

    <div id="authModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/80 backdrop-blur-sm hidden">
        <div class="bg-white w-full max-w-md rounded-2xl shadow-2xl overflow-hidden">
            <div class="bg-navy-900 text-white px-6 py-4 flex items-center justify-between">
                <h3 class="font-serif font-bold text-lg" id="authModalTitle">Área do Cliente LAMAVEO</h3>
                <button onclick="closeAuthModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
            </div>
            <div class="p-6 space-y-4">
                <div id="authFormContent">
                    <form onsubmit="handleLogin(event)" class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-slate-700 mb-1">E-mail</label>
                            <input type="email" id="loginEmail" required class="w-full bg-slate-50 border border-slate-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-gold">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-slate-700 mb-1">Senha</label>
                            <input type="password" id="loginPass" required class="w-full bg-slate-50 border border-slate-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-gold">
                        </div>
                        <button type="submit" class="w-full bg-gold hover:bg-gold-600 text-navy-950 font-bold py-3 rounded-xl shadow transition-all">
                            Entrar na Conta
                        </button>
                        <div class="text-center pt-2">
                            <a href="#" onclick="toggleAuthMode()" class="text-xs text-gold hover:underline font-semibold">Não tem conta? Cadastre-se agora</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div id="msgModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/60 backdrop-blur-sm hidden">
        <div class="bg-white w-full max-w-sm rounded-2xl shadow-2xl p-6 text-center space-y-4">
            <div id="msgIcon" class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 text-2xl flex items-center justify-center mx-auto">
                <i class="fa-solid fa-check"></i>
            </div>
            <h3 id="msgTitle" class="font-serif font-bold text-xl text-slate-900">Sucesso!</h3>
            <p id="msgText" class="text-slate-600 text-sm">Operação realizada com sucesso.</p>
            <button onclick="closeMsgModal()" class="w-full bg-navy-900 text-white font-semibold py-2.5 rounded-xl text-sm">Entendido</button>
        </div>
    </div>

    <script>
        // Database of Books, Ebooks, and Free materials for LAMAVEO
        const products = [
            {
                id: 1,
                title: "Fisioterapia Respiratória na UTI: Evidências e Prática",
                author: "Dr. Roberto Sampaio",
                category: "saude-fisio",
                type: "Livro Físico",
                price: 189.90,
                image: "https://placehold.co/400x550/0f172a/c59b27?text=Fisioterapia+UTI",
                description: "Obra de referência para profissionais de fisioterapia em terapia intensiva."
            },
            {
                id: 2,
                title: "Empreendedorismo Científico: Da Bancada ao Mercado",
                author: "Dra. Mariana Costa",
                category: "educacao-empreendedorismo",
                type: "Ebook",
                price: 79.90,
                image: "https://placehold.co/400x550/1e293b/e6c559?text=Empreendedorismo",
                description: "Guia completo para pesquisadores que desejam inovar e criar startups de sucesso."
            },
            {
                id: 3,
                title: "O Segredo da Floresta Encantada",
                author: "Clara Mendonça",
                category: "infantil-jovem",
                type: "Livro Físico",
                price: 49.90,
                image: "https://placehold.co/400x550/334155/ffffff?text=Floresta+Encantada",
                description: "Literatura infantil ilustrada que estimula a imaginação e a preservação ambiental."
            },
            {
                id: 4,
                title: "Ensino Contemporâneo: Metodologias Ativas na Educação",
                author: "Prof. Dr. Fernando Azevedo",
                category: "educacao-empreendedorismo",
                type: "Livro Físico",
                price: 98.00,
                image: "https://placehold.co/400x550/0f172a/ffffff?text=Educacao+Moderna",
                description: "Abordagem moderna para educadores transformarem suas salas de aula."
            },
            {
                id: 5,
                title: "Anatomia Humana Aplicada à Reabilitação Motora",
                author: "Dra. Helena Viana",
                category: "saude-fisio",
                type: "Livro Físico",
                price: 210.00,
                image: "https://placehold.co/400x550/1e293b/c59b27?text=Anatomia+Reabilitacao",
                description: "Atlas detalhado com foco clínico para fisioterapeutas e educadores físicos."
            },
            {
                id: 6,
                title: "Crônicas da Juventude Conectada",
                author: "Lucas Ribeiro",
                category: "infantil-jovem",
                type: "Ebook",
                price: 39.90,
                image: "https://placehold.co/400x550/0f172a/e6c559?text=Literatura+Jovem",
                description: "Contos reflexivos sobre os desafios e sonhos da juventude atual."
            },
            {
                id: 7,
                title: "Filosofia da Ciência e Epistemologia Moderna",
                author: "Dr. Alexandre Moreira",
                category: "literatura-cientificos",
                type: "Livro Físico",
                price: 125.00,
                image: "https://placehold.co/400x550/1e293b/ffffff?text=Filosofia+Ciencia",
                description: "Uma imersão profunda nos métodos científicos e suas bases filosóficas."
            },
            {
                id: 8,
                title: "Guia Prático: Primeiros Socorros na Infância",
                author: "Dra. Patrícia Lima",
                category: "gratuitos",
                type: "Apostila Gratuita",
                price: 0.00,
                image: "https://placehold.co/400x550/0f172a/c59b27?text=Guia+Gratis+Saude",
                description: "Material gratuito essencial para pais, professores e cuidadores."
            },
            {
                id: 9,
                title: "E-book: Introdução à Fisioterapia Esportiva",
                author: "Dr. Marcos Vinicius",
                category: "gratuitos",
                type: "Ebook Gratuito",
                price: 0.00,
                image: "https://placehold.co/400x550/1e293b/e6c559?text=Fisio+Esportiva+Gratis",
                description: "Conceitos iniciais e prevenção de lesões em atletas de alta performance."
            },
            {
                id: 10,
                title: "Cartilha de Educação Financeira para Jovens",
                author: "Ana Beatriz Souza",
                category: "gratuitos",
                type: "Apostila Gratuita",
                price: 0.00,
                image: "https://placehold.co/400x550/334155/ffffff?text=Educacao+Financeira",
                description: "Educação financeira descomplicada para o público infanto-juvenil."
            }
        ];

        let cart = [];
        let currentCategory = 'todos';
        let shippingFee = 0.00;
        let shippingInfoText = '';
        let selectedPayment = 'pix';
        let currentUser = null;

        // Initialize App on Window Load
        window.onload = function() {
            renderProducts(products);
            renderFreeDownloads();
            setupSearchListeners();
            selectPaymentMethod('pix');
        };

        // Render Catalog Products
        function renderProducts(itemsToRender) {
            const grid = document.getElementById('productsGrid');
            if (itemsToRender.length === 0) {
                grid.innerHTML = `<div class="col-span-full text-center py-12 text-slate-500">Nenhum livro encontrado nesta categoria.</div>`;
                return;
            }

            grid.innerHTML = itemsToRender.map(item => `
                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col group">
                    <div class="aspect-[3/4] overflow-hidden bg-slate-100 relative">
                        <img src="${item.image}" alt="${item.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        <span class="absolute top-3 right-3 bg-navy-900 text-white text-[11px] font-semibold px-2.5 py-1 rounded-full shadow">
                            ${item.type}
                        </span>
                    </div>
                    <div class="p-5 flex-1 flex flex-col justify-between">
                        <div>
                            <span class="text-xs text-gold font-semibold uppercase tracking-wider">${item.author}</span>
                            <h3 class="font-serif font-bold text-slate-900 text-base mt-1 mb-2 leading-snug">${item.title}</h3>
                            <p class="text-slate-500 text-xs line-clamp-2 mb-4">${item.description}</p>
                        </div>
                        <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                            <span class="text-lg font-bold ${item.price === 0 ? 'text-emerald-600' : 'text-slate-900'}">
                                ${item.price === 0 ? 'Gratuito' : 'R$ ' + item.price.toFixed(2).replace('.', ',')}
                            </span>
                            ${item.price === 0 ? 
                                `<button onclick="downloadFreeItem('${item.title}')" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-4 py-2 rounded-lg transition-colors flex items-center space-x-1.5"><i class="fa-solid fa-download"></i><span>Baixar</span></button>` :
                                `<button onclick="addToCart(${item.id})" class="bg-gold hover:bg-gold-600 text-navy-950 text-xs font-semibold px-4 py-2 rounded-lg transition-colors flex items-center space-x-1.5"><i class="fa-solid fa-cart-plus"></i><span>Comprar</span></button>`
                            }
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // Render Free Downloads Section
        function renderFreeDownloads() {
            const freeGrid = document.getElementById('freeGrid');
            const freeItems = products.filter(p => p.price === 0);
            
            freeGrid.innerHTML = freeItems.map(item => `
                <div class="bg-slate-800 border border-slate-700 p-6 rounded-2xl flex flex-col justify-between shadow-lg">
                    <div>
                        <div class="inline-block bg-gold/10 text-gold text-xs font-semibold px-3 py-1 rounded-full mb-3">${item.type}</div>
                        <h3 class="font-serif font-bold text-white text-lg mb-2">${item.title}</h3>
                        <p class="text-slate-400 text-sm mb-6">${item.description}</p>
                    </div>
                    <button onclick="downloadFreeItem('${item.title}')" class="w-full bg-gold hover:bg-gold-600 text-navy-950 font-semibold py-2.5 rounded-xl text-sm transition-colors flex items-center justify-center space-x-2">
                        <i class="fa-solid fa-file-arrow-down"></i>
                        <span>Download Imediato (PDF)</span>
                    </button>
                </div>
            `).join('');
        }

        // Filter Categories
        function filterCategory(cat) {
            currentCategory = cat;
            document.querySelectorAll('.cat-btn').forEach(btn => {
                if (btn.getAttribute('data-category') === cat) {
                    btn.classList.add('bg-navy-900', 'text-white', 'shadow');
                    btn.classList.remove('bg-slate-100', 'text-slate-700');
                } else {
                    btn.classList.remove('bg-navy-900', 'text-white', 'shadow');
                    if(btn.getAttribute('data-category') !== 'gratuitos') {
                        btn.classList.add('bg-slate-100', 'text-slate-700');
                    }
                }
            });

            if (cat === 'todos') {
                renderProducts(products);
            } else if (cat === 'gratuitos') {
                renderProducts(products.filter(p => p.price === 0));
            } else {
                renderProducts(products.filter(p => p.category === cat));
            }

            // Scroll smoothly to catalog if clicked from outside
            document.getElementById('catalogo').scrollIntoView({ behavior: 'smooth' });
        }

        // Search functionality
        function setupSearchListeners() {
            const searchInput = document.getElementById('searchInput');
            const mobileSearch = document.getElementById('mobileSearchInput');

            const handleSearch = (e) => {
                const query = e.target.value.toLowerCase();
                const filtered = products.filter(p => p.title.toLowerCase().includes(query) || p.author.toLowerCase().includes(query));
                renderProducts(filtered);
                document.getElementById('catalogo').scrollIntoView({ behavior: 'smooth' });
            };

            searchInput.addEventListener('input', handleSearch);
            mobileSearch.addEventListener('input', handleSearch);
        }

        // Cart Drawer Control
        function toggleCart() {
            const drawer = document.getElementById('cartDrawer');
            drawer.classList.toggle('hidden');
            renderCartItems();
        }

        function addToCart(id) {
            const product = products.find(p => p.id === id);
            const existing = cart.find(item => item.id === id);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({ ...product, quantity: 1 });
            }
            updateCartBadge();
            showMsgBox("Adicionado!", `${product.title} foi adicionado ao carrinho.`, "fa-cart-shopping");
        }

        function quickAdd(title, price, type) {
            const existing = cart.find(item => item.title === title);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({ id: 999, title, price, type, image: "" });
            }
            updateCartBadge();
            toggleCart();
        }

        function updateCartBadge() {
            const count = cart.reduce((sum, item) => sum + item.quantity, 0);
            document.getElementById('cartBadge').innerText = count;
        }

        function renderCartItems() {
            const container = document.getElementById('cartItemsContainer');
            if (cart.length === 0) {
                container.innerHTML = `<div class="text-center py-12 text-slate-400">Seu carrinho está vazio.</div>`;
                document.getElementById('cartSubtotal').innerText = "R$ 0,00";
                document.getElementById('cartShippingCost').innerText = "R$ 0,00";
                document.getElementById('cartTotal').innerText = "R$ 0,00";
                return;
            }

            container.innerHTML = cart.map((item, index) => `
                <div class="py-4 flex items-center justify-between">
                    <div>
                        <h4 class="font-semibold text-sm text-slate-800">${item.title}</h4>
                        <span class="text-xs text-slate-500">${item.type} | R$ ${item.price.toFixed(2).replace('.', ',')}</span>
                    </div>
                    <div class="flex items-center space-x-3">
                        <span class="text-sm font-bold">Qtd: ${item.quantity}</span>
                        <button onclick="removeFromCart(${index})" class="text-red-500 hover:text-red-700 text-sm"><i class="fa-solid fa-trash"></i></button>
                    </div>
                </div>
            `).join('');

            calculateTotals();
        }

        function removeFromCart(index) {
            cart.splice(index, 1);
            updateCartBadge();
            renderCartItems();
        }

        function calculateShipping() {
            const cep = document.getElementById('cepInput').value.trim();
            if (cep.length < 8) {
                showMsgBox("Atenção", "Por favor, digite um CEP válido com 8 dígitos.", "fa-triangle-exclamation");
                return;
            }
            // Simulate freight calculation based on region
            shippingFee = 22.50;
            shippingInfoText = "Correios SEDEX (Prazo estimado: 3 a 5 dias úteis com código de rastreamento)";
            document.getElementById('shippingResult').innerHTML = `<span class="text-emerald-600 font-semibold"><i class="fa-solid fa-truck"></i> ${shippingInfoText} - R$ 22,50</span>`;
            calculateTotals();
        }

        function calculateTotals() {
            const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
            const total = subtotal + shippingFee;
            document.getElementById('cartSubtotal').innerText = "R$ " + subtotal.toFixed(2).replace('.', ',');
            document.getElementById('cartShippingCost').innerText = "R$ " + shippingFee.toFixed(2).replace('.', ',');
            document.getElementById('cartTotal').innerText = "R$ " + total.toFixed(2).replace('.', ',');
        }

        // Checkout process
        function proceedToCheckout() {
            if (cart.length === 0) {
                showMsgBox("Atenção", "Seu carrinho está vazio.", "fa-triangle-exclamation");
                return;
            }
            toggleCart();
            document.getElementById('checkoutModal').classList.remove('hidden');
        }

        function closeCheckoutModal() {
            document.getElementById('checkoutModal').classList.add('hidden');
        }

        function selectPaymentMethod(method) {
            selectedPayment = method;
            document.querySelectorAll('.payment-method-btn').forEach(btn => {
                btn.classList.remove('border-gold', 'bg-gold/5');
                btn.classList.add('border-slate-200');
            });
            const selectedBtn = document.getElementById(`pay${method.charAt(0).toUpperCase() + method.slice(1)}Btn`);
            selectedBtn.classList.add('border-gold', 'bg-gold/5');
            selectedBtn.classList.remove('border-slate-200');

            const formContainer = document.getElementById('paymentFormContainer');
            if (method === 'pix') {
                formContainer.innerHTML = `
                    <div class="bg-amber-50 border border-amber-200 p-4 rounded-xl text-center space-y-2">
                        <i class="fa-solid fa-qrcode text-3xl text-gold"></i>
                        <p class="text-xs text-slate-700 font-medium">Escaneie o QR Code abaixo pelo aplicativo do seu banco para pagamento instantâneo:</p>
                        <div class="bg-white p-3 inline-block rounded border border-amber-300 font-mono text-xs text-slate-600">00020126580014br.gov.bcb.pix... [SIMULADOR PIX LAMAVEO]</div>
                    </div>`;
            } else if (method === 'card') {
                formContainer.innerHTML = `
                    <div class="space-y-3">
                        <input type="text" placeholder="Número do Cartão" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-sm">
                        <div class="grid grid-cols-2 gap-3">
                            <input type="text" placeholder="MM/AA" class="bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-sm">
                            <input type="text" placeholder="CVV" class="bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-sm">
                        </div>
                    </div>`;
            } else {
                formContainer.innerHTML = `
                    <div class="bg-slate-100 p-4 rounded-xl text-xs text-slate-600 text-center">
                        O boleto bancário será gerado após a confirmação. O prazo de compensação é de até 2 dias úteis.
                    </div>`;
            }
        }

        function completeOrder() {
            const name = document.getElementById('checkoutName').value;
            const email = document.getElementById('checkoutEmail').value;
            if (!name || !email) {
                showMsgBox("Atenção", "Por favor, preencha seu nome e e-mail.", "fa-triangle-exclamation");
                return;
            }
            closeCheckoutModal();
            cart = [];
            updateCartBadge();
            showMsgBox("Pedido Realizado com Sucesso!", `Obrigado, ${name}! Seu pedido foi registrado. Os e-books foram enviados para ${email} e os livros físicos estão sendo preparados para envio por correio.`, "fa-circle-check");
        }

        // Free download simulation
        function downloadFreeItem(title) {
            showMsgBox("Download Iniciado", `O arquivo "${title}" está sendo baixado em formato PDF. Verifique sua pasta de downloads.`, "fa-file-arrow-down");
        }

        // Auth Modal
        function openAuthModal() {
            document.getElementById('authModal').classList.remove('hidden');
        }

        function closeAuthModal() {
            document.getElementById('authModal').classList.add('hidden');
        }

        function handleLogin(e) {
            e.preventDefault();
            const email = document.getElementById('loginEmail').value;
            currentUser = email;
            document.getElementById('userAc
