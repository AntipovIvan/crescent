<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import appdevImage from '../../assets/development/appdevImage.png';
	import { onMount } from 'svelte';

	onMount(() => {
		window.scrollTo(0, 0);
	});
</script>

<div class="content">
	<div class="hero">
		<h1>アプリケーション制作</h1>
		<!-- <button class="icon"><span>製品ページ</span></button> -->
	</div>

	<div class="content-intro">
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
	</div>

	<section class="cameraContent">
		<div class="container">
			<div>
				<h2>インタラクティブアプリケーション</h2>
				<ul>
					<li>XR(VR/MR/AR)アプリケーション</li>
					<li>自由視点ボリュメトリックアプリケーション</li>
					<li>CAVE(没⼊型多⾯⽴体視映像システム)用アプリケーション</li>
				</ul>

				<h2>コンシューマ向け受注案件事例</h2>
				<ul>
					<li>
						イベント・プレゼンテーション用コンテンツ
						<ul>
							<li>博物館等、展示施設のインフォメーション</li>
							<li>インタラクティブアートコンテンツ</li>
							<li>プレゼンテーション用コンテンツ</li>
							<li>街中やイベント会場、家庭にキャラクタや人物実写映像を重畳するARコンテンツ</li>
						</ul>
					</li>
					<li>
						マーケティングコンテンツ
						<ul>
							<li>カーコンフィギュレータ</li>
						</ul>
					</li>
				</ul>

				<h2>産業向け受注案件事例</h2>
				<ul>
					<li>
						設計・デザイン検討への応用
						<p>(目的)</p>
						<ul>
							<li>試作・模型・モックアップ製作工程の省略化</li>
							<li>国内・海外を問わない遠隔地事業所間での共同開発用</li>
							<li>オフィスレイアウトを可視化する</li>
							<li>工場作業を効率化する</li>
							<li>遠隔治療や治療の効果向上</li>
							<li>高機能なEラーニング教材作成</li>
						</ul>
					</li>

					<p>(具体的開発事例)</p>
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
					</ul>
				</ul>

				<h2>使用する技術・デバイスについて</h2>
				<p>弊社の理念である"Link-ALL"に基づき、多様な技術・デバイスを活用します。</p>
				<p>
					「VICON」「4D
					Views」「MREAL」等の弊社取扱い製品だけでなく、GPS、ジャイロ、アナログ信号データ処理、MIDI等、様々なデバイスやツール、言語を組み合わせてコンテンツ制作を行います。
				</p>
				<a href={`/contact/`} use:link>お問い合わせはこちらから</a>
			</div>
			<figure>
				<img src={appdevImage} alt="Valkyrie banner" />
			</figure>
		</div>
	</section>
</div>

<style>
	.linkTitle {
		font-weight: bold;
		font-size: calc(10px + 0.390625vw);
	}
	ul {
		margin: 0;
		padding: 0;
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
		min-height: 6rem;
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

	.noImageContainer {
		display: flex;
		flex-direction: row;
		gap: 2rem;
	}
	/* "More" button (like "VIEW MORE") */
	.more {
		display: flex;
		align-items: center;
		gap: 1rem;
		background-color: unset;
		border: none;
		cursor: pointer;
		color: var(--headers-color);
		width: 13rem;
		padding: 0;
		margin: 2rem 0 0 0;
		justify-content: end;
		align-self: self-end;
	}
	.viewMore {
		font-size: calc(12px + 0.390625vw);
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
	h1 {
		font-size: calc(36px + 0.390625vw);
		font-weight: 600;
		padding: 4rem 0 0 0;
	}
	h2 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
		padding: 0;
	}
	.content {
		background: #eeeeee;
		padding: 2rem 8rem;
	}

	section {
		width: 85%;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 2rem;
	}

	.softwareContent,
	.hardwareContent {
		margin-top: 5rem;
	}
	.container {
		background: white;
		display: flex;
		gap: 5rem;
		padding: 3rem 3rem;
		flex-direction: row;
		border-radius: 14px;
		-webkit-box-shadow: 0px 2px 4px 2px rgba(173, 173, 173, 0.5);
		-moz-box-shadow: 0px 2px 4px 2px rgba(173, 173, 173, 0.5);
		box-shadow: 0px 2px 4px 2px rgba(173, 173, 173, 0.5);
	}
	section div div {
		display: flex;
		flex-direction: column;
		flex: 50%;
		justify-content: unset;
	}
	section div figure {
		flex: 50%;
	}
	section div figure img {
		width: 100%;
	}
	.content-intro {
		width: 85%;
		text-align: left;
		font-size: calc(16px + 0.390625vw);
		margin: 0 auto;
		padding: 4rem 0;
	}

	.hero {
		position: relative;
		margin-bottom: 3rem;
	}
	.heroText {
		text-align: center;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		display: table;
		color: black;
		font-size: calc(12px + 0.390625vw);
	}

	.hero div p {
		/* width: 530px; */
		text-align: left;
		font-size: calc(64px + 0.390625vw);
		text-shadow: 2px 3px 3px rgba(0, 0, 0, 0.4);
		font-weight: 600;
		margin: 0;
	}

	figure {
		margin: 0;
		padding: 0;
		text-align: left;
	}

	.heroTextMobile {
		text-align: center;
		position: absolute;
		width: 80%;
		top: 50%;
		left: 50%;
		bottom: unset;
		transform: translate(-50%, -50%);
		color: white;
		font-size: calc(12px + 0.390625vw);
	}

	@media only screen and (max-width: 600px) {
		/* HERO */
		.heroTextMobile p {
			width: auto;
		}
	}

	@media (max-width: 800px) {
		section {
			width: 100%;
		}
		h1 {
			font-size: calc(28px + 0.390625vw);
			padding: 1rem 0 0 0;
		}
		h2 {
			font-size: calc(24px + 0.390625vw);
			padding: 1rem 0 2rem 0;
		}
		.container {
			flex-direction: column;
			padding: 3rem 1rem;
		}
		.content {
			padding: 2rem 2rem;
		}
		.content-intro {
			padding: 0rem;
			max-width: 86vw;
		}
		.cardList {
			grid-template-columns: repeat(auto-fill, 15.5rem);
			margin: 0 auto;
		}
		.noImageContainer {
			flex-direction: column;
		}
	}
</style>
