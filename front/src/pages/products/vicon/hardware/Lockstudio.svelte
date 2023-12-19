<script>
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import hero from '../../../../assets/products/vicon/hardware/lockstudio/lockbanner.jpg';
	import link1 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink1.png';
	import link2 from '../../../../assets/products/vicon/camera/valkyrie/valkyrieLink2.png';
	import { onMount } from 'svelte';

	let isFixedNav = false;
	let activeSection = null;

	onMount(async () => {
		window.scrollTo(0, 0);

		const heroHeight = document.querySelector('.hero');
		const sidebarItems = document.querySelectorAll('.sidebar-item');
		const sections = document.querySelectorAll('.content > section');

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting && entry.intersectionRatio >= 0.3) {
						const targetId = entry.target.id;
						activeSection = targetId;
						sidebarItems.forEach((item) => {
							if (item.getAttribute('href') === `#${targetId}`) {
								item.classList.add('active');
							} else {
								item.classList.remove('active');
							}
						});
					}
				});
			},
			{ threshold: 0.3 }
		);

		sections.forEach((section) => {
			observer.observe(section);
		});

		window.addEventListener('scroll', () => {
			const scrollPosition = window.scrollY || document.documentElement.scrollTop;
			isFixedNav = scrollPosition >= heroHeight.offsetHeight;
		});
	});

	function scrollToElement(event) {
		event.preventDefault();

		const targetId = event.target.hash.substr(1);
		const targetElement = document.getElementById(targetId);

		if (targetElement) {
			targetElement.scrollIntoView({ behavior: 'smooth' });
		}
	}
</script>

