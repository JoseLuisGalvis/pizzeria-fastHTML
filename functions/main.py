# main.py
# uvicorn main:app --reload

from fasthtml.common import *
from fasthtml.components import (
    HTML, Head, BODY, Title, Meta, Link, Script, Nav, H1, H2, H3, H4, A, P,
    Button, Section, IMG, Div, FORM, INPUT, TEXTAREA, FOOTER, SPAN, Iframe, Ul, Li, Label
)
from fastapi.responses import FileResponse
from fast_html import *


# Crear la aplicación y el enrutador
btlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css", type="text/css")
app, rt = fast_app(hdrs=[btlink])

# Ruta para servir archivos estáticos
@app.get("/static/{fname:path}")
def serve_static(fname: str):
    return FileResponse(f'static/{fname}')

@rt('/contact')
def contact():
    return P('Formulario de Contacto Aquí')

def create_head():
    return Head(
        Title('Pizzería Don Remolo - Menú Online'),
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"),
        Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css'),
        Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.1/aos.css"),
        Link(rel='stylesheet', href='/static/css/styles.css'),
        Script(src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'),
        Script(src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js'),
        Script(src='https://unpkg.com/aos@2.3.1/dist/aos.js'),
        Script(src='https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.1/aos.js'),
        Script(src='/static/scripts.js'),
        Script(src='https://cdn.emailjs.com/dist/email.min.js', type='text/javascript') 
    )

def create_navbar():
    return Nav(id='home', cls='navbar navbar-expand-lg navbar-dark bg-dark fixed-top')(
        Div(cls='container')(
            A(cls='navbar-brand d-flex align-items-center', href='#')(
                IMG(id='logo', src='static/images/logo.jpg', alt='Logo', cls='me-2'),
                H4('Pizzería Don Remolo', cls='text-white mb-0')
            ),
            Button(
                cls='navbar-toggler',
                type='button',
                data_bs_toggle='collapse',
                data_bs_target='#navbarNav',
                aria_controls='navbarNav',
                aria_expanded='false',
                aria_label='Toggle navigation'
            )(
                Span(cls='navbar-toggler-icon')
            ),
            Div(cls='collapse navbar-collapse justify-content-center', id='navbarNav')(
                Ul(cls='navbar-nav')(
                    Li(cls='nav-item')(
                        A('Inicio', cls='nav-link', href='#hero')
                    ),
                    Li(cls='nav-item')(
                        A('Nosotros', cls='nav-link', href='#about')
                    ),
                    Li(cls='nav-item dropdown')(
                        A('Menú', cls='nav-link dropdown-toggle', href='#menu', id='navbarDropdown', role='button', data_bs_toggle='dropdown', aria_expanded='false'),
                        Ul(cls='dropdown-menu', aria_labelledby='navbarDropdown')(
                            Li()(A('Pizzas', cls='dropdown-item', href='#menu_1')),
                            Li()(A('Empanadas', cls='dropdown-item', href='#menu_2')),
                            Li()(A('Bebidas', cls='dropdown-item', href='#menu_3')),
                            Li()(A('Postres', cls='dropdown-item', href='#menu_4'))
                        )
                    ),
                    Li(cls='nav-item')(
                        A('Contacto', cls='nav-link', href='#contacto')
                    )
                )
            ),
            Button('Ver Pedido', cls='btn btn-orange text-white', id='verPedido'),
            Button(cls='toggle-button m-2', id='darkModeToggle', aria_label='Toggle dark mode')(
                I(cls='fas fa-sun sun-icon'),
                I(cls='fas fa-moon moon-icon')
            )
        )
    )

def create_hero():
    return Div(
        Section(id='hero', cls='hero-section section-vh-100')(
            Div(cls='container')(
                Div(cls='row align-items-center')(
                    Div(cls='col-md-6', 
                        data_aos="zoom-in", 
                        data_aos_duration="3000", 
                        data_aos_delay="400")(
                        H2('Don Remolo, La Mejor Pizza', cls='title text-shadow'),
                        H3('¡Haz que tu día sea estupendo con nuestras Pizzas Especiales!', cls='subtitle text-shadow'),
                        P('Bienvenido a nuestro paraíso de la Pizza, donde cada una cuenta una historia y desata tu alegría.', cls='text-white text-shadow'),
                        Div(cls='buttons')(
                            A('Ordena Ahora', href='#menu_1', cls='btn btn-orange text-white', 
                              data_aos="zoom-in", data_aos_duration="3000", data_aos_delay="400"),
                            A('Contáctanos', href='#contacto', cls='btn btn-outline-secondary mx-2', 
                              data_aos="zoom-in", data_aos_duration="3000", data_aos_delay="400")
                        )
                    )
                )
            )
        )
    )


def create_about():
    return Div(
        Section(id='about', cls='about-section section-vh-100')(
            Div(cls='container')(
                Div(cls='row align-items-center')(
                    Div(cls='col-md-6', 
                        data_aos="zoom-in", 
                        data_aos_duration="3000", 
                        data_aos_delay="400")(
                        IMG(src='static/images/pizza.jpg', alt='pizzeria', cls='img-fluid')
                    ),
                    Div(cls='col-md-6', 
                        data_aos="zoom-in", 
                        data_aos_duration="3000", 
                        data_aos_delay="400")(
                        H2('Nosotros', cls='section-title'),
                        P('En Pizzeria Don Rémolo, nos enorgullecemos de ser un destino para los amantes de la Pizza y la conversación amena. Nos dedicamos a ofrecer una experiencia gastronómica excepcional en un ambiente acogedor, donde los clientes pueden relajarse, descansar y disfrutar de la calidad de nuestros platos.', cls='text'),
                        Div(cls='social-link-list')(
                            A('Facebook', href='#', cls='btn btn-outline-secondary me-2 fw-bold'),
                            A('Instagram', href='#', cls='btn btn-outline-secondary me-2 fw-bold'),
                            A('Twitter', href='#', cls='btn btn-outline-secondary fw-bold')
                        )
                    )
                )
            )
        )
    )

def menu_1():
    return Div(id='menu_1', cls='container mt-5')(
        H2('Menú', id='menu-title', cls='text-center mt-5 mb-5'),
        Section(
            id='pizzas', 
            data_aos="zoom-in", 
            data_aos_duration="3000", 
            data_aos_delay="400"
        )(
            H2('Pizzas', cls='mb-4'),
            Div(cls='row d-flex align-items-stretch')(
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/margarita.png', cls='card-img-top', alt='Pizza Margarita'),
                        Div(cls='card-body')(
                            H5('Pizza Margarita', cls='card-title'),
                            P('Deliciosa pizza con tomate, mozzarella y albahaca.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='Pizza Margarita', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/vegetariana.png', cls='card-img-top', alt='Pizza Vegetariana'),
                        Div(cls='card-body')(
                            H5('Pizza Vegetariana', cls='card-title'),
                            P('Opción fresca y colorida, cargada de verduras como pimientos, champiñones, cebollas y aceitunas.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='Pizza Vegetariana', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/pepperoni.png', cls='card-img-top', alt='Pizza Pepperoni'),
                        Div(cls='card-body')(
                            H5('Pizza Pepperoni', cls='card-title'),
                            P('Pizza americana cubierta con rodajas de salami picante, que le da un toque crujiente y sabroso.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='Pizza Pepperoni', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/cuatro_quesos.png', cls='card-img-top', alt='Pizza Cuatro Quesos'),
                        Div(cls='card-body')(
                            H5('Pizza Cuatro Quesos', cls='card-title'),
                            P('Combinación de quesos que incluye mozzarella, gorgonzola, parmesano y ricotta.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='Pizza Cuatro Quesos', 
                                data_precio='10.99'
                            )
                        )
                    )
                )
            )
        )
    )


def menu_2():
    return Div(id='menu_2', cls='container mt-5')(
        H2('Menú', id='menu-title', cls='text-center mt-5 mb-5'),
        Section(
            id='empanadas', 
            data_aos="zoom-in", 
            data_aos_duration="3000", 
            data_aos_delay="400"
        )(
            H2('Empanadas', cls='mb-4'),
            Div(cls='row d-flex align-items-stretch')(
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/emp-carne.png', cls='card-img-top', alt='carne', id='emp-img'),
                        Div(cls='card-body')(
                            H5('Carne', cls='card-title'),
                            P('Empanadas de Carne.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='Pizza Margarita', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/emp-pollo.jpg', cls='card-img-top', alt='pollo', id='emp-img'),
                        Div(cls='card-body')(
                            H5('Pollo', cls='card-title'),
                            P('Empanadas de Pollo.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='pollo', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/emp-queso.jpg', cls='card-img-top', alt='queso', id='emp-img'),
                        Div(cls='card-body')(
                            H5('Queso', cls='card-title'),
                            P('Empanadas de Queso.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='queso', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/emp-jamque.jpg', cls='card-img-top', alt='jamon y queso', id='emp-img'),
                        Div(cls='card-body')(
                            H5('Jamon y Queso', cls='card-title'),
                            P('Empanadas de Jamon y Queso.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='jamon y queso', 
                                data_precio='10.99'
                            )
                        )
                    )
                )
            )
        )
    )

def menu_3():
    return Div(id='menu_3', cls='container mt-5')(
        H2('Menú', id='menu-title', cls='text-center mt-5 mb-5'),
        Section(
            id='bebidas', 
            data_aos="zoom-in", 
            data_aos_duration="3000", 
            data_aos_delay="400"
        )(
            H2('Bebidas', cls='mb-4'),
            Div(cls='row d-flex align-items-stretch')(
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/refrescos.png', cls='card-img-top', alt='refrescos'),
                        Div(cls='card-body')(
                            H5('Refrescos', cls='card-title'),
                            P('Pepsi, Coca Cola, Fanta, Sprite, Pomelo.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='refrescos', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/agua.png', cls='card-img-top', alt='agua'),
                        Div(cls='card-body')(
                            H5('Agua', cls='card-title'),
                            P('Agua Mineral Envasada.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='agua', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/cafe.png', cls='card-img-top', alt='cafe'),
                        Div(cls='card-body')(
                            H5('Cafe', cls='card-title'),
                            P('Café Latte, Mokachino, Negro, Cortado.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='cafe', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/cerveza.png', cls='card-img-top', alt='cervezas'),
                        Div(cls='card-body')(
                            H5('Cervezas', cls='card-title'),
                            P('Cervezas Tradicionales y Artesanales.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='cerveza', 
                                data_precio='10.99'
                            )
                        )
                    )
                )
            )
        )
    )
    
def menu_4():
    return Div(id='menu_4', cls='container mt-5')(
        H2('Menú', id='menu-title', cls='text-center mt-5 mb-5'),
        Section(
            id='postres', 
            data_aos="zoom-in", 
            data_aos_duration="3000", 
            data_aos_delay="400"
        )(
            H2('Postres', cls='mb-4'),
            Div(cls='row')(
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/cake.png', cls='card-img-top', alt='tarta'),
                        Div(cls='card-body')(
                            H5('Tarta de Chocolate', cls='card-title'),
                            P('Deliciosa tarta elaborada con una base de galleta y un relleno cremoso de chocolate negro.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='tarta', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/flan.png', cls='card-img-top', alt='flan'),
                        Div(cls='card-body')(
                            H5('Flan de Caramelo', cls='card-title'),
                            P('Postre de origen español, hecho a base de huevos, leche y azúcar, con una capa de caramelo en la parte superior.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='flan', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/fruit.png', cls='card-img-top', alt='mousse'),
                        Div(cls='card-body')(
                            H5('Mousse de Frutas', cls='card-title'),
                            P('Ligera y esponjosa, esta mousse se elabora con puré de frutas frescas y crema batida.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='mousse', 
                                data_precio='10.99'
                            )
                        )
                    )
                ),
                Div(cls='col-md-3 mb-4')(
                    Div(cls='card menu-item')(
                        IMG(src='static/images/tiramisu.png', cls='card-img-top', alt='tiramisu'),
                        Div(cls='card-body')(
                            H5('Tiramisú', cls='card-title'),
                            P('Postre italiano que combina capas de bizcochos empapados en café y una mezcla cremosa de mascarpone.', cls='card-text'),
                            P(cls='card-price')(('Precio: $10.99')),
                            Button(
                                'Agregar al pedido', 
                                cls='btn btn-orange text-white agregar-al-pedido', 
                                data_nombre='tiramisu', 
                                data_precio='10.99'
                            )
                        )
                    )
                )
            )
        )
    )


def create_modals():
    return Div()(
        # Modal para agregar al pedido
        Div(
            cls="modal fade",
            id="pedidoModal",
            tabindex="-1",
            aria_labelledby="pedidoModalLabel",
            aria_hidden="true"
        )(
            Div(cls="modal-dialog")(
                Div(cls="modal-content")(
                    Div(cls="modal-header")(
                        H5("Agregar al Pedido", cls="modal-title", id="pedidoModalLabel"),
                        Button(
                            type="button",
                            cls="btn-close",
                            data_bs_dismiss="modal",
                            aria_label="Close"
                        )
                    ),
                    Div(cls="modal-body")(
                        H6(id="productoNombre"),
                        P("Precio: ", Span(id="productoPrecio")),
                        Input(
                            type="number",
                            id="cantidadInput",
                            value="1",
                            min="1",
                            style="width: 60px; margin-bottom: 10px"
                        )
                    ),
                    Div(cls="modal-footer")(
                        Button(
                            'Cerrar',
                            type="button",
                            cls="btn btn-secondary",
                            data_bs_dismiss="modal"
                        ),
                        Button(
                            'Agregar al pedido',
                            type="button",
                            cls="btn btn-primary",
                            id="agregarAlPedido"
                        )
                    )
                )
            )
        ),

        # Modal para ver el pedido
        Div(
            cls="modal fade",
            id="verPedidoModal",
            tabindex="-1",
            aria_labelledby="verPedidoModalLabel",
            aria_hidden="true"
        )(
            Div(cls="modal-dialog")(
                Div(cls="modal-content")(
                    Div(cls="modal-header")(
                        Img(src="static/images/logo.jpg", alt="Logo", style="height: 40px; margin-right: 10px"),
                        H5("Don Remolo | Tu Pedido", cls="modal-title", id="verPedidoModalLabel"),
                        Button(
                            type="button",
                            cls="btn-close",
                            data_bs_dismiss="modal",
                            aria_label="Close"
                        )
                    ),
                    Div(cls="modal-body")(
                        Ul(id="listaPedido", cls="list-group"),
                        Div(id="totalPedido", cls="mt-3")
                    ),
                    Div(cls="modal-footer")(
                        Button(
                            'Cerrar',
                            type="button",
                            cls="btn btn-secondary",
                            data_bs_dismiss="modal"
                        ),
                        Button(
                            'Confirmar Pedido',
                            type="button",
                            cls="btn btn-primary",
                            id="enviarPedido",
                            disabled=True
                        )
                    )
                )
            )
        )
    )

def create_contact_form():
    return Section(id='contacto', cls='container py-1 parallax-section')(
        Div(cls='row d-flex justify-content-center')(
            Div(cls='col-lg-8 col-md-10 col-12', data_aos="zoom-in", data_aos_duration="3000", data_aos_delay="400")(
                FORM(id='contactForm')(
                    Div(cls='text-center mb-4')(
                        H2('Contáctame', cls='display-4 fw-bold text-dark'),
                        H4('¡Me Encantaría Conocer tus Aportes y Opiniones!', cls='text-dark')
                    ),
                    Div(cls='row g-1')(
                        Div(cls='col-12')(
                            Div(cls='form-group')(
                                Label('Nombre y Apellido', for_='inputName', cls='text-dark'),
                                INPUT(type='text', id="inputName", name="nombre", cls='form-control', placeholder='Ingrese su nombre', required=True, pattern="[A-Za-záéíóúñÑ ]+", oninput="validarNombreApellido(event)")
                            )
                        ),
                        Div(cls='col-md-6')(
                            Div(cls='form-group')(
                                Label('Email', for_='inputEmail', cls='text-dark'),
                                INPUT(type='email', id="inputEmail", name="email", cls='form-control', required=True, placeholder='Ingrese su email')
                            )
                        ),
                        Div(cls='col-md-6')(
                            Div(cls='form-group')(
                                Label('Teléfono', for_='inputPhone', cls='text-dark'),
                                INPUT(type='tel', id="inputPhone", name="telefono", cls='form-control', required=True, pattern="^\+?[0-9]{7,15}$", placeholder='Ingrese su teléfono')
                            )
                        ),
                        Div(cls='col-12')(
                            Div(cls='form-group')(
                                Label('Mensaje', for_='inputMessage', cls='text-dark'),
                                TEXTAREA(id="inputMessage", name="mensaje", cls='form-control', required=True, placeholder='Ingrese su mensaje', rows=3)
                            )
                        ),
                        Div(cls='col-12 d-flex justify-content-between align-items-center mt-2')(
                            Button('Enviar Mensaje', type='submit', cls='btn btn-orange text-white mt-2 btn-proyectos'),
                            A(href="https://wa.me/1133649070", target="_blank", cls="ms-auto")(
                                IMG(src="static/icons/ws.png", alt="WhatsApp", width="50", height="50", id="icon-ws")
                            )
                        )
                    )
                ),
                A('Ir al Inicio', href="#hero", cls='btn btn-orange mt-1 text-white text-center')
            )
        )
    )


def create_footer():
    return Div(
        FOOTER(id="contacto", cls='footer bg-dark text-white py-2')(
            Div(cls='container')(
                Div(cls='row')(
                    Div(cls='col-md-4')(
                        H5('Contacto'),
                        P('Dirección: Calle Principal 123, Ciudad'),
                        P('Teléfono: (123) 456-7890'),
                        P('Email: info@donremolo.com')
                    ),
                    Div(cls='col-md-4')(
                        H5('Horarios'),
                        P('Lunes a Viernes: 11:00 AM - 10:00 PM'),
                        P('Sábados y Domingos: 12:00 PM - 11:00 PM')
                    ),
                    Div(cls='col-md-4')(
                        H5('Síguenos'),
                        A(href='https://www.facebook.com/sfti', target='_blank', rel='noopener noreferrer', cls='me-2')(
                            SPAN(cls='fab fa-facebook fa-2x')
                        ),
                        A(href='https://www.instagram.com/sfti', target='_blank', rel='noopener noreferrer', cls='me-2')(
                            SPAN(cls='fab fa-instagram fa-2x')
                        ),
                        A(href='https://www.twitter.com/sfti', target='_blank', rel='noopener noreferrer')(
                            SPAN(cls='fab fa-twitter fa-2x')
                        )
                    )
                )
            )
        )
    )


@rt('/')
def index():
    return Div(
        create_head(),
        create_navbar(),
        create_hero(),
        create_about(),
        menu_1(),
        menu_2(),
        menu_3(),
        menu_4(),
        create_modals(),
        create_contact_form(),
        create_footer()

    )

# Iniciar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)