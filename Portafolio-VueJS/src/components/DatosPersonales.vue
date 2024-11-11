<script setup>
import linkedin from "/src/assets/linkedin.svg";
import github from "/src/assets/github.svg";
import cv from "/src/assets/cv.svg";

const title = "Emmanuel Herrera Gandini";
const description = "Técnico Universitario en Programación - UTN";
const residencia = "Guaymallén, Mendoza, Argentina";
const presentacion = "¡Hola! Bienvenidos a mi portafolio de proyectos. Soy desarrollador web con experiencias en el desarrollode aplicaciones web y móviles.";
const redesSociales = [
    {id: 1, name: "linkedin", src: linkedin, url: "https://www.linkedin.com/in/emmanuel-herrera-gandini-29485a312/"},
    {id: 2, name: "github", src: github, url: "https://github.com/emmanhok"},
    {id: 3, name: "curriculum", src: cv, url: ""},
];
const telefono = "+54 9 2222-222222";
</script>

<template>
<section class="datos-personales">
    <div class="card">
        <h1>{{ title }}</h1>
        <h2>{{ description }}</h2>
        <p>{{ presentacion }}</p>
        <ul class="container-lista">
            <li v-for="red in redesSociales" :key="red.id">
              <!--Con los dos puntos delante de un atributo se resume el v-bind es decir se linkeando directamente al js-->
                <a :href="red.url" target="_blank"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
            </li>
        </ul>
        <h3>Mi teléfono personal: {{ telefono }}</h3>
        <h4>{{ residencia }}</h4>
    </div>
</section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}
p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}
.card {
  background-color: rgb(28, 41, 52);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}
.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}
.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}
.icon-redsocial:hover {
  background-color: rgb(28, 42, 52);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}
h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>