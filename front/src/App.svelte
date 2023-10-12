<script lang="ts">
	import Router, { link } from 'svelte-spa-router';
	import { routes } from './routes.js';
	import Header from './lib/Header.svelte';
	import Footer from './lib/Footer.svelte';
</script>

<Header />

<main>
	<Router {routes} />
</main>

<Footer />

<style lang="sass">
	main
		font-family: 'Lucida Sans', sans-serif
		background-color: #fff
		// padding: 1rem 5rem

</style>
