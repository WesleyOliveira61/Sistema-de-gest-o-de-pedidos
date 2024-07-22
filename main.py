from os import system

import flet as ft
from flet import (AppBar, Column, Container, Dropdown, ElevatedButton, Row,
                  Text, TextField, colors, icons)

system('cls')


class CadastroBar(Column):
    def __init__(self):
        super().__init__()
        self.produto = Dropdown(options=[ft.dropdown.Option('Milho'),
                                         ft.dropdown.Option('Arroz'),
                                         ft.dropdown.Option('Feijão'),
                                         ], width=200,
                                        hint_text='Selecione um produto')
        self.input_nfe = TextField(label='Digite o NFe', width=150)
        self.input_peso = TextField(label='Digite o peso', width=150)
        self.btn_cadastrar = ElevatedButton('Cadastrar',
                                            bgcolor='green',
                                            color='white', 
                                            height=50, icon=ft.icons.SAVE_SHARP)
        self.btn_edit = ElevatedButton('Editar',
                                            bgcolor='orange',
                                            color='white', 
                                            height=50, icon=ft.icons.EDIT)
        self.btn_delete = ElevatedButton('Deletar',
                                            bgcolor='red',
                                            color='white', 
                                            height=50, icon=ft.icons.DELETE)

        self.cliente = Dropdown(options=[
            ft.dropdown.Option('Fazenda tera fertil')                                                                                 ,
                                         ], hint_text='Selecione um cliente')
        self.controls=[self.build()]

    def build(self):        
        return Row(controls=[self.produto,
                             self.input_nfe,
                             self.input_peso,
                             self.cliente, 
                             self.btn_cadastrar,
                             self.btn_edit,
                             self.btn_delete]) 



def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    appbar = AppBar(title=Text('Cadastro pedidos'),
                    color=colors.BLACK87,
                    bgcolor=colors.WHITE70,
                    elevation=20,
                    leading=ft.Icon(icons.ADD_CARD_ROUNDED),
                    actions=[
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Cadastrar cliente",
                                        on_click=lambda e:print('Cliente cadastrado')),
                                    ft.PopupMenuItem(),  # divider
                                    ft.PopupMenuItem(text="Cadastrar produto",
                                        on_click=lambda e:print('Produto cadastrado')),
                                    
                ]
            ),
        ],
            )
    


    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.WHITE60,
        height=60,
        content=ft.Row(alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.ElevatedButton('Enviar relatorio', icon=ft.icons.EMAIL,
                                  bgcolor=ft.colors.AMBER_600),
                
            ]
        ),
    )

    page.padding=10
    
    
    page.add(appbar, CadastroBar(), ft.Divider(thickness=3))




ft.app(target=main)
