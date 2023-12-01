<script>
	export let params = null;
</script>

<h2>Loading</h2>
{#if params && params.message}
	<p id="loadingmessage">Loading...</p>
{/if}
