<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../assets/products/4dviews/holosys/holosysHero.jpg';
	import link1 from '../../../assets/products/4dviews/holosys/holosysLink1.jpg';
	import link2 from '../../../assets/products/4dviews/holosys/holosysLink2.jpg';

	import { onMount } from 'svelte';
	import urlSlug from 'url-slug';

	let products;
	let error;
	let isFixedNav = false;
	let activeSection = null;

	onMount(async () => {
		try {
			const response = await fetch('http://' + window.location.hostname + ':7000/api/product');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();
			products = results.filter((result) => {
				return result.title.includes('4D') || result.title.includes('Holo');
			});
		} catch (err) {
			error = err;
		}

		const heroHeight = document.querySelector('.hero');
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

		window.addEventListener('scroll', () => {
			const scrollPosition = window.scrollY || document.documentElement.scrollTop;
			isFixedNav = scrollPosition >= heroHeight.offsetHeight;
		});
	});

	function scrollToElement(event) {
		event.preventDefault();

		const targetId = event.target.hash.substr(1);
		const targetElement = document.getElementById(targetId);

		if (targetElement) {
			targetElement.scrollIntoView({ behavior: 'smooth' });
		}
	}
</script>

<div class="pageContent">
	<div class="hero">
		<h1>HOLOSYS</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>製品概要</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}
			>4Dviews ボリューメトリクスのコンセプト</a
		>
		<a class="sidebar-item" href="#download" on:click={scrollToElement}>カタログダウンロード</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h3>製品概要</h3>
				<p class="explanation">
					HOLOSYS
					技術は、人を撮影し、そこから360°バーチャル3Dオブジェクトを生成し生の人間の動きをそのままARやMR空間に表示させることができます。HOLOSYS
					3.0の高評価を得て、より高速処理、高効率化され、信頼度が増したHOLOSYS
					3.5をリリースしました。
				</p>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h3>4Dviews ボリューメトリクスのコンセプト</h3>
				<p>
					4Dviewsは世界初の商用ボリューメトリクスキャプチャシステムです。人間の動きを自由視点の映像にする為には必須のテクノロジーです。現在では、ARで人間を表示したり、5Gでデータ自体をストリーミング配信したりと用途は急速に拡がっています。
				</p>

				<iframe
					width="719"
					height="404"
					src="https://www.youtube.com/embed/SHSos66QKsk"
					frameborder="0"
					allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
					title="holosys"
				></iframe>
			</div>
		</section>

		<section class="download" id="download">
			<div class="container">
				<h3>カタログダウンロード</h3>
				<p>準備中。近日公開予定</p>
			</div>
		</section>
		<br />
		<br />
		<br />
		<a href={`/product/4dviews`} use:link>
			<button class="more">
				<span class="viewMore">4DVIEWSトップへ</span>
			</button></a
		>
	</div>
</div>
<section class="relatedLinks">
	<h2>関連リンク</h2>
	<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
		<li class="card">
			<article>
				<figure>
					<a href={`/product/holosuite`} use:link>
						<img src={link1} alt="title" width="400" height="200" />
					</a>
					<figcaption>
						<p class="linkTitle">HoloSuite</p>
						<span class="overflowed-text">ボリュメトリックデータの編集・配信ソフトウェア群</span>
					</figcaption>
				</figure>
			</article>
		</li>

		<li class="card">
			<article>
				<figure>
					<a href={`/services/4dstudio`} use:link>
						<img src={link2} alt="title" width="400" height="200" />
					</a>
					<figcaption>
						<p class="linkTitle">4D STUDIO</p>
						<span class="overflowed-text"
							>4Dviews社 HOLOSYSを使用したボリュメトリックキャプチャスタジオ</span
						>
					</figcaption>
				</figure>
			</article>
		</li>
	</ul>
</section>

<style>
	.viewMore {
		font-weight: 500;
		font-size: calc(20px + 0.390625vw);
	}
	.linkTitle {
		font-weight: bold;
	}
	.more {
		text-align: center;
		border: 1px solid rgb(92, 92, 92);
		padding: 1rem 5rem;
		background: none;
		border-radius: 8px;
		cursor: pointer;
	}
	th {
		padding: 10px;
		font-size: 12px;
		background: #e0e3e7;
	}
	table {
		margin-bottom: 20px;

		width: 100%;
		word-wrap: break-word;
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
		padding: 2rem 8rem;
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
	iframe {
		width: 100%;
		height: 35vw;
	}
	p {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
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
