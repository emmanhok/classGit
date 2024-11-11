<script setup>
import { ref } from "vue";
import FondoAnimado from "./FondoAnimado.vue";

const intereses = ref([
    "Apasionado por el mundo de la tecnología.",
    "Actualmente cursando la Tecnicatura Universitaria en Programación en la Universidad Tecnológica Nacional",
    "I.A.: interesado en el futuro de la IA, particularmente el desarrollo de androides",
    "Docencia: tengo vocación por la enseñanza por lo que soy profesor de historia ejerciendo desde el año 2015",
    "Hobbies: caminar y ciclismo urbano"
]);

</script>

<template>
    <div class="intereses-contenedor">
        <FondoAnimado />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
.intereses-contenedor {
    text-align: center;
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
    background-color: rgb(28, 41, 52);
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: 5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.8rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
}

.item {
    margin-bottom: 1rem;
}
</style>