<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';

	import { onMount } from 'svelte';

	onMount(() => {
		window.scrollTo(0, 0);
	});
</script>

<div class="content">
	<div class="hero">
		<h1>採用情報</h1>
		<!-- <button class="icon"><span>製品ページ</span></button> -->
	</div>

	<div class="content-intro">
		<h2>産業向け受注案件事例</h2>
		<p>現在、以下の内容で募集しています。</p>
		<p>
			面接希望の方は、履歴書等をPDF添付の上、<a href="mailto:recruit@crescentinc.co.jp"
				>recruit@crescentinc.co.jp</a
			> 宛にお送りください。 社員一同、素晴らしいご縁をお待ちしております。
		</p>
	</div>

	<section class="cameraContent">
		<div class="container">
			<div>
				<h2>募集要項</h2>
				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<td>最終学歴</td>
							<td>4年生大学卒 及び 専門学校卒　以上</td>
						</tr>
						<tr>
							<td>勤務地</td>
							<td>本社（江東区木場）</td>
						</tr>
						<tr>
							<td>賞与</td>
							<td>年2回</td>
						</tr>
						<tr>
							<td>昇給</td>
							<td>能力に応じて</td>
						</tr>
						<tr>
							<td>交通費</td>
							<td>支給あり</td>
						</tr>
						<tr>
							<td>試用期間</td>
							<td>6ヵ月</td>
						</tr>
						<tr>
							<td>初任給</td>
							<td>220,000円（新卒の場合）、経験者金額応談</td>
						</tr>
						<tr>
							<td>週休</td>
							<td>週休2日制</td>
						</tr>
						<tr>
							<td rowspan="2">職種</td>
							<td>
								<p
									style="font-weight:bold;color: #1E4990;text-decoration: underline;margin-bottom: 1rem;"
								>
									CGデザイン：モデラ、アニメータ
								</p>
								<ul>
									<li>
										<span style="font-weight:bold;">応募条件</span>
										<ul>
											<li>使用ツール問わず</li>
											<li>ゲームエンジン（特にUnity/Unreal Engine）が使えると尚良し</li>
										</ul>
									</li>
								</ul>
							</td>
						</tr>
						<tr>
							<td>
								<p
									style="font-weight:bold;color: #1E4990;text-decoration: underline;margin-bottom: 1rem;"
								>
									開発エンジニア
								</p>
								<ul>
									<li>
										<span style="font-weight:bold;">必須条件</span>
										<ul>
											<li>Unity/Unreal Engineを用いた開発ができる</li>
											<li>Virtual Production（スタジオ運営、オペレーション）に興味がある</li>
											<li>XR、メタバース等最新技術に興味がある</li>
										</ul>
									</li>
									<li>
										<span style="font-weight:bold;">歓迎条件</span>
										<ul>
											<li>C++を用いた開発経験</li>
											<li>AWSなどクラウドを活用した、インフラ設計/構築/運用の知識・経験</li>
										</ul>
									</li>
								</ul>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</section>
</div>

<style>
	tr:not(:last-child) td:first-child {
		background: #e7f2f9;
	}
	.linkTitle {
		font-weight: bold;
		font-size: calc(10px + 0.390625vw);
	}
	ul {
		margin-bottom: 2rem;
		margin-left: 1rem;
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
		min-height: 6rem;
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
	p,
	a,
	tr,
	td {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}
	a {
		text-decoration: underline;
	}

	li {
		font-size: calc(14px + 0.390625vw);
		margin-left: 1rem;
		margin-bottom: 0.5rem;
	}
	h1 {
		font-size: calc(36px + 0.390625vw);
		font-weight: 600;
		padding: 4rem 0 0 0;
	}
	h2 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
		padding: 1rem 0 2rem 0;
	}
	.content {
		background: #eeeeee;
		padding: 2rem 8rem;
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
		width: 85%;
		text-align: left;
		font-size: calc(16px + 0.390625vw);
		margin: 0 auto;
		padding: 4rem 0;
	}

	.hero {
		position: relative;
		margin-bottom: 3rem;
	}
	.heroText {
		text-align: center;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		display: table;
		color: black;
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
		section {
			width: 100%;
		}
		h1 {
			font-size: calc(28px + 0.390625vw);
			padding: 1rem 0 0 0;
		}
		h2 {
			font-size: calc(24px + 0.390625vw);
			padding: 1rem 0 2rem 0;
		}
		.container {
			flex-direction: column;
			padding: 3rem 1rem;
		}
		.content {
			padding: 2rem 2rem;
		}
		.content-intro {
			padding: 0rem;
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
