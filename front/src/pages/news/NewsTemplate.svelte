<script>
	import urlSlug from 'url-slug';
	import { onMount } from 'svelte';
	import NotFound from '../NotFound.svelte';
	import Loading from '../../lib/Loading.svelte';

	export let params = {};
	let news;
	let data;
	let error;
	let isLoading = true;

	const categoryMapping = {
		EVENT: 'セミナー&イベント',
		PRODUCT_INFO: '製品&開発情報',
		NOTICE: 'お知らせ'
	};

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/productcardmodels');
			const response = await fetch('http://' + window.location.hostname + ':7000/api/newsmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();
			isLoading = false;
			news = results.map((result) => {
				result.category = categoryMapping[result.category];
				return result;
			});
		} catch (err) {
			error = err;
		}
	});

	$: if (news != null) {
		news.forEach((result, index) => {
			if (params.id === urlSlug(result.id) && params.title !== 'vicon') {
				news = result;
			}
		});
	}
</script>

<section class="section">
	{#if isLoading}
		<Loading />
	{:else if news}
		<h1>{news.category}</h1>
		<div class="content">
			<h2>{news.title}</h2>

			<article>
				<time>{news.date.replaceAll('-', '.')}</time>
				<span class="cardTitle">{news.title}</span>
			</article>
		</div>
	{:else}
		<NotFound />
	{/if}
</section>

<style>
	.section {
		min-height: 53vh;
		position: relative;
	}

	.cardTitle {
		margin-left: 3rem;
	}

	h1 {
		margin: 0 0 3rem 0;
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}
	h2 {
		padding-bottom: 1rem;

		width: max-content;
	}
	section {
		padding: 5rem;
		background-color: #efefef;
	}

	.content {
		display: flex;
		gap: 5rem;
		flex-wrap: wrap;
		flex-direction: row;
		margin-top: 2rem;
		margin-bottom: 5rem;
		align-items: baseline;
	}

	p {
		margin: 0;
		font-weight: bold;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	@media screen and (max-width: 700px) {
		.content {
			flex-direction: column;
		}
		ul {
			flex-direction: column;
		}
		.cardTitle {
			margin-left: 1rem;
		}
	}
	@media screen and (max-width: 950px) {
		h1 {
			text-align: center;
		}
		section {
			padding: 2rem;
		}
		.content {
			flex-direction: column;
			gap: 1rem;
			justify-content: center;
			align-items: center;
		}

		ul {
			flex-direction: column;
		}
	}
</style>
