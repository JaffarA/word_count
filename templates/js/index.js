(function(){
    
    if (!("theme" in localStorage)) {
        localStorage.theme = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? 'dark' : 'light';
    }

    if (localStorage.theme == "dark") {
        document.querySelector("html").className = "dark"
    } else {
        document.querySelector("html").className = "light"
    }

    const set_theme_toggle_button_text = text => document.querySelector("#theme-toggle").textContent = text

    const toggle_colour_scheme = () => {
        if (localStorage.theme == "light") {
            document.querySelector("html").className = "dark"
            localStorage.theme = "dark"
            set_theme_toggle_button_text("toggle lightmode")
        } else {
            document.querySelector("html").className = "light"
            localStorage.theme = "light"
            set_theme_toggle_button_text("toggle darkmode")
        }
    }
    
    const fix_apostrophes = () => {
        const regex_replace_expressions = [/\s(\')/g, /(\')\s/g]
        Array.from(document.querySelectorAll(".first-sentence")).forEach(e => regex_replace_expressions.forEach(r => e.innerHTML = e.innerHTML.replace(r, "$1")))
        Array.from(document.querySelectorAll("div.collapse > div")).forEach(e => regex_replace_expressions.forEach(r => e.innerHTML = e.innerHTML.replace(r, "$1")))
    }
    
    document.addEventListener("DOMContentLoaded", () => {
        fix_apostrophes()
        set_theme_toggle_button_text((localStorage.theme == "light") ? "toggle darkmode" : "toggle lightmode")
        document.querySelector("#theme-toggle").addEventListener("click", toggle_colour_scheme)
    })
    
})();