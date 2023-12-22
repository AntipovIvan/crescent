<script>
	import { onMount } from 'svelte';

	onMount(() => {
		window.scrollTo(0, 0);
	});
</script>

<div class="content">
	<div class="hero">
		<h1>プライバシーポリシー</h1>
	</div>

	<div class="content-intro">
		<p>
			当社は、個人情報保護の重要性を認識し、個人情報保護の方針を定めるとともに、個人情報の適切な保護に努めます。
		</p>
	</div>

	<section class="cameraContent">
		<div class="container">
			<div>
				<h2><span style="color:#0b345b">個人情報の使用目的</span></h2>
				<ol>
					<li>
						当社は、お客様からご提供いただく個人情報を、お問い合わせ内容への返信、各種情報の送信、イベントのご案内等の目的で使用させていただきます。また、当社は、この範囲内で必要な業務を委託する協力会社に対し、厳重な個人情報の管理を求めたうえ、個人情報を開示することがあります。
					</li>
					<li>
						弊社および協力会社は、お客様からの問い合わせ対応歴などのお客様に関する個人履歴を記録する場合がありますことを予めご了承願います。
					</li>
				</ol>

				<hr />

				<h2><span style="color:#0b345b">個人情報の収集、利用、提供等に関する基本原則</span></h2>
				<ol>
					<li>
						個人情報を直接収集する際は、適法かつ公正な手段により、本人の同意を得た上で行います。
					</li>
					<li>収集にあたっては、利用目的を明確にし、その目的のために必要な範囲内にとどめます。</li>
					<li>
						当社が個人情報の処理を伴う業務を外部から受託する場合や外部へ委託する場合は、個人情報に関する秘密の保持、再委託に関する事項、事故時の責任分担、契約終了時の個人情報の返却および消去等について定め、それに従います。
					</li>
					<li>個人情報は、本人の同意を得た範囲内で利用、提供します。</li>
				</ol>

				<hr />

				<h2><span style="color:#0b345b">個人情報の管理について </span></h2>
				<ol>
					<li>
						当社が直接収集または外部から業務を受託する際に入手した個人情報は、正確な状態に保ち、不正アクセス、紛失・破壊・改ざんおよび漏洩等を防止するための措置を講じます。
					</li>
					<li>
						個人情報の処理を伴う業務を外部から受託する場合は、委託者が個人情報を入手した際、本人の同意を得た上で、適法かつ公正な手段によって収集したものであることを確認します。
					</li>
				</ol>

				<hr />

				<h2><span style="color:#0b345b">法令及びその他の規範について </span></h2>
				<ol>
					<li>
						当社は、個人情報の保護に関係する日本の法令及びその他の規範を遵守し、本方針の継続的改善に努めます。
					</li>
				</ol>

				<hr />

				<h2><span style="color:#0b345b">法令及びその他の規範について </span></h2>
				<ol>
					<li>
						本人からの個人情報の取扱いに関するお問い合わせには、妥当な範囲において、すみやかな対応に努めます。このページの内容に関するご質問及びお客様がご自身の個人情報についてご確認されたい場合には、
						こちらからお問い合わせください。
					</li>
				</ol>
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
