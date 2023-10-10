<script lang="ts">
	import svelteLogo from './assets/svelte.svg';
	import viteLogo from '/vite.svg';
	import Counter from './lib/Counter.svelte';
	import CatFacts from './CatFacts.svelte';
	import FetchApi from './FetchAPI.svelte';
	import Card from './lib/Card.svelte';
	import Router, { link } from 'svelte-spa-router';
	import { routes } from './routes.js';
</script>

<main>
	<Router {routes} />
</main>

<style lang="sass">
	main
		background-color: #fff
	.logo
		height: 6em
		padding: 1.5em
		will-change: filter
		transition: filter 300ms
	.logo:hover 
		filter: drop-shadow(0 0 2em #646cffaa)
	.logo.svelte:hover 
		filter: drop-shadow(0 0 2em #ff3e00aa)
	.read-the-docs 
		color: #888
	.card2
		position: absolute
		display: block
</style>
