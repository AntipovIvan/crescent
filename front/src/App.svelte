<script>
	import Router from 'svelte-spa-router';
	import { routes } from './routes.js';
	import Header from './lib/Header.svelte';
	import Footer from './lib/Footer.svelte';
	import BackToTop from './lib/BackToTop.svelte';
</script>

<Header />

<main>
	<Router {routes} />
</main>

<BackToTop />

<Footer />

<style lang="sass">
	// main
	// 	font-family: 'Montserrat', sans-serif
	// 	background-color: #fff

</style>
