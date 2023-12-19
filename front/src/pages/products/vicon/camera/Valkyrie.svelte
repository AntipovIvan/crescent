<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../../assets/products/vicon/camera/valkyrie/valkyrieHero.jpg';
	import image2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie2.jpg';
	import image3 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie3.jpg';
	import image4 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie4.jpg';
	import image5 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie5.jpg';
	import image6 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie6.jpg';
	import image7 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie7.jpg';
	import link1 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink1.png';
	import link2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink2.png';
	import imageSlide1 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie1-0.jpg';
	import imageSlide2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie1-1.jpg';
	import imageSlide3 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie1-2.jpg';
	import imageSlide4 from '../../../../assets/products/vicon/camera/valkyrie/valkyrie1-3.jpg';
	import { onMount } from 'svelte';
	import urlSlug from 'url-slug';

	let thumbnails = [imageSlide1, imageSlide2, imageSlide3, imageSlide4];

	let selectedImage = thumbnails[0];

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
					if (entry.isIntersecting && entry.intersectionRatio >= 0.1) {
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
			{ threshold: 0.1 }
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

	function selectImage(image) {
		selectedImage = image;
	}
</script>

<div class="pageContent">
	<div class="hero">
		<h1>Valkyrie</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>製品概要</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}>製品特徴</a>
		<a class="sidebar-item" href="#perfCapt" on:click={scrollToElement}
			>Valkyrie = “Performance Capture 3.0”</a
		>
		<a class="sidebar-item" href="#price" on:click={scrollToElement}>製品ラインアップ・価格</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h2>製品概要</h2>
				<p class="explanation">
					VANTAGEカメラのリリースから７年が過ぎ、満を持し最新カメラVALKYRIEが、遂にリリースされました。
				</p>
				<p class="explanation">
					開発の追い込み時期がコロナ禍悲惨な時期と重なり、開発遅延の恐れもありましたが、つつがなく製品も生産され始めています。但し、半導体の供給不足、仕入部材の高騰化が響き、円安の追い打ちもあいまって、製品価格は大きく上昇しています。しかし、更なる製品機能の向上で製品パフォーマンスを一層引き上げ、お買い得感を維持しています。
				</p>
				<p class="explanation">
					エントリーモデルのVEROは引き続き継続して生産されており、クレッセントとしては、お買い得のIratto1000でVICONをご体験頂き、VALKYRIEの800万画素VK8で本格導入をご検討頂き、“いつかは、VK26”のUXのシナリオを描いております
				</p>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>製品特徴</h2>
				<ul>
					<li>フラッグシップカメラの解像度が（1600万画素から）2600万画素に向上</li>
					<li>
						新搭載FPGA（TESLAにも搭載）によるカメラ内部の処理能力の大幅向上により、カメラの高精度、高速化を実現
					</li>
					<li>UPoEの供給電力能力向上を利用し、より強力で遠距離到達可能なLEDを実装</li>
					<li>新開発のカメラセンサに最適化されたVARIFOCALレンズ</li>
					<li>
						ユーザ要望による、映像表示によるカリブレーション調整機能や、熱膨張やアクシデント時のカリブレーション誤差の自動修正モード
					</li>
					<li>屋外利用を想定してのIP65ミリタリスペックで雨天悪天候下での利用が可能</li>
					<li>
						Virtual
						Productionでの所謂、ICVFXステージでのトラッキングデバイスとして、様々な機能の実装と、外部ハードウェアと連携
					</li>
				</ul>
				<div class="full-scale-image">
					<img src={selectedImage} alt="Full-scale Image" />
				</div>
				<div class="thumbnails">
					{#each thumbnails as thumbnail}
						<div class="thumbnail" on:click={() => selectImage(thumbnail)}>
							<img src={thumbnail} alt="Thumbnail" />
						</div>
					{/each}
				</div>
			</div>
		</section>

		<section class="perfCapt" id="perfCapt">
			<div class="container">
				<h2>Valkyrie = Performance Capture3.0</h2>
				<p>
					より高解像度でより高速撮像可能なカメラValkyrieシリーズは、より広範囲をより高精度に、しかもより操作性よくリアルタイムにキャプチャすることを実現しました。その上で、世界中の現場から要望されている機能をSHOGUN2.0にてんこ盛りして行きます。つまり、Valkyrieを導入することで、次世代リアルタイムキャプチャスタイル、Performance
					Capture3.0にモーションキャプチャスタジオを進化させることができます。
				</p>
				<h3>①10本指＠10mmマーカ リアルタイムが現実的に！</h3>
				<figure>
					<img src={image2} alt="Shooting system" />
				</figure>
				<p>
					VK26の超解像度が10mmマーカー捕捉に大きく貢献。今迄難しかった10同時10フィンガーキャプチャもリアルタイム処理が実現可能になりました。
				</p>
				<figure>
					<img src={image3} alt="Shooting system" />
				</figure>
				<p>
					クレッセント製専用手袋により装着性向上とマーカー位置保持、そして装着時間大幅短縮でアクターさんの負担を一気に軽減！
				</p>

				<h3>②リアルタイムデータ、MCPのPOST処理がSHOGUN2で楽ちんに</h3>
				<p>
					リアルタイムで出力されるMCPデータのPOSTがよりインテリジェントに高速になります。複雑で多くの処理が必要なシーンはX2Dで、ライブ中心のデータで多少の後処理で済みそうなデータはMCPで、SHOGUN
					POSTに投げ込む新しいワークフローがますます充実します。
				</p>

				<h3>③Multi-Machine機能でリアルタイム処理40%効率化</h3>
				<p>
					AMDの新RyzenのWorkStationを多重化し、10G
					HUBで接続することで大規模撮影時のリアルタイム処理のドロップフレームを40％改善します。10人＋10フィンガー同時撮影でも70～80％＠120fpsを実現します(社内比）
				</p>

				<h3>④INCAM-VFXの蓄積をPerformance Capture3.0へ移植</h3>

				<ul>
					<li>
						SuperNova
						<p>
							柔軟性高いアクティブマーカー。VirtualCameraや、動きの早いプロップ等に装着することで、複雑な形状にも容易にロックソリッドなRigidを作成することができます。
						</p>
						<br />
						<img src={image4} alt="title" width="100%" />
					</li>
					<br />
					<li>
						Crown
						<p>
							柔軟性高いアクティブマーカー。VirtualCameraや、動きの早いプロップ等に装着することで、複雑な形状にも容易にロックソリッドなRigidを作成することができます。
						</p>
						<br />
						<img src={image5} alt="title" width="100%" />
					</li>
					<br />
					<li>
						DCSをSHOGUNに統合　
						<p>
							レンズデータを自動で読み取ってくれるLDT-V1をSHOGUN側で入力できるように現在調整中。圧倒的な位置精度と共に、正確なレンズ値をリアルタイムにSHOGUN経由でモーションデータに統合できます。
						</p>
						<br />
						<img src={image6} alt="title" width="100%" />
					</li>
				</ul>

				<h3>⑤自動Healing機能で素早いシステム立ち上げと、中断の無い撮影を実現</h3>
				<figure>
					<img src={image7} alt="Shooting system" />
				</figure>
				<p>
					切削アルミケーシングによる熱を効率的に逃がすヒートフローとUPoEによるカメラへの供給電力の増加により、暖気時間を大幅削減。加速度センサと、熱電対サーモセンサ、トラッキング専用LEDを実装し、衝撃によるズレや熱による膨張を自動検知、自己診断的にリカリブレーションを行います。
				</p>
			</div>
		</section>

		<section class="price" id="price">
			<div class="container">
				<h2>製品ラインアップ・価格</h2>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th></th>
							<th>VK26</th>
							<th>VK16</th>
							<th>VK8</th>
						</tr>
						<tr>
							<td class="tblCap">解像度<br />（万画素）</td>
							<td>2600</td>
							<td>1600</td>
							<td>800</td>
						</tr>
						<tr>
							<td class="tblCap">最高FPS<br />（フル解像度）</td>
							<!--<td>250Hz</td>-->
							<td>150</td>
							<td>300</td>
							<td>500</td>
						</tr>
						<tr>
							<td class="tblCap">最高画角<br />（縦x横°）</td>
							<!--<td>250Hz</td>-->
							<td>72 x 72</td>
							<td>72 x 56</td>
							<td>72 x 42</td>
						</tr>
						<tr>
							<td class="tblCap">価格<br />（税別）</td>
							<!--<td>250Hz</td>-->
							<td>9,500,000円</td>
							<td>8,500,000円</td>
							<td>6,500,000円</td>
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
	.thumbnails {
		display: flex;
		flex-direction: row;
		justify-content: center;
	}

	.thumbnail {
		width: 100px;
		margin: 5px;
		cursor: pointer;
	}

	.full-scale-image {
		display: flex;
		justify-content: center;
		margin-top: 20px;
	}

	.full-scale-image img {
		max-width: 100%;
	}

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
	.special-ul {
		display: flex;
		gap: 3rem;
		list-style-type: none;
	}
	.special-overflowed-test {
		margin: 0;
	}
	.card article figure .special-card-figcaption {
		background: none;
	}
	li {
		font-size: calc(14px + 0.390625vw);
	}
	p {
		font-size: calc(14px + 0.390625vw);
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
