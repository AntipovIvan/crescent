<script>
	import fourdviews from '../assets/4dviews.png';
	import hero from '../assets/hero.png';
	import valkyrie from '../assets/valkyrie.jpg';
	import digicast from '../assets/digicast.png';
	import Device from 'svelte-device-info';
	import Carousel from 'svelte-carousel';
	import { link } from 'svelte-spa-router';

	let carousel; // for calling methods of the carousel instance

	const showPrevPage = () => {
		carousel.goToPrev();
	};

	const showNextPage = () => {
		carousel.goToNext();
	};
</script>

<Carousel dots={false} bind:this={carousel}
	><div slot="prev" on:click={showPrevPage} class="custom-arrow custom-arrow-prev">
		<svg width="64" height="64" viewBox="0 0 64 64" fill="none">
			<path
				d="M29.377 17.2959L20.7544 25.9185L29.377 34.541"
				stroke="white"
				stroke-width="2"
				stroke-linejoin="round"
			/>
			<circle cx="26" cy="26" r="25" stroke="white" stroke-width="2" />
		</svg>
	</div>
	<div class="heroContainer">
		<img src={hero} class="heroImage" alt="4dviews" width="400" height="100" />
		<div class="onimage">
			<figure>
				<img src={fourdviews} class="newsLogo" alt="4dviews" width="400" height="125" />
			</figure>
			<p>カメラの解像度が1200万画素にアップしたHOLOSYS+(プラス)販売開始！</p>
			<div class="heroButtonContainer">
				<a href={`/product/4dviews`} use:link>
					<button class="button"><span>製品ページ</span></button>
				</a>
				<a href={`/services/4dstudio`} use:link>
					<button class="button">
						<span>スタジオページ</span><img
							class="icon"
							src={digicast}
							alt="digicast logo"
						/></button
					></a
				>
			</div>
		</div>
	</div>
	<div class="heroContainer">
		<img src={valkyrie} class="heroImage" alt="4dviews" width="400" height="100" />
		<div class="onimage">
			<!-- <figure>
				<img src={fourdviews} class="newsLogo" alt="4dviews" width="400" height="125" />
			</figure> -->
			<!-- <p>カメラの解像度が1200万画素にアップしたHOLOSYS+(プラス)販売開始！</p>
			<div class="heroButtonContainer">
				<button class="icon"><span>製品ページ</span></button>
				<button class="icon"><span>スタジオページ</span> </button>
			</div> -->
		</div>
	</div>
	<!-- <div>3</div> -->
	<div slot="next" on:click={showNextPage} class="custom-arrow custom-arrow-next">
		<svg width="64" height="64" viewBox="0 0 64 64" fill="none">
			<path
				d="M26.623 40.7041L35.2456 32.0815L26.623 23.459"
				stroke="white"
				stroke-width="2"
				stroke-linejoin="round"
			/>
			<circle cx="32" cy="32" r="25" stroke="white" stroke-width="2" />
		</svg>
	</div>
</Carousel>

<style>
	.heroContainer {
		height: var(--hero-height);
	}
	.newsLogo {
		max-width: 80vw;
	}
	.icon {
		width: 55px;
	}
	.custom-arrow {
		position: absolute;
		cursor: pointer;
	}
	.custom-arrow-prev {
		left: 1%;
		z-index: 2;
		top: 50%;
	}
	.custom-arrow-next {
		right: 1%;
		top: 50%;
	}
	.heroContainer {
		position: relative;
	}
	.heroImage {
		width: 100%;
		object-fit: cover;
		filter: brightness(85%);
		/* margin-left: 7rem; */
		position: absolute;
		height: 100%;
	}
	.heroButtonContainer {
		display: flex;
		flex-direction: row;
		gap: 2rem;
	}

	.button span {
		font-size: calc(11px + 0.390625vw);
	}

	button {
		border: none;
		padding: 15px 30px;
		color: white;
		background-color: #47474752;
		text-align: center;
		cursor: pointer;
		border-radius: 0.5em;
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	button:hover {
		background-color: #555;
		color: white;
	}

	p {
		text-align: left;
		font-size: calc(24px + 0.390625vw);
		text-shadow: 2px 3px 3px rgba(0, 0, 0, 0.4);
		font-weight: 600;
	}

	figure {
		margin: 0;
		padding: 0;
		text-align: left;
	}

	.onimage {
		text-align: center;
		position: absolute;
		width: 40%;
		top: 60%;
		left: 30%;
		transform: translate(-30%, -60%);
		color: white;
		font-size: calc(12px + 0.390625vw);
		display: flex;
		flex-direction: column;
		gap: 4rem;
	}

	@media only screen and (max-width: 600px) {
		/* HERO */

		.onimage p {
			width: auto;
		}
	}

	@media only screen and (max-width: 1150px) {
		.newsLogo {
			max-width: 35vw;
			max-height: 10vw;
		}
		.onimage {
			gap: 1rem;
			width: 85%;
			left: 35%;
		}
		.button {
			padding: 5px 15px;
		}
		.heroImage {
			margin-left: 0;
		}
		p {
			font-size: calc(18px + 0.390625vw);
		}
	}
</style>
