---
name: nextjs-project-setup
version: 1.0.0
description: Set up a new Next.js project with best practices, configured development environment, TypeScript support, and production-ready structure. Use when starting a new Next.js project, initializing a web application, or setting up a project with recommended folder structure and tooling.
---

# Next.js Project Setup

Este Skill te ayuda a crear un nuevo proyecto Next.js con mejores prácticas, configuración de desarrollo optimizada y estructura lista para producción.

## Instructions

Para crear un nuevo proyecto Next.js con mis mejores prácticas, sigue estos pasos:

1. **Clonar el template:**
```bash
   git clone https://github.com/JoseCortezz25/template-starter-nextjs.git tu-nombre-proyecto
   cd tu-nombre-proyecto
```

2. **Limpiar el historial de git:**
```bash
   rm -rf .git
   git init
```

3. **Instalar dependencias con pnpm:**
```bash
   pnpm install
```

4. **Iniciar el servidor de desarrollo:**
```bash
   pnpm dev
   # Luego abre http://localhost:3000 en tu navegador
```

5. **Estructura del proyecto:**
   - `/app` - Rutas y componentes usando App Router
   - `/public` - Archivos estáticos
   - `/components` - Componentes reutilizables
   - `next.config.ts` - Configuración de Next.js
   - `tsconfig.json` - Configuración de TypeScript

## Características incluidas

- Next.js con App Router
- TypeScript configurado
- Fuente Geist optimizada con next/font
- Estructura lista para producción
- Soporte para desarrollo rápido con hot reload
- Gestión de dependencias con pnpm

## Ejemplos

### Crear un nuevo proyecto desde cero
```
"Necesito iniciar un nuevo proyecto Next.js con mis mejores prácticas"
```

### Clonar y configurar el template
```
"Clona el template starter de Next.js y configura todo para empezar a trabajar"
```

### Instalar y verificar la instalación
```
"Configura el template de Next.js con pnpm e inicia el servidor de desarrollo"
```

## Comandos útiles con pnpm

- `pnpm dev` - Inicia servidor de desarrollo
- `pnpm build` - Compila para producción
- `pnpm start` - Ejecuta servidor de producción
- `pnpm lint` - Ejecuta el linter

## Siguientes pasos

Después de crear el proyecto, puedes:
- Crear nuevas rutas en `/app`
- Agregar componentes a `/components`
- Personalizar estilos según tus necesidades
- Desplegar en Vercel u otro hosting