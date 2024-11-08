<script setup>
/* AQUÍ VA TODO PURO JS. Con setup luego en template utilizando doble-llaves se ejecutara directamente el codigo js*/
import NavBar from "./components/NavBar.vue";
import DatosPersonales from "./components/DatosPersonales.vue";
import Educacion from "./components/EducacionComponente.vue";
import ExperienciaComponente from "./components/ExperienciaComponente.vue";
import ProyectosComponente from "./components/ProyectosComponente.vue";

</script>

<template>
  <!--AQUÍ VA HTML-->
  <header>
    <!--Barra de navegacion-->
    <NavBar />
    <!--Datos personales-->
    <DatosPersonales />
  </header>
  <main>
    <!--El estilo css de section se encuentra en base.css-->
    <section id="educacion"><h2>Educación - Cursos</h2>
    <Educacion />
    </section>
    <section id="experiencia"><h2>Experiencia</h2></section>
    <ExperienciaComponente />
    <section id="proyectos"><h2>Proyectos</h2></section>
    <ProyectosComponente />
    <section id="habilidades"><h2>Habilidades</h2></section>
    <section id="intereses"><h2>Intereses</h2></section>
  </main>
  <!--Aqui va el contenido principal de la pagina web-->
</template>

<style scoped>
/* AQUÍ VA EL STYLE CSS */

</style>