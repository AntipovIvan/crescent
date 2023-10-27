<script>
	import urlSlug from 'url-slug';
	import NotFound from './NotFound.svelte';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';

	export let params = {};
	let news;
	let data;
	let error;

	onMount(async () => {
		try {
			const response = await fetch('http://172.31.4.199:7000/api/newsmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			news = results;
		} catch (err) {
			error = err;
		}
	});

	$: if (news != null) {
		news.forEach((result, index) => {
			if (params.id === urlSlug(result.id)) {
				news = result;
				console.log(news);
			}
		});
	}
</script>

{#if news}
	<div>
		<h1>{news.title}</h1>
		<p>{news.content}</p>
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
