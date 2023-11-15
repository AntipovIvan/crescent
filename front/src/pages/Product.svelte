<script>
	import urlSlug from 'url-slug';
	import NotFound from './NotFound.svelte';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';

	export let params = {};
	let product;
	let data;
	let error;

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/productcardmodels');
			const response = await fetch('http://localhost:7000/api/productcardmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			product = results;
		} catch (err) {
			error = err;
		}
	});

	$: if (product != null) {
		product.forEach((result, index) => {
			if (params.id === urlSlug(result.id)) {
				product = result;
			}
		});
	}
</script>

{#if product}
	<div>
		<h1>{product.title}</h1>
		<p>{product.content}</p>
		<a href="/" use:link>
			<h2>Take me home →</h2>
		</a>
	</div>
{:else}
	<NotFound />
{/if}

<style>
	p {
		text-align: justify;
	}
</style>
