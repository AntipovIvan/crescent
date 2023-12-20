<script>
	import Device from 'svelte-device-info';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';
	import appdev from '../assets/development/contentAppThumb.jpg';
	import support from '../assets/development/contentSupportThumb.jpg';
	import plugin from '../assets/development/contentPluginThumb.jpg';

	// let services;
	let error;

	// onMount(async () => {
	// 	try {
	// 		const response = await fetch(
	// 			'http://' + window.location.hostname + ':7000/api/servicesmodels'
	// 		);
	// 		if (!response.ok) {
	// 			throw new Error('Network response was not ok');
	// 		}
	// 		const { results } = await response.json();

	// 		services = results;
	// 	} catch (err) {
	// 		error = err;
	// 	}
	// });
</script>

<section>
	<h1>コンテンツ開発</h1>
	<div class="content">
		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			<li class="card">
				<article>
					<figure>
						<a href={`/development/appdev`} use:link>
							<img src={appdev} alt="appdev" width="400" height="200" />

							<!-- svelte-ignore a11y-structure -->
							<figcaption>
								<p>アプリケーション制作</p>
								<span class="overflowed-text"
									>経験豊富なエンジニアが最新の スタジオ機器を活用して個々のご注文に答えるユニークな
									VR/MR/ARアプリケーション制作 をいたします。</span
								>
								<button class="more">
									<span class="viewMore">VIEW MORE</span>
									<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
										<circle cx="12" cy="12" r="12" fill="#313132" />
										<path
											d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
											fill="white"
										/>
									</svg>
								</button>
							</figcaption>
						</a>
					</figure>
				</article>
			</li>

			<li class="card">
				<article>
					<figure>
						<a href={`/development/support`} use:link>
							<img src={support} alt="support" width="400" height="200" />

							<!-- svelte-ignore a11y-structure -->
							<figcaption>
								<p>映像企画・制作サポート</p>
								<span class="overflowed-text"
									>最新の映像技術を使用した高機 能な映像を制作するには、企画段
									階からのエンジニアの参画が不可 欠です。
									<br /><br />
									自社スタジオにおいて日々開 発・実験に取り組んでいる経験豊 富な技術スタッフが先端技術の導
									入をサポートします。
								</span>
								<button class="more">
									<span class="viewMore">VIEW MORE</span>
									<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
										<circle cx="12" cy="12" r="12" fill="#313132" />
										<path
											d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
											fill="white"
										/>
									</svg>
								</button>
							</figcaption>
						</a>
					</figure>
				</article>
			</li>

			<li class="card">
				<article>
					<figure>
						<a href={`/development/plugindev`} use:link>
							<img src={plugin} alt="Plugin" width="400" height="200" />

							<!-- svelte-ignore a11y-structure -->
							<figcaption>
								<p>インタラクティブプラグイン開発</p>
								<span class="overflowed-text"
									>お客様の既存のシステム/Webサ イトに、モーションキャプチャー/
									ボリュメトリック技術を生かした 3D/4D映像を組み込むために不可欠 な、オリジナル API
									/ プラグインを 開発いたします。</span
								>
								<button class="more">
									<span class="viewMore">VIEW MORE</span>
									<svg width="28" height="28" viewBox="0 0 24 24" fill="none">
										<circle cx="12" cy="12" r="12" fill="#313132" />
										<path
											d="M12.9561 7.64645C12.7608 7.45118 12.4442 7.45118 12.249 7.64645C12.0537 7.84171 12.0537 8.15829 12.249 8.35355L15.998 12.1025L12.249 15.8515C12.0537 16.0468 12.0537 16.3634 12.249 16.5586C12.4442 16.7539 12.7608 16.7539 12.9561 16.5586L16.7168 12.798C17.1008 12.4139 17.1008 11.7912 16.7168 11.4071L12.9561 7.64645ZM8 11.5C7.72386 11.5 7.5 11.7239 7.5 12C7.5 12.2761 7.72386 12.5 8 12.5H12C12.2761 12.5 12.5 12.2761 12.5 12C12.5 11.7239 12.2761 11.5 12 11.5H8Z"
											fill="white"
										/>
									</svg>
								</button>
							</figcaption>
						</a>
					</figure>
				</article>
			</li>
		</ul>
	</div>
</section>

<style>
	article {
		height: 100%;
	}
	.more {
		display: flex;
		align-items: center;
		justify-content: flex-end;
		gap: 1rem;
		background-color: unset;
		border: none;
		cursor: pointer;
		color: var(--headers-color);
		width: 13rem;
		padding: 0;
		margin: 2rem 0 0 0;
		align-self: self-end;
	}
	.viewMore {
		font-size: calc(12px + 0.390625vw);
	}

	.posts a {
		text-decoration: none;
	}

	h1 {
		margin: 0;
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}
	section {
		padding: 5rem 8rem;
		background-color: #efefef;
	}
	.overflowed-text {
		margin: 0;
	}
	.content {
		display: flex;
		gap: 5rem;
		flex-wrap: wrap;
		flex-direction: row;
		margin-top: 5rem;
	}

	p {
		margin: 0;
		font-weight: bold;
	}

	ul {
		display: flex;
		gap: 3rem;
		justify-content: space-between;
		padding: 0;
		margin: 0;
	}
	a:hover {
		color: unset;
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
	img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
		display: block;
		height: 300px;
		object-fit: cover;
	}
	figcaption {
		padding: 30px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		justify-content: space-between;
		text-align: left;
	}
	figcaption p {
		font-size: calc(18px + 0.390625vw);
	}
	figcaption span {
		font-size: calc(14px + 0.390625vw);
	}

	.cardList .card {
		display: flex;
		align-items: center;
		justify-content: center;
		width: -webkit-fill-available;
		width: 100%;
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
		}
		figcaption {
			font-size: calc(16px + 0.390625vw);
		}
		ul {
			flex-direction: column;
		}
	}
</style>