<div class="pageContent">
	<div class="hero">
		<h1>LOCK STUDIO/LAB</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>製品詳細</a>
		<a class="sidebar-item" href="#system" on:click={scrollToElement}>仕様・価格</a>
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h2>製品詳細</h2>
			</div>

			<div class="container">
				<p class="explanation">
					Lock
					Studio/LabはViconから新たにリリースされた他の周辺機器システムとの接続、融合、同期用のコントロールボックスになります。
				</p>

				<li>
					Connect
					<p>
						Vicon Lock
						Studio/Labは今まで複雑だった他の周辺機器などのシステムとの接続を飛躍的に簡略化する事に成功しました。他の周辺機器を直接Lock
						Studio/Labに接続するだけで、PoE経由でViconシステムと簡単に接続することが可能です。
					</p>
				</li>

				<li>
					Integrate
					<p>
						Lock Labには64チャンネルのA/D変換回路が内蔵してあり、アナログ機器も直接Lock
						Labに接続しViconシステムと統合されたデータを収録することが可能となります。
					</p>
				</li>

				<li>
					Synchronize
					<p>
						Lock Studio/Labは外部機器同期トリガー用にVESA規格にて8つのポートを持ちます。また、Lock
						StudioはSDI入力を持ち、Genlockやタイムコードもサポートしておりますので、互換性のある他機器との完全同期も保障されたデータを収録できます。
					</p>
				</li>
			</div>
		</section>

		<section class="system" id="system">
			<div class="container">
				<h2>仕様・価格</h2>
				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">接続/電源供給 - Studio/Lab 共通</th>
						</tr>
						<tr>
							<th class="tblCap">PoE</th>
							<td>IEEE 802.3af</td>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">消費電力</th>
							<td>7W </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">ケーブル長</th>
							<td>最長100m </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">コネクタータイプ</th>
							<td>RJ45 </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">LTC Output（100 ohm）</th>
							<td>RJ45 </td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">リモート入力（スタート/ストップ） - Studio/Lab 共通</th>
						</tr>
						<tr>
							<th class="tblCap">コネクター入力</th>
							<td>RCA</td>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">入力インピーダンス</th>
							<td>5Vを含む1K5 </td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">サイズ - Studio/Lab 共通</th>
						</tr>
						<tr>
							<th class="tblCap">奥行き x 幅 x 高さ</th>
							<td>200 x 445 x 44.5mm （高さと幅は1U規格）</td>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">重さ</th>
							<td>1.6kg </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">温度</th>
							<td>0度～35度 </td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">シンクアウト（x8） - Studio/Lab 共通</th>
						</tr>
						<tr>
							<th class="tblCap">GPO</th>
							<td>8 x programmable GPO</td>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">コネクタータイプ</th>
							<td>RCA </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">出力インピーダンス</th>
							<td>130 ohm </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">出力レベル（内部電圧ソース）</th>
							<td>0 - 4.3V </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">出力レベル（外部電圧ソース）</th>
							<td>0 - 18V </td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">VESAシンク入力 - Studio/Lab 共通</th>
						</tr>
						<tr>
							<th class="tblCap">VESAステレオ入力方法</th>
							<td>50, 60, 100, 120, 200Hz</td>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">コネクタータイプ</th>
							<td>3ピン　Mini DIN </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">入力インピーダンス</th>
							<td>10K </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">VESA出力（Studioのみ）</th>
							<td>3V3 TTL Square wave - BNC </td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">タイムコード入力（SDI）- Lock Studioのみ</th>
						</tr>
						<tr
							><th class="tblCap">アナログビデオ タイムコード入力</th><td
								>NTSC/PAL or HD Tri Level sync</td
							>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">コネクタータイプ</th>
							<td>BNC </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">入力インピーダンス</th>
							<td>75 ohm </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">サポートレート</th>
							<td>30P, 29.97P, 25P, 24P, 23.98P </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">LTC入出力（100 ohm）</th>
							<td>BNC </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">SDI入力</th>
							<td
								>576x50i, 487x59.94i, 1080x30P, 1080x24P, 1080x23.98P, 1080x29.97P, 1080x25P,
								1080x59.94i, 1080x50i
							</td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr>
							<th colspan="2">アナログ入力 - Lock Labのみ</th>
						</tr>
						<tr>
							<th class="tblCap">アナログチャンネル数</th>
							<td>64</td>
						</tr>
						<tr>
							<th class="tblCap">合計アナログサンプルレート</th>
							<td>192 KHz</td>
						</tr>
						<tr class="tblCap">
							<th class="tblCap">アナログ入力範囲</th>
							<td>+/-1.25V +/-2.5V +/-5V +/-10V </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">コネクタータイプ</th>
							<td>ワイドミュラー社製コネクター<br />パーツ番号: 1278100000 </td></tr
						>
						<tr class="tblCap">
							<th class="tblCap">入力インピーダンス</th>
							<td>1M ohm </td></tr
						>
					</tbody>
				</table>

				<table border="1" cellpadding="3">
					<tbody
						><tr class="tblCap">
							<th class="tblCap">価格（税別）</th>
							<td>1,950,000円 </td></tr
						>
					</tbody>
				</table>
			</div>
		</section>
		<br />
		<br />
		<br />
		<a href={`/product/vicon`} use:link>
			<button class="more">
				<span class="viewMore">VICONトップへ</span>
			</button></a
		>
	</div>
</div>
<section class="relatedLinks">
	<h2>関連リンク</h2>
	<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
		<li class="card">
			<article>
				<figure>
					<a href={`/product/holosuite`} use:link>
						<img src={link1} alt="title" width="400" height="200" />
					</a>
					<figcaption>
						<p class="linkTitle">Faceware</p>
						<span class="overflowed-text"
							>ビデオベースのフェイシャル専用モーションキャプチャーシステム</span
						>
					</figcaption>
				</figure>
			</article>
		</li>

		<li class="card">
			<article>
				<figure>
					<a href={`/services/4dstudio`} use:link>
						<img src={link2} alt="title" width="400" height="200" />
					</a>
					<figcaption>
						<p class="linkTitle">StretchSense</p>
						<span class="overflowed-text"
							>シリコン素材の伸縮センサーを搭載したワイアレス対応グローブデバイス</span
						>
					</figcaption>
				</figure>
			</article>
		</li>
	</ul>
</section>

