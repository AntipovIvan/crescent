<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../assets/services/lightcageFace/lightcageFace.png';
	import man from '../../assets/services/lightcageFace/lcstudio_syosai1.png';
	import video from '../../assets/services/lightcageFace/DigiTada_new_maps_test03.mp4';
	import figures from '../../assets/services/4dstudio/figures.jpg';
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
		<h1>LightCageスタジオ（顔用）</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="FullBodyLightCage" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>概要</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}>詳細</a>
		<a class="sidebar-item" href="#example" on:click={scrollToElement}>スタジオ利用価格</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h2>クレッセント ESPER LIGHTCAGE 専用スタジオ</h2>
				<p class="explanation">
					LIGHTCAGEを使用した高精細な3Dのフェイスメッシュスキャン、様々なテクスチャーのキャプチャーを行って頂けます。
					デジタルヒューマン製作の要となります、フェイス製作に必要なハイクオリティな素材を提供致します。
					控室、打合せスペースのご用意もございます。
				</p>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>詳細</h2>

				<h3>クレッセントスタジオ　設置カメラ</h3>
				<p>CANON　EOS 7D MarkII 53台</p>
			</div>

			<div class="container">
				<h3>出力データフォーマット</h3>
				<div>
					<ul>
						<li>
							撮影画像
							<ul>
								<li>
									CANON EOS 7D MarkII　53台分
									<ul>
										<li>解像度　　3648×5472</li>
									</ul>
								</li>
							</ul>
						</li>
						<li>
							テクスチャーマップ
							<ul>
								<li>DiffuseMap</li>
								<li>SpecularMap</li>
								<li>UnpolarizedMap</li>
								<li>
									TangentMap
									<ul>
										<li>bit 16bit</li>
										<li>解像度　16384×16384</li>
									</ul>
								</li>
							</ul>
						</li>
						<li>
							メッシュデータ
							<ul>
								<li>RAWメッシュ 500万ポリゴン程度</li>
								<li>クリーンナップメッシュ</li>
								<li>リトポロジーメッシュ</li>
							</ul>
						</li>
					</ul>
					<figure>
						<img src={man} alt="man" />
					</figure>
				</div>
				<p>※希望のベースメッシュを頂けますと、そちらに沿って製作致します。</p>
			</div>

			<div class="container">
				<h3>レンダリング例</h3>

				<p>MAYA/Arnold使用例</p>
				<video width="100%" height="100%" controls>
					<track default kind="captions" srclang="en" src="" />
					<source src={video} type="video/mp4" />
					Your browser does not support the video tag.
				</video>
			</div>

			<div class="container">
				<h3>サンプルデータ</h3>

				<p>・メッシュ</p>
				<p>・各種テクスチャーマップ</p>
				<p>https://send.crescentinc.co.jp/LightCage/Sample/LightCage_Sample.zip 1.21GB</p>
			</div>
		</section>

		<section class="example" id="example">
			<div class="container">
				<h2>スタジオ利用価格</h2>

				<h3>スタジオ利用価格</h3>
				<p>◇一日撮影利用料：　60万円(税別)</p>
				<p>(EOS 7D MarkII　53台分　撮影画像納品含む)</p>
			</div>

			<div class="container">
				<h3>データ処理価格</h3>

				<ul>
					<li>
						テクスチャマップフルセット生成・メッシュクリーンナップ：　18万円(税別)
						<ul>
							<li>
								各テクスチャマップ生成
								<ul>
									<li>
										DiffuseMap / SpecularMap / NormalMap (object space / tangent
										spaceから選択できます)
									</li>
								</ul>
							</li>
							<li>メッシュ生成</li>
							<li>クリーンナップ</li>
							<li>リトポロジー処理</li>
							<li>ブレンドシェイプ用処理</li>
						</ul>
					</li>
				</ul>

				<ul>
					<li>
						メッシュクリーンナップ（ブレンドシェイプ用）：　1表情 12万円(税別)
						<ul>
							<li>メッシュ生成</li>
							<li>クリーンナップ</li>
							<li>リトポロジー処理</li>
							<li>ブレンドシェイプ用処理</li>
						</ul>
					</li>
				</ul>

				<p>撮影について詳細、デモや打合せのご要望につきましては、</p>
				<p>
					lightcage@crescentinc.co.jp もしくは お電話（ 03-5875-9707 ）まで お問い合わせください
				</p>
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
			<p>Loading...</p>
		{/if}
	</ul>
</section>

<style>
	.linkTitle {
		font-weight: bold;
		font-size: calc(10px + 0.390625vw);
	}
	p {
		font-size: calc(14px + 0.390625vw);
	}
	ul {
		padding-left: 1rem;
		font-size: calc(14px + 0.390625vw);
	}
	li {
		padding-bottom: 0.5rem;
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
		width: 83%;
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
	.system div div {
		display: flex;
		flex-direction: row;
		gap: 5rem;
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
		.system div div {
			flex-direction: column;
			gap: 2rem;
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
