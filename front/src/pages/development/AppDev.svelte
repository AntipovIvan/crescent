<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import appdevImage from '../../assets/development/appdevImage.png';
	import hero from '../../assets/development/hero.png';
	import image1 from '../../assets/development/gaiyo_image6.png';
	import image2 from '../../assets/development/contentAppThumb.jpg';
	import appDevSub1 from '../../assets/development/AppDevSub1.png';
	import appDevSub2 from '../../assets/development/AppDevSub2.png';
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
</script>

<div class="pageContent">
	<div class="hero">
		<h1>アプリケーション制作</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>概要</a>
		<a class="sidebar-item" href="#special" on:click={scrollToElement}>特徴</a>
		<a class="sidebar-item" href="#interactive" on:click={scrollToElement}>インタラクティブアプリケーション</a>
		<a class="sidebar-item" href="#consumer" on:click={scrollToElement}>コンシューマー向けアプリケーション</a>
		<a class="sidebar-item" href="#business" on:click={scrollToElement}>産業向けアプリケーション</a>
		<a class="sidebar-item" href="#shared" on:click={scrollToElement}>公開されている制作事例</a>
	</div>
<!-- 
	<div class="hero">
		<h1>アプリケーション制作</h1>
		
	</div> -->

	<!-- <div class="content-intro">
		<h2>産業向け受注案件事例</h2>
		<p>
			経験豊富なエンジニアが最新のスタジオ設備・機器を活用して個々のご注文に答え、用途に応じたユニークなインタラクティブアプリケーションを制作いたします。
		</p>
		<p>
			弊社の受注制作は担当責任制ですので、見積制作から納品まで、直接制作担当者が責任を持って作業を進めますので、綿密な打ち合わせの必要な前例のない開発案件でも安心してご発注いただけます。バージョンアップや機能追加に対してもできる限り同一担当者が対応いたします。
		</p>
		<p>多くの会社・大学・研究所のお客様からご信頼をいただきリピート発注をいただいております。</p>
		<a href={`/development/appdev/appdevsub`} use:link style="text-align: right;display: block;"
			>（公開可能な事例紹介はこちら）</a
		>
	</div> -->
	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
			<h2>概要</h2>
			<p class="explanation">経験豊富なエンジニアが最新のスタジオ設備・機器を活用して個々のご注文に答え、用途に応じたユニークなインタラクティブアプリケー ションを制作いたします。 弊社の受注制作は担当責任制ですので、見積制作から納品まで、直接制作担当者が責任を持って作業を進めますので、綿密な打ち合わせの 必要な前例のない開発案件でも安心してご発注いただけます。バージョンアップや機能追加に対してもできる限り同一担当者が対応いたし ます</p>
			<p class="explanation">多くの会社・大学・研究所のお客様からご信頼をいただきリピート発注をいただいております。</p></div>
		</section>
		<section class="special" id="special">
			<div class="container">
				<h2>特徴</h2>
				<p class="explanation">弊社の理念である"Link-ALL"に基づき、多様な技術・デバイ スを活用します。</p>
				<p class="explanation">「VICON」「4D Views」 「MREAL」等の弊社取扱い製品 だけでなく、GPS、ジャイロ、アナログ信号データ処理、 MIDI等、様々なデバイスやツール、言語を組み合わせてコ ンテンツ制作を行います。</p>
			<p class="explanation">お問い合わせはこちらから</p>
			<figure>
				<img src={image1} alt="Studio overview" />
			</figure>
			</div>
		</section>
		<section class="interactive" id="interactive">
			<div class="container">
				<h2>インタラクティブアプリケーション</h2>
				<ul>
					<li>
						XR(VR/MR/AR) アプリケーション
					</li>
					<li>
						自由視点ボリュメトリックアプリケーション
					</li>
					<li>
						CAVE(没入型多面立体視映像システム)用アプリケーション
					</li>
				</ul>
			</div>
		</section>
		<section class="consumer" id="consumer">
			<div class="container">
				<h2>コンシューマー向けアプリケーション</h2>
				<ul>
					<li>
						イベント・プレゼンテーション用コンテンツ
						<ul>
							<li>博物館等、展示施設のインフォメーション</li>
							<li>インタラクティブアートコンテンツ</li>
							<li>プレゼンテーション用コンテンツ</li>
							<li>街中やイベント会場、家庭にキャラクタや人物実写映像 を重置するARコンテンツ</li>
						</ul>
					</li>

					<li>
						マーケティングコンテンツ
						<ul>
							<li>カーコンフィギュレータ</li>
						</ul>
					</li>
				</ul>

				<figure>
					<img src={image2} alt="Studio overview" />
				</figure>
			</div>
			
		</section>
		<section class="business" id="business">
			<div class="container">
				<h2>産業向け受注案件事例</h2>
				<ul>
					<li>
						設計・デザインプロセスへの応用
						<ul>
							<li>試作・模型・モックアップ製作工程の省略化</li>
							<li>国内・海外を問わない遠隔地事業所間での共同開発用</li>
							<li>オフィスレイアウトを可視化する</li>
							<li>工場作業を効率化する</li>
							<li>遠隔治療や治療の効果向上</li>
							<li>高機能なEラーニング教材作成</li>
						</ul>
					</li>

					<li>開発事例
					<ul>
						<li>核研究施設の構造把握用CAVE</li>
						<li>重機(大型土木機械)のデザイン検討用CAVE</li>
						<li>屋内の気流・温度3Dデータを可視化するアプリケーション</li>
						<li>自動車整備作業をアシストするVR</li>
						<li>工場内荷物の積下ろしを可視化</li>
						<li>工場見学者向けの工場内可視化シミュレータ</li>
						<li>工場内安全教育教材（体感型危機回避シミュレータ）</li>
						<li>重機(大型土木機械)の操作シミュレータ</li>
						<li>手術支援MRシステム</li>
						<li>大学病院でのリハビリ支援コンテンツ</li>
						<li>大学でのCAVE訓練用コンテンツ</li>
					</ul></li>
				</ul>
			</div>
		</section>
		<section class="shared" id="shared">
			<div class="container">
				<h2>公開されている制作事例</h2>
				<div class="container">
					<h2>BeHere/1942</h2>
					<figure class="figure">
						<img src={appDevSub1} alt="Valkyrie banner" />
					</figure>
					<p class="explanation">
						この作品は、2022年にロサンゼルス・リトルトーキョー内のJANM(全米日系人博物館)が主催した、heBeHere
						/
						1942展で発表された藤幡正樹氏制作のARインスタレーション作品です。太平洋戦争勃発時に当時の日系アメリカ人強制収容について新たな視点を提供して話題になりました。この作品のAR化プログラム開発を弊社スタッフが担当いたしました。
					</p>
					<p class="explanation">
						※JAMN(Japanese American National
						Museum)：日系アメリカ人の歴史や文化を伝承、展示している博物館で、1992年に設立
					</p>
					<p class="explanation">
						※この作品はJANM Webサイトよりダウンロード・体験できます（詳細は<a
							href="https://www.janm.org/ja/exhibits/behere1942"
							target="_blank">こちら</a
						>）
					</p>
				</div>
		
				<div class="container">
					<h2>Brain100 Studio</h2>
					<figure class="figure">
						<img src={appDevSub2} alt="Valkyrie banner" />
					</figure>
					<p class="explanation">MIG株式会社様</p>
					<p class="explanation">
						MIG株式会社様が運営するアルツハイマー型認知症予防を目指すプログラムであるBrain100向けに、Meta
						Quest2を使った脳機能テスト向け空間ナビ測定VRアプリケーションを開発しました。
						MIG株式会社様独自の脳機能測定アルゴリズムをVRアプリケーションに組み込み、ユーザー様の脳機能を計測することが可能です。
					</p>
					<p class="explanation"><b>開発環境：</b>Unity3D, Meta Quest2</p>
					<p class="explanation">
						<b>関連ページ：</b>
					</p>
					<p>
						<a href="https://brain100studio.com" target="_blank" style="padding-left: 1rem;"
							>Brain100サイト</a
						>
					</p>
		
					<p class="explanation">
						<a
							href="https://www.youtube.com/watch?v=3ptagjaajjs"
							target="_blank"
							style="padding-left: 1rem;">関係者向け紹介ビデオ</a
						>
					</p>
				</div>
		
				<div class="container">
					<h2>AR「とびだす佐渡さん」</h2>
					<figure class="figure">
						<iframe
							width="80%"
							height="720"
							src="https://www.youtube.com/embed/rf7YGbVMaEY"
							title="チラシから佐渡さんが飛び出す！？ #shorts"
							frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
							allowfullscreen
							style="height: 33vw;"
						></iframe>
						<!-- <img src={appDevSub3} alt="Valkyrie banner" /> -->
					</figure>
					<p class="explanation">新日本フィルハーモニー交響楽団様</p>
					<p class="explanation">
						すみだ音楽大使に就任された世界的指揮者の佐渡裕様を、弊社サービス4DViewsで撮影させて頂き、8thWallと組み合わせて、コンサートにご来場いただいた方々がその場で御覧いただけるコンテンツを作成いたしました。
						ロゴから出現したり、等身大パネルから出現したり、ご要望に合わせて様々なパターンを作成しました。
					</p>
					<p class="explanation">
						<b>関連ページ：</b>
					</p>
					<p>
						<a href="https://www.njp.or.jp/news/5754/" target="_blank" style="padding-left: 1rem;"
							>NJP</a
						>
					</p>
				</div>
		
				<div class="container">
					<h2>NJP Virtual Club</h2>
					<figure class="figure">
						<iframe
							width="80%"
							height="720"
							src="https://www.youtube.com/embed/G9xkhQfcmTQ"
							title="NJP Virtual Club"
							frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
							allowfullscreen
							style="height: 33vw;"
						></iframe>
						<!-- <img src={appDevSub3} alt="Valkyrie banner" /> -->
					</figure>
					<p class="explanation">新日本フィルハーモニー交響楽団様</p>
					<p class="explanation">
						すみだ音楽大使に就任された世界的指揮者の佐渡裕様を、弊社サービス4DViewsで撮影させて頂き、8thWallと組み合わせて、コンサートにご来場いただいた方々がその場で御覧いただけるコンテンツを作成いたしました。
						ロゴから出現したり、等身大パネルから出現したり、ご要望に合わせて様々なパターンを作成しました。
					</p>
					<p class="explanation">
						<b>関連ページ：</b>
					</p>
					<p>
						<a href="https://www.njp.or.jp/news/6238/" target="_blank" style="padding-left: 1rem;"
							>NJP</a
						>
					</p>
					<p>
						<a
							href="https://www.meta.com/ja-jp/experiences/8624751027549929/"
							target="_blank"
							style="padding-left: 1rem;">Meta</a
						>
					</p>
					<p>
						<a
							href="https://www.viveport.com/apps/c127156b-5f02-4cf6-8a42-7309eeca2071"
							target="_blank"
							style="padding-left: 1rem;">Viveport</a
						>
					</p>
					<p>
						<a
							href="https://www.youtube.com/watch?v=820JW-aCOCI"
							target="_blank"
							style="padding-left: 1rem;"
							>NJP Virtual Club Launch Trailer
						</a>
					</p>
				</div>
			</div>
		</section>

</div>
</div>

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
	p,
	a {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}
	a {
		text-decoration: underline;
	}
	ul {
		margin-bottom: 2rem;
	}
	li {
		font-size: calc(14px + 0.390625vw);
		margin-left: 1rem;
		margin-bottom: 0.5rem;
	}

	.explanation,li {
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
