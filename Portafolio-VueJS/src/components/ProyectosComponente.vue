<script setup>
import { ref } from "vue";
// .ref es una función que se utiliza para crear una referencia reactiva en Vue 3
var misProyectos = ref([]);
// .value es una propiedad que se utiliza para acceder al valor de una referencia reactiva en Vue 3
misProyectos.value = ([
    // Esto es un array de objetos que contiene informacion sobre los proyectos
    {
        id: 1,
        src: "/src/assets/proyecto1.png",
        titulo: "Aplicación de juegos en PSeInt (2024)",
        descripcion: "Creamos una serie de juegos con el grupo Solucion 202 de la TUP denominado SolucionCoin",
        proyectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/emmanhok"
    },
    {
        id: 2,
        src: "/src/assets/proyecto2.png",
        titulo: "Aplicacion de juegos en Java (2024)",
        descripcion: "Reformulamos la app de juegos SolucionCoin en lenguaje Java",
        proyectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/emmanhok"
    },
])
</script>

<template>
    <!--Aqui va el codigo HTML de la galeria de proyectos-->
    <div class="galeria">
        <!--Itera sobre cada proyecto en la lista de misProyectos-->
        <!--key es una propiedad especial que se utiliza para identificar de forma unica cada elemento en una lista de Vue.js-->
        <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
            <!-- Muestra la imagen del proyecto utilizando: una directiva de imagen de enlace de atributo en Vue.js-->
            <img :src="proyecto.src" :alt="proyecto.titulo">
            <div class="proyecto-info">
                <!--Muestr el titulo y la descripcion del proyecto utilizando la interpolacion de Vue.js-->
                <h3>{{ proyecto.titulo }}</h3>
                <p>{{ proyecto.descripcion }}</p>
                <div class="proyecto-links">
                    <!-- rel=noopener noreferrer es por un tema de seguridad -->
                    <a :href="proyecto.proyectoLink" class="btn-ver-mas" target="_blank" rel="noopener noreferrer">Ver Proyecto</a>
                    <a :href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer">Ver Código en GitHub</a>
                </div>
            </div>
        </li>
    </div>
</template>

<style scoped>
    /* Estilos Fondo Animado de CSS de la galería */
.galeria {
    /* Establece el ancho de la galería al 100% del contenedor padre */
    width: 100%;

    /* Establece la altura de la galería al 100% del contenedor padre */
    height: 100%;

    /* Utiliza Flexbox para organizar los elementos hijos en la galería */
    display: flex;

    /* Permite que los elementos se ajusten y pasen a la siguiente línea si no caben en una sola fila */
    flex-wrap: wrap;

    /* Establece un espacio de 20px entre los elementos de la galería */
    gap: 20px;

    /* Agrega un padding de 20px alrededor de la galería */
    padding: 20px;

    /* Centra los elementos hijos horizontalmente */
    justify-content: center;

    /* Aplica un fondo con un degradado de colores */
    background: linear-gradient(-20deg, #D5BA98, #0C223F);

    /* Ajusta el tamaño del fondo para que cubra el área completa */
    background-size: 400% 400%;

    /* Aplica una animación al fondo que dura 15 segundos, tiene una transición suave y se repite infinitamente */
    animation: gradient 5s infinite;
}

@keyframes gradient{
    0%{
        background-position: 0% 50%;
    }

    50%{
        background-position: 100% 50%;
    }
    100%{
        background-position: 0% 50%;
    }
}

.proyecto {
    /* Utiliza flexbox para organizar el contenido del proyecto en una columna */
    display: flex;
    flex-direction: column;

    /* Aplica un borde de 2px sólido y color gris claro (#ddd) alrededor del proyecto */
    border: 2px solid #353f5b;
    border-radius: 8px;

    /* Oculta cualquier contenido que se desborde del contenedor */
    overflow: hidden;

    /* Establece un color de fondo claro para el proyecto */
    background-color: #f9f9f9;

    /* Define el ancho máximo del proyecto en 222px */
    max-width: 222px;

    /* Hace que el contenedor se ajuste flexiblemente ocupando al menos 300px de ancho */
    flex: 1 300px;
}
    /* Estilo para las imágenes dentro del contenedor 'proyecto' */
.proyecto img {
    /* Hace que la imagen ocupe el 100% del ancho del contenedor */
    width: 100%;

    /* Mantiene la relación de aspecto de la imagen */
    height: auto;

    /* Asegura que la imagen se muestre como un bloque, sin espacio en línea alrededor */
    display: block;
}

    /* La clase 'proyecto-info' contiene la información del proyecto */
.proyecto-info {
    /* Agrega un padding de 15px alrededor de la información */
    padding: 15px;

    /* Centra el texto dentro del contenedor */
    text-align: center;
}
    /* Estilo para los títulos (h3) dentro de la sección de información del proyecto */
.proyecto-info h3 {
    /* Establece un margen superior e inferior de 10px */
    margin: 10px 0;

    /* Define el tamaño de la fuente a 1.3em (relativo al tamaño de fuente del contenedor) */
    font-size: 1.3em;

    /* Aplica un color gris oscuro (#333) al texto */
    color: #333;

    /* Investigue para personalizar el grosor de la fuente*/
    font-weight: bold;
}

    /* Estilo para los párrafos dentro de la sección de información del proyecto */
.proyecto-info p {
    /* Establece un margen superior e inferior de 10px */
    margin: 10px 0;

    /* Define el tamaño de la fuente a 1em (igual al tamaño de fuente base) */
    font-size: 1rem;

    /* Aplica un color gris (#666) al texto */
    color: #0C223F;

    /* Investigue para personalizar el grosor de la fuente*/
    font-weight: lighter;
}
    /* La clase 'proyecto-links' organiza los enlaces y botones del proyecto */
.proyecto-links {
      /* Utiliza flexbox para organizar los enlaces en una columna */
    display: flex;
    flex-direction: column;

    /* Establece un espacio de 10px entre los elementos */
    gap: 10px;

    /* Agrega un margen superior de 10px */
    margin-top: 10px;
}
    /* Aqui he agregado un estilo al texto que direcciona a los enlaces agregando un fondo y un contorno al texto */
.proyecto-links a{
    color: #d5be10;
    background-color: #353f5b;
    border: groove;
    border-radius: 3rem;
    border-width: 0.5rem;
}
</style>