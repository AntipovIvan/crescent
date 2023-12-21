<script>
	import Device from 'svelte-device-info';
	import { onMount, setContext } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';
	import Pagination from '../lib/Pagination.svelte';
	import { fade, blur, fly, slide, scale, draw } from 'svelte/transition';
	import { quintOut, circIn } from 'svelte/easing';
	import Loading from '../lib/Loading.svelte';

	let products;
	let error;
	let currentPage = 1;
	let totalPages = 1;
	let pageSize = 20;
	let selected = 'All';

	const categoryMapping = {
		SOLUTION: 'ソリューション',
		SOFTWARE: 'ソフトウェア',
		DEVICE: 'デバイス'
	};

	onMount(async () => {
		window.scrollTo(0, 0);
		try {
			const response = await fetch('http://' + window.location.hostname + ':7000/api/product');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();
			results.sort((a, b) => parseFloat(a.sorting_order) - parseFloat(b.sorting_order));

			products = results.map((result) => {
				result.category = categoryMapping[result.category];
				return result;
			});
			calculateTotalPages();
		} catch (err) {
			error = err;
		}
	});

	function calculateTotalPages() {
		totalPages = Math.ceil(products.length / pageSize);
	}

	function onPageChange(page) {
		currentPage = page;
	}

	setContext('pagination', { currentPage, totalPages, onPageChange });
</script>

<section class="section">
	<h1>製品販売</h1>
	<div class="content">
		<input type="radio" id="All" name="categories" value="All" bind:group={selected} />
		<input
			type="radio"
			id="ソリューション"
			name="categories"
			value="ソリューション"
			bind:group={selected}
		/>
		<input
			type="radio"
			id="ソフトウェア"
			name="categories"
			value="ソフトウェア"
			bind:group={selected}
		/>
		<input type="radio" id="デバイス" name="categories" value="デバイス" bind:group={selected} />

		<nav class={Device.isPhone || Device.isTablet ? 'navMobile' : 'nav'}>
			<h2>CATEGORY</h2>

			<ul class="localNavContainer">
				<li class="localNavContainerList">
					<label for="All" class:selectedInput={selected === 'All'}>All</label>
				</li>
				<li class="localNavContainerList">
					<label for="ソリューション" class:selectedInput={selected === 'ソリューション'}
						>ソリューション</label
					>
				</li>
				<li class="localNavContainerList">
					<label for="ソフトウェア" class:selectedInput={selected === 'ソフトウェア'}
						>ソフトウェア</label
					>
				</li>
				<li class="localNavContainerList">
					<label for="デバイス" class:selectedInput={selected === 'デバイス'}>デバイス</label>
				</li>
			</ul>
		</nav>

		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			{#if products}
				{#each products.slice((currentPage - 1) * pageSize, currentPage * pageSize) as { id, title, description, category, thumbnail }, index}
					{#if selected === 'All' ? (selected = 'All') : selected === category}
						<li
							class="card"
							data-category={category === 'Coming soon' ? (category = 'Coming soon') : category}
							transition:slide={{ delay: 0, duration: 1000, easing: quintOut, axis: 'y' }}
						>
							<article>
								<figure>
									<a
										href={title !== 'Vicon' &&
										title !== '4Dviews' &&
										title !== 'HoloSuite' &&
										title !== 'SyncVV'
											? `/products/${urlSlug(title)}`
											: title === 'Vicon'
											  ? `/product/vicon`
											  : title === 'HoloSuite'
											    ? `/product/holosuite`
											    : title === 'SyncVV'
											      ? `/product/syncvv`
											      : `/product/4dviews`}
										use:link
									>
										<img src={thumbnail} alt={title} width="400" height="200" />
									</a>
									<figcaption>
										<ul class="cardTags">
											<li>
												{category}
											</li>
										</ul>
										<p>{title}</p>
										<span class="overflowed-text">{description}</span>
									</figcaption>
								</figure>
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
	.posts .cardTags {
		margin-bottom: 0.75rem;
		font-size: 0.75rem;
	}

	.posts .cardTags * {
		display: inline-block;
	}

	.posts .cardTags li {
		margin-bottom: 0.2rem;
		padding: 0.2rem 0.5rem;
		border-radius: 1rem;
		border: 1px solid;
		line-height: normal;
	}

	.posts .cardTags a:hover {
		background: #0b345b;
		color: #fff;
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
	.overflowed-text {
		margin: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 3;
		white-space: pre-wrap;
		width: 100%;
	}
	.content {
		display: flex;
		gap: 5rem;
		flex-wrap: wrap;
		flex-direction: row;
		margin-top: 2rem;
	}

	p {
		margin: 0;
		font-weight: bold;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	figure {
		margin: 0;
		width: inherit;
		-webkit-box-shadow: 0px 2px 12px 2px rgb(0 0 0 / 11%);
		-moz-box-shadow: 0px 2px 12px 2px rgb(0 0 0 / 11%);
		box-shadow: 0px 2px 12px 2px rgb(0 0 0 / 11%);
		border-radius: 8px;
		height: 100%;
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
	img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
		display: block;
		max-height: 160px;
		object-fit: cover;
	}
	figcaption {
		padding: 15px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		gap: 0.5rem;
		font-size: calc(11px + 0.390625vw);
		text-align: left;
		min-height: 160px;
	}
	.cardList {
		width: 70%;
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

	.cardList .card {
		display: flex;
		align-items: center;
		justify-content: center;
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
	@media screen and (max-width: 700px) {
		.content {
			flex-direction: column;
		}
		ul {
			flex-direction: column;
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
		figcaption {
			font-size: calc(16px + 0.390625vw);
		}
		ul {
			flex-direction: column;
		}
	}
</style>
