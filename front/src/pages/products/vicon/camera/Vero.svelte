<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../../assets/products/vicon/camera/vero/veroxbanner.jpg';
	import hero2 from '../../../../assets/products/vicon/camera/vero/verobanner.jpg';
	import link1 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink1.png';
	import link2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink2.png';
	import { onMount } from 'svelte';
	import urlSlug from 'url-slug';

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
		<h1>Vero</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>製品詳細</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}>仕様・価格</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h2>製品詳細</h2>
			</div>

			<div class="container">
				<h3>Vero 1.3X</h3>
				<p class="explanation">
					コンパクトかつ高精度で世界中から大好評のVeroシリーズに、広角のVero 1.3Xが誕生しました。
					視野の広いVero
					1.3Xなら、限られた空間でも広いキャプチャエリアを確保でき、全身のトラッキングや収録が可能になります。
				</p>

				<ul class="features-list">
					<li class="features-list-item">
						SMALLNESS <p>
							カメラの小型化に伴い、CAVEやHolo
							Stageのようなカメラスペースの取れない空間であっても、他の機材と鑑賞すること無くスムースな設置が行えます。
						</p>
					</li>

					<li class="features-list-item">
						PoE(Power over Ethernet)接続 <p>
							汎用Etherrnetケーブル一本で電源の供給と、データの伝送を行う為、シンプルで設置場所を選ばないシステム設計が可能です。
						</p>
					</li>
					<li class="features-list-item">
						SMALL but BRIGHT STROBE <p>
							Veroにはより強力で高視野角のストロボが搭載されています。これにより、不要な光のノイズなどを識別しやすくなり、より的確なマーカーデータの検出が可能となります。
						</p>
					</li>
				</ul>
			</div>

			<div class="container">
				<h2>Vero 2.2</h2>
				<figure>
					<img src={hero2} alt="Shooting system" />
				</figure>
				<p class="explanation">
					Vero
					2.2は、Viconのモーションキャプチャの目指す部分とは一線を画した、廉価でコンパクト、且つ高精度なRigid
					Bodyに特化したトラッキング用のソリューションです。
				</p>

				<ul class="features-list">
					<li class="features-list-item">
						VARIFOCAL LENS
						<p>
							Vero
							2.2にはズーム可能なレンズが搭載されており、焦点距離を6mmから12mmまで変更することができます。その為、設置場所や使用用途に応じて設定を自由に変更することが可能です。
						</p>
					</li>
				</ul>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>仕様・価格</h2>
				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th></th>
							<!--<th>Vero v1.3</th>-->
							<th colspan="3">Vero v2.2</th>
							<th colspan="3">Vero 1.3X</th>
						</tr>

						<tr>
							<td class="tblCap">解像度</td>
							<!--<td>130万画素<br>1,280 x 1,024</td>-->
							<td colspan="3">220万画素<br />2,048 x 1,088</td>
							<td colspan="3">130万画素<br />1,280 x 1,024</td>
						</tr>

						<tr>
							<td class="tblCap">最大フレームレート</td>
							<!--<td>250Hz</td>-->
							<td colspan="3">330Hz</td>
							<td colspan="3">250Hz</td>
						</tr>

						<tr>
							<td class="tblCap">給電・伝送路</td>
							<td colspan="6">PoE+</td>
						</tr>

						<tr>
							<td class="tblCap">レンズ</td>
							<td colspan="3">6 - 12 mm （Varifocal：可変焦点レンズ）</td>
							<td colspan="3">4mm固定焦点レンズ</td>
						</tr>

						<tr>
							<td class="tblCap">視野角</td>
							<!--<td>W:　60.8° x 50.3°<br>T:　32.7° x 26.4°</td>-->
							<td colspan="3">W:　86.4° x 53.0°<br />T:　50.3° x 28.0°</td>
							<td colspan="3">79.0° x 67.6°</td>
						</tr>

						<tr>
							<td class="tblCap">ストロボ</td>
							<td colspan="6">IR（850nm）</td>
						</tr>

						<tr>
							<td class="tblCap">シャッタータイプ</td>
							<td colspan="6">Global</td>
						</tr>

						<tr>
							<td class="tblCap">接続ケーブル</td>
							<td colspan="6">Cat5e / RJ45</td>
						</tr>

						<tr>
							<td class="tblCap">消費電力/カメラ</td>
							<td colspan="6">12W</td>
						</tr>

						<tr>
							<td class="tblCap">サイズ</td>
							<td colspan="3">83 mm (H) x 80 mm (W) x 135 mm (D)、575g</td>
							<td colspan="3">83 mm (H) x 80 mm (W) x 112 mm (D)、560g</td>
						</tr>

						<tr>
							<td class="tblCap">対応ソフトウェア<br />バージョン</td>
							<td colspan="6">Shogun 1,Blade 3, Nexus 2, Tracker 3 以上必須</td>
						</tr>

						<tr>
							<td class="tblCap">価格(税別)</td>
							<!--<td>1,050,000円</td>-->
							<td colspan="6">1,500,000円</td>
						</tr>
						<tr>
							<td class="tblCap" rowspan="3">年間保守価格<br />(税別)</td>
							<td class="hoshuL hoshuT">モーションキャプチャ</td>
							<td colspan="5" class="hoshuR hoshuT">1,200,000円</td>
						</tr>
						<tr>
							<td class="hoshuL hoshuB">トラッキング</td>
							<td colspan="5" class="hoshuR hoshuB">800,000円</td>
						</tr>
						<tr>
							<td colspan="6"
								>オンサイトサポート、代替機材無償貸出、<br
								/>電話、メール、ファックス対応、修理品部品料のみ請求</td
							>
						</tr>
						<tr>
							<td class="tblCap" rowspan="3">取扱説明及び設置価格<br />(税別)</td>
							<td class="hoshuL hoshuT">モーションキャプチャ</td>
							<td colspan="5" class="hoshuR hoshuT">1,200,000円</td>
						</tr>
						<tr>
							<td class="hoshuL hoshuB">トラッキング</td>
							<td colspan="5" class="hoshuR hoshuB">600,000円</td>
						</tr>
						<tr>
							<td colspan="6"
								>スタジオ内カメラ設置（工事費別途）、<br
								/>取扱説明（約2日）、必要に応じて追加無償取扱説明１回実施</td
							>
						</tr>
					</tbody>
				</table>
			</div>
		</section>
		<br />
		<br />
		<br />
		<a href={`/product/vicon`} use:link>
			<button class="more">
				<span class="viewMore">VICONトップへ</span>
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
						<p class="linkTitle">Faceware</p>
						<span class="overflowed-text"
							>ビデオベースのフェイシャル専用モーションキャプチャーシステム</span
						>
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
						<p class="linkTitle">StretchSense</p>
						<span class="overflowed-text"
							>シリコン素材の伸縮センサーを搭載したワイアレス対応グローブデバイス</span
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
		border: 1px solid rgb(143, 143, 143);
		padding: 1rem 5rem;
		background: none;
		border-radius: 8px;
		cursor: pointer;
	}

	th {
		padding: 10px;
		font-size: calc(12px + 0.390625vw);
		background: #e0e3e7;
	}
	td {
		font-size: calc(12px + 0.390625vw);
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
