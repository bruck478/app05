import flet as ft
from pip._vendor.pygments.unistring import content
from pkg_resources._vendor.pyparsing import actions

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor = "yellow"
    
    txtPeso = ft.TextField(label="Ingresa tu peso (kg)")
    txtAltura = ft.TextField(label="Ingresa tu altura (m)")
    lblIMC = ft.Text("Tu IMC es de: ")
    
    img = ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/raw/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def calcular_imc(e):
        try:
            peso = float(txtPeso.value)
            altura = float(txtAltura.value)
            imc = peso / (altura ** 2)
            lblIMC.value = f"Tu IMC es de: {imc:.2f}"
            lblIMC.update()
            
            def cerrar_dialog(e):
                page.dialog.open = False
                page.update()
        
            if imc < 18.5:
                dialog=ft.AlertDialog(
                    title=ft.Text("Resultado de IMC")
                    content=ft.Text("Tu IMC indica que estas en bajo peso")
                    actions=[
                        ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                    ]
                )
            elif 18.5 <=  imc < 24.9:
                dialog = ft.AlertDiaog[
                    title=ft.Text("tu peso normal")
                    content=ft.text("tu IMC indoca que tienes un peso normal")
                    actions[
                        ft.TextButtton(text="Cerrar", on_click="cerrar_dialogo
                    ]
                ]
            elif 25 <= imc < 30: 
            dialog=ft.AlerDialog[
                title=ft.Text("Sobrepeso")
                content=ft.Text("Tu IMC indica que tienes sobrepeso")
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialog)
                ]
            ]
            else:
                dialog = ft.AlertDialog(
                    title = ft.Text("Odesidad"),
                    content= ft.Text("tu imc indica que tienes bajo peso"),
                    actions=(
                        ft.TextButton(text="Cerrar", on_clikc=cerrar_dialogo)
                    )
                )
            page.dialog = dialog
            page.dialog.open = True
            page.update()
            
        except ValueError:
            lblIMC.value = "Por favor, ingresa valores válidos."
            lblIMC.update()
                
                
                except Exception:
                    raise
                        
                        
                        ValueError:
            lblIMC.value = "Por favor, ingresa valores válidos."
            lblIMC.update()


    btnCalcular = ft.ElevatedButton(text="Calcular", on_click=calcular_imc)
    btnLimpiar = ft.ElevatedButton(text="Limpiar", on_click=limpiar)
    
                
            )
    page.add(
        ft.Column(
            controls=[
                txtPeso,
                txtAltura,
                lblIMC
            ],
            alignment="CENTER"
        ),
        ft.Row(
            controls=[
                img
            ],
            alignment="CENTER"
        ),
        ft.Row(
            controls=[
                btnCalcular,
                btnLimpiar
            ],
            alignment="CENTER"
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)


ft.app(main)
