<script>
	import fourdviews from '../assets/4dviews.png';
</script>

<div class="hero-text">
	<figure>
		<img src={fourdviews} class="newsLogo" alt="4dviews" width="300" height="100" />
	</figure>
	<p>カメラの解像度が1200万画素にアップしたHOLOSYS+(プラス)販売開始！</p>
	<button class="icon"><span>製品ページ</span></button>
</div>

<style>
	.hero-text {
		text-align: center;
		position: absolute;
		bottom: 15%;
		left: 10%;
		transform: translate(-10%, -15%);
		color: white;
		font-size: calc(12px + 0.390625vw);
	}

	.hero-text button {
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

	.hero-text button:hover {
		background-color: #555;
		color: white;
	}

	.hero-text p {
		width: 530px;
		text-align: left;
		font-size: calc(18px + 0.390625vw);
		text-shadow: 2px 3px 3px rgba(0, 0, 0, 0.4);
		font-weight: 600;
	}

	.hero-text figure {
		margin: 0;
		padding: 0;
		text-align: left;
	}

	@media only screen and (max-width: 600px) {
		/* HERO */
		.hero-text p {
			width: auto;
		}
		.hero-text {
			width: 80%;
			top: 50%;
			left: 50%;
			bottom: unset;
			transform: translate(-50%, -50%);
		}
	}
</style>
