document.addEventListener("DOMContentLoaded", () => {
    cargarElementos().then(() => console.log('cargo'));
});

async function cargarElementos() {
    await element_html("../static/components/navbar.html", ".navbar");
    await element_html("../static/components/header.html", ".header");
    await element_html("../static/components/main.html", ".main");
    evaluate_button_search();
}

async function element_html(route, classnames) {
    const response = await fetch(route);
    document.querySelector(classnames).innerHTML = await response.text();
}

function evaluate_button_search() {
    const formulario = document.getElementById("formulario-busqueda");
    if (formulario) {
        formulario.addEventListener('submit', function (event) {
            event.preventDefault(); // evitar que se recargue la página
            const url = construirURL(document.getElementById('tipo').value, document.getElementById('nombre').value);
            fetch_value(url);
        });
    }
}


function construirURL(tipo, nombre) {
    switch (tipo) {
        case "character":
            return "character/information/" + nombre;
        case "fusion":
            return "fusion/information/" + nombre;
        case "videogame":
            return "videogame/information/" + nombre;
        case "planet":
            return "planet/information/" + nombre;
        case "saga":
            return "saga/information/" + nombre;
        default:
            return "";
    }
}

function fetch_value(url) {
    fetch(url)
        .then(response => response.json())
        .then(resultados => {
            $("#resultados").JSONView(resultados);
        })
        .catch(error => console.error(error));
}