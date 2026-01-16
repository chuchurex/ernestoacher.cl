#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Directorios
const dataDir = path.join(__dirname, '../data/anecdotas');
const outputDir = path.join(__dirname, '../anecdotas');

// Crear directorio de salida si no existe
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// Leer índice
const indexPath = path.join(dataDir, 'index.json');
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

// Template HTML para cada anécdota
function generateAnecdotaHTML(anecdota, content) {
  return `<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${anecdota.cleanTitle} - Anecdotario - Ernesto Acher</title>
    <meta name="description" content="${anecdota.cleanTitle} - Anecdotario de Ernesto Acher">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-anecdotario">
    <div class="site-container">
        <!-- Sidebar (se carga dinámicamente) -->
        <div id="sidebar-container"></div>

        <div class="content-wrapper">
            <!-- Header con menú flotante (se carga dinámicamente) -->
            <div id="header-container"></div>

            <main class="main-content">
                <div class="anecdota-header">
                    <p><a href="../anecdotario-modular.html">← Volver al Anecdotario</a></p>
                    ${anecdota.category !== 'General' ? `<p class="anecdota-category">${anecdota.category}</p>` : ''}
                </div>

                <h1>${anecdota.cleanTitle}</h1>

                <div class="anecdota-content">
                    ${content}
                </div>

                <div class="anecdota-footer">
                    <p><a href="../anecdotario-modular.html">← Volver al Anecdotario</a></p>
                </div>
            </main>
        </div>
    </div>

    <script src="../js/components.js"></script>
</body>
</html>
`;
}

// Generar páginas
let generatedCount = 0;
const errors = [];

index.all.forEach(anecdota => {
  try {
    // Leer contenido del JSON
    const jsonPath = path.join(dataDir, `${anecdota.id}.json`);
    const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

    // Generar HTML
    const html = generateAnecdotaHTML(anecdota, data.content);

    // Guardar archivo
    const outputPath = path.join(outputDir, `${anecdota.id}.html`);
    fs.writeFileSync(outputPath, html, 'utf8');

    generatedCount++;
    console.log(`✓ Generada: ${anecdota.id}.html - ${anecdota.cleanTitle}`);
  } catch (error) {
    errors.push({ id: anecdota.id, error: error.message });
    console.error(`✗ Error al generar ${anecdota.id}.html: ${error.message}`);
  }
});

console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log(`Resumen: ${generatedCount}/${index.all.length} páginas generadas`);
if (errors.length > 0) {
  console.log(`Errores: ${errors.length}`);
  errors.forEach(e => console.log(`  - ${e.id}: ${e.error}`));
}
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
