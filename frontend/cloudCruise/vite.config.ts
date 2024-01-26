import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  define: {
    'process.env.VITE_BACKEND_API': JSON.stringify(process.env.VITE_BACKEND_API)
  },
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0'
  },
  build: {
    assetsDir: 'static'
    // outDir: process.env.VITE_OUTPUT_DIR ? process.env.VITE_OUTPUT_DIR : "dist",
  }
})
