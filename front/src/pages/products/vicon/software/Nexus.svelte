<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../../assets/products/vicon/software/nexus/biofeedback-600x300.png';
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
		<h1>Nexus</h1>
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
				<p class="explanation">
					Vicon
					Nexusは、初のライフサイエンスに特化したモーションキャプチャーソフトウェアです。日々のルーティンワークを簡略化し、如何なる条件下でも容易にカスタマイズが可能であり、且つ、如何なる複雑な要望にも対応可能なソフトウェアです。
				</p>

				<li>
					EASY TO LEARN, EASY TO USE
					<p>
						Nexusは卓越した使用感を提供します。インターフェースは、処理過程と同様にデータ準備、データ取得、レビューの順序で整頓されています。直感的に必要な作業ボタンを発見でき、ラーニングカーブが急速に上がる人間工学的設計に仕上がっています。
					</p>
				</li>

				<li>
					NATIVE REAL TIME
					<p>
						Nexusの真髄は、リアルタイム性にあります。あらゆるデータはその場でリアルタイム視認が可能です。カメラを追加した場合、その設定を行う必要はありません。Nexusが自動認識し、処理を行います。Nexusには自己診断モニタ機能が搭載され、随時実行しています。従い、撮影の終わりに予期せぬデータばかりが蓄積されて、一日が台無しになるようなこともありません。
					</p>
				</li>

				<li>
					CUSTOMIZE EVERYTHING
					<p>
						Nexusのカスタマイズ機能として、新たにProtocol
						Builderを搭載しています。これは、ご要望のパイプラインワークフローをウィザードベースのワークフローとして登録し、業務フローを一元化することが可能となりました。
					</p>
				</li>

				<li>
					PAST PRESENT, FUTURE PERFECT
					<p>
						Nexusは、過去、現在、将来のデータコンパティビリティを保証します。現在、ご利用のデータはもちろん、今後撮られるデータも含め、全てPlug-in
						GaitやPlug-in
						Modelerとの互換が保証され、現在のプロセス課程を変更する必要は一切ありません。同様に、取得されたNexusのデータはシームレスにPolygonへの移行が可能です。
					</p>
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
							<th>nexus</th>
						</tr>

						<tr>
							<td class="tblCap">名称</td>
							<td>エンジニアリング用モーションキャプチャ解析ソフトウェア</td>
						</tr>
						<tr>
							<td class="tblCap">対応OS</td>
							<td>Windows 10 (64bit)</td>
						</tr>
						<tr>
							<td class="tblCap">価格(税別)</td>
							<td>3,500,000円</td>
						</tr>
					</tbody>
				</table>
				<p>※ソフトウェアメジャーアップグレードについては別途費用発生</p>
				<br />

				<li>
					マーカーの3次元位置情報及び人体の姿勢データを、マーカー数の制限なく遅延なく記録し、TCP/IP経由でリアルタイムでの出力及び、ソフトウェア上で表示可能
				</li>

				<li>
					Lock Labから最大64チャンネルのアナログ信号を完全同期し、更に信号データの取得も可能

					<p>※Lock Labを追加すれば、64ch以上のアナログ信号動機も可能。</p>
				</li>

				<li>人体につけたマーカーから全身の人体骨格モデルが作成可能</li>

				<li>キャリブレーション時に特定のカメラを選択し、再キャリブレーションが可能</li>

				<li>CSV形式等のASCIIデータ及び、c3dデータの出力が可能。</li>
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
