<script>
	import hero from '../../assets/products/holosuite/holo-hero.jpg';
	import holoedit from '../../assets/products/holosuite/image5.png';
	import holostream from '../../assets/products/holosuite/image8.png';
	import holoeditImage from '../../assets/products/holosuite/image1.png';
	import holostreamImage from '../../assets/products/holosuite/image4.png';
	import { onMount } from 'svelte';

	let isFixedNav = false;
	let activeSection = null;

	onMount(async () => {
		window.scrollTo(0, 0);
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
		<h1>ARCTURUS HoloSuite</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>概要</a>
		<a class="sidebar-item" href="#holoedit" on:click={scrollToElement}>HoloEdit</a>
		<a class="sidebar-item" href="#holostream" on:click={scrollToElement}>HoloStream</a>
		<a class="sidebar-item" href="#price" on:click={scrollToElement}>価格</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h3>概要</h3>
				<p class="explanation">
					HoloSuiteは、あらゆる空間または3D環境に対するボリューメトリック・ビデオを編集・配信するためのプラットフォームです。
				</p>
				<p class="explanation">
					HoloSuiteは、ボリューメトリックビデオを効率的に編集・圧縮するノンリニアエディター、HoloEditと、様々なネットワーク速度に応じて確実にボリューメトリック・ビデオのストリーミング配信を実現する、HoloStreamで構成されています。
				</p>

				<figure>
					<img src={holoedit} alt="Holoedit" />
				</figure>
				<p class="explanation">
					HoloEditは、4DVIEWS、Tetaviなどのボリューメトリクスデータをノンリニア編集できる初のソフトウェアです。
					以下のような機能を使用して編集や圧縮が可能です。
				</p>

				<ul class="features-list">
					<li class="features-list-item">メッシュクリーンアップ、リダクション</li>
					<li class="features-list-item">複数クリップの横編集+マルチトラック処理</li>
					<li class="features-list-item">自動リギング、クリーンアップ</li>
					<li class="features-list-item">先進のメッシュ圧縮処理</li>
				</ul>

				<p class="explanation">
					イントロダクション動画：<a href="https://youtu.be/xma5ERYf9oU" target="_blank"
						>https://youtu.be/xma5ERYf9oU</a
					>
				</p>
			</div>

			<div class="container">
				<figure>
					<img src={holostream} alt="Holostream" />
				</figure>
				<p class="explanation">
					途切れる事の無い、視聴体験を実現するストリーミング再生環境を実現。
				</p>
				<ul class="features-list">
					<li class="features-list-item">
						アダプティブビットレートのサポートによりLTE・WIFIなど回線速度に応じて最適なクオリティで視聴が可能
					</li>
					<li class="features-list-item">ダウンロードの要らないコンテンツ体験</li>
					<li class="features-list-item">Unity, Unreal, Webへのストリーミング用API</li>
					<li class="features-list-item">マーカーレスARソフト：8th WALLとのインテグレーション</li>
				</ul>
				<!-- <p class="explanation">
					<a href="https://youtu.be/xma5ERYf9oU" target="_blank"
						>WEBプレイヤー サンプルページ (今週の月餅)</a
					>
				</p> -->
			</div>
		</section>

		<section class="holoedit" id="holoedit">
			<div class="container">
				<h2>HoloEdit</h2>

				<figure>
					<img src={holoeditImage} alt="holoeditImage" />
				</figure>
				<p class="explanation">
					HoloEditは、4DVIEWSなどのボリューメトリックデータをノンリニア編集できる初のソフトウェアです。以下のような機能を使用して編集や圧縮を行います。
				</p>
				<ul>
					<li>メッシュデータのクリーンアップ、リダクション</li>
					<li>複数クリップのノンリニア編集+マルチトラック処理</li>
					<li>自動リギング、クリーンアップ</li>
					<li>先進のメッシュ圧縮処理</li>
				</ul>
				<p class="explanation">
					ダイナミックなリターゲティング機能の付加や、メッシュデータの圧縮が可能で、
					出力されるOMS+MP4データは、様々バイスで再生可能です。
				</p>
				<p class="explanation">
					さらに、HoloStreamと組み合わせる事で、アダプティブビットレートのストリーミング再生が可能になります。
				</p>
				<p class="explanation">
					4DVIEWS以外のシステムでも、OBJ+PNGとしてデータ出力できればインポート可能です。
				</p>
			</div>

			<div class="container">
				<h3>対応ボリューメトリクスシステム</h3>

				<ul>
					<li>4DVIEWS</li>
					<li>Tetavi</li>
					<li>その他システムもOBJ+PNGとしてデータ出力できればインポート可能</li>
				</ul>
			</div>

			<div class="container">
				<h3>必要PCスペック</h3>

				<table border="1" cellpadding="3">
					<tbody>
						<tr>
							<th colspan="2">HARDWARE</th>
						</tr>
						<tr>
							<td>Processor</td>
							<td
								>Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz, 3401 Mhz, 4 Core(s), 8 Logical
								Processor(s)
							</td>
						</tr>
						<tr>
							<td>Memory</td>
							<td>16.0 GB</td>
						</tr>
						<tr>
							<td>Graphics</td>
							<td>NVIDIA GeForce GTX 1070</td>
						</tr>
						<tr>
							<td>OpenGL</td>
							<td>OpenGL 4.6</td>
						</tr>
						<tr>
							<td>Network</td>
							<td>240 Mbps down / 17 Mbps up</td>
						</tr>
						<tr>
							<td>Storage</td>
							<td>5 TB SSD</td>
						</tr>
						<tr>
							<th colspan="2">SOFTWARE</th>
						</tr>
						<tr>
							<td>OS (Operating System)</td>
							<td>Microsoft Windows 10 Home (Version 10.0.18362 Build 18362)</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>

		<section class="holostream" id="holostream">
			<div class="container">
				<h2>HoloStream</h2>
				<p class="explanation">
					途切れる事の無い、視聴体験を実現するストリーミング再生環境を実現します。
				</p>
				<ul>
					<li>
						アダプティブビットレートのサポートによりLTE・WIFIなど回線速度に応じて最適なクオリティで視聴が可能
					</li>
					<li>ダウンロードの要らないコンテンツ再生が可能</li>
					<li>Unity, Unreal, Webへのストリーミング用API</li>
					<li>マーカーレスARソフト：8th WALLとのインテグレーションも可能</li>
				</ul>
				<p class="explanation">
					業界標準のストリーミングプロトコルを拡張したストリーミングソリューションを使用して様々な伝送帯域にも対応し、世界中の人々が視聴可能な真の1対多数のソリューションです。
					また、ポリゴンデータをストリーミングしている為、6dofやAR体験が実現可能になっており、デバイスに最適な画質で、途切れの無いスムースな視聴体験が可能になります。
				</p>

				<figure>
					<img src={holostreamImage} alt="holostreamImage" />
				</figure>
			</div>

			<div class="container">
				<h3>対応プラットフォーム</h3>

				<table border="1" cellpadding="3" cellspacing="1">
					<tbody>
						<tr>
							<th>端末</th>
							<th>OS</th>
							<th>アプリ</th>
							<th>AR機能</th>
						</tr>

						<tr>
							<td colspan="1" rowspan="2">PC</td>
							<td colspan="1" rowspan="2">Windows</td>
							<td>Unity</td>
							<td>有償</td>
						</tr>
						<tr>
							<td>Chrome/Firefox/Edge</td>
							<td>-</td>
						</tr>

						<tr>
							<td colspan="1" rowspan="2">Mac</td>
							<td colspan="1" rowspan="2">OS X</td>
							<td>Unity</td>
							<td>有償</td>
						</tr>
						<tr>
							<td>Safari/Chrome/Firefox</td>
							<td>-</td>
						</tr>

						<tr>
							<td>Chrome</td>
							<td>Chrome</td>
							<td>Chrome</td>
							<td>AR-Core</td>
						</tr>

						<tr>
							<td colspan="1" rowspan="2">スマホ/タブレット</td>
							<td colspan="1" rowspan="2">Android</td>
							<td>Unity</td>
							<td>AR-Core</td>
						</tr>
						<tr>
							<td>Chrome</td>
							<td>8th WALL</td>
						</tr>

						<tr>
							<td colspan="1" rowspan="2">iPhone/iPad</td>
							<td colspan="1" rowspan="2">iOS</td>
							<td>Unity</td>
							<td>AR Toolkit</td>
						</tr>
						<tr>
							<td>Safari</td>
							<td>8th WALL</td>
						</tr>

						<tr>
							<td>HMD(ヘッドマウント)</td>
							<td>Android/PC</td>
							<td>Unity</td>
							<td>-</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>

		<section class="price" id="price">
			<div class="container">
				<h2>価格</h2>

				<h3>HoloSuite</h3>
				<p>年間サブスクリプション　800,000円(税別)</p>
				<p>内容物：</p>
				<table border="1" cellpadding="3" cellspacing="1">
					<tbody
						><tr style="background-color:#cccccc;">
							<th style="border:solid 1px #000000;font-weight:bold;">HoloEdit</th>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">HoloCompute Pack 500 Compute Hours</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">HoloSuite Player SDK</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">HoloEdit Mari Plugin</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">HoloEdit Maya Plugin</td>
						</tr>
						<tr style="background-color:#cccccc;font-weight:bold;">
							<th style="border:solid 1px #000000;font-weight:bold;">HoloStream</th>
						</tr>
						<tr>
							<td style="border:solid 1px #000000">HoloStream View Minutes : 5000 </td>
						</tr>
						<tr>
							<td style="border:solid 1px #000000">HoloEncode Minutes : 5 min</td>
						</tr>
					</tbody>
				</table>
			</div>

			<div class="container">
				<h3>HoloStream View Packs (ストリーミング費用)</h3>

				<table border="1" cellpadding="3" cellspacing="1">
					<tbody
						><tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;" rowspan="5">HoloStream View Pack</td>
							<td style="border:solid 1px #000000;">10,000 Views Minutes</td>
							<td style="border:solid 1px #000000;">30万円（税別）</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">25,000 Views Minutes</td>
							<td style="border:solid 1px #000000;">60万円（税別）</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">50,000 Views Minutes</td>
							<td style="border:solid 1px #000000;">100万円（税別）</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">100,000 Views Minutes</td>
							<td style="border:solid 1px #000000;">150万円（税別）</td>
						</tr>
						<tr style="border:solid 1px #000000">
							<td style="border:solid 1px #000000;">500,000 Views Minutes</td>
							<td style="border:solid 1px #000000;">500万円（税別）</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>
	</div>
</div>

<style>
	li {
		font-size: calc(14px + 0.390625vw);
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
