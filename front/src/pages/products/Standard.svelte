<script>
	import urlSlug from 'url-slug';

	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import NotFound from '../NotFound.svelte';
	import Loading from '../../lib/Loading.svelte';

	export let params = {};
	let product;
	let data;
	let error;
	let isLoading = true;

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/productcardmodels');
			const response = await fetch('http://' + window.location.hostname + ':7000/api/product');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();
			isLoading = false;
			product = results;
		} catch (err) {
			error = err;
		}
	});

	$: if (product != null) {
		product.forEach((result, index) => {
			if (params.title === urlSlug(result.title) && params.title !== 'vicon') {
				product = result;
			}
		});
	}
</script>

{#if isLoading}
	<Loading />
{:else if product}
	<div>
		<h1 class="hero">STANDARD</h1>
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
	.hero {
		color: black;
	}
	p {
		text-align: justify;
	}
</style>