<style>
	.viewMore {
		font-weight: 500;
		font-size: calc(20px + 0.390625vw);
	}
	.linkTitle {
		font-weight: bold;
	}
	.more {
		text-align: center;
		border: 1px solid rgb(143, 143, 143);
		padding: 1rem 4rem;
		background: none;
		border-radius: 8px;
		cursor: pointer;
	}
	th {
		padding: 10px;
		font-size: calc(12px + 0.390625vw);
		background: #e0e3e7;
	}
	td {
		font-size: calc(12px + 0.390625vw);
	}
	table {
		margin-bottom: 20px;
		width: 100%;
		word-wrap: break-word;
	}
	.overflowed-text {
		margin: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 3;
		white-space: pre-wrap;
	}
	.sidebar-item {
		font-size: calc(14px + 0.390625vw);
		color: #ababab;
		padding: 16px;
		text-decoration: none;
	}
	.sidebar-item.active {
		color: #000000;
		font-size: calc(14px + 0.390625vw);
	}
	.features-list {
		padding-left: 5rem;
	}
	.features-list-item {
		list-style-type: disc;
		font-size: calc(14px + 0.390625vw);
		line-height: 1.5;
	}
	.pageContent {
		padding: 2rem 8rem;
	}
	.sidebar {
		margin: 0;
		padding: 0;
		width: 25vw;
		position: absolute;
		height: 100%;
		overflow: auto;
		display: flex;
		flex-direction: column;
	}

	.sidebar-fixed {
		position: fixed;
		top: 0;
		left: 0;
		padding: 2rem 0 2rem 8rem;
	}

	.content {
		margin-left: 25vw;
		padding: 1px 16px;
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
		margin-top: 3rem;
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

	.hero {
		position: relative;
		margin-bottom: 5rem;
	}

	.hero-image-container {
		max-height: 70vh;
		overflow: hidden;
		display: flex;
		justify-content: center;
		align-items: center;
		border-radius: 15px;
	}

	.hero-image {
		width: 100%;
		max-height: 100%;
		object-fit: contain;
	}

	p,
	li {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}

	.image-text-flexbox img {
		width: 14vw;
	}
	.explanation {
		font-size: calc(14px + 0.390625vw);
	}
	h1 {
		font-size: calc(36px + 0.390625vw);
		font-weight: 600;
		padding: 4rem 0;
	}
	h2 {
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}

	h3 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
		color: #0b345b;
	}

	section:not(.relatedLinks) {
		width: 100%;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 0;
		border-top: 2px solid black;
	}

	.container {
		display: flex;
		gap: 2rem;
		padding: 3rem 0;
		flex-direction: column;
	}
	/* section div div {
		display: flex;
		flex-direction: column;
		flex: 50%;
		justify-content: space-between;
	} */
	section div figure {
		flex: 50%;
	}
	section div figure img {
		width: 100%;
	}

	figure {
		margin: 0;
		padding: 0;
		text-align: left;
	}

	@media (max-width: 800px) {
		.container {
			flex-direction: column;
		}

		.cardList {
			grid-template-columns: repeat(auto-fill, 15.5rem);
			margin: 0 auto;
		}
	}

	@media screen and (max-width: 700px) {
		.sidebar {
			width: 100%;
			height: auto;
			position: relative;
			flex-direction: row;
			justify-content: flex-start;
			align-items: center;
		}
		.sidebar-fixed {
			background-color: white;
		}
		.hero {
			margin-bottom: 2rem;
		}
		.sidebar-fixed {
			position: fixed;
			padding: 0rem;
		}
		.sidebar a {
			float: left;
		}
		div.content {
			margin-left: 0;
		}
		iframe {
			width: 100%;
		}
	}

	@media screen and (max-width: 1200px) {
		.pageContent {
			padding: 0 1rem;
		}
		h1 {
			padding: 2rem 0;
		}
	}

	@media screen and (max-width: 400px) {
		.sidebar a {
			text-align: center;
			float: none;
		}
	}
</style>
