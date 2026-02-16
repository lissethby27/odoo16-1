from odoo import models, fields

class BibliotecaAutor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Autor de libros en la biblioteca'

    name = fields.Char(string='Nombre', required=True)
    nacionalidad = fields.Char(string='Nacionalidad')
    biografia = fields.Text(string='Biografía')
    
    # IMPORTANTE: El nombre debe ser exacto y el string obligatorio
    image_1920 = fields.Binary(string="Foto del Autor")
    
    libro_autor_ids = fields.One2many(
        'biblioteca.autor_libro', 
        'autor_id', 
        string='Libros del Autor'
    )