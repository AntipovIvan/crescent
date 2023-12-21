<script>
	import urlSlug from 'url-slug';
	import NotFound from './NotFound.svelte';
	import { onMount, setContext } from 'svelte';
	import { link } from 'svelte-spa-router';
	import Device from 'svelte-device-info';
	import Pagination from '../lib/Pagination.svelte';
	import Loading from '../lib/Loading.svelte';

	let usercase;
	let error;
	let currentPage = 1;
	let totalPages = 1;
	const pageSize = 10;

	onMount(async () => {
		window.scrollTo(0, 0);
		try {
			const response = await fetch('http://' + window.location.hostname + ':7000/api/usercase');
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
			usercase = results;
			calculateTotalPages();
		} catch (err) {
			error = err;
		}
	});
	function calculateTotalPages() {
		totalPages = Math.ceil(usercase.length / pageSize);
	}

	function onPageChange(page) {
		currentPage = page;
	}

	setContext('pagination', { currentPage, totalPages, onPageChange });
</script>

<section class="section">
	<h1>ピックアップ&ユーザー事例</h1>
	<div class="content">
		<ul class="posts cardList">
			{#if usercase}
				{#each usercase.slice((currentPage - 1) * pageSize, currentPage * pageSize) as { id, date, title }, index}
					<li class="card">
						<article>
							<a href={`/usercase/${urlSlug(id)}`} use:link class="cardLink">
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

	.cardLink {
		font-size: calc(16px + 0.390625vw);
		text-decoration: none;
	}
	.cardTitle {
		margin-left: 3rem;
	}

	h1 {
		margin: 0 0 3rem 0;
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
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
