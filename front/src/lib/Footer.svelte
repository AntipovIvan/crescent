<script>
	import { link } from 'svelte-spa-router';
</script>

<footer class="flex-rw">
	<div class="footer-container">
		<div class="companyname">株式会社クレッセント</div>
		<div class="addresses">
			<div>
				<span>本社</span>
				<p>東京都江東区木場3-14-8</p>
			</div>
			<br />
			<div>
				<span>4D STUDIO</span>
				<p>東京都江東区平野2-11-5</p>
				<p>パシフィック第二門前仲町 2F</p>
			</div>
		</div>
		<div class="contacts">
			<span>お問い合わせ</span>
			<p>Tel: 03-5875-9707</p>
			<p>Fax: 03-5875-9708</p>
			<p>Mail: info@crescentinc.co.jp</p>
		</div>
		<div class="mainlinks">
			<p>ホーム</p>
			<p>お知らせ</p>
			<p>会社情報</p>
			<p>採用情報</p>
		</div>
		<div class="sublinks">
			<p>サイトマップ</p>
			<p>プライバシーポリシー</p>
			<p>免責事項</p>
			<p>FAQ</p>
		</div>
		<div class="social">
			<a href="#" class="generic-anchor" target="_blank" title="Twitter"
				><svg viewBox="0 0 50 50" width="40px" height="40px">
					<path
						fill="black"
						d="M 6.9199219 6 L 21.136719 26.726562 L 6.2285156 44 L 9.40625 44 L 22.544922 28.777344 L 32.986328 44 L 43 44 L 28.123047 22.3125 L 42.203125 6 L 39.027344 6 L 26.716797 20.261719 L 16.933594 6 L 6.9199219 6 z"
					/></svg
				></a
			>
			<a href="#" class="generic-anchor" target="_blank" title="Instagram"
				><svg viewBox="0 0 50 50" width="40px" height="40px">
					<path
						fill="black"
						d="M 16 3 C 8.83 3 3 8.83 3 16 L 3 34 C 3 41.17 8.83 47 16 47 L 34 47 C 41.17 47 47 41.17 47 34 L 47 16 C 47 8.83 41.17 3 34 3 L 16 3 z M 37 11 C 38.1 11 39 11.9 39 13 C 39 14.1 38.1 15 37 15 C 35.9 15 35 14.1 35 13 C 35 11.9 35.9 11 37 11 z M 25 14 C 31.07 14 36 18.93 36 25 C 36 31.07 31.07 36 25 36 C 18.93 36 14 31.07 14 25 C 14 18.93 18.93 14 25 14 z M 25 16 C 20.04 16 16 20.04 16 25 C 16 29.96 20.04 34 25 34 C 29.96 34 34 29.96 34 25 C 34 20.04 29.96 16 25 16 z"
					/></svg
				></a
			>
			<a href="#" class="generic-anchor" target="_blank" title="Youtube"
				><svg viewBox="0 0 50 50" width="40px" height="40px">
					<path
						fill="black"
						d="M 44.898438 14.5 C 44.5 12.300781 42.601563 10.699219 40.398438 10.199219 C 37.101563 9.5 31 9 24.398438 9 C 17.800781 9 11.601563 9.5 8.300781 10.199219 C 6.101563 10.699219 4.199219 12.199219 3.800781 14.5 C 3.398438 17 3 20.5 3 25 C 3 29.5 3.398438 33 3.898438 35.5 C 4.300781 37.699219 6.199219 39.300781 8.398438 39.800781 C 11.898438 40.5 17.898438 41 24.5 41 C 31.101563 41 37.101563 40.5 40.601563 39.800781 C 42.800781 39.300781 44.699219 37.800781 45.101563 35.5 C 45.5 33 46 29.398438 46.101563 25 C 45.898438 20.5 45.398438 17 44.898438 14.5 Z M 19 32 L 19 18 L 31.199219 25 Z"
					/></svg
				></a
			>
		</div>
	</div>

	<div class="footer-bottom-wrapper">
		<p>Copyright @ CRESCENT, INC.</p>
	</div>
</footer>

<style>
	span,
	p {
		color: #313132;
	}
	span {
		font-weight: 600;
	}
	p {
		font-weight: 400;
		line-height: 1.7em;
	}
	.footer-container {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
		grid-template-rows: 1fr 2fr;
		gap: 0px 0px;
		grid-template-areas:
			'companyname companyname companyname companyname companyname'
			'addresses contacts mainlinks sublinks social';
		padding: 3rem 5rem 1rem 7vw;
		gap: 1rem;
	}

	.companyname {
		font-size: calc(18px + 0.390625vw);
		font-weight: 600;
		grid-area: companyname;
	}
	.addresses {
		grid-area: addresses;
	}
	.contacts {
		grid-area: contacts;
		border-right: 1px solid black;
	}
	.mainlinks {
		grid-area: mainlinks;
		text-align: center;
	}
	.sublinks {
		grid-area: sublinks;
		border-right: 1px solid black;
	}
	.social {
		grid-area: social;
		display: flex;
		justify-content: center;
		gap: 1rem;
	}

	.flex-rw {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		border-top: 13px solid #313132;
		margin-top: auto;
		background: #f9f7f0;
		font-family: NotoSans;
	}

	.footer-bottom-wrapper {
		border-top: 2px solid black;
		text-align: center;
		padding: 1rem 0;
	}

	@media only screen and (max-width: 568px) {
		.footer-bottom-wrapper {
			text-align: center;
			width: 100%;
			margin-top: 10px;
		}
	}

	@media only screen and (max-width: 320px) {
		.footer-bottom-wrapper {
			font-size: 1.3em;
		}
	}

	@media only screen and (max-width: 768px) {
		.footer-bottom-wrapper {
			font-size: 16px;
			line-height: 25px;
		}
	}
	@media only screen and (max-width: 1200px) {
		.footer-container {
			display: grid;
			grid-template-columns: 1fr 1fr;
			grid-template-rows: 0.2fr 1fr 0.8fr 0.2fr;
			grid-template-areas:
				'companyname companyname'
				'addresses contacts'
				'mainlinks sublinks'
				'social social';
			padding: 3rem 2rem 1rem 3rem;
			column-gap: 1rem;
			/* row-gap: 3rem; */
		}
		.contacts,
		.sublinks {
			border: none;
		}
		.companyname {
			text-align: center;
		}
	}
</style>
