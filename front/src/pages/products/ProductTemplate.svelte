<script>
	import urlSlug from 'url-slug';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import NotFound from '../NotFound.svelte';
	import Loading from '../../lib/Loading.svelte';

	export let params = {};
	let product;
	let error;
	let isLoading = true;
	let isFixedNav = false;
	let activeSection = null;

	const sectionsMapping = {
		OVERVIEW: '概要',
		FEATURE: '特徴',
		DETAILS_PRICE: '仕様・価格',
		SUPPORT: 'サポート',
		OTHER: 'その他'
	};

	onMount(async () => {
		try {
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

		setTimeout(() => {
			const sidebarItems = document.querySelectorAll('.sidebar-item');
			const sections = document.querySelectorAll('.content > section');

			const observer = new IntersectionObserver(
				(entries) => {
					entries.forEach((entry) => {
						if (entry.isIntersecting && entry.intersectionRatio >= 0.3) {
							const targetId = entry.target.id;
							activeSection = targetId;
							sidebarItems.forEach((item) => {
								if (item.getAttribute('href') === `#${targetId}`) {
									item.classList.add('active');
								} else {
									item.classList.remove('active');
								}
							});
						}
					});
				},
				{ threshold: 0.3 }
			);

			sections.forEach((section) => {
				observer.observe(section);
			});
		}, 200);

		window.addEventListener('scroll', () => {
			const heroHeight = document.querySelector('.hero');
			if (heroHeight) {
				const scrollPosition = window.scrollY || document.documentElement.scrollTop;
				isFixedNav = scrollPosition >= heroHeight.offsetHeight;
			}
		});
	});

	$: if (product != null) {
		product.forEach((result, index) => {
			if (params.title === urlSlug(result.title) && params.title !== 'vicon') {
				product = result;
			}
		});
	}
	function scrollToElement(event) {
		event.preventDefault();

		const targetId = event.target.hash.substr(1);
		const targetElement = document.getElementById(targetId);

		if (targetElement) {
			const sidebarItems = document.querySelectorAll('.sidebar-item');

			sidebarItems.forEach((item) => {
				item.classList.remove('active');
				if (item.getAttribute('href') === `#${targetId}`) {
					item.classList.add('active');
				}
			});

			setTimeout(() => {
				targetElement.scrollIntoView();
			}, 0);
		}
	}

	// function hasCategory
</script>

{#if isLoading}
	<Loading />
{:else if product}
	<div class="pageContent">
		<div class="hero">
			<h1>{product.title}</h1>
			<figure class="hero-image-container">
				<img class="hero-image" src={product.hero} alt="Hero" />
			</figure>
		</div>

		<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
			{#each Object.entries(sectionsMapping) as [key, value]}
				{#if product.productContent.some((item) => item.section === key)}
					<a class="sidebar-item active" href={`#${key}`} on:click={scrollToElement}>{value}</a>
				{/if}
			{/each}
		</div>

		<div class="content">
			{#if product.productContent.length > 0}
				{#if product.productContent.some((item) => item.section === 'OVERVIEW')}
					<section class="overview" id="OVERVIEW">
						{#each product.productContent.filter((item) => item.section === 'OVERVIEW') as { id, productTitle, productText, image }}
							<div class="container">
								<h3>{productTitle}</h3>
								<div class="explanation">
									{@html productText}
								</div>
								{#if image}
									<figure>
										<img src={image} alt={productTitle} />
									</figure>{/if}
							</div>
						{/each}
					</section>
				{/if}

				{#if product.productContent.some((item) => item.section === 'FEATURE')}
					<section class="feature" id="FEATURE">
						{#each product.productContent.filter((item) => item.section === 'FEATURE') as { id, productTitle, productText, image }}
							<div class="container">
								<h3>{productTitle}</h3>
								<div class="explanation">
									{@html productText}
								</div>
								{#if image}
									<figure>
										<img src={image} alt={productTitle} />
									</figure>
								{/if}
							</div>
						{/each}
					</section>
				{/if}

				{#if product.productContent.some((item) => item.section === 'DETAILS_PRICE')}
					<section class="price" id="DETAILS_PRICE">
						{#each product.productContent.filter((item) => item.section === 'DETAILS_PRICE') as { id, productTitle, productText, image }}
							<div class="container">
								<h3>{productTitle}</h3>
								{#if image}
									<figure>
										<img src={image} alt={productTitle} />
									</figure>
								{/if}

								<div class="explanation">
									{@html productText}
								</div>
							</div>
						{/each}
					</section>
				{/if}

				{#if product.productContent.some((item) => item.section === 'SUPPORT')}
					<section class="support" id="SUPPORT">
						{#each product.productContent.filter((item) => item.section === 'SUPPORT') as { id, productTitle, productText, image }}
							<div class="container">
								<h3>{productTitle}</h3>
								{#if image}
									<figure>
										<img src={image} alt={productTitle} />
									</figure>
								{/if}

								<div class="explanation">
									{@html productText}
								</div>
							</div>
						{/each}
					</section>
				{/if}

				{#if product.productContent.some((item) => item.section === 'OTHER')}
					<section class="other" id="OTHER">
						{#each product.productContent.filter((item) => item.section === 'OTHER') as { id, productTitle, productText, image }}
							<div class="container">
								<h3>{productTitle}</h3>
								{#if image}
									<figure>
										<img src={image} alt={productTitle} />
									</figure>
								{/if}

								<div class="explanation">
									{@html productText}
								</div>
							</div>
						{/each}
					</section>
				{/if}
			{/if}
		</div>
	</div>
{:else}
	<NotFound />
{/if}

<style>
	ul,
	ol {
		list-style-type: unset;
	}

	.overflowed-text {
		margin: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 3;
		white-space: pre-wrap;
	}
	.sidebar-item {
		font-size: calc(14px + 0.390625vw);
		color: #ababab;
		padding: 16px;
		text-decoration: none;
	}
	.sidebar-item.active {
		color: #000000;
		font-size: calc(14px + 0.390625vw);
	}
	.features-list {
		padding-left: 5rem;
	}
	.features-list-item {
		list-style-type: disc;
		font-size: calc(14px + 0.390625vw);
		line-height: 1.5;
	}
	.pageContent {
		padding: 2rem 8rem;
	}
	.sidebar {
		margin: 0;
		padding: 0;
		width: 25vw;
		position: absolute;
		height: 100%;
		overflow: auto;
		display: flex;
		flex-direction: column;
	}

	.sidebar-fixed {
		position: fixed;
		top: 0;
		left: 0;
		padding: 2rem 0 2rem 8rem;
	}

	.content {
		margin-left: 25vw;
		padding: 1px 16px;
	}

	.relatedLinks {
		overflow: hidden;
		padding: 4rem 0;
		background-color: #dddddd;
		margin: 5rem 0 0 0;
		text-align: center;
		width: 100%;
	}
	.card article figure {
		margin: 0;
		width: inherit;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		border-radius: 8px;
		height: 100%;
	}

	.card article figure figcaption {
		padding: 15px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		gap: 0.5rem;
		font-size: calc(11px + 0.390625vw);
		text-align: left;
		min-height: 8rem;
		background: white;
	}

	.card article figure a img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
		display: block;
		max-height: 160px;
		object-fit: cover;
	}
	.cardList {
		width: 100%;
		margin-top: 3rem;
		display: flex;
		justify-content: center;
		align-items: flex-start;
		list-style: none;
	}

	.cardList .card {
		width: 15.5rem;
		margin-right: 2rem;

		&:last-child {
			margin-right: 0;
		}
	}

	.cardListMobile {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(auto-fill, 13.5rem);
		grid-gap: 2rem;
		justify-content: center;
		align-content: flex-start;
		list-style: none;
		margin: 2vh auto;
		padding: 0 0 1.5vh 0;
		overflow: hidden;
	}

	.cardListMobile .card {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.hero {
		position: relative;
		margin-bottom: 5rem;
	}

	.hero-image-container {
		max-height: 70vh;
		overflow: hidden;
		display: flex;
		justify-content: center;
		align-items: center;
		border-radius: 15px;
	}

	.hero-image {
		width: 100%;
		max-height: 100%;
		object-fit: contain;
	}

	p {
		margin: 0;
	}
	.explanation {
		font-size: calc(14px + 0.390625vw);
	}
	h1 {
		font-size: calc(36px + 0.390625vw);
		font-weight: 600;
		padding: 4rem 0;
	}
	h2 {
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}

	h3 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
		color: #0b345b;
	}

	section:not(.relatedLinks) {
		width: 100%;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 0;
		border-top: 2px solid black;
	}

	.container {
		display: flex;
		gap: 2rem;
		padding: 3rem 0;
		flex-direction: column;
	}
	section div div {
		display: flex;
		flex-direction: column;
		flex: 50%;
		justify-content: space-between;
	}
	section div figure {
		flex: 50%;
	}
	section div figure img {
		width: 100%;
	}

	figure {
		margin: 0;
		padding: 0;
		text-align: left;
	}

	@media (max-width: 800px) {
		.container {
			flex-direction: column;
		}

		.cardList {
			grid-template-columns: repeat(auto-fill, 15.5rem);
			margin: 0 auto;
		}
	}

	@media screen and (max-width: 700px) {
		.sidebar {
			width: 100%;
			height: auto;
			position: relative;
			flex-direction: row;
			justify-content: flex-start;
			align-items: center;
		}
		.sidebar-fixed {
			background-color: white;
		}
		.hero {
			margin-bottom: 2rem;
		}
		.sidebar-fixed {
			position: fixed;
			padding: 0rem;
		}
		.sidebar a {
			float: left;
		}
		div.content {
			margin-left: 0;
		}
		iframe {
			width: 100%;
		}
	}

	@media screen and (max-width: 1200px) {
		.pageContent {
			padding: 0 1rem;
		}
		h1 {
			padding: 2rem 0;
		}
	}

	@media screen and (max-width: 400px) {
		.sidebar a {
			text-align: center;
			float: none;
		}
	}
</style>
