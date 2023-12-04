<script>
	export let currentPage;
	export let totalPages;
	export let onPageChange;

	const pageRange = 1;
</script>

<nav>
	<button class:disabled={currentPage === 1} on:click={() => onPageChange(currentPage - 1)}>
		&#10094;
	</button>

	{#if currentPage - pageRange > 1}
		<button on:click={() => onPageChange(1)}>1</button>
		<li class="ellipsis">
			{'... '}
		</li>
	{/if}

	<ul>
		{#each Array.from({ length: totalPages }, (_, i) => i + 1) as page}
			{#if page >= currentPage - pageRange && page <= currentPage + pageRange}
				<li class:selected={currentPage === page} on:click={() => onPageChange(page)}>
					{page}
				</li>
			{/if}
		{/each}
	</ul>

	{#if currentPage + pageRange < totalPages}
		<li class="ellipsis">
			{'... '}
		</li>
		<button on:click={() => onPageChange(totalPages)}>
			{totalPages}
		</button>
	{/if}

	<button
		class:disabled={currentPage === totalPages}
		on:click={() => onPageChange(currentPage + 1)}
	>
		&#10095;
	</button>
</nav>

<style>
	.disabled {
		display: none;
	}
	.selected {
		color: #929292;
		border-bottom: 1px solid #929292;
	}
	nav {
		width: fit-content;
		margin: 0 auto;
		display: flex;
		gap: 1rem;
		justify-content: center;
		align-items: center;
		border-bottom: 1px solid black;
		font-size: 24px;
		position: absolute;
		bottom: 1rem;
		left: 50%;
		transform: translateX(-50%);
	}
	ul {
		display: flex;
	}
	li {
		cursor: pointer;
		padding: 0 1rem;
		list-style-type: none;
	}
	.ellipsis {
		padding: 0;
	}
	button {
		font-size: 20px;
		border: none;
		cursor: pointer;
	}
</style>
