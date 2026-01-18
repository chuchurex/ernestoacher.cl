const fs = require('fs-extra');
const Handlebars = require('handlebars');
const path = require('path');
const chalk = require('chalk');

class SiteBuilder {
  constructor() {
    this.siteData = require('../src/data/site.json');
    this.navigation = require('../src/data/navigation.json');
    this.templates = {};
    this.partials = {};
  }

  // Registrar helpers de Handlebars
  registerHelpers() {
    Handlebars.registerHelper('eq', (a, b) => a === b);
    Handlebars.registerHelper('ne', (a, b) => a !== b);
    Handlebars.registerHelper('or', (a, b) => a || b);
    Handlebars.registerHelper('and', (a, b) => a && b);
  }

  // Registrar plantillas y partials
  async registerTemplates() {
    console.log(chalk.blue('📦 Registrando plantillas y partials...'));

    // Registrar partials
    const partialFiles = ['sidebar', 'header', 'nav-right', 'icon'];
    for (const partial of partialFiles) {
      try {
        const content = await fs.readFile(
          path.join(__dirname, `../src/templates/partials/${partial}.html`),
          'utf8'
        );
        Handlebars.registerPartial(partial, content);
        console.log(chalk.gray(`  ✓ Partial registrado: ${partial}`));
      } catch (error) {
        console.error(chalk.red(`  ✗ Error registrando partial ${partial}:`, error.message));
      }
    }

    // Cargar plantillas principales
    try {
      const baseTemplate = await fs.readFile(
        path.join(__dirname, '../src/templates/base.html'),
        'utf8'
      );
      this.templates.base = Handlebars.compile(baseTemplate);
      console.log(chalk.gray('  ✓ Plantilla base cargada'));

      const interiorTemplate = await fs.readFile(
        path.join(__dirname, '../src/templates/page-interior.html'),
        'utf8'
      );
      this.templates.interior = Handlebars.compile(interiorTemplate);
      console.log(chalk.gray('  ✓ Plantilla interior cargada'));

      const homeTemplate = await fs.readFile(
        path.join(__dirname, '../src/templates/page-home.html'),
        'utf8'
      );
      this.templates.home = Handlebars.compile(homeTemplate);
      console.log(chalk.gray('  ✓ Plantilla home cargada'));
    } catch (error) {
      console.error(chalk.red('  ✗ Error cargando plantillas:', error.message));
      throw error;
    }
  }

  // Construir una página individual
  async buildPage(sectionId) {
    try {
      // Cargar datos de la sección
      const sectionData = require(`../src/data/sections/${sectionId}.json`);

      // Encontrar la sección en navegación
      const navSection = this.navigation.sidebar.find(s => s.id === sectionId);
      if (!navSection) {
        console.error(chalk.red(`  ✗ Sección no encontrada en navegación: ${sectionId}`));
        return;
      }

      // Leer contenido HTML
      const contentPath = path.join(__dirname, `../src/content/${sectionId}.html`);
      let pageContent = '';

      if (await fs.pathExists(contentPath)) {
        pageContent = await fs.readFile(contentPath, 'utf8');
      } else {
        console.log(chalk.yellow(`  ⚠ No se encontró contenido para ${sectionId}, usando placeholder`));
        pageContent = `<p>Contenido en construcción...</p>`;
      }

      // Preparar menú flotante derecho (subNavItems)
      const subNavItems = navSection.subPages.map((sp, index) => ({
        label: sp.label,
        url: sp.default ? null : sp.url,
        active: sp.default
      }));

      // Renderizar contenido interior
      const interiorContent = this.templates.interior({
        siteName: this.siteData.siteName,
        pageTitle: sectionData.title,
        currentSection: sectionId,
        navigation: this.navigation,
        pageContent: pageContent,
        subNavItems: subNavItems
      });

      // Renderizar página completa con plantilla base
      const fullHtml = this.templates.base({
        siteName: this.siteData.siteName,
        pageTitle: sectionData.title,
        bodyClass: sectionData.bodyClass,
        meta: sectionData.meta,
        content: interiorContent
      });

      // Determinar archivo de salida
      const outputFileName = navSection.url.replace(/^\//, '');
      const outputPath = path.join(__dirname, '../public', outputFileName);

      // Asegurar que el directorio existe
      await fs.ensureDir(path.dirname(outputPath));

      // Escribir archivo
      await fs.writeFile(outputPath, fullHtml);

      console.log(chalk.green(`  ✓ Generada: ${outputFileName}`));
    } catch (error) {
      console.error(chalk.red(`  ✗ Error construyendo página ${sectionId}:`), error.message);
    }
  }

  // Construir homepage
  async buildHomePage() {
    try {
      const homeData = this.siteData.homePage;

      const homeHtml = this.templates.home({
        siteName: this.siteData.siteName,
        meta: this.siteData.meta,
        navigation: this.navigation,
        carousel: homeData.carousel,
        ernestoPhoto: homeData.ernestoPhoto,
        menuMedia: homeData.menuMedia,
        footer: homeData.footer
      });

      const outputPath = path.join(__dirname, '../public/index.html');
      await fs.writeFile(outputPath, homeHtml);

      console.log(chalk.green('  ✓ Generada: index.html'));
    } catch (error) {
      console.error(chalk.red('  ✗ Error construyendo homepage:'), error.message);
    }
  }

  // Construir todas las páginas
  async buildAll() {
    console.log(chalk.bold.blue('\n🚀 INICIANDO BUILD DEL SITIO\n'));

    // Registrar helpers y templates
    this.registerHelpers();
    await this.registerTemplates();

    console.log(chalk.blue('\n📄 Generando páginas...'));

    // Construir homepage
    await this.buildHomePage();

    // Construir cada sección del sidebar
    for (const section of this.navigation.sidebar) {
      await this.buildPage(section.id);
    }

    console.log(chalk.bold.green('\n✅ Build completado exitosamente\n'));
  }

  // Copiar archivos estáticos
  async copyAssets() {
    console.log(chalk.blue('📁 Copiando assets...'));

    const assetsToCopy = [
      { src: 'images', dest: 'public/images' },
      { src: 'js', dest: 'public/js' }
    ];

    for (const asset of assetsToCopy) {
      const srcPath = path.join(__dirname, '..', asset.src);
      const destPath = path.join(__dirname, '..', asset.dest);

      if (await fs.pathExists(srcPath)) {
        await fs.copy(srcPath, destPath);
        console.log(chalk.gray(`  ✓ Copiado: ${asset.src} → ${asset.dest}`));
      }
    }
  }

  // Limpiar directorio public
  async clean() {
    const publicDir = path.join(__dirname, '../public');
    await fs.emptyDir(publicDir);
    console.log(chalk.gray('🗑️  Directorio public limpiado'));
  }

  // Build completo
  async fullBuild() {
    try {
      await this.clean();
      await this.copyAssets();
      await this.buildAll();
    } catch (error) {
      console.error(chalk.bold.red('\n❌ ERROR EN BUILD:'), error);
      process.exit(1);
    }
  }
}

// Ejecutar build si se llama directamente
if (require.main === module) {
  const builder = new SiteBuilder();
  builder.fullBuild();
}

module.exports = SiteBuilder;
