import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '0.0.0.0',
    hmr: {
      clientPort: 8080,
    },
    port: 8080,
    watch: {
      usePolling: true,
    },
  },
});
