<script setup>
import { ref } from 'vue';

const titulo = 'Desarrollador Full Stack';
const fecha = 'Desde Enero 2022 / Julio 2024';

const experiencias = ref([
    { id: 1, src: '/src/assets/develop1.png', parrafo: 'Desarrolle una aplicación con mi equipo de estudio de la Tecnicatura llamada SolucionCoin en pseudocodigo (PSeInt), la cual consiste en una serie de juegos de azar y de acertijos.' },
    { id: 2, src: '/src/assets/develop2.png', parrafo: 'Desarrolle junto con mi equipo de estudios la app de juegos SolucionCoin en lenguaje de programación Java.' }
    /*{ id: 3, src: '/src/assets/configuracion.svg', parrafo: 'Implementé soluciones de autenticación y autorización, mejorando la seguridad del sitio web y reduciendo los intentos de acceso no autorizado en un 20%.' },
    { id: 4, src: '/src/assets/olux.svg', parrafo: 'Colaboré con diseñadores de UX/UI para crear interfaces de usuario atractivas y fáciles de usar, aumentando la satisfacción del cliente en un 15%.' },
    { id: 5, src: '/src/assets/watch.svg', parrafo: 'Automatizé procesos de despliegue continuo utilizando Jenkins y Docker, reduciendo los tiempos de despliegue en un 40%.' }*/
]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="imagen-svg" :src="experiencia.src" :width="45" :alt="experiencia.parrafo">
                <p>{{ experiencia.parrafo }}</p>
            </li>
            <!--<li class="item">
                <img class="imagen-svg" src="/src/assets/develop1.png" width="45" alt="">
                <p>Lideré un equipo de 5 desarrolladores en la creación de una plataforma de comercio electrónico que incrementó las ventas en un 35% durante el primer año.</p>
            </li>
            <li class="item">
                <img class="imagen-svg" src="/src/assets/develop2.png" width="45" alt="">
                <p>Diseñé y desarrollé aplicaciones web utilizando Node.js, React y Mongo, logrando reducir el tiempo de carga de las páginas en un 50%.</p>
            </li>-->
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
}

.titulo {
    font-size: 1.5rem;
    color: coral;
}

.fecha {
    font-size: 1rem;
    color: burlywood;
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>