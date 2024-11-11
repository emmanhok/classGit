<script setup>
// Importamos la función 'ref' de Vue para crear referencias reactivas
import { ref } from 'vue';

import html from '/src/components/icons/html.svg';
import python from '/src/components/icons/python.svg';
import java from '/src/components/icons/java.svg';
import js from '/src/components/icons/js.svg';
import sql from '/src/components/icons/sql.svg';

import vue from '/src/components/icons/vue.svg';

import git from '/src/components/icons/git.svg';
import vsc from '/src/components/icons/vsc.svg';

import mysql from '/src/components/icons/mysql.svg';

import sp from '/src/components/icons/sp.svg';
import en from '/src/components/icons/en.svg';

// Creamos un array de objetos para almacenar las habilidades.
// Este array se puede modificar o agregar más habilidades en el futuro.
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            { id: 1, nombre: 'HTML/CSS', nivel: 'Principiante', icono: html },
            { id: 2, nombre: 'Python', nivel: 'Principiante', icono: python },
            { id: 3, nombre: 'Java', nivel: 'Principiante', icono: java },
            { id: 4, nombre: 'JavaScript', nivel: 'Principiante', icono: js },
            { id: 5, nombre: 'SQL', nivel: 'Principiante', icono: sql }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'Vue.js', nivel: 'Principiante', icono: vue },
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Intermedio', icono: git },
            { id: 2, nombre: 'Visual Studio Code', nivel: 'Intermedio', icono: vsc }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos',
        habilidades: [
            { id: 1, nombre: 'MySQL', nivel: 'Principiante', icono: mysql },
        ]
    },
    {
        id: 5, nombre: 'Idiomas',
        habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: sp },
            { id: 2, nombre: 'Inglés', nivel: 'Medio', icono: en }
        ]
    }
]);
</script>

<template>
    <div class="skills-contenedor">
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <span>{{ habilidad.nombre }} {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor{
    padding: 2rem;
    margin-inline: 2rem;
}
.skills-categoria {
    margin-bottom: 10px;
    height: 10rem;
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
    text-shadow: 1px 1px #ff0000;
}

.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5em;
    color: aliceblue;
    font-size: 1.5em;
    font-weight: bold;
    text-shadow: 6px 6px #060606;
}
.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    background-color: rgba(241, 245, 243, 0.856);
    padding: 0.2em;
    border-radius: 20px;
    box-shadow: 8px 0px 15px 8px rgb(207, 20, 20);
    flex: 1 1 200px;
    max-width: 250px;
}
.skill:hover {
    background-color: rgba(255, 240, 29, 0.963);
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: #333;
}

.skill:hover {
    font-size: 1.3em;
    transition: 1s ease;
}
@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center;
    }

    .skill {
        justify-content: center;
    }
}
</style>