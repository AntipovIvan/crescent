<script>
	import { link } from 'svelte-spa-router';
	import active from 'svelte-spa-router/active';
	import { fly } from 'svelte/transition';
	import logo from '../assets/logo.png';
	import Device from 'svelte-device-info';

	let sidebar_show = false;

	// console.log('this device is ' + (Device.isMobile ? '' : 'not') + ' mobile');

	// switch (true) {
	// 	case Device.isPhone:
	// 		console.log('this device is a smartphone');
	// 		break;
	// 	case Device.isTablet:
	// 		console.log('this device is a tablet');
	// 		break;
	// 	default:
	// 		console.log('this device is neither a smartphone nor a tablet');
	// }
</script>

{#if Device.isPhone || Device.isTablet}
	<header class="mobileHeader">
		<button class:sidebar_show class="hamburger" on:click={() => (sidebar_show = !sidebar_show)}>
			{#if sidebar_show}
				<svg width="32" height="24">
					<line id="topShow" x1="0" y1="2" x2="32" y2="2" />
					<line id="middleShow" x1="0" y1="12" x2="24" y2="12" />
					<line id="bottomShow" x1="0" y1="22" x2="32" y2="22" />
				</svg>
			{:else}
				<svg width="32" height="24">
					<line id="top" x1="0" y1="2" x2="32" y2="2" />
					<line id="middle" x1="0" y1="12" x2="24" y2="12" />
					<line id="bottom" x1="0" y1="22" x2="32" y2="22" />
				</svg>
			{/if}
		</button>

		<figure class="logoContainer">
			<a href={`/`} use:link
				><img src={logo} class="logo" alt="Crescent" width="170" height="80" /></a
			>
		</figure>

		{#if sidebar_show}
			<nav class="mobile" transition:fly={{ x: 250, opacity: 1 }}>
				<ul class="mobileNavi">
					<li>
						<button
							on:click={() => {
								sidebar_show = false;
							}}><a href={`/products/`} use:link>製品販売</a></button
						>
					</li>
					<li>
						<button
							on:click={() => {
								sidebar_show = false;
							}}><a href={`/services/`} use:link>スタジオサービス</a></button
						>
					</li>
					<li>
						<button
							on:click={() => {
								sidebar_show = false;
							}}><a href={`/development/`} use:link>コンテンツ開発</a></button
						>
					</li>
					<li>
						<button
							on:click={() => {
								sidebar_show = false;
							}}><a href={`/aboutus/`} use:link>会社情報</a></button
						>
					</li>
					<li>
						<button
							on:click={() => {
								sidebar_show = false;
							}}><a href={`/contact/`} use:link>お問い合わせ</a></button
						>
					</li>
				</ul>
			</nav>
		{/if}
	</header>
{:else}
	<header>
		<figure>
			<a href={`/`} use:link
				><img src={logo} class="logo" alt="Crescent" width="170" height="80" /></a
			>
		</figure>
		<nav class="pc">
			<ul class="pcNavi">
				<li><a href={`/products/`} use:link use:active>製品販売</a></li>
				<li><a href={`/services/`} use:link use:active>スタジオサービス</a></li>
				<li><a href={`/development/`} use:link use:active>コンテンツ開発</a></li>
				<li><a href={`/aboutus/`} use:link use:active>会社情報</a></li>
				<li><a href={`/contact/`} use:link use:active>お問い合わせ</a></li>
			</ul>
		</nav>
	</header>
{/if}

<style>
	.mobileHeader {
		padding: 1rem 1rem;
	}
	.logoContainer {
		z-index: 1;
		width: 50%;
		text-align: center;
		cursor: pointer;
		border-radius: 0.5em;
		margin: 0;
	}
	.pc {
		height: 100%;
	}
	.pcNavi {
		display: flex;
		font-size: calc(12px + 0.390625vw);
		list-style-type: none;
		padding: 0;
		margin: 0;
	}
	.pcNavi li {
		border-left: 2px solid black;
		height: 5rem;
		padding: 0 3rem 0 1rem;
		display: flex;
	}

	.pcNavi li a {
		align-self: flex-end;
		font-weight: 600;
	}
	.mobileNavi {
		display: flex;
		gap: 2rem;
		font-size: calc(12px + 0.390625vw);
		list-style-type: none;
		flex-direction: column;
		padding: 0;
		margin: 0;
		position: absolute;
		width: 100%;
		top: 50%;
		left: 50%;
		bottom: unset;
		transform: translate(-50%, -50%);
		align-items: center;
	}
	.mobileNavi li button {
		background: none;
	}

	.mobileNavi li button a {
		color: white;
		font-size: calc(16px + (24 - 16) * (100vw - 320px) / (2560 - 320));
	}
	.mobile {
		position: fixed;
		top: 0;
		right: 0;
		height: 100%;
		border-left: 1px solid #aaa;
		background: rgba(0, 0, 0, 0.8);
		overflow-y: auto;
		width: 100%;
		z-index: 5;
	}

	svg {
		min-height: 24px;
		transition: transform 0.3s ease-in-out;
	}

	svg line {
		stroke: black;
		stroke-width: 3;
		transition: transform 0.3s ease-in-out;
	}

	.hamburger {
		position: fixed;
		right: 0;
		top: 1rem;
		background: none;
		border: 1px solid rgb(0, 0, 0);
		padding: 0.5rem;
		border-radius: 10px;
		margin-right: 1rem;
		color: #6b7280;
		cursor: pointer;
		z-index: 20;
	}

	.hamburger:hover {
		color: #374151;
	}

	.sidebar_show {
		border: 1px solid rgb(255, 255, 255);
	}
	.sidebar_show svg {
		transform: scale(0.7);
	}

	.sidebar_show #top {
		transform: translate(6px, 0px) rotate(45deg);
	}

	#topShow {
		transform: translate(6px, 0px) rotate(45deg);
		stroke: white;
	}

	.sidebar_show #middle {
		opacity: 0;
	}

	#middleShow {
		stroke: white;
		opacity: 0;
	}

	.sidebar_show #bottom {
		transform: translate(-12px, 9px) rotate(-45deg);
	}

	#bottomShow {
		stroke: white;
		transform: translate(-12px, 9px) rotate(-45deg);
	}

	nav label a:hover,
	nav label a:active {
		background-color: rgb(216, 216, 216);
	}

	header {
		background-color: #f9f7f0;
		color: #000000;
		padding: 0 8rem;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}

	/* HEADER */
	.logo {
		width: 100%;
		max-width: 130px;
		height: auto;
	}
	@media only screen and (max-width: 1150px) {
		header {
			padding: 0 2rem;
		}
		.pcNavi li {
			padding: 0 1rem 0 1rem;
		}

		.pcNavi li a {
			align-self: center;
		}
	}
</style>
