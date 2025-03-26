/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html"],
  theme: {
    extend: {},
    colors: {
      bgprimary: "#12170e",
      bgsecondary: "#1D3416",
      action: "#90c623",
      body: "#f3f6f8",
      body2: "#d8e6df",
      accent: "#99b0a2",
      transparent: "transparent",
      inherit: "inherit",
    },
    fontFamily: {
      sans: ['"Funnel Sans"', "sans-serif"],
    },
  },
  plugins: [],
};
