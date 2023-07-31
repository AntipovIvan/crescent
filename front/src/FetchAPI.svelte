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
