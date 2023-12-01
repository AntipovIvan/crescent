<script>
	import Device from 'svelte-device-info';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';

	let products;
	let error;

	const categoryMapping = {
		MOTION_CAPTURE: 'モーションキャプチャー',
		VOLUMETRICS_CAPTURE: 'ボリュメトリックキャプチャー',
		PHOTOGRAMMETRY: 'フォトグラフメトリ',
		HARDWARE: 'Hardware',
		SOFTWARE: 'Software',
		COMING_SOON: 'Coming soon'
	};

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/productcardmodels');
			const response = await fetch('http://' + window.location.hostname + ':7000/api/product');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			products = results.map((result) => {
				result.category = categoryMapping[result.category];
				return result;
			});
		} catch (err) {
			error = err;
		}
	});
</script>

<section>
	<h1>製品販売</h1>
	<div class="content">
		<input type="radio" id="All" name="categories" value="All" checked />
		<!-- {#each Object.entries(categoryMapping) as [fetch, category]}
			<input type="radio" id={category} name="categories" value={category} />
		{/each} -->
		<input
			type="radio"
			id="モーションキャプチャー"
			name="categories"
			value="モーションキャプチャー"
		/>
		<input
			type="radio"
			id="ボリュメトリックキャプチャー"
			name="categories"
			value="ボリュメトリックキャプチャー"
		/>
		<input type="radio" id="フォトグラフメトリ" name="categories" value="フォトグラフメトリ" />
		<input type="radio" id="Hardware" name="categories" value="Hardware" />
		<input type="radio" id="Software" name="categories" value="Software" />
		<input type="radio" id="Coming soon" name="categories" value="Coming soon" />

		<nav class={Device.isPhone || Device.isTablet ? 'navMobile' : 'nav'}>
			<h2>CATEGORY</h2>

			<ul class="localNavContainer">
				<li class="localNavContainerList"><label for="All">All</label></li>
				<li class="localNavContainerList">
					<label for="モーションキャプチャー">モーションキャプチャー</label>
				</li>
				<li class="localNavContainerList">
					<label for="ボリュメトリックキャプチャー">ボリュメトリックキャプチャー</label>
				</li>
				<li class="localNavContainerList">
					<label for="フォトグラフメトリ">フォトグラフメトリ</label>
				</li>

				<li class="localNavContainerList">
					<label for="Hardware">Hardware</label>
				</li>

				<li class="localNavContainerList">
					<label for="Software">Software</label>
				</li>
				<li class="localNavContainerList"><label for="Coming soon">Coming soon</label></li>
			</ul>
		</nav>

		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			{#if products}
				{#each products as { id, title, contents, category, thumbnail }, index}
					<li
						class="card"
						data-category={category === 'Coming soon' ? (category = 'Coming soon') : category}
					>
						<article>
							<figure>
								<a
									href={title !== 'Vicon' && title !== '4Dviews'
										? `/products/${urlSlug(title)}`
										: title === 'Vicon'
										  ? `/product/vicon`
										  : `/product/4dviews`}
									use:link
								>
									<img src={thumbnail} alt={title} width="400" height="200" />
								</a>
								<figcaption>
									<ul class="cardTags">
										<li>
											<a href="">{category}</a>
										</li>
									</ul>
									<p>{title}</p>
									<span class="overflowed-text">{contents[0].content}</span>
								</figcaption>
							</figure>
						</article>
					</li>
				{/each}
			{:else}
				<p>Loading...</p>
			{/if}
		</ul>
	</div>
</section>

<style>
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
		border: 1px solid #8b8b8b;
		color: #8b8b8b;
		margin: 0.5rem 0;
		border-radius: 25px;
	}
	.localNavContainer * {
		display: inline-block;
	}

	.localNavContainer label {
		padding: 0.5rem 1rem;
		/* margin-bottom: 0.25rem; */
		border-radius: 2rem;
		min-width: 50px;
		line-height: normal;
		cursor: pointer;
		transition: all 0.1s;
	}

	.localNavContainer label:hover {
		background: #0b345b;
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
	}

	.posts .cardTags a {
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
	[value='All']:checked ~ nav .localNavContainer [for='All'],
	[value='モーションキャプチャー']:checked ~ nav .localNavContainer [for='モーションキャプチャー'],
	[value='ボリュメトリックキャプチャー']:checked
		~ nav
		.localNavContainer
		[for='ボリュメトリックキャプチャー'],
	[value='フォトグラフメトリ']:checked ~ nav .localNavContainer [for='フォトグラフメトリ'],
	[value='Hardware']:checked ~ nav .localNavContainer [for='Hardware'],
	[value='Software']:checked ~ nav .localNavContainer [for='Software'],
	[value='Coming soon']:checked ~ nav .localNavContainer [for='Coming soon'] {
		background: #0b345b;
		color: #fff;
	}

	[value='All']:checked ~ .posts [data-category] {
		display: block;
	}

	[value='モーションキャプチャー']:checked
		~ .posts
		.card:not([data-category~='モーションキャプチャー']),
	[value='ボリュメトリックキャプチャー']:checked
		~ .posts
		.card:not([data-category~='ボリュメトリックキャプチャー']),
	[value='フォトグラフメトリ']:checked ~ .posts .card:not([data-category~='フォトグラフメトリ']),
	[value='Hardware']:checked ~ .posts .card:not([data-category~='Hardware']),
	[value='Software']:checked ~ .posts .card:not([data-category~='Software']),
	[value='Coming soon']:checked ~ .posts .card:not([data-category~='Coming soon']) {
		display: none;
	}

	h1 {
		margin: 0;
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
