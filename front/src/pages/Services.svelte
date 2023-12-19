<script>
	import Device from 'svelte-device-info';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';
	import fourdstudio from '../assets/services/4dstudioHero.jpg';
	import bodyLightcage from '../assets/services/lightcageFull.jpeg';
	import faceLightcage from '../assets/services/lightcageFace.png';

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
	<h1>スタジオサービス</h1>
	<div class="content">
		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			<li class="card">
				<article>
					<figure>
						<a href={`/services/4dstudio`} use:link>
							<img src={fourdstudio} alt="4dstudio" width="400" height="200" />
							<figcaption>
								<p>4DSTUDIO</p>
								<span class="overflowed-text"
									>4Dviews社 HOLOSYSを使用したボリュメトリックキャプチャスタジオ</span
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
						<a href={`/services/bodylightcage`} use:link>
							<img src={bodyLightcage} alt="bodylightcage" width="400" height="200" />
							<figcaption>
								<p>FullBodyLightCageスタジオ（全身用）</p>
								<span class="overflowed-text"
									>ESPER社 FullBodyLightCageを使用した高精細な3D全身メッシュスキャン</span
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
						<a href={`/services/facelightcage`} use:link>
							<img src={faceLightcage} alt="facelightcage" width="400" height="200" />
							<figcaption>
								<p>LightCageスタジオ（顔用）</p>
								<span class="overflowed-text"
									>ESPER社 LightCageを使用した高精細な3Dフェイスメッシュスキャン</span
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

	h1 {
		margin: 0;
		font-size: calc(32px + 0.390625vw);
	}
	section {
		padding: 5rem 8rem;
		background-color: #efefef;
	}
	.overflowed-text {
		margin: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 2;
		white-space: pre-wrap;
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
		height: 16vw;
		object-fit: cover;
	}
	figcaption {
		padding: 30px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		justify-content: space-between;
		text-align: left;
		height: 13rem;
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
		img {
			height: 60vw;
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
