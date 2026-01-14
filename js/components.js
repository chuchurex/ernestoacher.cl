// Sistema de carga dinámica de componentes
class ComponentLoader {
    constructor() {
        this.menusData = null;
        this.icons = {
            home: `<svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <polyline points="9 22 9 12 15 12 15 22"/>
            </svg>`,
            link: `<svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="7" y1="17" x2="17" y2="7"/>
                <polyline points="10 7 17 7 17 14"/>
            </svg>`,
            refresh: `<svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="23 4 23 10 17 10"/>
                <polyline points="1 20 1 14 7 14"/>
                <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>
            </svg>`,
            sitemap: `<svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="9" y="2" width="6" height="4"/>
                <line x1="12" y1="6" x2="12" y2="10"/>
                <line x1="4" y1="10" x2="20" y2="10"/>
                <line x1="5" y1="10" x2="5" y2="14"/>
                <line x1="12" y1="10" x2="12" y2="14"/>
                <line x1="19" y1="10" x2="19" y2="14"/>
                <rect x="2" y="14" width="6" height="4"/>
                <rect x="9" y="14" width="6" height="4"/>
                <rect x="16" y="14" width="6" height="4"/>
            </svg>`,
            mail: `<svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
            </svg>`,
            audio: `<svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
            </svg>`
        };
        this.audioPlaying = false;
    }

    async init() {
        await this.loadMenusData();
        await this.loadComponents();
        this.renderMenus();
    }

    async loadMenusData() {
        try {
            const response = await fetch('data/menus.json');
            this.menusData = await response.json();
        } catch (error) {
            console.error('Error loading menus data:', error);
        }
    }

    async loadComponents() {
        await Promise.all([
            this.loadComponent('sidebar', '#sidebar-container'),
            this.loadComponent('header', '#header-container')
        ]);
    }

    async loadComponent(name, selector) {
        try {
            const response = await fetch(`components/${name}.html`);
            const html = await response.text();
            const container = document.querySelector(selector);
            if (container) {
                container.innerHTML = html;
            }
        } catch (error) {
            console.error(`Error loading ${name} component:`, error);
        }
    }

    renderMenus() {
        this.renderSidebar();
        this.renderHeaderPrimary();
        this.renderHeaderSecondary();
    }

    renderSidebar() {
        const sidebarMenu = document.getElementById('sidebar-menu');
        if (!sidebarMenu || !this.menusData) return;

        sidebarMenu.innerHTML = this.menusData.sidebar
            .map(item => `<li><a href="${item.href}">${item.label}</a></li>`)
            .join('');
    }

    renderHeaderPrimary() {
        const headerMenu = document.getElementById('header-menu');
        if (!headerMenu || !this.menusData) return;

        headerMenu.innerHTML = this.menusData.headerPrimary
            .map(item => `
                <a href="${item.href}">
                    ${this.icons[item.icon] || ''}
                    ${item.label}
                </a>
            `).join('');
    }

    renderHeaderSecondary() {
        const secondaryMenu = document.getElementById('secondary-menu');
        if (!secondaryMenu || !this.menusData) return;

        secondaryMenu.innerHTML = this.menusData.headerSecondary
            .map(item => `<a href="${item.href}">${item.label}</a>`)
            .join('');
    }
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        const loader = new ComponentLoader();
        loader.init();
    });
} else {
    const loader = new ComponentLoader();
    loader.init();
}
