<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../../assets/products/vicon/software/shogun/shogunhead.png';
	import image1 from '../../../../assets/products/vicon/software/shogun/Apose.png';
	import image2 from '../../../../assets/products/vicon/software/shogun/overray.png';
	import image3 from '../../../../assets/products/vicon/software/shogun/soft_shogun_realtime.png';
	import image4 from '../../../../assets/products/vicon/software/shogun/soft_shogun_unbreak.png';
	import link1 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink1.png';
	import link2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink2.png';

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
		<h1>Shogun</h1>
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
					“Shogun”は“Final quality skeletal data by day's
					end(キャプチャしたその日の内にデータを納品)”を目標に作られ、品質を犠牲にすることなくデータ処理のパイプラインを圧倒的に速めるエンターテインメント用モーションキャプチャーツールであり、“Blade”の後継ソフトウェアです。
					Bladeよりも堅牢かつ高精度のデータをサードパーティのソリューションにあっという間にストリーミングできるため、キャプチャ前の準備時間も大幅に削減できます。
				</p>

				<li>
					Live Subject Calibration
					<div class="image-text-flexbox">
						<p>
							柔軟性高いアクティブマーカー。VirtualCameraや、動きの早いプロップ等に装着することで、複雑な形状にも容易にロックソリッドなRigidを作成することができます。
						</p>
						<br />
						<img src={image1} alt="title" width="100%" />
					</div>
				</li>
				<br /> <br />
				<li>
					フルボディメッシュとビデオオーバーレイ表示

					<div class="image-text-flexbox">
						<p>
							Shogunはスキンという専用のカスタムメッシュを持っています。スキンにより各アクターの判別が簡易になっただけでなく、Solvingのクオリティを即座に把握できます。
							また、高解像度のデジタルリファレンスカメラVueをシステムに組み込むことによって、完全同期したビデオの映像に、スキンとSolving
							Skeletonをオーバーレイ表示します。
						</p>
						<br />
						<img src={image2} alt="title" width="100%" />
					</div>
				</li>
				<br /> <br />
				<li>
					リアルタイムの新機能によるデータの品質向上

					<div class="image-text-flexbox">
						<p>
							Shogunは今までにないリアルタイム用の機能を備えています。
							<br />
							ShogunはVantage、Veroの両カメラに備えられた加速度計と温度計を使って、一つひとつのカメラをモニタリングできます。また、撮影中に誤ってカメラを動かしてしまったとき、カメラの位置を変更したいときに、システム全体をキャリブレーションし直さなくても、その場にいるアクターやプロップを使って特定のカメラのみを再キャリブレーションできるようになりました。
							<br />
							これにより、システムを常に最適な状態に保ち、データの品質を向上させます。
						</p>
						<br />
						<img src={image3} alt="title" width="100%" />
					</div>
				</li>
				<br /> <br />
				<li>
					“UNBREAKABLE" Solving

					<div class="image-text-flexbox">
						<p>
							Shogunのオクルージョンに対する性能は世界最高の品質を誇っています。マーカーが見えづらい状況でもキャラクターが崩壊せず、複数のアクターが複雑に入り乱れるテイクであっても正確なリアルタイムプレビューが可能です。
							<br />
							リアルタイムでのモーションキャプチャーへの需要が高まっている今、Shogunはあなたの強力な助けとなります。
						</p>
						<br />
						<img src={image4} alt="title" width="100%" />
					</div>
				</li>
				<br /> <br />
				<li>
					.mcpファイル

					<div class="image-text-flexbox">
						<p>
							Shogunでは、これまでのように撮影したデータを三次元化するところからポスト処理を始める必要はありません。リアルタイムで直接ディスクに書き込まれた.mcpファイルをShogunPostで開くと、マーカーやカメラ、骨などの撮影した当時のデータをそのまま処理することが可能です。
							<br />
							また、データが荒れている箇所は新しく搭載されたヒートマップ機能により簡単に発見できるようになりました。
						</p>
						<br />
					</div>
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
							<th>Shogun</th>
						</tr>

						<tr>
							<td class="tblCap">名称</td>
							<td>エンターテインメント用モーションキャプチャ編集ソフトウェア</td>
						</tr>
						<tr>
							<td class="tblCap">対応OS</td>
							<td>Window 10 (64bit)<br />Windows 7 (64bit)</td>
						</tr>
						<tr>
							<td class="tblCap">価格(税別)</td>
							<td>3,500,000円</td>
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
