# 🌐 Puerto Asignado

## Puerto: **3012**

Este proyecto usa el puerto **3012** según la convención de puertos del equipo.

### Comandos de desarrollo:

```bash
# Modo desarrollo completo (puerto 3012)
npm run dev

# URL de desarrollo
http://localhost:3012
```

### Registro central

Puerto registrado en: `/Sites/vigentes/dashboard/PORTS.md`

### Rango de puertos

- **3000-3019**: Frontends Node/Vite (ernestoacher.cl usa 3012)
- **8000-8019**: Backends Python/APIs
- **8080-8099**: Docker/WordPress

---

**Nota**: Si necesitas cambiar el puerto, actualiza:
1. `package.json` → scripts `dev:serve` y `legacy:serve`
2. `/Sites/vigentes/dashboard/PORTS.md`
3. Este archivo (PUERTO.md)
