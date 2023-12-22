<script>
	import hero from '../../assets/logo.png';
	import { onMount } from 'svelte';

	onMount(() => {
		window.scrollTo(0, 0);
	});
</script>

<div class="pageContent">
	<div class="content">
		<div class="hero">
			<h1>映像企画・制作サポート</h1>
			<figure class="hero-image-container">
				<img class="hero-image" src={hero} alt="FullBodyLightCage" />
			</figure>
		</div>

		<div class="content-intro">
			<p>
				従来のメディア（2D映像、通常のWebコンテンツ）やCM・イベント・プロモーション企画も、
				最新の技術要素を付け加えるだけで斬新な映像効果が得られ、強いインパクトを与えることができます。
			</p>
		</div>

		<section class="overview" id="overview">
			<div class="container">
				<div>
					<p class="explanation">
						従来のメディア（2D映像、通常のWebコンテンツ）やCM・イベント・プロモーション企画も、
						最新の技術要素を付け加えるだけで斬新な映像効果が得られ、強いインパクトを与えることができます。
					</p>

					<ul>
						<li>モーションキャプチャを使用することで3DCGキャラクターが しなやかにに動きます</li>
						<li>4Dスタジオで収録することで、自由視点映像の表示が可能になります</li>
						<li>デジタル・ヒューマンの繊細な作り込みも最早身近になりました</li>
						<li>スマホを利用することでARの配信も普及してきました</li>
						<li>
							最新のプリビズ（プレビズ/アニマティック）技術を導入する
							ことでロケのリスク・コストを減らせます
						</li>
					</ul>
					<p>
						こうした新しい技術・素材を活用したコンテンツ制作を企画の段階からクレッセントがサポートします。
					</p>
					<details>
						<summary>サポート事例はこちら</summary>
						<div class="dynamic-image-text-flexbox"></div>
					</details>
					<p>
						最新の映像技術を使用した高機能な映像を制作するには、企画段階からのエンジニアの参画が必要です。自社スタジオにおいて日々開発・実験に取り組んでいる経験豊富な技術スタッフが、貴社企画、コンテンツ製作への先端技術の導入をサポートします。
					</p>
					<p>弊社の提供するサポート技術の特徴</p>
					<ul>
						<li>
							社内のモーションキャプチャースタジオ、4D
							スタジオを活用した開発環境と運用実績を背景にした熟練スタッフがサポートします。
						</li>
						<li>
							最新の技術要素を導入するに当たって、3Dグラフィクスソフトやミドルウェアの活用はもちろんのこと、必要に応じてプログラム言語レベルからで開発も行いますので、様々なご要望に対して柔軟な対応が可能となります。
						</li>
					</ul>
				</div>

				<div>
					<figure>
						<img src={hero} alt="Valkyrie banner" />
					</figure>
					<figure>
						<img src={hero} alt="Valkyrie banner" />
					</figure>
				</div>
			</div>
		</section>
	</div>
</div>

<style>
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
