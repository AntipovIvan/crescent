<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../assets/services/lightcageFull.jpeg';
	import man from '../../assets/services/lightcageBody/man.jpeg';
	import studio1 from '../../assets/services/lightcageBody/Dress1.png';
	import studio2 from '../../assets/services/lightcageBody/Dress2.png';
	import studio3 from '../../assets/services/lightcageBody/Stage.png';
	import studio4 from '../../assets/services/lightcageBody/owl.png';
	import studio5 from '../../assets/services/lightcageBody/Free.png';
	import studio6 from '../../assets/services/lightcageBody/alcohol.png';
	import studio7 from '../../assets/services/lightcageBody/parking.png';
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
		<h1>FullBodyLightCage スタジオ（全身用）</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="FullBodyLightCage" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>撮影システム</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}>データ形式・価格等</a>
		<a class="sidebar-item" href="#example" on:click={scrollToElement}>スタジオ設備</a>
		<a class="sidebar-item" href="#access" on:click={scrollToElement}>アクセス・問合せ</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h2>撮影システム</h2>
				<p class="explanation">
					全身をスキャン可能な大型LightCageが登場しました。
					168台の一眼レフカメラと290台の新型MultiFlashが配備され、
					超高精細な形状・服や肌の質感を詳細にスキャンします。 ※顔のスキャンに特化した顔用の
					LightCageスタジオ はクレッセント本社（徒歩数分）にございます。
				</p>
			</div>

			<div class="container">
				<h3>システムの特徴</h3>
				<table border="1" cellpadding="3">
					<tbody>
						<tr>
							<td>RigSize</td>
							<td>5m</td>
						</tr>
						<tr>
							<td>Camera</td>
							<td>Sony α6400 168台 </td>
						</tr>
						<tr>
							<td>Light</td>
							<td>ESPER MultiFlash V3 290台</td>
						</tr>
					</tbody>
				</table>
				<p class="explanation">
					専用の同期信号分配システム「ESPER ControllerBox」「ESPER
					TriggerBox」により、CameraとMultiFlashは完全に同期された連続撮影を行います。 MultiFlash
					V3は三種類のフラッシュLEDが搭載されています。色味成分・反射光成分・リファレンス素材を一回の撮影で取得することが出来ます。素早く複数の照明パターンでの撮影を行い、人物撮影時のブレを抑制します。
				</p>
				<figure>
					<img src={man} alt="Man" />
				</figure>
			</div>

			<!-- <div class="container">
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
			</div> -->
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>データ形式・価格等</h2>

				<h3>データ形式</h3>
				<ul>
					<li>
						撮影画像
						<ul>
							<li>
								SONY α6400 168台分
								<ul>
									<li>解像度 4000×6000</li>
								</ul>
							</li>
						</ul>
					</li>
					<li>
						テクスチャーマップ "tiff .png"
						<ul>
							<li>DiffuseMap</li>
							<li>SpecularMap</li>
							<li>
								UnpolarizedMap
								<ul>
									<li>bit 16bit</li>
									<li>解像度 8192×8192</li>
								</ul>
							</li>
						</ul>
					</li>
					<li>
						メッシュデータ "obj .fbx"
						<ul>
							<li>RAWメッシュ 1000万ポリゴン程度</li>
							<li>クリーンナップメッシュ</li>
							<li>リトポロジーメッシュ</li>
						</ul>
					</li>
				</ul>
			</div>

			<div class="container">
				<h3>価格</h3>
				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th>タイトル</th>
							<th>数</th>
							<th>価格</th>
						</tr>
						<tr>
							<td>FullBodyLightCageStudio</td>
							<td>一日使用料</td>
							<td>100万円</td>
						</tr>
						<tr>
							<td>FullBodyLightCageStudio</td>
							<td>半日使用料</td>
							<td>70万円</td>
						</tr>
						<tr>
							<td>画像納品</td>
							<td>1Shot 504枚</td>
							<td>3万円</td>
						</tr>
						<tr>
							<td>RAWメッシュ(リファレンステクスチャマップ含む)</td>
							<td>1体</td>
							<td>3万円</td>
						</tr>
						<tr>
							<td>メッシュクリーンナップ</td>
							<td>1体</td>
							<td>3万円</td>
						</tr>
						<tr>
							<td>リトポロジー処理</td>
							<td>1体</td>
							<td>6万円</td>
						</tr>
						<tr>
							<td>テクスチャマップ生成(Diffuse/Specular/Unpolarized)</td>
							<td>1体</td>
							<td>3万円</td>
						</tr>
						<tr>
							<td>オートリギング/オートブレンドシェイプ</td>
							<td>1体</td>
							<td>お問い合わせください</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>

		<section class="example" id="example">
			<div class="container">
				<h2>スタジオ設備</h2>

				<h3>楽屋</h3>
				<p>お着替え室つきの大部屋を2部屋ご用意。広々とした空間で大勢の演者様でも対応可能です。</p>
				<figure>
					<img src={studio1} alt="Studio 1" />
				</figure>
				<figure>
					<img src={studio2} alt="Studio 2" />
				</figure>
			</div>

			<div class="container">
				<h3>ステージ</h3>

				<figure>
					<img src={studio3} alt="Studio 3" />
				</figure>
				<figure>
					<img src={studio4} alt="Studio 4" />
				</figure>
			</div>

			<div class="container">
				<h3>ミーティング用個室ほかフリースペース</h3>

				<figure>
					<img src={studio5} alt="Studio 5" />
				</figure>
			</div>

			<div class="container">
				<h3>感染防止対策</h3>
				<ul>
					<li>各部屋に手指アルコール消毒スプレーなどを配備</li>
					<li>予備マスク常備</li>
					<li>次亜塩素酸水生成器コアクリーンの設置</li>
					<li>使い捨てカップの使用</li>
				</ul>
				<figure>
					<img src={studio6} alt="Studio 6" />
				</figure>
			</div>

			<div class="container">
				<h3>その他</h3>
				<ul>
					<li>シャワールームあり</li>
					<li>ゲストwifiあり</li>
					<li>飲料・お茶菓子のご提供</li>
					<li>駐車場あり※3台まで、事前にお知らせください</li>
					<li>犬あり ※苦手な方はお知らせください</li>
				</ul>
				<figure>
					<img src={studio7} alt="Studio 7" />
				</figure>
			</div>
		</section>

		<section class="access" id="access">
			<div class="container">
				<h2>アクセス・問合せ</h2>

				<h3>アクセス</h3>
				<iframe
					src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d810.2391349384023!2d139.8034515!3d35.6780721!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889ee15f69fe3%3A0x6cbe90ef9134b552!2z44Kv44Os44OD44K744Oz44OIIOS6jOOCueOCvw!5e0!3m2!1sja!2sjp!4v1680571156281!5m2!1sja!2sjp"
					width="600"
					height="450"
					frameborder="0"
					style="border:0"
				></iframe>
			</div>

			<div class="container">
				<h3>問合せ</h3>

				<p>お問い合わせは以下メールアドレスまで。</p>
				<p><a href="mailto:info@crescentinc.co.jp">info@crescentinc.co.jp</a></p>
				<p><a href="mailto:lightcage@crescentinc.co.jp">lightcage@crescentinc.co.jp</a></p>
				<p>スタジオ見学はいつでも行っております。</p>
				<p>スタジオ導入・製品販売・見積りもこちらからお問い合わせください。</p>
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
	p,
	td,
	th {
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
