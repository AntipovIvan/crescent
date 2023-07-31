<script>
	import { onMount } from 'svelte';
	import { createScene } from './scene';
	let el;
	onMount(() => {
		createScene(el);
	});
</script>

<canvas bind:this={el} />

<style lang="sass">
    canvas 
        width: 100vw
        height: 100vh
        display: block
</style>
