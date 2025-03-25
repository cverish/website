/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html"],
  theme: {
    extend: {},
    colors: {
      bgprimary: "#12170e",
      bgsecondary: "#1D3416",
      action: "#84B12B",
      body: "#F0F3F4",
      body2: "#C5D2CB",
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
