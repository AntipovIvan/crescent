<script>
	import fourdviews from '../assets/4dviews.png';
	import Device from 'svelte-device-info';
</script>

<div class={Device.isPhone ? 'heroTextMobile' : 'heroText'}>
	<figure>
		<img src={fourdviews} class="newsLogo" alt="4dviews" width="300" height="100" />
	</figure>
	<p>カメラの解像度が1200万画素にアップしたHOLOSYS+(プラス)販売開始！</p>
	<div class="heroButtonContainer">
		<button class="icon"><span>製品ページ</span></button>
		<button class="icon"><span>スタジオページ</span> </button>
	</div>
</div>

<style>
	.heroButtonContainer {
		display: flex;
		flex-direction: row;
		gap: 2rem;
	}

	.icon span {
		font-size: calc(12px + 0.390625vw);
	}
	.heroText {
		text-align: center;
		position: absolute;
		bottom: 15%;
		left: 10%;
		transform: translate(-10%, -15%);
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

	p {
		width: 530px;
		text-align: left;
		font-size: calc(18px + 0.390625vw);
		text-shadow: 2px 3px 3px rgba(0, 0, 0, 0.4);
		font-weight: 600;
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

	@media only screen and (max-width: 1150px) {
		header {
			padding: 0 2rem;
		}
	}
</style>
