module.exports = {
  purge: {
    content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}']
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    screens: {
      xxs: '380px',
      mxs: '425px',
      xs: '475px',
      xsm: '540px',
      sm: '670px',
      // => @media (min-width: 640px) { ... }

      md: '800px',
      // => @media (min-width: 768px) { ... }

      lg: '1038px',
      // => @media (min-width: 1024px) { ... }

      xl: '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1550px'
      // => @media (min-width: 1536px) { ... }
    },
    extend: {
      animation: {
        marquee: 'marquee 30s linear infinite'
      },
      keyframes: {
        marquee: {
          '-100%': { transform: 'translateX(0%)' },
          '0%': { transform: 'translateX(-100%)' }
        }
      },

      colors: {
        light: {
          400: '#fde9e9;',
          500: '#fcdedf;',
          600: '#f8babc;'
        },
        primary: {
          400: '#ea2127;',
          500: '#d31e23;',
          600: '#bb1a1f;'
        },
        secondary: {
          400: '#b0191d;',
          500: '#8c1417;',
          600: '#690f12;',
          700: '#520c0e;'
        }
      }
    }
  },
  variants: {
    extend: {
      fontFamily: {
        Poppins: ['"Poppins"', 'sans-serif']
      }
    }
  },
  plugins: []
}
