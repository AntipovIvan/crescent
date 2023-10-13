<script>
	import { link } from 'svelte-spa-router';
</script>

<footer class="flex-rw">
	<div class="footer-flex">
		<ul class="footer-list-top">
			<li>
				<a href={`/products/`} use:link class="generic-anchor footer-list-anchor">製品販売</a>
			</li>
			<li><a href="#" class="generic-anchor footer-list-anchor">スタジオサービス</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">コンテンツ開発</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">会社情報</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">お問い合わせ</a></li>
		</ul>

		<ul class="footer-list-top">
			<li><a href="#" class="generic-anchor footer-list-anchor">サイトマップ</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">プライバシーポリシー</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">免責事項</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">採用情報</a></li>
			<li><a href="#" class="generic-anchor footer-list-anchor">FAQ</a></li>
		</ul>

		<section class="footer-social-section flex-rw">
			<a href="#" class="generic-anchor" target="_blank" title="Twitter"
				><svg viewBox="0 0 50 50" width="50px" height="50px">
					<path
						fill="white"
						d="M 6.9199219 6 L 21.136719 26.726562 L 6.2285156 44 L 9.40625 44 L 22.544922 28.777344 L 32.986328 44 L 43 44 L 28.123047 22.3125 L 42.203125 6 L 39.027344 6 L 26.716797 20.261719 L 16.933594 6 L 6.9199219 6 z"
					/></svg
				></a
			>
			<a href="#" class="generic-anchor" target="_blank" title="Instagram"
				><svg viewBox="0 0 50 50" width="50px" height="50px">
					<path
						fill="white"
						d="M 16 3 C 8.83 3 3 8.83 3 16 L 3 34 C 3 41.17 8.83 47 16 47 L 34 47 C 41.17 47 47 41.17 47 34 L 47 16 C 47 8.83 41.17 3 34 3 L 16 3 z M 37 11 C 38.1 11 39 11.9 39 13 C 39 14.1 38.1 15 37 15 C 35.9 15 35 14.1 35 13 C 35 11.9 35.9 11 37 11 z M 25 14 C 31.07 14 36 18.93 36 25 C 36 31.07 31.07 36 25 36 C 18.93 36 14 31.07 14 25 C 14 18.93 18.93 14 25 14 z M 25 16 C 20.04 16 16 20.04 16 25 C 16 29.96 20.04 34 25 34 C 29.96 34 34 29.96 34 25 C 34 20.04 29.96 16 25 16 z"
					/></svg
				></a
			>
			<a href="#" class="generic-anchor" target="_blank" title="Youtube"
				><svg viewBox="0 0 50 50" width="50px" height="50px">
					<path
						fill="white"
						d="M 44.898438 14.5 C 44.5 12.300781 42.601563 10.699219 40.398438 10.199219 C 37.101563 9.5 31 9 24.398438 9 C 17.800781 9 11.601563 9.5 8.300781 10.199219 C 6.101563 10.699219 4.199219 12.199219 3.800781 14.5 C 3.398438 17 3 20.5 3 25 C 3 29.5 3.398438 33 3.898438 35.5 C 4.300781 37.699219 6.199219 39.300781 8.398438 39.800781 C 11.898438 40.5 17.898438 41 24.5 41 C 31.101563 41 37.101563 40.5 40.601563 39.800781 C 42.800781 39.300781 44.699219 37.800781 45.101563 35.5 C 45.5 33 46 29.398438 46.101563 25 C 45.898438 20.5 45.398438 17 44.898438 14.5 Z M 19 32 L 19 18 L 31.199219 25 Z"
					/></svg
				></a
			>
		</section>
	</div>

	<section class="footer-bottom-section flex-rw">
		<div class="footer-bottom-wrapper">
			<p>&copy;2023 CRESCENT,INC | All Rights Reserved</p>
		</div>
	</section>
</footer>

<style>
	a {
		text-decoration: none;
	}

	ul {
		list-style-type: none;
	}

	.generic-anchor {
		color: #ffffff;
	}
	.generic-anchor:visited {
		color: #ffffff;
	}
	.generic-anchor:hover {
		color: #ccc;
	}

	.flex-rw {
		display: flex;
		flex-flow: row wrap;
		gap: 3rem;
	}

	footer {
		padding: 4rem 6rem;
		margin-top: auto;
		/* width: 100%; */
		color: #ffffff;
		position: relative;
		background: #0b345b;
		min-height: 100px;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}

	.footer-list-top {
		width: 12rem;
		margin: 0;
		padding: 0;
	}

	.footer-list-top > li {
		text-align: left;
		padding-bottom: 10px;
	}

	.footer-list-anchor {
		font-size: calc(8px + 0.390625vw);
	}

	.footer-social-section {
		display: flex;
		flex: 2;
		flex-direction: row;
		justify-content: flex-end;
		gap: 1.5rem;
		margin-left: auto;
	}

	.footer-bottom-section {
		width: 100%;
		margin-top: 10px;
	}

	.footer-bottom-section > div:first-child {
		margin-right: auto;
	}

	.footer-bottom-wrapper {
		color: #fff;
	}

	.footer-flex {
		display: flex;
		flex-wrap: wrap;
		justify-content: flex-start;
		flex: 1;
	}

	@media only screen and (max-width: 568px) {
		.footer-list-top {
			width: 100%;
		}

		.footer-list-anchor {
			font-size: 1.5em;
		}

		.footer-social-section {
			justify-content: center;
		}

		.footer-bottom-section {
			padding: 0 5px 10px 5px;
		}

		.footer-bottom-wrapper {
			text-align: center;
			width: 100%;
			margin-top: 10px;
		}
	}

	@media only screen and (max-width: 320px) {
		.footer-list-anchor {
			font-size: 1.2em;
		}

		.footer-bottom-wrapper {
			font-size: 1.3em;
		}
	}

	@media only screen and (max-width: 768px) {
		.footer-list-anchor {
			font-size: 1.1em;
		}

		.footer-bottom-wrapper {
			font-size: 1.3em;
		}
	}
</style>
