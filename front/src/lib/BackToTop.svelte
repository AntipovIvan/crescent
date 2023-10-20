<script>
	export let showOnPx = 150;
	let hidden = true;

	function goTop() {
		document.body.scrollIntoView();
	}

	function scrollContainer() {
		return document.documentElement || document.body;
	}

	function handleOnScroll() {
		if (!scrollContainer()) {
			return;
		}

		if (scrollContainer().scrollTop > showOnPx) {
			hidden = false;
		} else {
			hidden = true;
		}
	}
</script>

<svelte:window on:scroll={handleOnScroll} />

<a class="back-to-top" on:click={goTop} class:hidden />

<style>
	.back-to-top {
		display: inline-block;
		background-color: #ff9800;
		width: 50px;
		height: 50px;
		text-align: center;
		border-radius: 4px;
		position: fixed;
		bottom: 30px;
		right: 30px;
		transition: background-color 0.3s, opacity 0.5s, visibility 0.5s;
		/* opacity: 0; */
		/* visibility: hidden; */
		z-index: 1000;
		opacity: 1;
		user-select: none;
		color: white;
	}
	.back-to-top::after {
		content: '↑';
		font-size: 2em;
		line-height: 3rem;
		color: #fff;
	}
	.back-to-top:hover {
		cursor: pointer;
		background-color: #333;
	}
	.back-to-top:active {
		background-color: #555;
	}

	.back-to-top.hidden {
		opacity: 0;
		visibility: hidden;
	}
</style>
