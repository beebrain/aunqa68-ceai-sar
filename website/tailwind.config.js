module.exports = {
  content: ["./*.html", "./*.py"],
  darkMode: "class",
  theme: {
      extend: {
          "colors": {
              "tertiary-fixed": "#c8eaff",
              "inverse-surface": "#2e1a28",
              "on-tertiary-fixed": "#001a33",
              "on-surface": "#2e1a28",
              "tertiary-fixed-dim": "#80d0f0",
              "on-surface-variant": "#604868",
              "surface-tint": "#e040a0",
              "on-error-container": "#9b1c1c",
              "on-background": "#2e1a28",
              "error-container": "#ffe8e8",
              "primary": "#e040a0",
              "tertiary-container": "#40c0ee",
              "on-secondary-fixed": "#1a1030",
              "on-tertiary-fixed-variant": "#005580",
              "on-secondary": "#ffffff",
              "background": "#fef7ff",
              "outline": "#907898",
              "on-primary": "#ffffff",
              "primary-fixed-dim": "#f0a0cc",
              "surface-bright": "#fef7ff",
              "surface-container-high": "#f2e8f2",
              "primary-fixed": "#ffd6ee",
              "outline-variant": "#dcc8e0",
              "on-tertiary": "#ffffff",
              "surface-container": "#f8eef8",
              "primary-container": "#f080c0",
              "on-primary-fixed": "#3d0028",
              "on-secondary-fixed-variant": "#4a3068",
              "secondary-container": "#eedcff",
              "surface": "#fef7ff",
              "inverse-primary": "#f0a0cc",
              "surface-container-highest": "#ece2ec",
              "on-error": "#ffffff",
              "surface-variant": "#f2e8f2",
              "inverse-on-surface": "#fef7ff",
              "surface-dim": "#e0d6e0",
              "secondary-fixed-dim": "#c8a8e8",
              "on-primary-container": "#2e1a28",
              "error": "#e53e3e",
              "on-secondary-container": "#2e2040",
              "surface-container-low": "#fbf2fb",
              "secondary": "#7c52aa",
              "on-tertiary-container": "#00334d",
              "on-primary-fixed-variant": "#a02070",
              "tertiary": "#0096cc",
              "secondary-fixed": "#eedcff",
              "surface-container-lowest": "#ffffff"
          },
          "borderRadius": {
              "DEFAULT": "1rem",
              "lg": "2rem",
              "xl": "3rem",
              "full": "9999px"
          },
          "fontFamily": {
              "sans": ["Dm Sans", "sans-serif"],
              "headline": ["Dm Sans", "sans-serif"],
              "display": ["Dm Sans", "sans-serif"],
              "body": ["Dm Sans", "sans-serif"]
          },
          "animation": {
              "fade-in-up": "fade-in-up 0.5s ease-out forwards",
              "fade-in": "fade-in 0.5s ease-out forwards",
              "float": "float 3s ease-in-out infinite",
          },
          "keyframes": {
              "fade-in-up": {
                  "0%": { opacity: "0", transform: "translateY(20px)" },
                  "100%": { opacity: "1", transform: "translateY(0)" },
              },
              "fade-in": {
                  "0%": { opacity: "0" },
                  "100%": { opacity: "1" },
              },
              "float": {
                  "0%, 100%": { transform: "translateY(0)" },
                  "50%": { transform: "translateY(-10px)" },
              }
          }
      }
  }
}
