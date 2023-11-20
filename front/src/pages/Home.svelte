<script>
	import Hero from '../lib/Hero.svelte';
	import banner1 from '../assets/MashiMashi.jpg';
	import banner2 from '../assets/Iratto.jpg';
	import banner3 from '../assets/certificate.jpg';
	import banner4 from '../assets/robogeppei.jpg';
	import banner5 from '../assets/stretchsense.jpg';
	import banner6 from '../assets/syncvv.jpg';
	import geppei from '../assets/geppei.gif';
	import blog from '../assets/blog.png';
	import rabbit from '../assets/rabbit.jpg';
	import volumetrix from '../assets/volumetrix.gif';
	import story1 from '../assets/capcom.jpg';
	import story2 from '../assets/osaka.jpg';
	import story3 from '../assets/aura.jpg';
	import story4 from '../assets/balus.jpg';
	import story5 from '../assets/soup.jpg';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';

	let news;
	let error;

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/newsmodels');
			const response = await fetch('http://' + window.location.hostname + ':7000/api/newsmodels');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			news = results.reverse();
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

		<input type="radio" id="All" name="categories" value="All" checked />
		<input type="radio" id="イベント" name="categories" value="イベント" />
		<input type="radio" id="製品情報" name="categories" value="製品情報" />
		<input type="radio" id="その他" name="categories" value="その他" />

		<nav class="navMobile">
			<ul class="localNavContainer">
				<li class="localNavContainerList"><label for="All">All</label></li>
				<li class="localNavContainerList">
					<label for="イベント">イベント</label>
				</li>
				<li class="localNavContainerList">
					<label for="製品情報">製品情報</label>
				</li>
				<li class="localNavContainerList">
					<label for="その他">その他</label>
				</li>
			</ul>
		</nav>

		{#if news}
			<ul class="posts">
				{#each news as { id, date, title, content, category }, index}
					<li class="news" data-category={category}>
						{#if index < 6}
							<article class="news-article">
								<a href={`/news/${urlSlug(id)}`} use:link>
									<time>{date.replaceAll('-', '.')}</time>
									<p>{title}</p>
								</a>
							</article>
						{/if}
					</li>
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

		<div class="featuredTopics">
			<figure>
				<img src={banner1} alt="Banner" />
			</figure>
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
			<figure>
				<img src={blog} alt="Staff blog" />
			</figure>
			<figure>
				<img src={rabbit} alt="Rabbitchant" />
			</figure>
			<figure>
				<img src={volumetrix} alt="Volumetrix" />
			</figure>
		</aside>
	</section>

	<!-- CUSTOMER STORIES -->
	<section class="col-9 col-s-12 storiesSection">
		<div class="blockHeader">
			<h1>CUSTOMER STORIES</h1>
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

		<ul class="cardList">
			<li class="card">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={story1} alt="Capcom" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.08.10</time>カプコンが新しくクリエイティブスタジオをオープン
					</figcaption>
					<!-- <div class="skewed-outer">
						<div class="skewed-inner" />
					</div> -->
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story2.png">
						<img src={story2} alt="Osaka University" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.06.11</time>大阪電気通信大学に日本教育機関最大級のスタジオが完成
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={story3} alt="Capcom" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.05.10</time>アウラの成り立ちやVICON導入のきっかけと今後の展望
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story2.png">
						<img src={story4} alt="Osaka University" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.03.10</time>多方面で活躍するBalusの最近のスタジオ動向を取材
					</figcaption>
				</figure>
			</li>

			<li class="card">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={story5} alt="Capcom" width="400" height="200" />
					</a>
					<figcaption>
						<time>2023.02.10</time>渋谷区代々木のスタジオSoup.が一般に向けても利用可能に
					</figcaption>
				</figure>
			</li>
		</ul>
	</section>
</div>

<style>
	.card figure div {
		width: 100%;
		height: 100%;
		position: absolute;
	}
	.skewed-outer {
		z-index: -1;
		left: 0;
		top: 0;
		border-bottom: 10px solid #bada55;
		transform: skewy(5deg);
		overflow: hidden;
	}

	.skewed-inner {
		border-left: 10px solid #bada55;
		border-top: 10px solid #bada55;
		border-right: 10px solid #bada55;
		transform: skewy(-10deg);
		/* Trigonometry, bitches */
		top: 1.5748em;
		left: 0;
		overflow: hidden;
	}
	.skewed-inner::after {
		content: '';
		display: block;
		background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAG0lEQVQYV2NkYGD4D8QEASNUIYjGC0YVUid4ALAnCgo7ftFaAAAAAElFTkSuQmCC);
		height: 110%;
		width: 110%;
		position: absolute;
		top: -5%;
		transform: skewy(5deg);
	}

	.localNavContainer label {
		color: #a1a1a1;
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
	[value='その他']:checked ~ nav .localNavContainer [for='その他'] {
		color: black;
	}

	[value='All']:checked ~ nav .localNavContainer .localNavContainerList:has(label[for='All']) {
		border-top: 3px solid #ff4b33;
	}

	[data-category='イベント'] .news-article a time {
		border-left: 6px solid #ffb34e;
	}
	[data-category='製品情報'] .news-article a time {
		border-left: 6px solid #47b7f6;
	}
	[data-category='その他'] .news-article a time {
		border-left: 6px solid #3ed144;
	}

	[value='イベント']:checked
		~ nav
		.localNavContainer
		.localNavContainerList:has(label[for='イベント']) {
		border-top: 3px solid #ffb34e;
	}

	[value='製品情報']:checked
		~ nav
		.localNavContainer
		.localNavContainerList:has(label[for='製品情報']) {
		border-top: 3px solid #47b7f6;
	}

	[value='その他']:checked
		~ nav
		.localNavContainer
		.localNavContainerList:has(label[for='その他']) {
		border-top: 3px solid #3ed144;
	}

	[value='All']:checked ~ .posts [data-category] {
		display: block;
	}

	[value='イベント']:checked ~ .posts .news:not([data-category~='イベント']),
	[value='製品情報']:checked ~ .posts .news:not([data-category~='製品情報']),
	[value='その他']:checked ~ .posts .news:not([data-category~='その他']),
	[value='ComingSoon']:checked ~ .posts .news:not([data-category~='ComingSoon']) {
		display: none;
	}

	h1 {
		font-size: calc(28px + 0.390625vw);
	}
	h4 {
		padding-bottom: 0.2rem;
	}

	section {
		padding: 0 0.3rem;
	}
	.newsSection,
	.topicsSection,
	.originalContentsSection,
	.storiesSection {
		border-top: 13px solid #313132;
	}
	.topicsSection .blockHeader,
	.storiesSection .blockHeader {
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

	/* "More" button (like "VIEW MORE") */
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
		/* margin: 1rem 0.5rem; */
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
		/* -webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1); */
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
		/* border-left: 2px #bebebe solid; */
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
			width: 41%;
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
