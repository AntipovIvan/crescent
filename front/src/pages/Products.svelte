<script>
	import vicon from '../assets/products/vicon.png';
	import fourdviews from '../assets/products/4dviews.png';
	import faceware from '../assets/products/faceware.png';
	import stretchsense from '../assets/products/stretchsense.png';
	import holosuite from '../assets/products/holosuite.png';
	import lightcage from '../assets/products/lightcage.png';
	import bluefish from '../assets/products/bluefish.png';
	import syncvv from '../assets/products/syncvv.png';
	import comingsoon from '../assets/products/comingsoon.png';
	import Device from 'svelte-device-info';
</script>

<section>
	<h1>PRODUCTS</h1>
	<div class="content">
		<input type="radio" id="All" name="categories" value="All" checked />
		<input type="radio" id="MotionCapture" name="categories" value="MotionCapture" />
		<input type="radio" id="VolumetricCapture" name="categories" value="VolumetricCapture" />
		<input type="radio" id="Photogrametry" name="categories" value="Photogrametry" />
		<input type="radio" id="ComingSoon" name="categories" value="ComingSoon" />

		<nav class={Device.isPhone || Device.isTablet ? 'navMobile' : 'nav'}>
			<h2>CATEGORY</h2>

			<ul class="localNavContainer">
				<li class="localNavContainerList"><label for="All">All</label></li>
				<li class="localNavContainerList">
					<label for="MotionCapture">モーションキャプチャー</label>
				</li>
				<li class="localNavContainerList">
					<label for="VolumetricCapture">ボリュメトリックキャプチャー</label>
				</li>
				<li class="localNavContainerList"><label for="Photogrametry">フォトグラフメトリ</label></li>
				<li class="localNavContainerList"><label for="ComingSoon">Coming soon</label></li>
			</ul>
		</nav>

		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			<li class="card" data-category="MotionCapture VolumetricCapture">
				<article>
					<figure>
						<a target="_blank" href="story1.png">
							<img src={vicon} alt="Vicon" width="400" height="200" />
						</a>
						<figcaption>
							<ol class="cardTags">
								<li>
									<a href="">モーションキャプチャー</a>
								</li>
								<li>
									<a href="">ボリュメトリックキャプチャー</a>
								</li>
							</ol>
							<p>Vicon</p>
							<span class="overflowed-text"
								>業界最高水準の光学反射式モーションキャプチャシステム</span
							>
						</figcaption>
					</figure>
				</article>
			</li>

			<li class="card" data-category="MotionCapture VolumetricCapture">
				<article>
					<figure>
						<a target="_blank" href="story2.png">
							<img src={fourdviews} alt="4d Views" width="400" height="200" />
						</a>
						<figcaption>
							<ol class="cardTags">
								<li>
									<a href="">モーションキャプチャー</a>
								</li>
								<li>
									<a href="">ボリュメトリックキャプチャー</a>
								</li>
							</ol>
							<p>4Dviews</p>
							<span class="overflowed-text">業界最高水準のボリュメトリックキャプチャシステム</span>
						</figcaption>
					</figure>
				</article>
			</li>

			<li class="card" data-category="VolumetricCapture Photogrametry">
				<article>
					<figure>
						<a target="_blank" href="story1.png">
							<img src={faceware} alt="Faceware" width="400" height="200" />
						</a>
						<figcaption>
							<ol class="cardTags">
								<li>
									<a href="">フォトグラフメトリ</a>
								</li>
								<li>
									<a href="">ボリュメトリックキャプチャー</a>
								</li>
							</ol>
							<p>Faceware</p>
							<span class="overflowed-text"
								>ビデオベースのフェイシャル専用モーションキャプチャーシステム</span
							>
						</figcaption>
					</figure>
				</article>
			</li>

			<li class="card" data-category="VolumetricCapture MotionCapture">
				<figure>
					<a target="_blank" href="story2.png">
						<img src={stretchsense} alt="StretchSense" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">モーションキャプチャー</a>
							</li>
							<li>
								<a href="">ボリュメトリックキャプチャー</a>
							</li>
						</ol>
						<p>StretchSense</p>
						<span class="overflowed-text"
							>シリコン素材の伸縮センサーを搭載したワイアレス対応グローブデバイス</span
						>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="VolumetricCapture Photogrametry">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={holosuite} alt="HoloSuite" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">フォトグラフメトリ</a>
							</li>
							<li>
								<a href="">ボリュメトリックキャプチャー</a>
							</li>
						</ol>
						<p>HoloSuite</p>
						<span class="overflowed-text">ボリュメトリックデータの編集・配信ソフトウェア群</span>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="VolumetricCapture Photogrametry">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={lightcage} alt="LightCage" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">フォトグラフメトリ</a>
							</li>
							<li>
								<a href="">ボリュメトリックキャプチャー</a>
							</li>
						</ol>
						<p>LightCage</p>
						<span class="overflowed-text">高精細フォトグラメトリスキャンシステム</span>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="Photogrametry">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={bluefish} alt="Bluefish444" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">フォトグラフメトリ</a>
							</li>
						</ol>
						<p>Bluefish444</p>
						<span class="overflowed-text"
							>Windows・Mac・Linux環境における業界最高品質HD-SDI入出力ボード</span
						>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="Photogrametry">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={syncvv} alt="SyncVV" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">フォトグラフメトリ</a>
							</li>
						</ol>
						<p>SyncVV</p>
						<span class="overflowed-text">運用負荷を大幅に軽減する頼れる収録再生システム</span>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="ComingSoon">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={comingsoon} alt="SyncVV" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">Coming soon</a>
							</li>
						</ol>
						<p>DIGITAL HUMAN</p>
						<span class="overflowed-text"
							>運昨今、 デジタルアバターはデジタルサイネージやSNS、
							メタバース空間といった場所や環境に捉われず活躍の場を広げています。</span
						>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="ComingSoon">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={comingsoon} alt="SyncVV" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">Coming soon</a>
							</li>
						</ol>
						<p>Robo-Geppei</p>
						<span class="overflowed-text"
							>Robo-Geppeiとは、カナダのAhead.io社が開発した四足歩行ロボットプラットフォームの総称です。</span
						>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="ComingSoon">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={comingsoon} alt="SyncVV" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">Coming soon</a>
							</li>
						</ol>
						<p>Multiverse</p>
						<span class="overflowed-text"
							>Multiverseは誰でも簡単に非破壊なワークフローで、非常に巨大な3Dデータセットを再生、レイアウト、ルックデブ、ライティング、レンダリングする事を可能にします。</span
						>
					</figcaption>
				</figure>
			</li>

			<li class="card" data-category="ComingSoon">
				<figure>
					<a target="_blank" href="story1.png">
						<img src={comingsoon} alt="SyncVV" width="400" height="200" />
					</a>
					<figcaption>
						<ol class="cardTags">
							<li>
								<a href="">Coming soon</a>
							</li>
						</ol>
						<p>MIST</p>
						<span class="overflowed-text"
							>MISTは、ビデオでもファイルシーケンスでも、あらゆる種類のプロジェクトに対応したDI（デジタルインターミディエイト）デッキです。</span
						>
					</figcaption>
				</figure>
			</li>
		</ul>
	</div>
