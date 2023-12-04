<script>
	import urlSlug from 'url-slug';

	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import NotFound from '../NotFound.svelte';

	export let params = {};
	let service;
	let data;
	let error;

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/productcardmodels');
			const response = await fetch(
				'http://' + window.location.hostname + ':7000/api/servicesmodels'
			);
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			service = results;
		} catch (err) {
			error = err;
		}
	});

	$: if (service != null) {
		service.forEach((result, index) => {
			if (params.title === urlSlug(result.title)) {
				service = result;
			}
		});
	}
</script>

{#if service}
	<div>
		<h1 class="hero">STANDARD</h1>
		<h1>{service.title}</h1>
		<p>{service.content}</p>
		<a href="/" use:link>
			<h2>Take me home →</h2>
		</a>
	</div>
{:else}
	<NotFound />
{/if}

<style>
	.hero {
		color: black;
	}
	p {
		text-align: justify;
	}
</style>
