<script>
	import Hero from '../lib/Hero.svelte';
	import banner1 from '../assets/banner1.png';
	import banner2 from '../assets/banner2.png';
	import banner3 from '../assets/banner3.png';
	import banner4 from '../assets/banner4.png';
	import geppei from '../assets/geppei.gif';
	import blog from '../assets/blog.png';
	import rabbit from '../assets/rabbit.jpg';
	import volumetrix from '../assets/volumetrix.gif';
	import capcom from '../assets/story1.png';
	import osakaUniveristy from '../assets/story2.png';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';

	let news;
	let error;

	onMount(async () => {
		try {
			const response = await fetch('http://localhost:7000/api/newsmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			news = results;
		} catch (err) {
			error = err;
		}
	});
</script>

<section class="hero-image">
	<Hero />
</section>

<div class="pageContent">
	<!-- NEWS -->
	<section class="col-5 news">
		<div class="blockHeader">
			<h1>NEWS</h1>
			<button class="more">
				<span>View more</span>
				<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
					<path
						d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
					/>
				</svg>
			</button>
		</div>

		{#if news}
			{#each news as { id, date, title, content }, index}
				{#if index < 6}
					<article class="news-article">
						<a href={`/news/${urlSlug(id)}`} use:link>
							<time>{date.replaceAll('-', '.')}</time>
							<p>{title}</p>
						</a>
					</article>
				{/if}
			{/each}
		{:else}
			<p>Loading...</p>
		{/if}
	</section>

	<!-- FEATURED TOPICS -->
	<section class="col-5 col-s-12">
		<div class="blockHeader">
			<h1>FEATURED TOPICS</h1>
		</div>

		<div class="featuredTopics">
			<figure>
				<img src={banner1} alt="Banner" class="center-cropped" />
			</figure>
			<figure>
				<img src={banner2} alt="Banner" class="center-cropped" />
			</figure>
			<figure>
				<img src={banner3} alt="Banner" class="center-cropped" />
			</figure>
			<figure>
				<img src={banner4} alt="Banner" class="center-cropped" />
			</figure>
		</div>
	</section>

	<!-- ORIGINAL CONTENTS -->
	<section class="col-2 col-s-12 originalContentsSection">
		<div class="blockHeader">
			<h2>ORIGINAL CONTENTS</h2>
		</div>
		<aside>
			<figure>
				<img src={geppei} alt="Geppei" class="center-cropped" />
			</figure>
			<figure>
				<img src={blog} alt="Staff blog" class="center-cropped" />
			</figure>
			<figure>
				<img src={rabbit} alt="Rabbitchant" class="center-cropped" />
			</figure>
			<figure>
				<img src={volumetrix} alt="Volumetrix" class="center-cropped" />
			</figure>
		</aside>
	</section>

	<!-- CUSTOMER STORIES -->
	<section class="col-9 col-s-12">
		<div class="blockHeader">
			<h1>CUSTOMER STORIES</h1>
			<button class="more">
				<span>View more</span>
				<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
					<path
						d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
					/>
				</svg>
			</button>
		</div>

		<ul class="cardList">
			<li class="card">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={capcom} alt="Capcom" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.08.10</time>カプコンが新しくクリエイティブスタジオをオープン
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story2.png">
						<img src={osakaUniveristy} alt="Osaka University" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.06.11</time>大阪電気通信大学に日本教育機関最大級のスタジオが完成
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={capcom} alt="Capcom" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.08.10</time>カプコンが新しくクリエイティブスタジオをオープン
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story2.png">
						<img src={osakaUniveristy} alt="Osaka University" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.06.11</time>大阪電気通信大学に日本教育機関最大級のスタジオが完成
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={capcom} alt="Capcom" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.08.10</time>カプコンが新しくクリエイティブスタジオをオープン
					</figcaption>
				</figure>
			</li>
		</ul>
	</section>
</div>

<style>
	.pageContent::after {
		content: '';
		clear: both;
		display: table;
	}

	[class*='col-'] {
		float: left;
		padding: 15px;
	}

	a {
		text-decoration: none;
	}

	.pageContent {
		padding: 1rem 5rem;
	}

	@media only screen and (max-width: 768px) {
		.pageContent {
			padding: 1rem 0;
		}
	}

	ul {
		list-style-type: none;
	}

	/* Head with button of the block */
	.blockHeader {
		display: flex;
		justify-content: flex-start;
		gap: 2.5rem;
		color: var(--headers-color);
	}

	/* "More" button (like "View more") */
	.more {
		display: flex;
		align-items: center;
		gap: 1rem;
		background-color: unset;
		border: none;
		cursor: pointer;
		color: var(--headers-color);
	}

	/* For mobile phones: */
	[class*='col-'] {
		width: auto;
	}

	/* HERO */
	.hero-image {
		background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
			url('../assets/hero.png');
		height: 88vh;
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		position: relative;
	}

	/* NEWS BLOCK */
	.news-article {
		display: flex;
		gap: 1rem;
		margin: 0.5rem 0;
		/* padding: 1rem 0; */
		border-bottom: 1px #bebebe solid;
	}

	.news-article a {
		display: flex;
		gap: 2rem;
		align-items: center;
		align-content: center;
	}

	.news-article:last-child {
		border-bottom: none;
	}

	/* FEATURED TOPICS BLOCK */
	.featuredTopics {
		display: flex;
		flex-wrap: wrap;
	}

	.featuredTopics figure {
		margin: 1rem 0.5rem;
	}

	.featuredTopics figure img {
		object-fit: cover;
		object-position: center;
		height: 140px;
		width: 140px;
		border-radius: 20px;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
	}

	/* ORIGINAL CONTENTS BLOCK */
	aside {
		background-color: #ffffff;
		padding: 15px;
		color: #000000;
		text-align: center;
		font-size: 14px;
		width: 70%;
	}

	aside figure {
		margin: 1rem 0.5rem;
	}

	.originalContentsSection .blockHeader {
		width: 60%;
	}

	.originalContentsSection {
		border-left: 2px #bebebe solid;
		height: 100%;
		position: absolute;
		right: 5%;
		text-align: center;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	aside figure img {
		object-fit: cover;
		object-position: center;
		height: 90px;
		width: 130px;
		border-radius: 15px;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
	}

	/* CUSTOMER STORIES BLOCK */
	.card figure {
		border: none;
	}

	.card figure {
		margin: 0.5rem 0;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		border-radius: 8px;
	}

	.card figure img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
	}

	.card figcaption {
		padding: 15px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		gap: 0.5rem;
		font-size: calc(10px + 0.390625vw);
		text-align: left;
		min-height: 120px;
	}

	.card {
		padding: 0 6px;
		float: left;
		width: 12.5rem;
	}
	.cardList {
		padding: 0;
		display: flex;
		flex-wrap: wrap;
		flex-direction: row;
		justify-content: space-between;
	}

	@media only screen and (max-width: 700px) {
		.card {
			width: 49.99999%;
			margin: 6px 0;
		}
		.cardList {
			padding: 0;
			justify-content: center;
		}
	}
	@media only screen and (max-width: 500px) {
		.card {
			width: 100%;
		}
	}

	@media only screen and (max-width: 768px) {
		/* ORIGINAL CONTENTS */
		aside {
			width: auto;
			display: flex;
			flex-wrap: wrap;
		}

		.originalContentsSection {
			position: relative;
			right: 0;
		}
		.news {
			width: auto;
		}
		aside,
		.blockHeader,
		.featuredTopics {
			justify-content: center;
		}
	}
	@media only screen and (min-width: 600px) {
		/* For tablets: */
		.col-s-1 {
			width: 8.33%;
		}
		.col-s-2 {
			width: 16.66%;
		}
		.col-s-3 {
			width: 25%;
		}
		.col-s-4 {
			width: 33.33%;
		}
		.col-s-5 {
			width: 41.66%;
		}
		.col-s-6 {
			width: 50%;
		}
		.col-s-7 {
			width: 58.33%;
		}
		.col-s-8 {
			width: 66.66%;
		}
		.col-s-9 {
			width: 75%;
		}
		.col-s-10 {
			width: 83.33%;
		}
		.col-s-11 {
			width: 91.66%;
		}
		.col-s-12 {
			width: auto;
		}
	}
	@media only screen and (min-width: 768px) {
		/* For desktop: */
		.col-1 {
			width: 8.33%;
		}
		.col-2 {
			/* CHANGED (16) */
			width: 16.66%;
		}
		.col-3 {
			width: 25%;
		}
		.col-4 {
			width: 33.33%;
		}
		.col-5 {
			/* CHANGED (41) */
			width: 37.66%;
		}
		.col-6 {
			width: 50%;
		}
		.col-7 {
			width: 58.33%;
		}
		.col-8 {
			width: 66.66%;
		}
		.col-9 {
			width: 75%;
		}
		.col-10 {
			width: 83.33%;
		}
		.col-11 {
			width: 91.66%;
		}
		.col-12 {
			width: auto;
		}
	}
</style>
