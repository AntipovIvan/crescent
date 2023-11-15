<script>
	import Device from 'svelte-device-info';
	import { onMount } from 'svelte';
	import { link } from 'svelte-spa-router';
	import urlSlug from 'url-slug';

	let services;
	let error;

	onMount(async () => {
		try {
			// const response = await fetch('http://52.69.50.8:7000/api/productcardmodels');
			const response = await fetch(
				'http://' + window.location.hostname + ':7000/api/servicesmodels'
			);
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			services = results;
		} catch (err) {
			error = err;
		}
	});
</script>

<section>
	<h1>STUDIO SERVICES</h1>
	<div class="content">
		<ul class={Device.isPhone || Device.isTablet ? 'posts cardListMobile' : 'posts cardList'}>
			{#if services}
				{#each services as { id, title, content, category, thumbnail }, index}
					<li
						class="card"
						data-category={category === 'Coming soon' ? (category = 'ComingSoon') : category}
					>
						<article>
							<figure>
								<a href={`/services/${urlSlug(title)}`} use:link>
									<img
										src={thumbnail.replace('localhost:7000', window.location.hostname)}
										alt={title}
										width="400"
										height="200"
									/>

									<figcaption>
										<p>{title}</p>
										<span class="overflowed-text">{content}</span>
										<button class="more">
											<span class="viewMore">View more</span>
											<svg fill="#0b345b" viewBox="0 0 31.33 31.33" width="35">
												<path
													d="M15.667,0C7.029,0,0.001,7.028,0.001,15.667c0,8.64,7.028,15.667,15.666,15.667c8.639,0,15.666-7.027,15.666-15.667 C31.333,7.028,24.306,0,15.667,0z M18.097,23.047c-0.39,0.393-0.902,0.587-1.414,0.587s-1.022-0.194-1.414-0.587 c-0.781-0.779-0.781-2.047,0-2.827l2.552-2.553H8.687c-1.104,0-2-0.896-2-2c0-1.104,0.896-2,2-2h9.132l-2.552-2.552 c-0.781-0.781-0.781-2.047,0-2.828c0.78-0.781,2.048-0.781,2.828,0l7.381,7.381L18.097,23.047z"
												/>
											</svg>
										</button>
									</figcaption>
								</a>
							</figure>
						</article>
					</li>
				{/each}
			{:else}
				<p>Loading...</p>
			{/if}
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
		justify-content: flex-start;
		gap: 1rem;
		background-color: unset;
		border: none;
		cursor: pointer;
		color: var(--headers-color);
		width: 13rem;
		padding: 0;
		margin: 2rem 0 0 0;

		align-self: self-start;
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
