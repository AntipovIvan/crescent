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

	<div class="content-intro">
		<p>
			最新の映像技術を使用した高機能な映像を制作するには、企画段階から
			のエンジニアの参画が不可欠です。
		</p>
		<p>
			自社スタジオにおいて日々開発・実験に取り組んでいる経験豊富な技術
			スタッフが貴社企画のコンテンツ製作への先端技術の導入をサポートします。
		</p>
	</div>

	<section class="cameraContent">
		<div class="leftContent">
			<ul>
				<li>
					弊社の提供するサポート技術の特徴
					<ul>
						<li>
							社内のモーションキャプチャースタジオ、4D スタジオを
							活用した開発環境と運用実績を背景にした熟練スタッフがサ ポートします。
						</li>
						<li>
							最新の技術要素を導入するに当たって、3Dグラフィクスソ
							フトやミドルウェアの活用はもちろんのこと、必要に応じて
							C#などのプログラム言語レベルでの開発も行いますので、
							様々なご要望に対して柔軟な対応が可能となります。
						</li>
					</ul>
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
		/* max-width: 65rem; */
		text-align: center;
		font-size: calc(16px + 0.390625vw);
		margin: 0 auto;
		padding: 10rem 0 5rem 0;
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
