<script>
	import urlSlug from 'url-slug';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import NotFound from '../NotFound.svelte';
	import Device from 'svelte-device-info';
	import valkyrie from '../../assets/products/vicon/valkyrie.jpg';
	import vero from '../../assets/products/vicon/vero.jpg';
	import shogun from '../../assets/products/vicon/shogun.jpg';
	import nexus from '../../assets/products/vicon/nexus.jpg';
	import vue from '../../assets/products/vicon/vue.jpg';
	import lock from '../../assets/products/vicon/lock.jpg';
	import bicam from '../../assets/products/vicon/bicam.jpg';
	import cert from '../../assets/products/vicon/viconCert.jpg';
	import tutorial from '../../assets/products/vicon/videoTut.jpg';
	import customers from '../../assets/products/vicon/customerLink.jpg';
</script>

<div class="content">
	<div class="hero">
		<div class={Device.isPhone ? 'heroTextMobile' : 'heroText'}>
			<p>V I C O N</p>
			<!-- <button class="icon"><span>製品ページ</span></button> -->
		</div>
	</div>

	<div class="content-intro">
		<p>Viconは、業界最高水準の光学反射式モーションキャプチャシステムです。</p>
		<p>
			製品のバリエーションは圧倒的な価格訴求力のあるカメラから、業界最高分解能を持つ1600万画素のカメラまで、お客様の用途と予算に応じたシステム提案ができる幅広いラインナップをご用意しています。
		</p>
	</div>

	<section class="cameraContent">
		<h1>Camera</h1>
		<div class="container">
			<div>
				<h2>VALKYRIE</h2>
				<p class="explanation">
					Viconは、業界最高水準の光学反射式モーションキャプチャシステムです。
				</p>
				<p class="explanation">
					製品のバリエーションは圧倒的な価格訴求力のあるカメラから、業界最高分解能を持つ1600万画素のカメラまで、お客様の用途と予算に応じたシステム提案ができる幅広いラインナップをご用意しています。
				</p>
				<a href={`/product/vicon/camera/valkyrie`} use:link>
					<button class="more">
						<span class="viewMore">View more</span>
						<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
							<path
								d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
							/>
						</svg>
					</button></a
				>
			</div>
			<figure>
				<img src={valkyrie} alt="Valkyrie banner" />
			</figure>
		</div>

		<div class="container">
			<div>
				<h2>VERO</h2>
				<p class="explanation">
					コンパクトかつ高精度で世界中から大好評のVeroシリーズに、広角のVero
					1.3Xが誕生しました。視野の広いVero
					1.3Xなら、限られた空間でも広いキャプチャエリアを確保でき、全身のトラッキングや収録が可能になります。
				</p>
				<a href={`/product/vicon/camera/vero`} use:link>
					<button class="more">
						<span class="viewMore">View more</span>
						<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
							<path
								d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
							/>
						</svg>
					</button></a
				>
			</div>
			<figure>
				<img src={vero} alt="Vero banner" />
			</figure>
		</div>
	</section>

	<section class="softwareContent">
		<h1>Software</h1>
		<div class="container">
			<div>
				<h2>SHOGUN</h2>
				<p class="explanation">
					Viconは、業界最高水準の光学反射式モーションキャプチャシステムです。
				</p>
				<p class="explanation">
					製品のバリエーションは圧倒的な価格訴求力のあるカメラから、業界最高分解能を持つ1600万画素のカメラまで、お客様の用途と予算に応じたシステム提案ができる幅広いラインナップをご用意しています。
				</p>
				<button class="more">
					<span class="viewMore">View more</span>
					<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
						<path
							d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
						/>
					</svg>
				</button>
			</div>
			<figure>
				<img src={shogun} alt="Shogun banner" />
			</figure>
		</div>

		<div class="container">
			<div>
				<h2>NEXUS</h2>
				<p class="explanation">
					Vicon
					Nexusは、初のライフサイエンスに特化したモーションキャプチャーソフトウェアです。日々のルーティンワークを簡略化し、如何なる条件下でも容易にカスタマイズが可能であり、且つ、如何なる複雑な要望にも対応可能なソフトウェアです。
				</p>

				<button class="more">
					<span class="viewMore">View more</span>
					<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
						<path
							d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
						/>
					</svg>
				</button>
			</div>
			<figure>
				<img src={nexus} alt="Nexus banner" />
			</figure>
		</div>

		<div class="noImageContainer">
			<div class="container">
				<div>
					<h2>TRACKER</h2>
					<p class="explanation">
						Vicon
						Trackerは、MXカメラシステムをトラッキング用途にご利用いただく際のインターフェースとなるソフトウェアです。シミュレーション、ビジュアリゼーション、バーチャルリアリティ等の用途の制御用ソフトウェアです。
					</p>

					<button class="more">
						<span class="viewMore">View more</span>
						<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
							<path
								d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
							/>
						</svg>
					</button>
				</div>
			</div>

			<div class="container">
				<div>
					<h2>POLYGON</h2>
					<p class="explanation">
						Vicon
						Polygonは、世界で唯一、インタラクティブに3Dデータを含むマルチメディアの素材を簡単に扱えるレポートツールです。最新のVer4に至る現在、Polygonは、世界中数百のサイトで様々なレポート作成に携わっています。
					</p>

					<button class="more">
						<span class="viewMore">View more</span>
						<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
							<path
								d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
							/>
						</svg>
					</button>
				</div>
			</div>
		</div>
	</section>

	<section class="hardwareContent">
		<h1>Hardware</h1>
		<div class="container">
			<div>
				<h2>VUE</h2>
				<p class="explanation">
					Vueは業界唯一のHD高解像度デジタルリファレンスビデオとしてモーションキャプチャシステムとの完全同期を実現しました。PoE接続で設置場所を選ばず簡単に接続でき、3D情報のオーバーレイ表示等様々なデータ取得が可能になります。
				</p>
				<button class="more">
					<span class="viewMore">View more</span>
					<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
						<path
							d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
						/>
					</svg>
				</button>
			</div>
			<figure>
				<img src={vue} alt="Vue banner" />
			</figure>
		</div>

		<div class="container">
			<div>
				<h2>LOCK STUDIO/LAB</h2>
				<p class="explanation">
					Lock
					Studio/LabはViconから新たにリリースされた他の周辺機器システムとの接続、融合、同期用のコントロールボックスになります。
				</p>

				<button class="more">
					<span class="viewMore">View more</span>
					<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
						<path
							d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
						/>
					</svg>
				</button>
			</div>
			<figure>
				<img src={lock} alt="LOCK STUDIO banner" />
			</figure>
		</div>

		<div class="container">
			<div>
				<h2>BICAM</h2>
				<p class="explanation">
					BICAMはViconの光学式モーションキャプチャカメラVEROをより手軽に、スピーディーにご利用頂く為に弊社独自に開発したシステムです。簡単に一方向だけを3次元的にリアルタイムにトラッキングしたい用途に最適です。
				</p>

				<button class="more">
					<span class="viewMore">View more</span>
					<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
						<path
							d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
						/>
					</svg>
				</button>
			</div>
			<figure>
				<img src={bicam} alt="Bicam banner" />
			</figure>
		</div>
	</section>

	<section class="relatedLinks">
		<h2>関連リンク</h2>
		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			<li class="card">
				<article>
					<figure>
						<a href={'/'} use:link>
							<img src={cert} alt="Certificate" width="400" height="200" />
						</a>
						<figcaption>
							<p>モーションキャプチャスペシャリスト養成講座</p>
							<span class="overflowed-text">モーキャプエンジニア短期集中型養成講座</span>
						</figcaption>
					</figure>
				</article>
			</li>

			<li class="card">
				<article>
					<figure>
						<a href={'/'} use:link>
							<img src={tutorial} alt="Video Tutorial" width="400" height="200" />
						</a>
						<figcaption>
							<p>ビデオチュートリアル</p>
							<span class="overflowed-text"
								>お客様から寄せられる主なご質問をまとめたビデオチュートリアル</span
							>
						</figcaption>
					</figure>
				</article>
			</li>

			<li class="card">
				<article>
					<figure>
						<a href={'/'} use:link>
							<img src={customers} alt="Customers links" width="400" height="200" />
						</a>
						<figcaption>
							<p>カスタマーズリンク</p>
							<span class="overflowed-text"
								>Viconを運用いただいているお客様の情報をまとめました</span
							>
						</figcaption>
					</figure>
				</article>
			</li>
		</ul>
	</section>
</div>

<style>
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
		min-height: 8rem;
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
	/* "More" button (like "View more") */
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
	p {
		margin: 0;
	}
	.explanation {
		font-size: calc(14px + 0.390625vw);
	}
	h1 {
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}
	h2 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
	}
	.content {
		background: #eeeeee;
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
		max-width: 65rem;
		text-align: left;
		font-size: calc(16px + 0.390625vw);
		margin: 0 auto;
		padding: 10rem 0;
	}

	.hero {
		background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
			url(/src/assets/products/vicon/hero.png);
		height: 88vh;
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		position: relative;
	}
	.heroText {
		text-align: center;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		display: table;
		color: white;
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
		.container {
			flex-direction: column;
		}
		.content-intro {
			padding: 5rem;
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
