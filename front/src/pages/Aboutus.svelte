<script>
	import hero from '../assets/aboutustop.jpg';

	import { onMount } from 'svelte';

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

<section class="pageContent">
	<div class="hero">
		<h1>会社情報</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#profile" on:click={scrollToElement}>会社概要</a>
		<a class="sidebar-item" href="#business" on:click={scrollToElement}>業容</a>
		<a class="sidebar-item" href="#linkAll" on:click={scrollToElement}>Link-ALL</a>
		<a class="sidebar-item" href="#access" on:click={scrollToElement}>アクセス</a>
	</div>

	<div class="content">
		<section class="profile" id="profile">
			<div class="container">
				<h2>会社概要</h2>
				<table class="tbl">
					<tbody
						><tr>
							<th>名称</th>
							<td>株式会社クレッセント</td>
							<th>英文名称</th>
							<td>Crescent,inc.</td>
						</tr>
						<tr>
							<th>代表者</th>
							<td colspan="3">代表取締役 小谷 創</td>
						</tr>
						<tr>
							<th>本社登記</th>
							<td>東京都江東区木場3-14-8</td>
							<th>所在地</th>
							<td
								>〒135-0042&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br
								/>東京都江東区木場3-14-8</td
							>
						</tr>
						<tr>
							<th>事業所</th>
							<td colspan="3">
								<dl id="office">
									<dt>4D STUDIO<br />(Digi-Cast第二スタジオ)<br />&nbsp;<br />&nbsp;</dt>
									<dd>〒135-0023<br />東京都江東区平野2-11-5<br />パシフィック第二門前仲町 2F</dd>
									<dt>鳥取エレクトロ・センター<br />&nbsp;<br />&nbsp;</dt>
									<dd>
										〒689-1112<br />鳥取市若葉台南7-1-1<br />鳥取県産業技術センター内　A-206号室
									</dd>
									<dt>京都スタジオ<br />&nbsp;<br />&nbsp;</dt>
									<dd>〒603-8202<br />京都府京都市北区紫竹東桃ノ本町８<br />細井ビル5階</dd>
								</dl>
							</td>
						</tr>
						<tr>
							<th>連絡先</th>
							<td colspan="3">
								<a href="tel:03-5875-9707">03-5875-9707</a> (TEL) / 9708 (FAX)
							</td>
						</tr>
						<tr>
							<th>E-mail</th>
							<td><a href="mailto:info@crescentinc.co.jp">info@crescentinc.co.jp</a></td>
							<th>Web</th>
							<td><a href="https://www.crescentinc.co.jp">www.crescentinc.co.jp</a></td>
						</tr>
						<tr>
							<th>会社設立</th>
							<td>平成11年3月</td>
							<th>資本金</th>
							<td>40,000,000円</td>
						</tr>
						<tr>
							<th>取引銀行</th>
							<td colspan="3">
								<dl id="bank">
									<dt>みずほ銀行</dt>
									<dd>銀座通支店</dd>
									<dt>阿波銀行</dt>
									<dd>東京支店</dd>
									<dt>きらぼし銀行</dt>
									<dd>日本橋支店</dd>
									<dt>りそな銀行</dt>
									<dd>室町支店</dd>
									<dt>商工中金</dt>
									<dd>本店営業部</dd>
									<dt>三菱東京UFJ銀行<br />&nbsp;</dt>
									<dd>日本橋支店<br />銀座支店</dd>
									<dt>三井住友銀行</dt>
									<dd>築地支店</dd>
									<dt>東京東信用金庫</dt>
									<dd>深川支店</dd>
								</dl>
							</td>
						</tr>
						<tr>
							<th>業務内容</th>
							<td colspan="3">
								<ul id="top_business">
									<li>画像処理ソフトウェア・ハードウェアの輸入、販売、サポート</li>
									<li>画像処理プログラムの開発販売、サポート</li>
									<li>画像機器の開発、販売、サポート</li>
									<li>画像コンテンツの開発・制作援助</li>
								</ul>
							</td>
						</tr>
						<tr>
							<th rowspan="2">子会社</th>
							<td colspan="3">
								<h5>新月映像股份有限公司<span>（100％子会社）</span></h5>
								<dl>
									<dt class="subsidiary">住所</dt>
									<dd class="subsidiary">台湾・高雄市鹽埕區真愛路1號11樓</dd>
									<dt class="subsidiary">業務</dt>
									<dd class="subsidiary">映像制作スタジオ</dd>
									<dt class="subsidiary">Web</dt>
									<dd class="subsidiary">
										<a href="https://www.digicast.com.tw">www.digicast.com.tw</a>
									</dd>
								</dl></td
							>
						</tr>
						<tr>
							<td colspan="3">
								<h5>Digicast ( UK ) Limited<span>（100％子会社）</span></h5>
								<dl>
									<dt class="subsidiary">住所<br />&nbsp;<br />&nbsp;</dt>
									<dd class="subsidiary">
										Centrum Business Centre<br />38 Queen Street<br />Glasgow, G1 3DX
									</dd>
									<dt class="subsidiary">業務<br />&nbsp;<br />&nbsp;<br />&nbsp;</dt>
									<dd class="subsidiary">
										<ul>
											<li>日本向けVRコンテンツのデザイン業務</li>
											<li>ESPER DESIGN社フォトグラメトリシステム<br />"LightCage"のサポート</li>
											<li>データ処理ソフト開発</li>
										</ul>
									</dd>
									<dt class="subsidiary">TEL</dt>
									<dd class="subsidiary">+44-141 548 8000</dd>
								</dl>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>

		<section class="business" id="business">
			<div class="container">
				<h2>業容</h2>
				<p class="explanation">
					最先端のイメージエンジニアリング技術を駆使した製品、サービスを提供することで、産業立国日本に貢献します！
				</p>
			</div>

			<div class="container">
				<h3>製品販売</h3>
				<p class="explanation">
					最先端のお気に入りテクノロジを世界中から集めて提供します。
					各製品には専門のエンジニアを付けて、お客様の利用用途やワークフローに最適な製品のありかたを模索します。開発元との太いパイプでお客様の製品へのご要望を的確に最短で伝え、より良い製品に進化させます。ご購入後、繁忙期や、人手不足の折など、ご要望に応じて機材の貸出、設置運用の援助などを行い、お客様の業務に支障がきたした際、柔軟に迅速に支援を行います。
				</p>
			</div>

			<div class="container">
				<h3>製品開発</h3>
				<p class="explanation">
					絶えず最先端のソリューション提供を目指します。そのソリューションフロー内で必要でありながら、世界に無い製品やプログラムは、迅速に自社内で開発します。今迄に高視野角、高解像度のHMDを世界に先駆けて販売し、その製品の最初のユーザはフランスの自動車会社でした。VICONカメラ専用の明るく歪みの少ない高FOVレンズを開発、ハリウッドや、ゲーム製作会社、航空宇宙開発会社等、世界中のお客様に1,000本以上出荷され、ご愛用頂いています。
				</p>
			</div>

			<div class="container">
				<h3>スタジオサービス</h3>
				<p class="explanation">
					クレッセントしか出来ないデジタルスタジオサービスを提供します。複数のテクノロジを最適化して融合させることで、今迄やりたくてもできなかったことや、手間暇掛かっていたことを一気に解決する仕組みを提供します。
					スタジオスペースと設置機材を有効利用し、タイムスライス撮影、フルグリーンバック撮影、産業VR用大規模テスト、近未来型多人数同時没入型ゲームテストサイトとしてもご利用頂けます。岡山児島にデータトラッキング工場を中塚興業様と共同運営し、ご購入頂いたモーションキャプチャ、Faceware等の後処理、3D点群データ処理サービスを行います。
				</p>
			</div>

			<div class="container">
				<h3>コンテンツ・アプリ開発</h3>
				<p class="explanation">
					腕利きを揃えたソフトウェアエンジニアチームが、想定しうる現存のデバイスやアプリケーションと、クレッセント取扱製品・サービスとを恙無く繋ぐ開発を日々行っています。
					故に、クレッセントの製品・サービスは、映像制作、VR開発、ロボティックス等、あらゆる用途で購入後即日、即戦力としてご利用頂くことが可能です。
					クレッセントデザイナチームと製品専門エンジニアが協業し、特殊用途の映像制作の受託も行います。群衆シミュレーションや、大規模景観制作を始め、様々なコンテンツ開発に対応致します。VICONをベースにエンジニアが開発のプログラムで、スウェーデンのデザイナグループ”FRONT”とコラボした”SKETCH
					FURNITURE"は、そのプロジェクトの秀逸性を認められ、提供プログラムとテクノロジを含むプロジェクト全体が英国国立ヴィクトリア・アンド・アルバート美術館に永久保存されています。
				</p>
			</div>
		</section>

		<section class="linkAll" id="linkAll">
			<div class="container">
				<h2>Link-ALL</h2>
				<p class="explanation">
					Link-ALLはクレッセントのステークホルダーへのプロトコールです。
					<br /><br />
					クレッセントの様々なリソースを「紡いで繋ぐ」ことで、 クレッセントが皆様にとってより便利で、より信頼できる、より楽しい、より拡張性のあるパートナーであり続けます。
				</p>
			</div>

			<div class="container">
				<h3>製品同士を「紡いで繋ぐ」</h3>
				<p class="explanation">
					一番お客様が望むところです。YAMAHA
					Cyber-MANUSの関節情報をVICONのリアルタイムストリームSDKから
					手軽に取得できたり、CityEngineや、Massiveを3Delightでレンダリングできたり、VICONのスレーブとしてbluefish444経由でFACEWAREやリファレンスビデオがキャプチャできたり…。
					4D
					Viewsがリアルタイムになって、VICONでトラッキングしたHEWDD-2のHMDから自由視点で自分がお気に入りのバンドのLIVEに入れたら最高です。
					それを実現するには、開発元との強い絆や、優秀なソフトウェアエンジニアの存在が必須です。
				</p>
			</div>

			<div class="container">
				<h3>サービスを「紡いで繋ぐ」</h3>
				<p class="explanation">
					アプリケーションは、今や必ずしも購入するのでなく、使用した量に応じて課金される従量制の仕組みに変わって来ました。では、購入してしまったお客様はどうするのか？
					クレッセントは、開発元との間にたってお客様の便宜を図るのは勿論、レンタルや、サービス受託での体制も整えて行きます。新規購入を検討されながら、
					使用頻度が高くない場合、或いは、利用が短期間で終わってしまう場合などは、
					投資判断が難しいケースも多くあります。こうした場合も、上記のスキームを提案することで、お客様の投資負担を減らして、効率的なプロジェクトを遂行頂けます。
				</p>
			</div>

			<div class="container">
				<h3>お客様同士を「紡いで繋ぐ」</h3>
				<p class="explanation">
					映画のディレクタも、メーカーのデザイナもアウトプットに対するパッションは同じです。製作会社のプロデューサも、
					生産技術のエンジニアも効率化や精度に対する要求は絶えません。使い手としてのユーザと、開発元のエンジニアは、絶えず情報交換を生の声でするべきです。
					アジアの製作会社やメーカーは、日本の会社様との協業や情報交換を望んでいます。
					クレッセントは、展示会や製品発表会、月次のセミナ等、あらゆる機会に積極的にステークホルダー皆様の交流を行える場を提供します。
					そこで皆様の知見を拡げて頂き、ビジネスチャンスを掴んで頂ければ幸甚です。
				</p>
			</div>
		</section>

		<section class="access" id="access">
			<div class="container">
				<h2>アクセス</h2>
			</div>

			<div class="container">
				<h3>本社</h3>
				<p class="explanation">郵便番号135-0042 東京都江東区木場3-14-8</p>
				<ul>
					<li>東京メトロ 「木場」 東口 徒歩13分</li>
					<li>都営大江戸線 「清澄白河」 A3出口 徒歩15分</li>
					<li>都営大江戸線 「門前仲町」 A5出口 徒歩15分</li>
				</ul>
				<iframe
					title="fromKiyosumi"
					src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d6481.852598490301!2d139.79726864472636!3d35.67881668543798!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x6018893dc19c7e69%3A0x6545c36eacca3d2b!2z5riF5r6E55m95rKz!3m2!1d35.6822525!2d139.79877779999998!4m5!1s0x6018891a91fc54ab%3A0x3bdc9a387b55e42!2z44CSMTM1LTAwNDIg5p2x5Lqs6YO95rGf5p2x5Yy65pyo5aC077yT5LiB55uu77yR77yU4oiS77yY!3m2!1d35.675502099999996!2d139.8045357!5e0!3m2!1sja!2sjp!4v1559564689511!5m2!1sja!2sjp"
					width="600"
					height="450"
					allow="fullscreen"
				></iframe>
				<iframe
					title="fromMonnaka"
					src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d3241.131364173925!2d139.79789615019442!3d35.67376728789272!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x60188912f795e52d%3A0xe16a21450a578ef0!2z6ZaA5YmN5Luy55S66aeF77yI5p2x5Lqs77yJ!3m2!1d35.6720326!2d139.7956907!4m5!1s0x6018891a91fc54ab%3A0x3bdc9a387b55e42!2z44CSMTM1LTAwNDIg5p2x5Lqs6YO95rGf5p2x5Yy65pyo5aC077yT5LiB55uu77yR77yU4oiS77yY!3m2!1d35.675502099999996!2d139.8045357!5e0!3m2!1sja!2sjp!4v1559564786433!5m2!1sja!2sjp"
					width="600"
					height="450"
					allow="fullscreen"
				></iframe>
				<iframe
					title="fromKiba"
					src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d6482.369516977799!2d139.80121249472552!3d35.672452436139!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x601889068f61bc53%3A0x3994f044202c2b20!2z5pyo5aC06aeF!3m2!1d35.6693855!2d139.8068585!4m5!1s0x6018891a91fc54ab%3A0x3bdc9a387b55e42!2z44CSMTM1LTAwNDIg5p2x5Lqs6YO95rGf5p2x5Yy65pyo5aC077yT5LiB55uu77yR77yU4oiS77yY!3m2!1d35.675502099999996!2d139.8045357!5e0!3m2!1sja!2sjp!4v1559564845244!5m2!1sja!2sjp"
					width="600"
					height="450"
					allow="fullscreen"
				></iframe>
			</div>
		</section>
	</div>
