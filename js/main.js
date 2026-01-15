/**
 * Ernesto Acher - Sitio Homenaje
 * JavaScript principal
 * Carrusel controlado por menú
 */

document.addEventListener('DOMContentLoaded', function () {
    // ========== CARRUSEL ==========
    const carousel = {
        container: document.querySelector('.carousel'),
        slides: document.querySelectorAll('.carousel-slide'),
        menuLinks: document.querySelectorAll('.menu-principal a[data-section]'),
        currentIndex: -1,
        autoPlayInterval: null,
        introTimeout: null,
        autoPlayDelay: 6000, // 6 segundos

        init() {
            if (!this.container || this.slides.length === 0) return;

            // Configurar event listeners para el menú principal
            this.menuLinks.forEach((link, index) => {
                // Al pasar el mouse sobre un ítem del menú, mostrar ese slide
                link.addEventListener('mouseenter', () => {
                    this.goToSlide(index);
                    this.pauseAutoPlay();
                });

                link.addEventListener('mouseleave', () => {
                    this.startAutoPlay();
                });

                // Al hacer click, navegar a la página (comportamiento por defecto del enlace)
            });

            // Iniciar secuencia de intro (0 -> 1)
            this.startIntroSequence();

            // Pausar en hover del carrusel
            this.container.addEventListener('mouseenter', () => this.pauseAutoPlay());
            this.container.addEventListener('mouseleave', () => this.startAutoPlay());
        },

        startIntroSequence() {
            // Estado 0: Todo vacío por defecto
            // Esperar un momento antes de mostrar el primer slide
            this.introTimeout = setTimeout(() => {
                this.goToSlide(0);
                this.startAutoPlay();
            }, 3500); // 3.5 segundos de "silencio" inicial
        },

        goToSlide(index) {
            // Validar índice
            if (index < 0) index = this.slides.length - 1;
            if (index >= this.slides.length) index = 0;

            // Remover clase active de todas las slides y links
            this.slides.forEach(slide => slide.classList.remove('active'));
            this.menuLinks.forEach(link => link.classList.remove('active'));

            // Activar la slide correspondiente
            this.slides[index].classList.add('active');

            // Activar el link del menú si existe
            if (this.menuLinks[index]) {
                this.menuLinks[index].classList.add('active');
            }

            this.currentIndex = index;
        },

        nextSlide() {
            this.goToSlide(this.currentIndex + 1);
        },

        prevSlide() {
            this.goToSlide(this.currentIndex - 1);
        },

        startAutoPlay() {
            this.pauseAutoPlay(); // Limpiar intervalo existente
            this.autoPlayInterval = setInterval(() => {
                this.nextSlide();
            }, this.autoPlayDelay);
        },

        pauseAutoPlay() {
            if (this.autoPlayInterval) {
                clearInterval(this.autoPlayInterval);
                this.autoPlayInterval = null;
            }
            if (this.introTimeout) {
                clearTimeout(this.introTimeout);
                this.introTimeout = null;
            }
        }
    };

    // ========== NAVEGACIÓN MENÚ MEDIA ==========
    const menuMedia = {
        links: document.querySelectorAll('.menu-media a'),

        init() {
            this.links.forEach(link => {
                link.addEventListener('click', (e) => {
                    // Por ahora solo marca como activo
                    this.links.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    // La navegación real se implementará cuando existan las páginas
                });
            });
        }
    };

    // ========== EFECTOS VISUALES ==========
    const visualEffects = {
        init() {
            // Efecto parallax sutil en la elipse
            const ellipse = document.querySelector('.ellipse-bg');
            if (ellipse && window.innerWidth > 768) {
                document.addEventListener('mousemove', (e) => {
                    const moveX = (e.clientX - window.innerWidth / 2) * 0.005;
                    const moveY = (e.clientY - window.innerHeight / 2) * 0.005;
                    ellipse.style.transform = `translate(calc(-50% + ${moveX}px), calc(-50% + ${moveY}px))`;
                });
            }
        }
    };

    // ========== KEYBOARD NAVIGATION ==========
    const keyboardNav = {
        init() {
            document.addEventListener('keydown', (e) => {
                switch (e.key) {
                    case 'ArrowLeft':
                        carousel.prevSlide();
                        carousel.pauseAutoPlay();
                        setTimeout(() => carousel.startAutoPlay(), 10000);
                        break;
                    case 'ArrowRight':
                        carousel.nextSlide();
                        carousel.pauseAutoPlay();
                        setTimeout(() => carousel.startAutoPlay(), 10000);
                        break;
                }
            });
        }
    };

    // ========== INICIALIZACIÓN ==========
    carousel.init();
    menuMedia.init();
    visualEffects.init();
    keyboardNav.init();

    // El primer link ya no se marca activo manualmente para respetar el estado inicial vacío

    console.log('🎭 Sitio Ernesto Acher cargado');
});
