<script>
	import urlSlug from 'url-slug';
	import NotFound from './NotFound.svelte';
	import { onMount, setContext } from 'svelte';
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import Pagination from '../lib/Pagination.svelte';
	import Loading from '../lib/Loading.svelte';

	let blog;
	let error;
	let currentPage = 1;
	let totalPages = 1;
	const pageSize = 10;

	onMount(async () => {
		window.scrollTo(0, 0);
		try {
			const response = await fetch('http://' + window.location.hostname + ':7000/api/blog');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			const { results } = await response.json();

			results.sort((a, b) => {
				const dateA = a.date.toUpperCase();
				const dateB = b.date.toUpperCase();
				if (dateA < dateB) {
					return 1;
				}
				if (dateA > dateB) {
					return -1;
				}

				return 0;
			});
			blog = results;
			calculateTotalPages();
		} catch (err) {
			error = err;
		}
	});
	function calculateTotalPages() {
		totalPages = Math.ceil(blog.length / pageSize);
	}

	function onPageChange(page) {
		currentPage = page;
	}

	setContext('pagination', { currentPage, totalPages, onPageChange });
</script>

<section class="section">
	<h1>スタッフブログ</h1>
	<div class="content">
		<ul class="posts cardList">
			{#if blog}
				{#each blog.slice((currentPage - 1) * pageSize, currentPage * pageSize) as { id, date, title }, index}
					<li class="card">
						<article>
							<a href={`/blog/${urlSlug(id)}`} use:link class="cardLink">
								<time>{date.replaceAll('-', '.')}</time>
								<span class="cardTitle">{title}</span>
							</a>
						</article>
					</li>
				{/each}
			{:else}
				<Loading />
			{/if}
		</ul>
	</div>
	<Pagination {currentPage} {totalPages} {onPageChange} />
</section>

<style>
	.section {
		min-height: 53vh;
		position: relative;
	}
	input[type='radio'] {
		position: absolute;
		left: -9999px;
	}

	/* localNavContainer
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	.localNavContainer {
		text-align: center;
		margin: 1rem 0;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}

	.localNavContainerList {
		cursor: pointer;
		border: 1px solid #8b8b8b;
		color: #8b8b8b;
		margin: 0.5rem 0;
		border-radius: 25px;
	}
	.localNavContainer * {
		display: inline-block;
	}

	.localNavContainer label {
		padding: 0.5rem 1rem;
		/* margin-bottom: 0.25rem; */
		border-radius: 2rem;
		min-width: 50px;
		line-height: normal;
		cursor: pointer;
		transition: all 0.1s;
	}

	.localNavContainer label:hover {
		background: #0b345b;
		color: #fff;
	}

	/* FILTERED ELEMENTS (POSTS)
–––––––––––––––––––––––––––––––––––––––––––––––––– */

	.cardLink {
		font-size: calc(16px + 0.390625vw);
	}
	.cardTitle {
		margin-left: 3rem;
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
		background: #0b345b;
		color: #fff;
	}

	/* FILTERING RULES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
	/* [value='All']:checked ~ nav .localNavContainer [for='All'],
	[value='お知らせ']:checked ~ nav .localNavContainer [for='お知らせ'],
	[value='製品&開発情報']:checked ~ nav .localNavContainer [for='製品&開発情報'],
	[value='セミナー&イベント']:checked ~ nav .localNavContainer [for='セミナー&イベント'] {
		background: #0b345b;
		color: #fff;
	}

	[value='All']:checked ~ .posts [data-category] {
		display: block;
	}

	[value='お知らせ']:checked ~ .posts .card:not([data-category~='お知らせ']),
	[value='製品&開発情報']:checked ~ .posts .card:not([data-category~='製品情報']),
	[value='セミナー&イベント']:checked ~ .posts .card:not([data-category~='イベント']) {
		display: none;
	} */

	h1 {
		margin: 0 0 3rem 0;
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}
	h2 {
		padding-bottom: 1rem;

		width: max-content;
	}
	section {
		padding: 5rem;
		background-color: #efefef;
	}

	.content {
		display: flex;
		gap: 5rem;
		flex-wrap: wrap;
		flex-direction: row;
		margin-top: 2rem;
		margin-bottom: 5rem;
		align-items: baseline;
	}

	p {
		margin: 0;
		font-weight: bold;
	}

	ul {
		margin: 0;
		padding: 0;
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
		justify-content: center;
		column-gap: 1rem;
	}
	.cardList {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: flex-start;
		list-style: none;
		overflow: hidden;
		flex: 1;
	}

	.cardList .card {
		align-items: center;
		justify-content: center;
		padding: 2rem 0;
		border-bottom: 1.5px solid black;
		width: 100%;
	}

	@media screen and (max-width: 700px) {
		.content {
			flex-direction: column;
		}
		ul {
			flex-direction: column;
		}
		.cardTitle {
			margin-left: 1rem;
		}
		.cardLink {
			overflow: hidden;
			text-overflow: ellipsis;
			display: -webkit-box;
			-webkit-box-orient: vertical;
			-webkit-line-clamp: 1;
			white-space: pre-wrap;
		}
		.cardList .card {
			padding: 1rem 0;
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

		ul {
			flex-direction: column;
		}
	}
</style>
