<script setup>
// Importamos la función 'ref' de Vue para crear referencias reactivas
import { ref } from 'vue';

// Creamos un array de objetos para almacenar las habilidades.
// Este array se puede modificar o agregar más habilidades en el futuro.
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: '/src/components/icons/js.svg' },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: '/src/components/icons/python.svg' },
            { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: '/src/components/icons/html-css.svg' },
            { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: '/src/components/icons/java.svg' },
            { id: 5, nombre: 'SQL', nivel: 'Intermedio', icono: '/src/components/icons/sql.svg' }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: '/src/components/icons/react.svg' },
            { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: '/src/components/icons/vue.svg' },
            { id: 3, nombre: 'Node.js', nivel: 'Avanzado', icono: '/src/components/icons/node.svg' },
            { id: 4, nombre: 'Django', nivel: 'Intermedio', icono: '/src/components/icons/django.svg' },
            { id: 5, nombre: 'Bootstrap', nivel: 'Avanzado', icono: '/src/components/icons/bootstrap.svg' }
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: '/src/components/icons/git.svg' },
            { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: '/src/components/icons/docker.svg' },
            { id: 3, nombre: 'Cypress', nivel: 'Intermedio', icono: '/src/components/icons/cypress.svg' },
            { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: '/src/components/icons/figma.svg' },
            { id: 5, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: '/src/components/icons/visual.svg' }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos',
        habilidades: [
            { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: '/src/components/icons/mongo.svg' },
            { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: '/src/components/icons/mysql.svg' },
            { id: 3, nombre: 'PostgreSQL', nivel: 'Intermedio', icono: '/src/components/icons/postgres.svg' }
        ]
    },
    {
        id: 5, nombre: 'Idiomas',
        habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/components/icons/arg.svg' },
            { id: 2, nombre: 'Inglés', nivel: 'Avanzado (C1)', icono: '/src/components/icons/eeuu.svg' }
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