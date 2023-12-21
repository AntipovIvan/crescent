<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../../assets/products/vicon/software/polygon/soft_polygon_key.jpg';
	import image1 from '../../../../assets/products/vicon/software/polygon/soft_polygon_data_m.jpg';
	import image2 from '../../../../assets/products/vicon/software/polygon/soft_polygon_key.jpg';
	import link1 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink1.png';
	import link2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink2.png';
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
		<h1>Polygon</h1>
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
				<p>
					Vicon
					Polygonは、世界で唯一、インタラクティブに3Dデータを含むマルチメディアの素材を簡単に扱えるレポートツールです。最新のVer4に至る現在、Polygonは、世界中数百のサイトで様々なレポート作成に携わっています。
				</p>
			</div>

			<div class="container">
				<li>
					1つのアプリケーションであらゆるデータを可視化
					<div class="image-text-flexbox">
						<p>
							Polygonは、あらゆる動作解析関連のデータを読み込め、それらを、テキスト、AVI、Webページなどあらゆるデータと連携して取り扱うことが可能です。各データは、パネル上で様々な他データと同期させながら表示させることができ、解析作業の効率的が飛躍的にあがります。
						</p>
						<br />
						<img src={image1} alt="title" width="100%" />
					</div>
				</li>

				<li>
					効率的なハイパーリンクによるナビゲーション
					<p>
						Web手法同様に、Polygonでは様々なデータやテキストをハイパーリンクで繋げながら効率的なデータのナビゲーションを行います。データ内部の一部分の参照したい箇所に対してのみでも、ハイパーリンクを使って設定することが可能です。
					</p>
					<br />
				</li>

				<li>
					豊富なテンプレートによる迅速なレポート作成
					<p>
						Polygonは、あらゆるレポートをテンプレートとして保存することが可能です。従い、同じレポート形式を違ったデータセットで使いまわすことが可能です。
					</p>
					<br />
				</li>

				<li>
					レポートプレゼンテーションツール
					<p>
						インタラクティブでハイパーリンクが可能なPolygonは、データをプレゼンテーションする最適なツールです。プロジェクタにう上手くフィットするPowerPoint系での処理も可能です。従い、時間の無駄無くデータの転送も不要で、簡単にモーションデータを含むプレゼンテーションが作成できます。
					</p>
					<br />
				</li>

				<li>
					データ出力や、配布に優れた機能
					<p>
						Polygonで作成したデータを容易にPDFやWord、Excelに出力することが可能です。従い、Excelとのやり取りを通してデータの編集、アーカイブ化、プリントアウト等がシームレスにできます。同様に、無償配布のPolygonViewerを使い、作成したデータをWindowsPCを持つ視聴者に対し自由に配布することが可能です。
					</p>
					<br />
				</li>

				<li>
					筋骨格モデリング
					<div class="image-text-flexbox">
						<p>
							Polygonは、ビルトインのインターフェースを用い、筋骨格を3次元の高品位なデータで簡単に作成することが可能です。他のアプリケーションのように、作成したデータの入出力を繰り返し、視覚化する必要は一切ありません。ラッピングする筋肉の数を任意に選択でき、これらのオブジェクトは、点、球、円柱、楕円系など自由度高くひょうげんすることが可能です。
						</p>
						<br />
						<img src={image2} alt="title" width="100%" />
					</div>
				</li>

				<li>
					リアルタイムフィードバック
					<p>
						Polygonの表示能力は卓越しており、グラフでも3Dデータでもリアルタイムに再生することが可能です。生物工学モデルもリアルタイムにモーションデータを入れて再生可能であり、そこから同時にジョイントアングルや、3Dのセグメント等も再生が可能です。
					</p>
					<br />
				</li>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>仕様・価格</h2>
				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th></th>
							<th>polygon</th>
						</tr>

						<tr>
							<td class="tblCap">名称</td>
							<td>レポート作成ソフトウェア</td>
						</tr>
						<tr>
							<td class="tblCap">対応OS</td>
							<td>Windows XP (32bit) Windows 7 (64bit/32bit)</td>
						</tr>
						<tr>
							<td class="tblCap">価格(税別)</td>
							<td>3,000,000円</td>
						</tr>
					</tbody>
				</table>
				<p>※ソフトウェアメジャーアップグレードについては別途費用発生</p>
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
		padding: 1rem 4rem;
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

	p,
	li {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}

	.image-text-flexbox img {
		width: 14vw;
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
		.image-text-flexbox img {
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
