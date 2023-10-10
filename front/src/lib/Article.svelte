<script>
	import urlSlug from 'url-slug';
	import NotFound from './NotFound.svelte';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';

	export let params = {};
	let article;
	let data;

	onMount(async () => {
		const response = await fetch('http://localhost:7000/api/yourmodels', {
			cache: 'default'
		});
		data = await response.json();
	});

	$: if (data != null) {
		data.results.forEach((result, index) => {
			if (params.field1 === urlSlug(result.field1)) {
				article = result;
			}
		});
	}
</script>

{#if article}
	<div>
		<h1>{article.field1}</h1>
		<img src={article.cover} alt="img" />
		<p>{article.field2}</p>
		<a href="/" use:link>
			<h2>Take me home →</h2>
		</a>
	</div>
{:else}
	<NotFound />
{/if}

<style>
	img {
		max-width: 100%;
	}

	p {
		text-align: justify;
	}
</style>
