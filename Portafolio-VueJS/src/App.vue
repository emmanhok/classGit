<script setup>
/* AQUÍ VA TODO PURO JS. Con setup luego en template utilizando doble-llaves se ejecutara directamente el codigo js*/
import NavBar from './components/navbar.vue';
</script>

<template>
  <!--AQUÍ VA HTML-->
  <!--Barra de navegacion-->
  <header>
    <NavBar />
  </header>
  <main>
    <section id="educacion"><h2>Educación - Cursos</h2></section>
    <section id="experiencia"><h2>Experiencia</h2></section>
    <section id="proyectos"><h2>Proyectos</h2></section>
    <section id="habilidades"><h2>Habilidades</h2></section>
    <section id="intereses"><h2>Intereses</h2></section>
  </main>
  <!--Aqui va el contenido principal de la pagina web-->
</template>

<style scoped>
/* AQUÍ VA EL STYLE CSS */


</style>
