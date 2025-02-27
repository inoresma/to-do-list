// tailwind.config.js
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'media', // Updated from 'false' to 'media'
  theme: {
    extend: {
      colors: {
        'text': '#0c0d13',
        'background': '#f8f9fc',
        'primary': '#3b54ce',
        'secondary': '#8192ee',
        'accent': '#3f5ef8',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}