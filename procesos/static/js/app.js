let pasos = [];

function agregarPaso() {
    const input = document.getElementById("paso");
    const lista = document.getElementById("lista");

    if (input.value.trim() === "") return;

    pasos.push(input.value);

    const li = document.createElement("li");
    li.textContent = input.value;

    lista.appendChild(li);

    input.value = "";
}