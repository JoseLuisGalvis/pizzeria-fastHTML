// scripts.js:
document.addEventListener("DOMContentLoaded", function () {
  AOS.init();

  // Alternar el modo oscuro y guardar el estado en localStorage
  document
    .getElementById("darkModeToggle")
    .addEventListener("click", function () {
      document.body.classList.toggle("dark-mode");

      // Guarda la preferencia del usuario
      if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("darkMode", "enabled");
      } else {
        localStorage.setItem("darkMode", "disabled");
      }
    });

  // Mantener la preferencia al recargar la página
  if (localStorage.getItem("darkMode") === "enabled") {
    document.body.classList.add("dark-mode");
  }

  // Gestion de Pedidos
  let pedido = [];

  // Agregra pedido
  document.querySelectorAll(".agregar-al-pedido").forEach((button) => {
    button.addEventListener("click", function () {
      const nombre = this.getAttribute("data-nombre");
      const precio = parseFloat(this.getAttribute("data-precio"));

      // Mostrar el nombre y precio del producto en el modal
      document.getElementById("productoNombre").textContent = nombre;
      document.getElementById(
        "productoPrecio"
      ).textContent = `$${precio.toFixed(2)}`;

      // Abrir el modal
      const cantidadInput = document.getElementById("cantidadInput");
      cantidadInput.value = 1; // Reiniciar a 1 cada vez que se abre el modal

      const pedidoModal = new bootstrap.Modal(
        document.getElementById("pedidoModal")
      );
      pedidoModal.show();

      // Al hacer clic en "Agregar al Pedido" dentro del modal
      document.getElementById("agregarAlPedido").onclick = function () {
        const cantidad = parseInt(cantidadInput.value);
        if (cantidad > 0) {
          pedido.push({ nombre, precio, cantidad });
          actualizarPedido();
          pedidoModal.hide(); // Cerrar el modal
        } else {
          alert("Por favor, ingrese una cantidad válida.");
        }
      };
    });
  });

  // Actualizar Pedido
  function actualizarPedido() {
    const listaPedido = document.getElementById("listaPedido");
    listaPedido.innerHTML = "";
    let total = 0;

    pedido.forEach((item) => {
      const totalItem = item.precio * item.cantidad;
      total += totalItem;
      const li = document.createElement("li");
      li.className = "list-group-item";
      li.textContent = `${item.cantidad} x ${
        item.nombre
      } - $${totalItem.toFixed(2)}`;
      listaPedido.appendChild(li);
    });

    document.getElementById(
      "totalPedido"
    ).textContent = `Total: $${total.toFixed(2)}`;

    // Habilitar/Deshabilitar botón de enviar pedido según si hay elementos en el pedido
    document.getElementById("enviarPedido").disabled = pedido.length === 0;
  }

  // Ver pedido
  document.getElementById("verPedido").addEventListener("click", function () {
    const verPedidoModal = new bootstrap.Modal(
      document.getElementById("verPedidoModal") // Cambiado aquí
    );
    verPedidoModal.show();
    actualizarPedido();
  });

  // Enviar Pedido por Whatsapp
  function enviarPedidoWhatsApp() {
    let mensaje = "Hola, quiero realizar el siguiente pedido:\n";
    let total = 0;

    pedido.forEach((item) => {
      mensaje += `${item.cantidad} x ${item.nombre} - $${(
        item.precio * item.cantidad
      ).toFixed(2)}\n`;
      total += item.precio * item.cantidad;
    });

    mensaje += `\nTotal: $${total.toFixed(
      2
    )}\nPago en efectivo y con delivery propio del negocio.`;

    const numeroWhatsApp = "1234567890"; // Reemplaza con el número de WhatsApp del local
    const url = `https://wa.me/${numeroWhatsApp}?text=${encodeURIComponent(
      mensaje
    )}`;

    window.open(url, "_blank");
  }

  // Validaciones de Formulario
  function validarNombreApellido(event) {
    const regex = /^[A-Za-záéíóúñÑ ]+$/;
    if (!regex.test(event.target.value)) {
      event.target.setCustomValidity("Solo se permiten letras en este campo");
      alert("Por favor, ingrese solo letras en el campo de Nombre.");
    } else {
      event.target.setCustomValidity("");
    }
  }

  document.getElementById("inputPhone").addEventListener("input", function (e) {
    if (!/^[0-9]*$/.test(e.target.value)) {
      e.target.value = e.target.value.replace(/[^0-9]/g, "");
      alert("Por favor, ingrese solo números en el campo de Teléfono.");
    }
  });

  document.addEventListener("contextmenu", function (event) {
    event.preventDefault();
  });

  document.addEventListener("keydown", function (event) {
    if (event.ctrlKey && (event.key === "u" || event.key === "U")) {
      event.preventDefault();
    }
  });

  (function () {
    // Reemplaza "tu_user_id" con tu User ID de EmailJS
    emailjs.init("ZFNa8J5Ckf-Cv-kv1");
  })();

  document
    .getElementById("contactForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      const form = this; // Guardar referencia al formulario

      emailjs.sendForm("service_hc1g5ck", "template_omfi5rs", this).then(
        function () {
          console.log("Mensaje Enviado con Éxito!");
          alert("Mensaje Enviado con Éxito");

          // Limpiar el formulario después de enviarlo con éxito
          form.reset();
        },
        function (error) {
          console.log("Error al Enviar el Mensaje", error);
          alert("Error al Enviar el Mensaje");
        }
      );
    });
});
