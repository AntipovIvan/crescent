<script>
	import urlSlug from 'url-slug';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import NotFound from '../NotFound.svelte';
	import Device from 'svelte-device-info';
	import appdevImage from '../../assets/development/appdevimage.jpg';
</script>

<div class="content">
	<!-- <div class="hero">
		<div class={Device.isPhone ? 'heroTextMobile' : 'heroText'}>
			<p>V I C O N</p>
		</div>
	</div> -->

	<!-- <div class="content-intro">
		<p>Viconは、業界最高水準の光学反射式モーションキャプチャシステムです。</p>
		<p>
			製品のバリエーションは圧倒的な価格訴求力のあるカメラから、業界最高分解能を持つ1600万画素のカメラまで、お客様の用途と予算に応じたシステム提案ができる幅広いラインナップをご用意しています。
		</p>
	</div> -->

	<section class="cameraContent">
		<div class="leftContent">
			<ul>
				<li>
					産業向け受注案件事例
					<p>
						経験豊富なエンジニアが最新のスタジオ機器を活用して個々のご注文に答え、
						用途に応じたユニークなインタラクティブアプリケーションを制作いたします。
						(公開可能な事例紹介はこちら)
					</p>
				</li>
				<li>
					インタラクティブアプリケーションのタイプ
					<ul>
						<li>XR(VR/MR/AR)アプリケーション</li>
						<li>自由視点ボリュメトリックアプリケーション</li>
						<li>CAVE(没入型多面立体視映像システム)用アプリケーション</li>
					</ul>
				</li>
				<li>
					コンシューマ向け受注案件事例
					<ul>
						<li>
							イベント・プレゼンテーション用コンテンツ
							<p>博物館等、展示施設のインフォメーション</p>
							<p>インタラクティブアートコンテンツ</p>
							<p>プレゼンテーション用コンテンツ</p>
							<p>街中にキャラクタや人物実写映像を重畳するARコンテンツ</p>
						</li>
						<li>
							マーケティングコンテンツ
							<p>カーコンフィギュレータ</p>
							<p>ECアパレルサイト用自由視点動画</p>
						</li>
					</ul>
				</li>
				<li>
					産業向け受注案件事例
					<ul>
						<li>
							・設計・デザイン検討への応用
							<ul>
								<li>
									(目的)
									<p>試作・模型・モックアップ製作工程の省略化</p>
									<p>国内・海外を問わない遠隔地事業所間での共同開発用</p>
									<p>オフィスレイアウトを可視化</p>
									<p>工場作業を効率化する</p>
									<p>遠隔治療や治療効果の向上</p>
									<p>高機能なEラーニング教材作成</p>
								</li>

								<li>
									(具体的開発事例)
									<p>核研究施設の構造把握用CAVE</p>
									<p>重機(大型土木機械)のデザイン検討用CAVE</p>
									<p>屋内の気流・温度3Dデータを可視化するアプリケーション</p>
									<p>自動車整備作業をアシストするVR</p>
									<p>工場内荷物の積下ろしを可視化</p>
									<p>工場見学者向けの工場内可視化シミュレータ</p>
									<p>工場内安全教育教材(体感型危機回避シミュレータ)</p>
									<p>重機(大型土木機械)の操作シミュレータ</p>
									<p>手術支援MRシステム</p>
									<p>大学病院でのリハビリ支援コンテンツ</p>
									<p>大学でのCAVE訓練用コンテンツ</p>
								</li>
							</ul>
						</li>
					</ul>
				</li>
				<li>
					使用する技術・デバイスについて
					<p>
						弊社の理念である"Link-ALL"に基づき、多様な技術・デバイスを活用します。 「VICON」「4D
						Views」「MREAL」等の弊社取扱い製品だけでなく、GPS、ジャイロ、アナログ信号
						データ処理、MIDI等、様々なデバイスやツールを組み合わせてコンテンツ制作を行います。
					</p>
					<p>お問い合わせはこちらから</p>
				</li>
			</ul>
		</div>

		<div class="rightContent">
			<figure>
				<img src={appdevImage} alt="appdevImage" />
			</figure>
		</div>
	</section>
</div>

<style>
	ul {
		margin: 0;
		padding: 0 3rem;
	}
	p {
		padding: 0 1rem;
	}
	li {
		font-size: calc(14px + 0.390625vw);
	}
	.leftContent ul li {
		padding-bottom: 1rem;
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
	/* "More" button (like "View more") */
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
	p {
		margin: 0;
	}
	.explanation {
		font-size: calc(14px + 0.390625vw);
	}
	h1 {
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}
	h2 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
	}
	.content {
		background: #eeeeee;
	}

	section {
		width: 85%;
		margin: 0 auto;
		display: flex;
		flex-direction: row;
		gap: 2rem;
		padding: 3rem 0;
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
		justify-content: space-between;
	}
	section div figure {
		flex: 50%;
	}
	section div figure img {
		width: 100%;
	}
	.content-intro {
		max-width: 65rem;
		text-align: left;
		font-size: calc(16px + 0.390625vw);
		margin: 0 auto;
		padding: 10rem 0;
	}

	.hero {
		background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
			url(/src/assets/products/vicon/hero.png);
		height: 88vh;
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		position: relative;
	}
	.heroText {
		text-align: center;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		display: table;
		color: white;
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
		.container {
			flex-direction: column;
		}
		.content-intro {
			padding: 5rem;
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
