<template>
  <div class="main-container">
    <h1>Autocomplete Searchbar</h1>
    <Autocomplete />
    <p>An Autocomplete searchbar powered by Deep Learning</p>
  </div>
</template>

<script>
import Autocomplete from './components/Autocomplete.vue'

export default {
  name: 'App',
  components: {
    Autocomplete
  }
}
</script>

<style>

  .main-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-family: 'Fredoka', sans-serif;
  }

  h1 {
    font-size: 3rem;
  }

  @import url('https://fonts.googleapis.com/css2?family=Fredoka&display=swap');
</style>