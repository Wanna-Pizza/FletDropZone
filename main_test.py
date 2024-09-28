import time
import flet as ft
from DropZone import LoadDLL


def main(page: ft.Page):
    page.title = 'DLLDropZone' #To start DLL working, you must add name to your application
    page.update()

    def dropped(e:list = None):
        grid.controls.clear()
        grid.update()
        for i in e: # LIST!!!!
            grid.controls.append(
                ft.Container(ft.Text(i),bgcolor='white,0.1',border_radius=10,padding=10)
                )
        grid.update()

    grid = ft.Row(controls=[],wrap=True)



    time.sleep(0.1)  # There is pause. It must be here for DLL.
    DropZone_dll = LoadDLL(
        page=page,
        on_dropped=lambda e: (print(f'Dropped {e}'),dropped(e)), # E = returns list of paths droped files
        on_entered=lambda e: print('entered'),
        on_leaved=lambda e: print('leaved'))
    page.add(grid)
ft.app(main)