</section>

<style>
	iframe {
		border: 2px solid #0b345b;
	}
	ul#top_business li {
		text-align: left;
		margin-left: 1.5rem;
	}
	ul {
		list-style: none; /* Remove default bullets */
	}

	ul li::before {
		position: absolute;
		top: 0;
		margin: 4px 0 0 -24px;
		vertical-align: middle;
		display: inline-block;
		width: 1rem;
		height: 1rem;
		background: #0b345b;
		content: '';
	}
	ul li {
		margin-bottom: 5px;
		margin-left: 1rem;
		position: relative;
	}

	dl#office dd {
		text-align: left;
		padding-left: 10%;
		padding-right: 5%;
	}
	dd {
		margin: 0 0 5px 12em;
	}
	dl#office dt {
		text-align: left;
		width: 12em;
	}
	dt {
		width: 9em;
		float: left;
		clear: both;
		border-right: 1px solid #c4ccd2;
		padding: 0 1em;
	}
	dl dt.subsidiary {
		width: 50px;
		text-align: right;
		padding-left: 0px;
	}
	dl dd.subsidiary {
		text-align: left;
		padding-left: 0px;
		margin-left: 80px;
	}
	table.tbl {
		margin-bottom: 20px;
		table-layout: fixed;
		width: 100%;
		word-wrap: break-word;
		font-size: 90%;
	}
	table {
		border-collapse: collapse;
	}
	table {
		-webkit-text-size-adjust: 100%;
	}
	.tbl td {
		text-align: center;
	}
	.tbl th,
	.tbl td {
		padding: 10px;
	}
	table tr th {
		background: #e0e3e7;
	}
	table th {
		text-align: center;
	}
	table th,
	table td {
		border: solid 1px #c4ccd2;
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
	.pageContent {
		padding: 2rem 8rem;
		/* background-color: #efefef; */
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

	.card article figure a img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
		display: block;
		max-height: 160px;
		object-fit: cover;
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

	section:not(.pageContent) {
		width: 100%;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 0;
		border-top: 2px solid black;
		padding-bottom: 5rem;
	}

	.container {
		display: flex;
		gap: 2rem;
		padding: 2rem 0;
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

	@media screen and (max-width: 500px) {
		dl#office dd {
			text-align: left;
			padding-left: 0;
			padding-right: 0;
		}

		dd {
			margin: 0 0 5px 0em;
		}

		dl#office dt {
			text-align: left;
			width: 6em;
		}
		dt {
			padding: 0;
		}
	}
</style>
