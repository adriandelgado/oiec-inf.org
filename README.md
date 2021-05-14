# oiec-inf.org

Código fuente de la página oficial de la Olimpiada Informática Ecuatoriana (OIEC).

## Desarrollo

Este proyecto usa [`Hugo`](https://gohugo.io/), [`Tailwind CSS`](https://tailwindcss.com/),
`NPM` y [`Node.js`](https://nodejs.org/) (incluye NPM).

Después de clonar el repositorio, instale todas las dependencias:

```bash
npm install
```

Inicie el servidor de desarrollo con:

```bash
npm run server
```

## ¿Cómo contribuir?

Para los colaboradores autorizados: Debido a que cada push gasta "build minutes"
en Netlify, se debe hacer pruebas locales y solo hacer push cuando se tiene
completo el cambio.

Para colaboradores externos, Push Requests son bienvenidas.

## ¿Cómo crear una noticia/publicación nueva?

Es recomendado tener [`Hugo`](https://gohugo.io/getting-started/installing/) instalado.

```bash
hugo new noticias/nombre-de-la-publicacion/index.md
```

Esto hace que hugo cree un archivo nuevo dentro del directorio
[`contents/noticias`](https://github.com/adriandelgado/oiec-inf.org/tree/main/content/noticias),
y automáticamente lo llena con información determinada basada en archetipes. Dentro
de este directorio se puede poner una imagen llamada `thumbnail.jpg|png`.

Usar Hugo no es estrictamente necesario, solo es necesario el
[Front Matter](https://gohugo.io/content-management/front-matter) en `index.md`.
