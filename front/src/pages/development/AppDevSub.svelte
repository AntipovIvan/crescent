<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import appDevSub1 from '../../assets/development/AppDevSub1.png';
	import appDevSub2 from '../../assets/development/AppDevSub2.png';
	import appDevSub3 from '../../assets/development/AppDevSub3.png';
	import appDevSub4 from '../../assets/development/AppDevSub4.png';
	import { onMount } from 'svelte';

	onMount(() => {
		window.scrollTo(0, 0);
	});
</script>

<div class="content">
	<div class="hero">
		<h1>アプリケーション制作</h1>
	</div>

	<div class="content-intro">
		<h2>公開されている制作事例紹介</h2>
		<p>弊社の受注案件の多くは非公開が原則なのですが、一部の公開可能なものをご紹介します。</p>
	</div>

	<section class="cameraContent">
		<div class="container">
			<h2>BeHere/1942</h2>
			<figure class="figure">
				<img src={appDevSub1} alt="Valkyrie banner" />
			</figure>
			<p class="explanation">
				この作品は、2022年にロサンゼルス・リトルトーキョー内のJANM(全米日系人博物館)が主催した、heBeHere
				/
				1942展で発表された藤幡正樹氏制作のARインスタレーション作品です。太平洋戦争勃発時に当時の日系アメリカ人強制収容について新たな視点を提供して話題になりました。この作品のAR化プログラム開発を弊社スタッフが担当いたしました。
			</p>
			<p class="explanation">
				※JAMN(Japanese American National
				Museum)：日系アメリカ人の歴史や文化を伝承、展示している博物館で、1992年に設立
			</p>
			<p class="explanation">
				※この作品はJANMWebサイトよりダウンロード・体験できます（詳細は<a
					href="https://www.janm.org/ja/exhibits/behere1942"
					target="_blank">こちら</a
				>）
			</p>
		</div>

		<div class="container">
			<h2>Brain100 Studio</h2>
			<figure class="figure">
				<img src={appDevSub2} alt="Valkyrie banner" />
			</figure>
			<p class="explanation">MIG株式会社様</p>
			<p class="explanation">
				MIG株式会社様が運営するアルツハイマー型認知症予防を目指すプログラムであるBrain100向けに、Meta
				Quest2を使った脳機能テスト向け空間ナビ測定VRアプリケーションを開発しました。
				MIG株式会社様独自の脳機能測定アルゴリズムをVRアプリケーションに組み込み、ユーザー様の脳機能を計測することが可能です。
			</p>
			<p class="explanation"><b>開発環境：</b>Unity3D, Meta Quest2</p>
			<p class="explanation">
				<b>関連ページ：</b>
			</p>
			<p><a href="https://brain100studio.com" target="_blank">Brain100サイト</a></p>

			<p class="explanation">
				<a href="https://www.youtube.com/watch?v=3ptagjaajjs" target="_blank"
					>関係者向け紹介ビデオ</a
				>
			</p>
		</div>

		<div class="container">
			<h2>AR「とびだす佐渡さん」</h2>
			<figure class="figure">
				<img src={appDevSub3} alt="Valkyrie banner" />
			</figure>
			<p class="explanation">新日本フィルハーモニー交響楽団様</p>
			<p class="explanation">
				すみだ音楽大使に就任された世界的指揮者の佐渡裕様を、弊社サービス4DViewsで撮影させて頂き、8thWallと組み合わせて、コンサートにご来場いただいた方々がその場で御覧いただけるコンテンツを作成いたしました。
				ロゴから出現したり、等身大パネルから出現したり、ご要望に合わせて様々なパターンを作成しました。
			</p>
			<p class="explanation">
				<b>関連ページ：</b>
			</p>
			<p><a href="https://www.njp.or.jp/news/5754/" target="_blank">NJP</a></p>
		</div>

		<div class="container">
			<h2>NJP Virtual Club</h2>
			<figure class="figure">
				<iframe
					width="80%"
					height="720"
					src="https://www.youtube.com/embed/G9xkhQfcmTQ"
					title="NJP Virtual Club"
					frameborder="0"
					allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
					allowfullscreen
					style="height: 33vw;"
				></iframe>
				<!-- <img src={appDevSub3} alt="Valkyrie banner" /> -->
			</figure>
			<p class="explanation">新日本フィルハーモニー交響楽団様</p>
			<p class="explanation">
				すみだ音楽大使に就任された世界的指揮者の佐渡裕様を、弊社サービス4DViewsで撮影させて頂き、8thWallと組み合わせて、コンサートにご来場いただいた方々がその場で御覧いただけるコンテンツを作成いたしました。
				ロゴから出現したり、等身大パネルから出現したり、ご要望に合わせて様々なパターンを作成しました。
			</p>
			<p class="explanation">
				<b>関連ページ：</b>
			</p>
			<p><a href="https://www.njp.or.jp/news/6238/" target="_blank">NJP</a></p>
			<p>
				<a href="https://www.meta.com/ja-jp/experiences/8624751027549929/" target="_blank">Meta</a>
			</p>
			<p>
				<a href="https://www.viveport.com/apps/c127156b-5f02-4cf6-8a42-7309eeca2071" target="_blank"
					>Viveport</a
				>
			</p>
			<p>
				<a href="https://www.youtube.com/watch?v=820JW-aCOCI" target="_blank"
					>NJP Virtual Club Launch Trailer
				</a>
			</p>
		</div>
	</section>
</div>

<style>
	.linkTitle {
		font-weight: bold;
		font-size: calc(10px + 0.390625vw);
	}
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
	a {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}
	a {
		text-decoration: underline;
	}
	ul {
		margin-bottom: 2rem;
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
		gap: 1rem;
		padding: 3rem 3rem;
		flex-direction: column;
		border-radius: 14px;
		-webkit-box-shadow: 0px 2px 4px 2px rgba(173, 173, 173, 0.5);
		-moz-box-shadow: 0px 2px 4px 2px rgba(173, 173, 173, 0.5);
		box-shadow: 0px 2px 4px 2px rgba(173, 173, 173, 0.5);
	}
	/* section div div {
		display: flex;
		flex-direction: column;
		flex: 50%;
		justify-content: space-between;
	} */
	.figure {
		/* flex: 50%; */
		text-align: center;
	}
	.figure img {
		width: 80%;
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
