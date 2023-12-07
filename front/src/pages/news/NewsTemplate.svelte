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
			if (params.id === urlSlug(result.id)) {
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

		<article class="content">
			<time>{news.date.replaceAll('-', '.')}</time>
			<h2 class="cardTitle">{news.title}</h2>
			<p>{news.content}</p>

			{#if news.images.length > 0}
				<ul class="image-gallery">
					{#each news.images as image}
						<li>
							<img src={image.image} alt={image.id} />
						</li>
					{/each}
				</ul>
			{/if}
		</article>
	{:else}
		<NotFound />
	{/if}
</section>

<style>
	ul {
		list-style: none;
	}

	.image-gallery {
		text-align: center;
	}

	.image-gallery > li {
		display: inline-block;
		width: 49%;
		margin: 0 5px 10px 5px;
		position: relative;
		cursor: pointer;
	}

	@supports (display: flex) {
		.image-gallery {
			display: flex;
			flex-wrap: wrap;
			justify-content: center;
			gap: 10px;
		}

		.image-gallery > li {
			margin: 0;
		}

		/* .image-gallery::after {
			content: '';
			flex-basis: 350px;
		} */
	}

	.image-gallery li img {
		object-fit: cover;
		max-width: 100%;
		height: auto;
		vertical-align: middle;
		border-radius: 5px;
	}

	.section {
		min-height: 53vh;
		position: relative;
	}

	.cardTitle {
		font-weight: bold;
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
		gap: 2rem;
		flex-wrap: wrap;
		flex-direction: column;
		margin-top: 2rem;
		margin-bottom: 5rem;
		align-items: baseline;
		padding: 0 10%;
	}

	p {
		margin: 0;
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
	@media screen and (max-width: 500px) {
		h2 {
			width: auto;
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
			padding: 0;
		}

		ul {
			flex-direction: column;
		}
		.image-gallery > li {
			display: inline-block;
			width: 100%;
			margin: 0 5px 10px 5px;
			position: relative;
			cursor: pointer;
		}
	}
</style>
