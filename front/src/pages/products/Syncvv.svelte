<script>
	import { link } from 'svelte-spa-router';
	import hero from '../../assets/products/syncvv/banner.jpg';
	import image1 from '../../assets/products/syncvv/system-picture-1.png';
	import image2 from '../../assets/products/syncvv/vicon-rec-trigger.png';
	import image3 from '../../assets/products/syncvv/system-block-diagram.png';
	import image4 from '../../assets/products/syncvv/bluefish444.png';
	import image5 from '../../assets/products/syncvv/channel-expansion.png';
	import image6 from '../../assets/products/syncvv/high-quality-encoder.png';
	import image7 from '../../assets/products/syncvv/various-video-formats.jpg';

	import holoedit from '../../assets/products/holosuite/image5.png';
	import holostream from '../../assets/products/holosuite/image8.png';
	import holoeditImage from '../../assets/products/holosuite/image1.png';
	import holostreamImage from '../../assets/products/holosuite/image4.png';
	import { onMount } from 'svelte';
	import urlSlug from 'url-slug';

	let products;
	let error;
	let isFixedNav = false;
	let activeSection = null;

	onMount(async () => {
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
		<h1>SyncVV II</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>概要</a>
		<a class="sidebar-item" href="#specs" on:click={scrollToElement}>特徴</a>
		<a class="sidebar-item" href="#support" on:click={scrollToElement}>サポート</a>
		<a class="sidebar-item" href="#contact" on:click={scrollToElement}>お問い合わせ</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h3>概要</h3>
				<p class="explanation">
					初代SyncVV
					から大幅に機能強化し、収録作業だけでなくポストプロダクション作業を含めて運用負荷を軽減します
				</p>
				<figure>
					<img alt="" src={image1} />
				</figure>
				<p class="explanation">
					SyncVVII は、4 系統のSDI
					入力を備えた業務用映像音声収録システムです。高度に統合化されたソフトウェアアーキテクチャにより、撮影からポストプロダクションまでをシームレスに接続。新たに追加された素材管理システムにより、収録現場の大幅な省力化が可能になりました。10
					年続いた初代SyncVV のDNA を受け継ぎ、新しく 撮影していることを忘れさせる撮影ソリューション
					として生まれ変わったSyncVV II は、次の時代の収録システムを実現します。
				</p>

				<iframe
					frameborder="0"
					height="400px"
					src="https://player.vimeo.com/video/867536797?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
					style="width:100%;"
					title="Tether Video"
					width="400px"
				></iframe>
			</div>

			<!-- <ul class="features-list">
					<li class="features-list-item">
						アダプティブビットレートのサポートによりLTE・WIFIなど回線速度に応じて最適なクオリティで視聴が可能
					</li>
					<li class="features-list-item">ダウンロードの要らないコンテンツ体験</li>
					<li class="features-list-item">Unity, Unreal, Webへのストリーミング用API</li>
					<li class="features-list-item">マーカーレスARソフト：8th WALLとのインテグレーション</li>
				</ul> -->
		</section>

		<section class="specs" id="specs">
			<div class="container">
				<h2>特徴</h2>

				<h3>Viconシステムと連動した自動収録</h3>
				<p class="explanation-big">
					進化したVicon システム連動自動収録機能は、現場作業負荷を大幅に低減しました。
				</p>

				<details>
					<summary>Vicon システムと連動した自動収録に対応</summary>
					<div class="dynamic-image-text-flexbox">
						<img alt="" src={image2} style="float:left" />

						<p>
							Viconシステムと連動した自動収録機能は、SyncVV-IIシステムの操作負荷を大幅に低減します。
							Viconシステムの収録開始信号を受信したSyncVV-IIは、自動的にテイク情報を取得。
							プロジェクトへのテイク登録から収録開始と収録終了までを完全自動化できます。
							数多くの機材が並ぶ収録現場において、機材オペレーションにかかる負荷は日々高まるばかりですが、SyncVV-IIに搭載されたViconシステム連動自動収録機能は、現場作業負荷を大幅に低減します。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>柔軟な入力ソース</h3>
				<p class="explanation-big">従来どおりの4 チャネルSDI 入力は非同期信号にも対応しました。</p>

				<details>
					<summary>4チャネル同期 非同期SDI 信号収録システム</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image3} style="float:left" /></p>

						<p>
							SyncVV-IIは、同期した4チャネルSDI信号の収録はもちろんのこと、異なるビデオフォーマットを組み合わせた非同期4チャネルSDI信号の収録にも対応しました。
							1台のシステムで異なるビデオフォーマットに柔軟に対応することで、システム全体コストを大幅に低減。
							入力した映像はmp4コンテナに入った映像素材ファイルにリアルタイムエンコードされ、即座にポストプロダクションで使用可能な映像素材に変換されます。
						</p>
					</div>
				</details>

				<details>
					<summary>高信頼性SDI 入力カード採用</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image4} style="float:left" /></p>

						<p>
							SyncVV-IIのSDI入力には、高い信頼性を誇るBluefish Technologies社のSupernova S+を採用。
							広帯域性能を安定して得る基幹技術群には、業界における長年の経験から得られた数多くの知見が活かされています。
							Bluefish444の無制限保証と極めて低いRMA率は、米軍がITハードウェア製造に要求するのと同じ厳しい基準を満たす工業用製造工程によって実現されています。
							組み立て工程は、政府機関による監査で定期的に検証され、ISO9001の認定を受けています。
							業務用機器には業務用コンポーネントを。 SyncVVのこだわりのひとつです。
						</p>
					</div>
				</details>

				<details>
					<summary>複数台並列稼働によるチャネル拡張</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image5} style="float:left" /></p>

						<p>
							近年、Viconシステムを使った撮影環境は大規模化の一途をたどっています。
							精細感溢れる映像表現を創り出す撮影環境において、制作支援のための映像収録環境も拡張が欠かせません。
							SyncVVシステムは、複数台並列稼働によるチャネル数の拡張にも対応。
							Viconシステムからブロードキャストされる収録トリガー信号を使って、複数のSyncVVシステムを連動制御できます。
							ハウスシンクと同期した適切なタイムコードを入力することで、頭のフレームが完全に揃う同期収録制御を新たに開発。
							ポストプロダクションにおいても煩雑な頭合わせのような作業が一切不要の高効率ワークフローを構築できます。
						</p>
					</div>
				</details>

				<details>
					<summary>業務用高品質SDI リアルタイムエンコーダ搭載</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image6} style="float:left" /></p>

						<p>
							4系統のSDI信号を同時入力するシステムにおいて、優れたリアルタイム性を持つエンコーダの存在は非常に重要です。
							SyncVV-IIでは、基幹設計に業務用高品質リアルタイムエンコーダを搭載。
							ベースバンドSDI信号を広帯域で取り込みながら、同時に映像と音声のリアルタイムエンコードを4系統並列で実行する能力を兼ね備えました。
							この高いリアルタイム性と高品質な映像を実現する基本設計により、ミッションクリティカルな収録業務を強力にサポート。
							業務用ビデオからポストプロダクションまでを一気通貫で接続する、新しい映像メディアシステムが誕生しました。
						</p>
					</div>
				</details>

				<details>
					<summary>豊富な入力ビデオフォーマット</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image7} style="float:left" /></p>

						<p>
							SyncVV-IIは、様々な入力ビデオフォーマットに対応することで、現場で映像機器を選定する負荷を大幅に低減します。
							対応ビデオフォーマットは、2048x1080プログレッシブの場合に60pから23.98p、1920x1080プログレッシブの場合に60pから23.98p、1920x1080インターレースの場合に60iから50i。
							1280x720は60pから23.98pまでと、幅広い入力ビデオフォーマットに対応。
							プログレッシブセグメンテッドフレームにも対応し、様々な映像機器が接続される現場でも安心して御利用頂けます。
						</p>
					</div>
				</details>
			</div>
		</section>

		<section class="support" id="support"></section>

		<section class="contact" id="contact"></section>
	</div>
</div>

<style>
	li {
		font-size: calc(14px + 0.390625vw);
	}

	details summary {
		font-weight: bold;
		font-size: calc(16px + 0.390625vw);
		cursor: pointer;
	}
	details[open] summary {
		position: absolute;
		right: 0;
		font-weight: bold;
		font-size: calc(16px + 0.390625vw);
	}

	details[open] {
		position: relative;
	}
	details[open] div {
		margin-top: 2rem;
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
		width: 100%;
		max-height: 100%;
		object-fit: contain;
	}

	p {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}
	.explanation {
		font-size: calc(14px + 0.390625vw);
	}
	.explanation-big {
		font-size: calc(18px + 0.390625vw);
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
	/* section div div {
		display: flex;
		flex-direction: column;
		flex: 50%;
		justify-content: space-between;
	} */
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
