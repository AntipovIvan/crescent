<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../assets/services/4dstudio/hero.png';
	import overview from '../../assets/services/4dstudio/overview.jpg';
	import specs from '../../assets/services/4dstudio/specs.jpg';
	import banner from '../../assets/services/4dstudio/banner.jpg';
	import shootsystem from '../../assets/services/4dstudio/shootsystem.jpg';
	import about from '../../assets/services/4dstudio/about.jpg';
	import figures from '../../assets/services/4dstudio/figures.jpg';
	import { onMount } from 'svelte';
	import urlSlug from 'url-slug';
	import Loading from '../../lib/Loading.svelte';

	let products;
	let error;
	let isFixedNav = false;
	let activeSection = null;

	onMount(async () => {
		window.scrollTo(0, 0);
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
		<h1>4D STUDIO</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>スタジオ概要</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}>撮影システム</a>
		<a class="sidebar-item" href="#example" on:click={scrollToElement}>用途・事例</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h2>スタジオ概要</h2>
				<p class="explanation">
					清澄白河駅から徒歩数分。ボリュメトリックビデオの量産体制を整えました。カメラ48台の4Dviewsシステムを常設、吸音材を全壁面と天井に設置、オーディオの同録も可能です。また、Viconによるモーションキャプチャの同録、LightCageによるフォトグラメトリ撮影、ステージ上でのスチル撮影なども行える最新鋭のスタジオです。400坪の広さをフル活用して大勢のスタッフ様、演者様を迎えても快適な撮影進行が可能です。オフラインデータ・ストリーミング配信等の活用についても一気通貫でサポートいたします。
				</p>

				<figure>
					<img src={overview} alt="Studio overview" />
				</figure>
			</div>

			<div class="container">
				<h3>ボリュメトリックビデオとは</h3>
				<p class="explanation">
					ボリュメトリックビデオ（Volumetric
					Video）とは、現実の人や物をそのまま三次元デジタルデータとして撮影する技術のことです。ビデオという名のとおり、写真のように一瞬をとらえるのではなく、立体的な動画として撮影することができます。三次元動画や自由視点動画とも呼ばれ、次世代の映像技術として注目されています。
				</p>
			</div>

			<div class="container">
				<h3>ボリュメトリックビデオの特徴</h3>
				<ul class="features-list">
					<li class="features-list-item">好きな角度から映像を観ることができる</li>
					<li class="features-list-item">
						撮影した後に人物やセットの位置関係やカメラワークを何度でも自由に変えることができる
					</li>
					<li class="features-list-item">
						実写撮影には難しい、もしくは不可能なカメラワークを実現できる
					</li>
					<li class="features-list-item">
						人物のリアルな表情や服の揺れ・皺など、CGで再現するのが困難な動きや形状を簡単にデジタル化することができる
					</li>
					<li class="features-list-item">
						曲げたり巨大化させたり増殖させたりなど、CGに対して行えるさまざまな加工を行うことができる
					</li>
					<li class="features-list-item">
						遠く離れた場所にいる人やバーチャル空間にしか存在しないキャラクターが同じ空間で共演することができる
					</li>
				</ul>
				<figure>
					<img src={specs} alt="Volumetric video features" />
				</figure>
			</div>

			<div class="container">
				<h3>4Dviewsのボリュメトリックキャプチャシステム</h3>
				<p class="explanation">
					このスタジオでは、4Dviews社のボリュメトリックキャプチャシステム HOLOSYS
					を使用しています。4Dviewsは2007年以来、ボリュメトリックキャプチャのパイオニアとして活躍してきました。2010年には、私たちクレッセントと共同で世界初の商用ボリュメトリックキャプチャスタジオを開設し、映画やCM、ミュージックビデオ、アート、アパレル、教育など、さまざまな分野でボリュメトリックビデオを活用したプロジェクトを生み出しています。4DviewsはHOLOSYSのほかにもノンリニア編集ソフトウェア
					4Dfx
					を開発しており、ボリュメトリックビデオのエコシステムの構築に大きく貢献しています。私たちクレッセントは日本・台湾における4Dviews製品の総代理店です。
				</p>
				<figure>
					<img src={banner} alt="4DViews banner" />
				</figure>
				<iframe
					width="560"
					height="315"
					src="https://www.youtube.com/embed/Rkp7bjVsVgc?si=mVGQao_rS8gcHbAw"
					title="YouTube video player"
					frameborder="0"
					allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
					allowfullscreen
				></iframe>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>撮影システム</h2>
				<p class="explanation">
					このスタジオでは、4Dviews社のボリュメトリックキャプチャシステム HOLOSYS
					を使用しています。2023年3月に、HOLOSYSが HOLOSYS+(プラス)
					にバージョンアップしたことにより、カメラ1台ごとの解像度が500万画素から1200万画素に上がり、より広いエリアをより精細にキャプチャすることが可能になりました。立体化のアルゴリズムも進化しており、よりリアルで実写と見まがうほどのクオリティに近づいています。
				</p>

				<figure>
					<img src={shootsystem} alt="Shooting system" />
				</figure>
			</div>

			<div class="container">
				<h3>システムの特徴</h3>
				<p class="explanation">
					HOLOSYSでは中央のキャプチャエリアを取り囲む48台のカメラが完全に同期し、すべて同じタイミングで動画撮影を行います。撮影後、それらの動画をもとに1フレームずつサーバで計算することで、三次元のメッシュとテクスチャのシーケンスを生成します。カメラと照明がセットになったスタジオレイアウトになっているため、色ムラや影の少ないテクスチャの生成が可能です。
				</p>
				<figure>
					<img src={about} alt="About 4D studio" />
				</figure>
			</div>
		</section>

		<section class="example" id="example">
			<div class="container">
				<h2>用途・事例</h2>

				<figure>
					<img src={figures} alt="Figures" />
				</figure>
			</div>
		</section>
	</div>
</div>
<section class="relatedLinks">
	<h2>関連リンク</h2>
	<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
		{#if products}
			{#each products as { id, title, description, category, thumbnail }, index}
				<li class="card">
					<article>
						<figure>
							<a href={title !== '4Dviews' ? `/product/holosuite` : `/product/4dviews`} use:link>
								<img src={thumbnail} alt={title} width="400" height="200" />
							</a>
							<figcaption>
								<p class="linkTitle">{title}</p>
								<span class="overflowed-text">{description}</span>
							</figcaption>
						</figure>
					</article>
				</li>
			{/each}
		{:else}
			<Loading />
		{/if}
	</ul>
</section>

<style>
	.linkTitle {
		font-weight: bold;
		font-size: calc(10px + 0.390625vw);
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
		max-height: 105vh;
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
