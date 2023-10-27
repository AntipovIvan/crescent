<script>
	let promise;
	const handleClick = () => {
		promise = fetch('http://172.31.4.199:7000/api/yourmodels', {
			cache: 'default'
		}).then((x) => x.json());
	};
</script>

<button on:click={handleClick}> Click to Load Data </button>

{#await promise}
	<!-- optionally show something while promise is pending -->
	<p>Loading...</p>
{:then data}
	{#if !data}
		<p>Nothing to see here</p>
	{:else}
		<!-- promise was fulfilled -->
		<pre>
      {JSON.stringify(data, null, 2)}
      <p>{JSON.stringify(data.results[0])}</p>
    </pre>
	{/if}
	<!-- <p>{data.results}</p> -->
{:catch error}
	<!-- optionally show something while promise was rejected -->
	<p>Nothing (rejected)</p>
{/await}
