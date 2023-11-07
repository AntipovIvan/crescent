<script>
	import urlSlug from 'url-slug';

	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import NotFound from '../../NotFound.svelte';
	import Device from 'svelte-device-info';
	import hero from '../../../assets/products/vicon/hero.png';

	import valkyrie from '../../../assets/valkyrie.jpg';
</script>

<div class="content">
	<div class="hero">
		<div class={Device.isPhone ? 'heroTextMobile' : 'heroText'}>
			<p>V I C O N</p>
			<!-- <button class="icon"><span>製品ページ</span></button> -->
		</div>
	</div>

	<div class="content-intro">
		<p>Viconは、業界最高水準の光学反射式モーションキャプチャシステムです。</p>
		<p>
			製品のバリエーションは圧倒的な価格訴求力のあるカメラから、業界最高分解能を持つ1600万画素のカメラまで、お客様の用途と予算に応じたシステム提案ができる幅広いラインナップをご用意しています。
		</p>
	</div>
	<section>
		<h1>Camera</h1>
		<div class="container">
			<div>
				<h2>VALKYRIE</h2>
				<p class="explanation">
					Viconは、業界最高水準の光学反射式モーションキャプチャシステムです。
				</p>
				<p class="explanation">
					製品のバリエーションは圧倒的な価格訴求力のあるカメラから、業界最高分解能を持つ1600万画素のカメラまで、お客様の用途と予算に応じたシステム提案ができる幅広いラインナップをご用意しています。
				</p>
				<button class="more">
					<span class="viewMore">View more</span>
					<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
						<path
							d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
						/>
					</svg>
				</button>
			</div>
			<figure>
				<img src={valkyrie} alt="Valkyrie banner" />
			</figure>
		</div>
	</section>
</div>

<style>
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
		font-size: calc(16px + 0.390625vw);
	}
	h1 {
		font-size: calc(32px + 0.390625vw);
	}
	h2 {
		font-size: calc(28px + 0.390625vw);
		margin: 0 0 2rem 0;
	}
	.content {
		background: #eeeeee;
	}
	section {
		width: 85%;
		margin: 0 auto;
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

	button {
		border: none;
		display: inline-block;
		padding: 15px 30px;
		color: white;
		background-color: #47474752;
		text-align: center;
		cursor: pointer;
		border-radius: 0.5em;
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		display: flex;
	}

	button:hover {
		background-color: #555;
		color: white;
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
		section div {
			flex-direction: column;
		}
	}
</style>
