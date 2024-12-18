import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        credentials: 'include'
      },
      '/media': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
