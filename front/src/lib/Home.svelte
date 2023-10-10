<script lang="ts">
	import Card from './Card.svelte';

	let promise;

	promise = fetch('http://localhost:7000/api/yourmodels', {
		cache: 'default'
	}).then((x) => x.json());
	console.log(promise);
</script>

<h1>Vite + Svelte</h1>

<div class="card">
	{#await promise}
		<p>Loading...</p>
	{:then data}
		{#if !data}
			<p>Nothing to see here</p>
		{:else}
			{#each data.results as result, i}
				<Card field1={result.field1} description={result.field2} image={result.cover} />
			{/each}
		{/if}
	{:catch error}
		<p>Nothing (rejected)</p>
	{/await}
</div>
