<script>
	import urlSlug from 'url-slug';
	import NotFound from './NotFound.svelte';
	import { onMount, setContext } from 'svelte';
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import Pagination from '../lib/Pagination.svelte';
	import { fade, blur, fly, slide, scale, draw } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
	import Loading from '../lib/Loading.svelte';

	const categoryMapping = {
		EVENT: 'イベント',
		PRODUCT_INFO: '製品情報',
		NOTICE: 'お知らせ'
	};

	// export let params = {};
	let news;
	let error;
	let currentPage = 1;
	let totalPages = 1;
	let pageSize = 10;
	let selected = 'All';

	onMount(async () => {
		window.scrollTo(0, 0);
		try {
			const response = await fetch('http://' + window.location.hostname + ':7000/api/newsmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			results.sort((a, b) => {
				const dateA = a.date.toUpperCase();
				const dateB = b.date.toUpperCase();
				if (dateA < dateB) {
					return 1;
				}
				if (dateA > dateB) {
					return -1;
				}

				return 0;
			});
			news = results.map((result) => {
				result.category = categoryMapping[result.category];
				return result;
			});
			calculateTotalPages();
		} catch (err) {
			error = err;
		}
	});
	function calculateTotalPages() {
		totalPages = Math.ceil(news.length / pageSize);
	}

	function onPageChange(page) {
		currentPage = page;
	}

	setContext('pagination', { currentPage, totalPages, onPageChange });
</script>

<section class="section">
	<h1>ニュース</h1>
	<div class="content">
		<input type="radio" id="All" name="categories" value="All" bind:group={selected} />
		<input type="radio" id="お知らせ" name="categories" value="お知らせ" bind:group={selected} />
		<input type="radio" id="製品情報" name="categories" value="製品情報" bind:group={selected} />
		<input type="radio" id="イベント" name="categories" value="イベント" bind:group={selected} />

		<nav class={Device.isPhone || Device.isTablet ? 'navMobile' : 'nav'}>
			<h2>CATEGORY</h2>

			<ul class="localNavContainer">
				<li class="localNavContainerList">
					<label for="All" class:selectedInput={selected === 'All'}>All</label>
				</li>
				<li class="localNavContainerList">
					<label for="お知らせ" class:selectedInput={selected === 'お知らせ'}>お知らせ</label>
				</li>
				<li class="localNavContainerList">
					<label for="製品情報" class:selectedInput={selected === '製品情報'}>製品&開発情報</label>
				</li>
				<li class="localNavContainerList">
					<label for="イベント" class:selectedInput={selected === 'イベント'}
						>セミナー&イベント</label
					>
				</li>
			</ul>
		</nav>

		<ul class="posts cardList">
			{#if news}
				{#each news.slice((currentPage - 1) * pageSize, currentPage * pageSize) as { id, date, title, contents, category }, index}
					{#if selected === 'All' ? (selected = 'All') : selected === category}
						<li
							class="card"
							data-category={category}
							transition:slide={{ delay: 0, duration: 500, easing: quintOut, axis: 'y' }}
						>
							<article>
								<a href={`/news/${urlSlug(id)}`} use:link class="cardLink">
									<time>{date.replaceAll('-', '.')}</time>
									<span class="cardTitle">{title}</span>
								</a>
							</article>
						</li>
					{/if}
				{/each}
			{:else}
				<Loading />
			{/if}
		</ul>
	</div>
	<Pagination {currentPage} {totalPages} {onPageChange} />
</section>

<style>
	.section {
		min-height: 53vh;
		position: relative;
	}
	input[type='radio'] {
		position: absolute;
		left: -9999px;
	}

	/* localNavContainer
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	.localNavContainer {
		text-align: center;
		margin: 1rem 0;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}

	.localNavContainerList {
		cursor: pointer;
		margin: 0.5rem 0;
		border-radius: 25px;
		height: auto;
		place-items: center;
		background-color: #f3eded;
		font-size: 1.2rem;
		line-height: 1;
		color: currentColor;
		text-decoration: none;
		display: block;
		position: relative;
		text-align: center;
	}

	.localNavContainerList:hover {
		background-position: 0% 100%;
	}

	.localNavContainerList label:hover {
		transform: translate(0px, 0px);
		transition: 0.2s ease-in-out;
	}
	.localNavContainerList::after {
		content: '';
		display: block;
		width: 100%;
		height: 100%;
		border-radius: 2em;
		position: absolute;
		top: 0;
		left: 0;
		border: 2px solid currentColor;
		background-color: inherit;
		pointer-events: none;
		mix-blend-mode: darken;
		filter: contrast(1200%) brightness(100%) saturate(0.25);
		overflow: hidden;
		background: linear-gradient(182deg, currentColor, currentColor 25%, rgba(0, 0, 0, 0) 100%),
			url("data:image/svg+xml,%3Csvg viewBox='0 0 400 75' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='7' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
	}

	.localNavContainer * {
		display: inline-block;
	}

	.localNavContainer label {
		padding: 0.5rem 1rem;
		min-width: 50px;
		line-height: normal;
		cursor: pointer;
		transition: all 0.1s;
		display: inherit;
		border-radius: 2em;
		position: relative;
		z-index: 1;
	}

	.localNavContainer label:not(.selectedInput) {
		transform: translate(-0.4rem, -0.4rem);
		transition: 0.2s ease-in-out;
		background-color: #efefef;
		border: 2px solid currentColor;
	}

	.localNavContainer label:hover {
		transform: translate(0px, 0px);
		transition: 0.2s ease-in-out;
		background-color: #0b345b;
		color: #fff;
	}
	.selectedInput {
		transform: translate(0px, 0px);
		transition: 0.2s ease-in-out;
		background-color: #0b345b;
		color: #fff;
	}

	/* FILTERED ELEMENTS (POSTS)
–––––––––––––––––––––––––––––––––––––––––––––––––– */

	.cardLink {
		font-size: calc(16px + 0.390625vw);
	}
	.cardTitle {
		margin-left: 3rem;
	}

	.posts a {
		text-decoration: none;
	}

	/* FILTERING RULES
–––––––––––––––––––––––––––––––––––––––––––––––––– */

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

	.nav {
		width: 20%;
	}
	.navMobile {
		width: 100%;
		text-align: center;
	}
	.navMobile .localNavContainer {
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: center;
		column-gap: 1rem;
	}
	.cardList {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: flex-start;
		list-style: none;
		overflow: hidden;
		flex: 1;
	}

	.cardList .card {
		align-items: center;
		justify-content: center;
		padding: 2rem 0;
		border-bottom: 1.5px solid black;
		width: 100%;
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
		.cardLink {
			overflow: hidden;
			text-overflow: ellipsis;
			display: -webkit-box;
			-webkit-box-orient: vertical;
			-webkit-line-clamp: 1;
			white-space: pre-wrap;
		}
		.cardList .card {
			padding: 1rem 0;
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
		.cardList {
			grid-template-columns: repeat(auto-fill, 15.5rem);
			margin: 0 auto;
		}

		ul {
			flex-direction: column;
		}
	}
</style>
