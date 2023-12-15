<script>
	import Hero from '../lib/Hero.svelte';
	import banner1 from '../assets/MashiMashi.jpg';
	import banner2 from '../assets/Iratto.jpg';
	import banner3 from '../assets/certificate.jpg';
	import banner4 from '../assets/robogeppei.jpg';
	import banner5 from '../assets/stretchsense.jpg';
	import banner6 from '../assets/syncvv.jpg';
	import geppei from '../assets/geppei.jpg';
	import blog from '../assets/staffblog.jpg';
	import rabbit from '../assets/tsukimi.jpg';
	import volumetrix from '../assets/volumetrix.jpg';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';

	let news;
	let usercase;
	let special;
	let error;

	const categoryMapping = {
		EVENT: 'イベント',
		PRODUCT_INFO: '製品情報',
		NOTICE: 'お知らせ'
	};

	onMount(async () => {
		try {
			const response = await fetch('http://' + window.location.hostname + ':7000/api/newsmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const results = await response.json();

			const response2 = await fetch('http://' + window.location.hostname + ':7000/api/usercase');
			const data2 = await response2.json();

			const response3 = await fetch('http://' + window.location.hostname + ':7000/api/special');
			const data3 = await response3.json();

			news = results.results.sort((a, b) => {
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

			news = results.results.map((result) => {
				result.category = categoryMapping[result.category];
				return result;
			});

			usercase = data2.results.sort((a, b) => {
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

			special = data3.results.sort((a, b) => {
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
	<section class="col-4 col-s-12 newsSection">
		<div class="blockHeader">
			<h1>NEWS</h1>
			<h4>お知らせ</h4>
			<button class="more">
				<a href={`/news/`} class="moreLink" use:link>
					<span>VIEW MORE</span>
					<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
						<circle cx="12" cy="12" r="12" fill="#313132" />
						<path
							d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
							fill="white"
						/>
					</svg>
				</a>
			</button>
		</div>

		<input type="radio" id="All" name="categories" value="All" checked />
		<input type="radio" id="お知らせ" name="categories" value="お知らせ" />
		<input type="radio" id="製品情報" name="categories" value="製品情報" />
		<input type="radio" id="イベント" name="categories" value="イベント" />

		<nav class="navMobile">
			<ul class="localNavContainer">
				<li class="localNavContainerList"><label for="All">All</label></li>
				<li class="localNavContainerList">
					<label for="お知らせ">お知らせ</label>
				</li>
				<li class="localNavContainerList">
					<label for="製品情報">製品情報</label>
				</li>
				<li class="localNavContainerList">
					<label for="イベント">イベント</label>
				</li>
			</ul>
		</nav>

		{#if news}
			<ul class="posts">
				{#each news as { id, date, title, content, category }, index}{#if index < 6}
						<li class="news" data-category={category}>
							<article class="news-article">
								<a href={`/news/${urlSlug(id)}`} use:link>
									<time>{date.replaceAll('-', '.')}</time>
									<p>{title}</p>
								</a>
							</article>
						</li>
					{/if}
				{/each}
			</ul>
		{:else}
			<p>Loading...</p>
		{/if}
	</section>

	<!-- FEATURED TOPICS -->
	<section class="col-5 col-s-12 topicsSection">
		<div class="blockHeader">
			<h1>FEATURES</h1>
			<h4>特集</h4>
			<button class="more">
				<span>VIEW MORE</span>
				<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
					<circle cx="12" cy="12" r="12" fill="#313132" />
					<path
						d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
						fill="white"
					/>
				</svg>
			</button>
		</div>

		{#if special}
			<div class="featuredTopics">
				{#each special as { id, date, title, content, thumbnail }, index}{#if index < 5}
						<a href={`/special/${urlSlug(id)}`} use:link>
							<figure>
								<img src={thumbnail} alt="title" />
							</figure></a
						>
					{/if}
				{/each}
				<figure>
					<img src={banner2} alt="Banner" />
				</figure>
				<figure>
					<img src={banner3} alt="Banner" />
				</figure>
				<figure>
					<img src={banner4} alt="Banner" />
				</figure>
				<figure>
					<img src={banner5} alt="Banner" />
				</figure>
				<figure>
					<img src={banner6} alt="Banner" />
				</figure>
			</div>
		{:else}
			<p>Loading...</p>
		{/if}
	</section>

	<!-- ORIGINAL CONTENTS -->
	<section class="col-2 col-s-12 originalContentsSection">
		<div class="blockHeader">
			<h2>ORIGINAL CONTENTS</h2>
		</div>
		<aside>
			<figure>
				<img src={geppei} alt="Geppei" />
			</figure>
			<a href={`/blog/`} use:link>
				<figure>
					<img src={blog} alt="Staff blog" />
				</figure>
			</a>
			<a href="https://www.youtube.com/@user-we8zu8tu5h" target="_blank">
				<figure>
					<img src={rabbit} alt="Rabbitchant" />
				</figure></a
			>

			<a href="https://www.volumetrix.jp/" target="_blank">
				<figure>
					<img src={volumetrix} alt="Volumetrix" />
				</figure></a
			>
		</aside>
	</section>

	<!-- CUSTOMER STORIES -->
	<section class="col-9 col-s-12 storiesSection">
		<div class="blockHeader">
			<h1>CUSTOMER STORIES</h1>
			<h4>ユーザー事例</h4>

			<button class="more">
				<a href={`/usercase/`} class="moreLink" use:link>
					<span>VIEW MORE</span>
					<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
						<circle cx="12" cy="12" r="12" fill="#313132" />
						<path
							d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
							fill="white"
						/>
					</svg></a
				>
			</button>
		</div>

		{#if usercase}
			<ul class="cardList">
				{#each usercase as { id, date, title, content, thumbnail }, index}{#if index < 5}
						<li class="card">
							<a href={`/usercase/${urlSlug(id)}`} use:link>
								<figure>
									<img src={thumbnail} alt="Capcom" width="400" height="200" />
									<figcaption>
										<time>{date.replaceAll('-', '.')}</time>
										<span>{title}</span>
										<p>&#8250;</p>
										<div class="trapezoid" />
									</figcaption>
								</figure></a
							>
						</li>
					{/if}
				{/each}
			</ul>
		{:else}
			<p>Loading...</p>
		{/if}
	</section>
</div>

<style>
	.moreLink {
		display: contents;
	}
	.localNavContainer label {
		color: #a1a1a1;
		cursor: pointer;
	}
	.localNavContainerList {
		padding-top: 1rem;
		margin-top: 0.3rem;
		border-top: 3px solid #a1a1a1;
		width: 25%;
	}
	.posts {
		display: flex;
		gap: 1rem;
		flex-direction: column;
		margin-top: 2rem;
	}
	.navMobile {
		width: 100%;
		text-align: center;
	}
	.navMobile .localNavContainer {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: center;
	}
	input[type='radio'] {
		position: absolute;
		left: -9999px;
	}
	/* FILTERING RULES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	[value='All']:checked ~ nav .localNavContainer [for='All'],
	[value='イベント']:checked ~ nav .localNavContainer [for='イベント'],
	[value='製品情報']:checked ~ nav .localNavContainer [for='製品情報'],
	[value='お知らせ']:checked ~ nav .localNavContainer [for='お知らせ'] {
		color: black;
	}

	[value='All']:checked ~ nav .localNavContainer .localNavContainerList:has(label[for='All']) {
		border-top: 3px solid #ff4b33;
	}

	[data-category='イベント'] .news-article a time {
		border-left: 6px solid #3ed144;
	}
	[data-category='製品情報'] .news-article a time {
		border-left: 6px solid #47b7f6;
	}
	[data-category='お知らせ'] .news-article a time {
		border-left: 6px solid #ffb34e;
	}

	[value='イベント']:checked
		~ nav
		.localNavContainer
		.localNavContainerList:has(label[for='イベント']) {
		border-top: 3px solid #3ed144;
	}

	[value='製品情報']:checked
		~ nav
		.localNavContainer
		.localNavContainerList:has(label[for='製品情報']) {
		border-top: 3px solid #47b7f6;
	}

	[value='お知らせ']:checked
		~ nav
		.localNavContainer
		.localNavContainerList:has(label[for='お知らせ']) {
		border-top: 3px solid #ffb34e;
	}

	[value='All']:checked ~ .posts [data-category] {
		display: block;
	}

	[value='イベント']:checked ~ .posts .news:not([data-category~='イベント']),
	[value='製品情報']:checked ~ .posts .news:not([data-category~='製品情報']),
	[value='お知らせ']:checked ~ .posts .news:not([data-category~='お知らせ']),
	[value='ComingSoon']:checked ~ .posts .news:not([data-category~='ComingSoon']) {
		display: none;
	}

	h1 {
		font-size: calc(28px + 0.390625vw);
	}
	h4 {
		padding-bottom: 0.2rem;
	}

	.newsSection,
	.topicsSection,
	.originalContentsSection,
	.storiesSection {
		border-top: 13px solid #313132;
		padding: 0 0.3rem;
	}
	.topicsSection .blockHeader,
	.storiesSection .blockHeader,
	.originalContentsSection .blockHeader {
		border-bottom: 1px solid black;
		padding-bottom: 0.4rem;
	}

	/* Head with button of the block */
	.blockHeader {
		display: flex;
		justify-content: flex-start;
		gap: 0.5rem;
		color: var(--headers-color);
		align-items: flex-end;
		margin-top: 1.5rem;
	}

	.originalContentsSection .blockHeader {
		border-bottom: 1px solid black;
	}

	.originalContentsSection .blockHeader h2 {
		margin: 0 auto;
	}
	.news {
		grid-area: news;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}
	.pageContent::after {
		content: '';
		clear: both;
		display: table;
	}

	[class*='col-'] {
		float: left;
		margin: 15px;
	}

	a {
		text-decoration: none;
	}

	.pageContent {
		padding: var(--page-padding);
	}

	@media only screen and (max-width: 768px) {
		.pageContent {
			padding: 1rem 0;
		}
	}

	@media only screen and (min-width: 768px) and (max-width: 870px) {
		.pageContent {
			padding: var(--page-padding-tablet);
		}
	}

	ul {
		list-style-type: none;
	}

	.more {
		display: flex;
		align-items: center;
		gap: 1rem;
		background-color: unset;
		border: none;
		cursor: pointer;
		color: var(--headers-color);
		align-self: center;
		margin: 0 0 0 auto;
	}

	.more span {
		font-weight: 600;
	}

	/* For mobile phones: */
	[class*='col-'] {
		width: auto;
	}

	/* HERO */
	.hero-image {
		height: var(--hero-height);
		position: relative;
	}

	/* NEWS BLOCK */
	.news-article {
		-webkit-box-shadow: 0px 1px 4px 0 rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 1px 4px 0 rgba(173, 173, 173, 1);
		box-shadow: 0px 1px 4px 0 rgba(173, 173, 173, 1);
		background-color: #fffef9;
	}

	.news-article a {
		display: flex;
		gap: 2rem;
		align-items: center;
		align-content: center;
		padding: 0.3rem 0;
	}
	.news-article a p {
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 1;
		white-space: pre-wrap;
	}

	.news-article a time {
		min-width: 85px;
		color: #606060;
		padding-left: 1rem;
	}

	.news-article:last-child {
		border-bottom: none;
	}

	/* FEATURED TOPICS BLOCK */
	.featuredTopics {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(auto-fill, 9.8rem);
		grid-gap: 1rem;
		justify-content: center;
		align-content: flex-start;
		list-style: none;
		margin: 2vh auto;
		padding: 0 0 1.5vh 0;
		overflow: hidden;
	}

	.featuredTopics figure {
		padding: 0.3rem 0.3rem 0 0.3rem;
		border: 1px solid black;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
	}

	.featuredTopics figure img {
		object-fit: cover;
		object-position: center;
		height: 140px;
		width: 145px;
	}

	/* ORIGINAL CONTENTS BLOCK */
	aside {
		padding: 15px;
		color: #000000;
		text-align: center;
		font-size: 14px;
		width: 100%;
	}

	aside figure {
		margin: 1rem 0.5rem;
	}

	.originalContentsSection .blockHeader {
		width: 100%;
		min-height: 45px;
	}

	.originalContentsSection .blockHeader h2 {
		font-size: calc(15px + 0.390625vw);
	}

	.originalContentsSection {
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
		width: 100%;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		max-height: 12.5rem;
	}

	/* CUSTOMER STORIES BLOCK */
	.card figure {
		border: none;
	}

	.card a {
		display: block;
	}
	.card figure {
		margin: 0;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
	}

	.card figure img {
		width: 100%;
		cursor: pointer;
	}

	.card figcaption {
		position: relative;
		padding: 15px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		gap: 0.5rem;
		font-size: calc(10px + 0.390625vw);
		text-align: left;
		min-height: 5rem;
		height: 5rem;
	}

	.card figcaption time {
		z-index: 3;
		margin-top: -3rem;
		color: #2a8cb7;
	}

	.card figcaption span {
		z-index: 3;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 2;
		white-space: pre-wrap;
	}

	.card a {
		color: black;
		z-index: 4;
		margin: auto 0 0 auto;
		font-size: 1.8rem;
	}

	.card figcaption p {
		z-index: 99;
		margin: auto 0 auto auto;
	}

	.card {
		padding: 0;
		float: left;
		width: var(--card-width);
		border: 2px solid black;
	}
	.cardList {
		padding: 0;
		display: flex;
		flex-wrap: wrap;
		flex-direction: row;
		justify-content: space-between;
		margin-top: 2rem;
		row-gap: 1rem;
	}

	.trapezoid {
		border-bottom: var(--card-width) solid #ffffff;
		border-left: 50px solid transparent;
		border-right: 0 solid transparent;
		width: calc(var(--card-width) - 7.1rem);
		transform: rotate(90deg);
		position: absolute;
		top: -6.6rem;
		left: 2rem;
		height: 0;
	}
	.trapezoid::before,
	.trapezoid::after {
		content: '';
		position: absolute;
		width: 0;
		height: 0;
	}

	.trapezoid::after {
		top: 0;
		right: 0;
		border-top: var(--card-width) solid #e7e7e7;
		border-left: calc(var(--card-width) / 3) solid transparent;
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
		/* .col-s-1 {
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
		} */
		.col-s-12 {
			width: auto;
		}
	}
	@media only screen and (min-width: 768px) {
		/* For desktop: */
		/* .col-1 {
			width: 8.33%;
		} */
		.col-2 {
			/* CHANGED (16) */
			width: 16.66%;
		}
		/* .col-3 {
			width: 25%;
		} */
		.col-4 {
			width: 33.33%;
		}
		.col-5 {
			width: 41%;
		}
		/* .col-6 {
			width: 50%;
		}
		.col-7 {
			width: 58.33%;
		}
		.col-8 {
			width: 66.66%;
		} */
		.col-9 {
			width: 75%;
		}
		/* .col-10 {
			width: 83.33%;
		}
		.col-11 {
			width: 91.66%;
		}
		.col-12 {
			width: auto;
		} */
	}

	@media only screen and (max-width: 700px) {
		.card figcaption {
			font-size: calc(18px + 0.390625vw);
			gap: 0;
		}
		h1 {
			font-size: calc(24px + 0.390625vw);
		}
		.card {
			width: 18rem;
		}
		.storiesSection .blockHeader h1 {
			font-size: 21px;
		}
		.trapezoid {
			border-bottom: 18rem solid #ffffff;
			border-left: 50px solid transparent;
			border-right: 0 solid transparent;
			width: calc(18rem - 10.1rem);
			transform: rotate(90deg);
			position: absolute;
			top: -7.6rem;
			left: 3.5rem;
			height: 0;
		}
		.cardList {
			padding: 0;
			justify-content: center;
		}
	}
</style>
