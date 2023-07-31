<!-- https://svelte.dev/repl/98ec1a9a45af4d75ac5bbcb1b5bcb160?version=3.20.1 -->
<script>
  let promise;
  const handleClick = () => {
    promise = fetch('http://localhost:7000/api/yourmodels').then((x) => x.json());
  };
</script>

<button on:click={handleClick}> Click to Load Data </button>

{#await promise}
  <!-- optionally show something while promise is pending -->
  <p>Loading...</p>
{:then data}
  <!-- promise was fulfilled -->
  <pre>
        {JSON.stringify(data, null, 2)}
    </pre>
  <!-- <p>{data.results}</p> -->
{:catch error}
  <!-- optionally show something while promise was rejected -->
  <p>Nothing</p>
{/await}
