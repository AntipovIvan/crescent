<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Welcome to Your Vue.js App" />
  <div v-for="item in post.results" :key="item.id">
    <h2>{{ item.field1 }}</h2>
    <p>{{ item.field2 }}</p>
    <p>{{ item.additional_field2 }}</p>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  data() {
    return {
      post: [],
    };
  },
  components: {
    HelloWorld,
  },
  methods: {
    getPosts() {
      fetch('http://localhost:7000/api/yourmodels')
        .then((response) => response.json())
        .then((data) => {
          this.post = data;
          console.log(data);
        });
    },
  },
  mounted() {
    this.getPosts();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
