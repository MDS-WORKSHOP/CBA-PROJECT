/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        title: '#091B62',
        subtitle: '#666975',
        button: '#0045B6',
        link: '#091B62'
      },
      fontFamily: {
        norms: ['"TT Norms Pro"', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

