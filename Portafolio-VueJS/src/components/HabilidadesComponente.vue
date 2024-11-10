<script setup>
// Importamos la función 'ref' de Vue para crear referencias reactivas
import { ref } from 'vue';

// Creamos un array de objetos para almacenar las habilidades.
// Este array se puede modificar o agregar más habilidades en el futuro.
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            { id: 1, nombre: 'HTML/CSS', nivel: 'Principiante', icono: '/src/components/icons/html.svg' },
            { id: 2, nombre: 'Python', nivel: 'Principiante', icono: '/src/components/icons/python.svg' },
            { id: 3, nombre: 'Java', nivel: 'Principiante', icono: '/src/components/icons/java.svg' },
            { id: 4, nombre: 'JavaScript', nivel: 'Principiante', icono: '/src/components/icons/js.svg' },
            { id: 5, nombre: 'SQL', nivel: 'Principiante', icono: '/src/components/icons/sql.svg' }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'Vue.js', nivel: 'Principiante', icono: '/src/components/icons/vue.svg' },
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Intermedio', icono: '/src/components/icons/git.svg' },
            { id: 2, nombre: 'Visual Studio Code', nivel: 'Intermedio', icono: '/src/components/icons/vsc.svg' }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos',
        habilidades: [
            { id: 1, nombre: 'MySQL', nivel: 'Principiante', icono: '/src/components/icons/mysql.svg' },
        ]
    },
    {
        id: 5, nombre: 'Idiomas',
        habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/components/icons/sp.svg' },
            { id: 2, nombre: 'Inglés', nivel: 'Medio', icono: '/src/components/icons/en.svg' }
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