</section>

<style>
	input[type='radio'] {
		position: absolute;
		left: -9999px;
	}

	/* localNavContainer
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	.localNavContainer {
		text-align: center;
		margin-bottom: 2rem;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}

	.localNavContainerList {
		cursor: pointer;
	}
	.localNavContainer * {
		display: inline-block;
	}

	.localNavContainer label {
		padding: 0.5rem 1rem;
		margin-bottom: 0.25rem;
		border-radius: 2rem;
		min-width: 50px;
		line-height: normal;
		cursor: pointer;
		transition: all 0.1s;
	}

	.localNavContainer label:hover {
		background: #49b293;
		color: #fff;
	}

	/* FILTERED ELEMENTS (POSTS)
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	.posts .cardTags {
		margin-bottom: 0.75rem;
		font-size: 0.75rem;
	}

	.posts .cardTags * {
		display: inline-block;
	}

	.posts .cardTags li {
		margin-bottom: 0.2rem;
	}

	.posts .cardTags a {
		padding: 0.2rem 0.5rem;
		border-radius: 1rem;
		border: 1px solid;
		line-height: normal;
	}

	.posts .cardTags a:hover {
		background: #49b293;
		color: #fff;
	}

	/* FILTERING RULES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	[value='All']:checked ~ nav .localNavContainer [for='All'],
	[value='MotionCapture']:checked ~ nav .localNavContainer [for='MotionCapture'],
	[value='VolumetricCapture']:checked ~ nav .localNavContainer [for='VolumetricCapture'],
	[value='Photogrametry']:checked ~ nav .localNavContainer [for='Photogrametry'],
	[value='ComingSoon']:checked ~ nav .localNavContainer [for='ComingSoon'] {
		background: #49b293;
		color: #fff;
	}

	[value='All']:checked ~ .posts [data-category] {
		display: block;
	}

	[value='MotionCapture']:checked ~ .posts .card:not([data-category~='MotionCapture']),
	[value='VolumetricCapture']:checked ~ .posts .card:not([data-category~='VolumetricCapture']),
	[value='Photogrametry']:checked ~ .posts .card:not([data-category~='Photogrametry']),
	[value='ComingSoon']:checked ~ .posts .card:not([data-category~='ComingSoon']) {
		display: none;
	}

	h1 {
		margin: 0;
		font-size: calc(32px + 0.390625vw);
	}
	h2 {
		padding-bottom: 1rem;
		border-bottom: 1px solid black;
	}
	section {
		padding: 5rem;
		background-color: #efefef;
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
	.content {
		display: flex;
		gap: 5rem;
		flex-wrap: wrap;
		flex-direction: row;
		margin-top: 2rem;
	}

	p {
		margin: 0;
		font-weight: bold;
	}

	ul,
	ol {
		margin: 0;
		padding: 0;
	}

	figure {
		margin: 0;
		width: inherit;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		border-radius: 8px;
		height: 100%;
	}
	.nav {
		width: 20%;
	}
	.navMobile {
		width: 100%;
		text-align: center;
	}
	.navMobile .localNavContainer {
		flex-direction: row;
		flex-wrap: wrap;
	}
	img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
		display: block;
		max-height: 170px;
		object-fit: cover;
	}
	figcaption {
		padding: 15px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		gap: 0.5rem;
		font-size: calc(11px + 0.390625vw);
		text-align: left;
		min-height: 120px;
	}
	.cardList {
		width: 70%;
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

	.cardList .card {
		display: flex;
		align-items: center;
		justify-content: center;
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
	@media screen and (max-width: 700px) {
		.content {
			flex-direction: column;
		}
		ul {
			flex-direction: column;
		}
	}
	@media screen and (max-width: 950px) {
		h1 {
			text-align: center;
		}
		section {
			padding: 2rem;
		}
		.content {
			flex-direction: column;
			gap: 1rem;
			justify-content: center;
			align-items: center;
		}
		.cardList {
			grid-template-columns: repeat(auto-fill, 15.5rem);
			margin: 0 auto;
			/* padding: 0 7vw 1.5vh 7vw; */
		}
		figcaption {
			font-size: calc(16px + 0.390625vw);
		}
		ul {
			flex-direction: column;
		}
	}
</style>
