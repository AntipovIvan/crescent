<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import holosys from '../../assets/products/4dviews/holosys.jpg';
	import fourdfx from '../../assets/products/4dviews/4dfx.jpg';
	import cert from '../../assets/hero.png';
	import { onMount } from 'svelte';

	onMount(() => {
		window.scrollTo(0, 0);
	});
</script>

<div class="content">
	<div class="hero">
		<div class={Device.isPhone ? 'heroTextMobile' : 'heroText'}>
			<p>4DVIEWS</p>
		</div>
	</div>

	<div class="content-intro">
		<p>
			HOLOSYS
			は、人を撮影し、そこから360°バーチャル3Dオブジェクトを生成し生の人間の動きをそのままARやMR空間に表示させることができます。HOLOSYS
			3.0の高評価を得て、より高速処理、高効率化され、信頼度が増したHOLOSYS 3.5をリリースしました。
		</p>
	</div>

	<section class="captureSystem">
		<h1>Capture System</h1>
		<div class="container">
			<div>
				<h2>HOLOSYS</h2>
				<p class="explanation">
					HOLOSYSは、人を撮影し、そこから360°バーチャル3Dオブジェクトを生成し生の人間の動きをそのままARやMR空間に表示させることができます。HOLOSYS
					3.0の高評価を得て、より高速処理、高効率化され、信頼度が増したHOLOSYS
					3.5をリリースしました。
				</p>
				<a class="more" href={`/product/4dviews/capture/holosys`} use:link>
					<button class="more">
						<span class="viewMore">VIEW MORE</span>
						<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
							<circle cx="12" cy="12" r="12" fill="#313132" />
							<path
								d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
								fill="white"
							/>
						</svg>
					</button></a
				>
			</div>
			<figure>
				<img src={holosys} alt="Holosys banner" />
			</figure>
		</div>
	</section>

	<section class="softwareContent">
		<h1>Software</h1>
		<div class="container">
			<div>
				<h2>4DFX</h2>
				<p class="explanation">
					4Dfxは、4Dviews社が開発した、ボリュメトリックビデオ加工ソフトウェアです。HOLOSYSでキャプチャしたデータの色補正や形状補正、メッシュリダクション、トランジションなど様々な加工を施すことができます。また、各種ファイル形式への書き出しやテクスチャサイズの調整なども柔軟に行うことができます。
				</p>
				<a class="more" href={`/product/4dviews/software/4dfx`} use:link>
					<button class="more">
						<span class="viewMore">VIEW MORE</span>
						<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
							<circle cx="12" cy="12" r="12" fill="#313132" />
							<path
								d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
								fill="white"
							/>
						</svg>
					</button></a
				>
			</div>
			<figure>
				<img src={fourdfx} alt="4DFX banner" />
			</figure>
		</div>
	</section>

	<section class="relatedLinks">
		<h2>関連リンク</h2>
		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			<li class="card">
				<article>
					<figure>
						<a href={'/'} use:link>
							<img src={cert} alt="Certificate" width="400" height="200" />
						</a>
						<figcaption>
							<p>4D STUDIO</p>
							<span class="overflowed-text"
								>4Dviews社 HOLOSYSを使用したボリュメトリックキャプチャスタジオ</span
							>
						</figcaption>
					</figure>
				</article>
			</li>
		</ul>
	</section>
</div>

<style>
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
			url(/src/assets/products/4dviews/4dviews.jpg);
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
