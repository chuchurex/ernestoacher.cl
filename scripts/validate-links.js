const fs = require('fs-extra');
const path = require('path');
const cheerio = require('cheerio');
const chalk = require('chalk');

class LinkValidator {
  constructor() {
    this.errors = [];
    this.warnings = [];
    this.checkedLinks = new Set();
    this.publicDir = path.join(__dirname, '../public');
  }

  // Obtener todos los archivos HTML
  async getAllHtmlFiles(dir) {
    const files = [];
    const entries = await fs.readdir(dir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await this.getAllHtmlFiles(fullPath)));
      } else if (entry.name.endsWith('.html')) {
        files.push(fullPath);
      }
    }

    return files;
  }

  // Validar un archivo HTML
  async validateFile(filePath) {
    try {
      const html = await fs.readFile(filePath, 'utf8');
      const $ = cheerio.load(html);
      const relativePath = path.relative(this.publicDir, filePath);

      // Validar enlaces <a href>
      $('a[href]').each((i, el) => {
        const href = $(el).attr('href');
        this.checkLink(href, relativePath, 'link');
      });

      // Validar imágenes <img src>
      $('img[src]').each((i, el) => {
        const src = $(el).attr('src');
        this.checkLink(src, relativePath, 'image');
      });

      // Validar CSS <link>
      $('link[rel="stylesheet"]').each((i, el) => {
        const href = $(el).attr('href');
        this.checkLink(href, relativePath, 'stylesheet');
      });

      // Validar scripts <script src>
      $('script[src]').each((i, el) => {
        const src = $(el).attr('src');
        this.checkLink(src, relativePath, 'script');
      });
    } catch (error) {
      console.error(chalk.red(`Error validando ${filePath}:`), error.message);
    }
  }

  // Verificar un enlace individual
  checkLink(url, sourceFile, type) {
    // Ignorar enlaces externos, anclas, y protocolos especiales
    if (!url ||
        url.startsWith('http://') ||
        url.startsWith('https://') ||
        url.startsWith('#') ||
        url.startsWith('mailto:') ||
        url.startsWith('tel:') ||
        url.startsWith('javascript:')) {
      return;
    }

    // Crear clave única para evitar verificar el mismo link múltiples veces
    const key = `${sourceFile}::${url}`;
    if (this.checkedLinks.has(key)) {
      return;
    }
    this.checkedLinks.add(key);

    // Resolver ruta absoluta
    let targetPath;
    if (url.startsWith('/')) {
      // Ruta absoluta desde raíz
      targetPath = path.join(this.publicDir, url);
    } else {
      // Ruta relativa desde el archivo fuente
      const sourceDir = path.dirname(path.join(this.publicDir, sourceFile));
      targetPath = path.resolve(sourceDir, url);
    }

    // Remover query strings y fragments
    targetPath = targetPath.split('?')[0].split('#')[0];

    // Verificar existencia
    if (!fs.existsSync(targetPath)) {
      this.errors.push({
        type: type,
        source: sourceFile,
        target: url,
        message: `${type} no encontrado: ${url}`
      });
    }
  }

  // Escanear todos los archivos
  async scanAll() {
    console.log(chalk.blue('\n🔍 VALIDANDO ENLACES DEL SITIO\n'));

    const htmlFiles = await this.getAllHtmlFiles(this.publicDir);
    console.log(chalk.gray(`Archivos HTML encontrados: ${htmlFiles.length}\n`));

    for (const file of htmlFiles) {
      await this.validateFile(file);
    }
  }

  // Generar reporte
  report() {
    console.log(chalk.blue('\n📋 REPORTE DE VALIDACIÓN\n'));
    console.log(chalk.gray(`Enlaces únicos verificados: ${this.checkedLinks.size}`));

    if (this.warnings.length > 0) {
      console.log(chalk.yellow(`\n⚠️  ${this.warnings.length} advertencias:\n`));
      this.warnings.forEach((warn, i) => {
        console.log(chalk.yellow(`  ${i + 1}. ${warn.source}`));
        console.log(chalk.gray(`     ${warn.message}`));
      });
    }

    if (this.errors.length > 0) {
      console.log(chalk.red(`\n❌ ${this.errors.length} errores encontrados:\n`));

      // Agrupar por tipo
      const byType = {};
      this.errors.forEach(err => {
        if (!byType[err.type]) byType[err.type] = [];
        byType[err.type].push(err);
      });

      Object.keys(byType).forEach(type => {
        console.log(chalk.red(`  ${type.toUpperCase()}S (${byType[type].length}):`));
        byType[type].forEach(err => {
          console.log(chalk.red(`    ✗ ${err.source}`));
          console.log(chalk.gray(`      → ${err.target}`));
        });
        console.log('');
      });

      console.log(chalk.bold.red('Build FAILED: Hay enlaces rotos\n'));
      process.exit(1);
    } else {
      console.log(chalk.bold.green('\n✅ Todos los enlaces son válidos\n'));
    }
  }

  // Ejecutar validación completa
  async validate() {
    await this.scanAll();
    this.report();
  }
}

// Ejecutar validación si se llama directamente
if (require.main === module) {
  const validator = new LinkValidator();
  validator.validate().catch(error => {
    console.error(chalk.red('Error en validación:'), error);
    process.exit(1);
  });
}

module.exports = LinkValidator;
